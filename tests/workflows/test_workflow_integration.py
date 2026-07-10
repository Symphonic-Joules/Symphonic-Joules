import os
import pytest
import yaml
import requests
from pathlib import Path

class TestCrossWorkflowConsistency:
    """Validates structural consistency across the entire ecosystem of workflows."""

    @pytest.fixture(scope="class")
    def all_workflows(self):
        """Loads all YAML workflows in the directory into a dictionary."""
        workflow_dir = Path(".github/workflows")
        workflows = {}
        # Gracefully handle if the directory doesn't exist during local testing
        if not workflow_dir.exists():
            return workflows
            
        for file in workflow_dir.glob("*.yml"):
            with open(file, "r") as f:
                workflows[file.name] = yaml.safe_load(f)
        return workflows

    @pytest.mark.integration
    def test_consistent_runner_environments(self, all_workflows):
        """Ensures all jobs across all workflows use 'ubuntu-latest' to prevent fragmented environments."""
        if not all_workflows:
            pytest.skip("No workflows found to test.")
            
        for file_name, workflow in all_workflows.items():
            jobs = workflow.get("jobs", {})
            for job_id, job in jobs.items():
                runs_on = job.get("runs-on")
                assert runs_on == "ubuntu-latest", \
                    f"Fragmentation detected: {file_name} job '{job_id}' uses '{runs_on}' instead of 'ubuntu-latest'"

    @pytest.mark.integration
    def test_no_duplicate_workflow_names(self, all_workflows):
        """Ensures no two workflows share the same display name, which causes UI confusion in GitHub."""
        names_seen = set()
        for file_name, workflow in all_workflows.items():
            workflow_name = workflow.get("name", file_name)
            assert workflow_name not in names_seen, \
                f"Duplicate workflow name found: '{workflow_name}' in {file_name}"
            names_seen.add(workflow_name)


class TestLiveWorkflowExecution:
    """
    Hits the GitHub API to verify actual workflow run statuses.
    These tests will skip locally unless a GITHUB_TOKEN is provided, 
    but will run perfectly inside your actual CI pipeline.
    """

    @pytest.fixture(scope="class")
    def github_headers(self):
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            pytest.skip("GITHUB_TOKEN environment variable not set. Skipping live API tests.")
        return {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    @pytest.fixture(scope="class")
    def repo_name(self):
        # We can dynamically pull this from the environment if running in Actions
        return os.getenv("GITHUB_REPOSITORY", "JaclynCodes/Symphonic-Joules-a67272a4")

    @pytest.mark.integration
    def test_latest_main_build_success(self, github_headers, repo_name):
        """Verifies the most recent workflow execution on the main branch was a success."""
        url = f"https://api.github.com/repos/{repo_name}/actions/runs?branch=main&status=completed"
        
        response = requests.get(url, headers=github_headers)
        assert response.status_code == 200, f"GitHub API returned {response.status_code}: {response.text}"
        
        runs = response.json().get("workflow_runs", [])
        if runs:
            latest_run = runs[0]
            conclusion = latest_run.get("conclusion")
            html_url = latest_run.get("html_url")
            assert conclusion == "success", f"Latest build on main failed! See: {html_url}"
        else:
            pytest.skip("No completed workflow runs found for the main branch.")
