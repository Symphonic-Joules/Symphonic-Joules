<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Symphonic-Joules | Where Sound Meets Science</title>
    <style>
        /* Base Environment */
        :root {
            --bg-dark: #0f172a;
            --bg-card: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #6366f1;
            --accent-hover: #4f46e5;
        }

        body {
            font-family: system-ui, -apple-system, sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-main);
            margin: 0;
            line-height: 1.6;
        }

        a { text-decoration: none; color: var(--accent); }
        a:hover { color: var(--text-main); }

        /* 1. The Lighthouse (Hero Section) */
        .hero {
            text-align: center;
            padding: 120px 20px;
            /* Fluid animated gradient to represent sound/energy */
            background: linear-gradient(-45deg, #0f172a, #1e1b4b, #312e81, #0f172a);
            background-size: 400% 400%;
            animation: fluidWave 15s ease infinite;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        @keyframes fluidWave {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .hero h1 {
            font-size: 3.5rem;
            margin: 0 0 10px 0;
            letter-spacing: -0.05em;
        }

        .hero p.subtitle {
            font-size: 1.25rem;
            color: var(--text-muted);
            max-width: 600px;
            margin: 0 auto 30px auto;
        }

        .cta-group {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn {
            padding: 12px 24px;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.2s;
        }

        .btn-primary {
            background: var(--accent);
            color: white;
        }

        .btn-primary:hover {
            background: var(--accent-hover);
            transform: translateY(-2px);
        }

        .btn-outline {
            border: 1px solid rgba(255,255,255,0.2);
            color: var(--text-main);
        }

        .btn-outline:hover {
            background: rgba(255,255,255,0.1);
        }

        /* Container for content */
        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 60px 20px;
        }

        .section-title {
            text-align: center;
            font-size: 2rem;
            margin-bottom: 40px;
        }

        /* 2. Features Quadrant */
        .quadrant {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
        }

        .card {
            background: var(--bg-card);
            padding: 30px;
            border-radius: 12px;
            border-top: 3px solid var(--accent);
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2);
        }

        .card h3 { margin-top: 0; }
        .card p { color: var(--text-muted); margin-bottom: 0; }
        .icon { font-size: 1.5rem; margin-bottom: 15px; display: inline-block; }

        /* 3. Side-by-Side: Theory & Execution */
        .split-view {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 60px;
        }

        .code-block, .math-block {
            background: #000;
            padding: 24px;
            border-radius: 12px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 0.9rem;
            overflow-x: auto;
            border: 1px solid rgba(255,255,255,0.1);
        }

        .math-block {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .equation {
            font-size: 1.2rem;
            color: #38bdf8;
            text-align: center;
            margin-bottom: 20px;
        }

        .variables { color: var(--text-muted); }
        .keyword { color: #f472b6; }
        .string { color: #a3e635; }
        .comment { color: #64748b; }

        @media (max-width: 768px) {
            .split-view { grid-template-columns: 1fr; }
            .hero h1 { font-size: 2.5rem; }
        }
        
        /* Footer */
        footer {
            text-align: center;
            padding: 40px;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: var(--text-muted);
            margin-top: 40px;
        }
    </style>
</head>
<body>

    <!-- 1. The Lighthouse -->
    <header class="hero">
        <div style="position: relative; z-index: 2;">
            <h1>Symphonic-Joules</h1>
            <p class="subtitle">Where Sound Meets Science. A unified computational framework connecting audio analysis with physics-based energy calculations.</p>
            <div class="cta-group">
                <a href="#quick-start" class="btn btn-primary">Get Started</a>
                <a href="#examples" class="btn btn-outline">View Examples</a>
                <a href="https://github.com/JaclynCodes/Symphonic-Joules-a67272a4" class="btn btn-outline">GitHub Repository</a>
            </div>
        </div>
    </header>

    <main class="container">
        
        <!-- 2. Features Quadrant -->
        <h2 class="section-title">Why Symphonic-Joules?</h2>
        <div class="quadrant">
            <div class="card">
                <span class="icon">🌉</span>
                <h3>Bridge Science & Sound</h3>
                <p>Unified framework connecting audio analysis with physics-based energy calculations directly in Python.</p>
            </div>
            <div class="card">
                <span class="icon">🧩</span>
                <h3>Open & Extensible</h3>
                <p>Build on acoustic energy models with a modular, plugin-friendly architecture designed for scale.</p>
            </div>
            <div class="card">
                <span class="icon">🔬</span>
                <h3>Science-Driven</h3>
                <p>Every calculation is strictly grounded in established physics principles and peer-reviewed acoustic methods.</p>
            </div>
            <div class="card">
                <span class="icon">🤝</span>
                <h3>Built for Collaboration</h3>
                <p>Designed for musicians, physicists, researchers, and developers to work seamlessly together.</p>
            </div>
        </div>

        <!-- 3. Side-by-Side: Theory & Execution -->
        <div class="split-view">
            <!-- Theory -->
            <div class="math-block">
                <h3 style="margin-top: 0; color: white;">The Physics</h3>
                <p class="variables" style="margin-top: 0;">Governing how sound carries energy through space:</p>
                <div class="equation">
                    w = p² / (2ρc²) + ρv² / 2
                </div>
                <div class="variables">
                    <strong>w</strong> = acoustic energy density (J/m³)<br>
                    <strong>p</strong> = sound pressure (Pa)<br>
                    <strong>ρ</strong> = medium density (kg/m³)<br>
                    <strong>c</strong> = speed of sound (m/s)<br>
                    <strong>v</strong> = particle velocity (m/s)
                </div>
            </div>

            <!-- Execution -->
            <div class="code-block">
                <h3 style="margin-top: 0; color: white;">The Code</h3>
<pre style="margin: 0;"><code><span class="keyword">from</span> symphonic_joules <span class="keyword">import</span> AudioSignal, EnergyCalculator

<span class="comment"># Load an audio signal</span>
signal = AudioSignal.from_file(<span class="string">"symphony.wav"</span>)

<span class="comment"># Calculate acoustic energy</span>
calculator = EnergyCalculator(
    medium_density=1.225, 
    sound_speed=343.0
)
energy = calculator.compute_total_energy(signal)

print(f<span class="string">"Total Energy: {energy:.6f} J"</span>)</code></pre>
            </div>
        </div>

    </main>

    <footer>
        <p>Current Phase: 🏗️ Foundation (v0.1.0) | Open Source under MIT License</p>
        <p><a href="https://github.com/JaclynCodes/Symphonic-Joules-a67272a4/blob/main/CONTRIBUTING.md">Contributing Guidelines</a> • <a href="https://github.com/JaclynCodes/Symphonic-Joules-a67272a4/issues/new">Report Bugs</a></p>
    </footer>

</body>
</html>
**Thank you for your interest in Symphonic-Joules!**

*Where sound meets science, harmony meets energy.*

[⭐ Star on GitHub](https://github.com/JaclynCodes/Symphonic-Joules-a67272a4)

</div>
