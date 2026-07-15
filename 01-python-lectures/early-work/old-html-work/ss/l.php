<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>NEXUS — Beyond Tomorrow</title>

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&family=Share+Tech+Mono&display=swap" rel="stylesheet" />

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

    <style>
        /* Existing Styles Included + Fixes */
        :root {
            --cyan: #00f5ff; --blue: #0066ff; --purple: #8b00ff;
            --white: #f0f4ff; --bg: #010208; --bg2: #040b18;
            --border: rgba(0, 245, 255, 0.15);
            --glow: 0 0 20px rgba(0,245,255,0.3);
            --font-display: 'Orbitron', sans-serif;
            --font-body: 'Rajdhani', sans-serif;
            --font-mono: 'Share Tech Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            background: var(--bg); color: var(--white); 
            font-family: var(--font-body); overflow-x: hidden;
            line-height: 1.6;
        }

        /* CUSTOM CURSOR */
        #cursor-dot {
            position: fixed; top: 0; left: 0; width: 8px; height: 8px;
            background: var(--cyan); border-radius: 50%; pointer-events: none;
            z-index: 10000; box-shadow: var(--glow);
        }

        /* LOADER */
        #loader {
            position: fixed; inset: 0; z-index: 9999;
            background: var(--bg); display: flex; flex-direction: column;
            align-items: center; justify-content: center;
        }

        /* HERO & CANVAS */
        #bg-canvas { position: fixed; top: 0; left: 0; z-index: 0; }
        
        nav {
            position: fixed; top: 0; width: 100%; z-index: 100;
            display: flex; justify-content: space-between; align-items: center;
            padding: 20px 5%; backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border);
        }

        section { position: relative; z-index: 1; padding: 100px 5%; }
        
        .hero-title {
            font-family: var(--font-display); font-size: clamp(3rem, 8vw, 7rem);
            text-transform: uppercase; line-height: 0.9; margin-bottom: 20px;
        }

        .accent-text {
            background: linear-gradient(90deg, var(--cyan), var(--purple));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }

        /* FEATURE CARDS */
        .features-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px; margin-top: 50px;
        }
        .feature-card {
            background: rgba(255,255,255,0.03); padding: 40px;
            border: 1px solid var(--border); transition: 0.3s;
        }
        .feature-card:hover { background: rgba(0, 245, 255, 0.05); border-color: var(--cyan); }

        /* FAQ */
        .faq-item { border-bottom: 1px solid var(--border); cursor: pointer; }
        .faq-question { padding: 20px 0; display: flex; justify-content: space-between; font-family: var(--font-display); }
        .faq-answer { height: 0; overflow: hidden; color: rgba(255,255,255,0.6); transition: 0.3s; }
        .faq-item.active .faq-answer { height: auto; padding-bottom: 20px; }
    </style>
</head>
<body>

    <div id="loader">
        <h1 id="loader-logo" style="font-family: var(--font-display); color: var(--cyan);">NEXUS</h1>
        <div style="width: 200px; height: 2px; background: rgba(255,255,255,0.1); margin-top: 20px;">
            <div id="loader-bar" style="width: 0%; height: 100%; background: var(--cyan);"></div>
        </div>
    </div>

    <div id="cursor-dot"></div>
    <canvas id="bg-canvas"></canvas>

    <nav>
        <div class="nav-logo" style="font-family: var(--font-display); font-weight: 900;">NEXUS</div>
        <button style="background: transparent; border: 1px solid var(--cyan); color: var(--cyan); padding: 8px 20px; font-family: var(--font-mono); cursor: pointer;">CONNECT_</button>
    </nav>

    <section id="hero">
        <div class="hero-content">
            <p style="font-family: var(--font-mono); color: var(--cyan); margin-bottom: 10px;">[ SYSTEM STATUS: ONLINE ]</p>
            <h1 class="hero-title">Architecting <br><span class="accent-text">The Neural</span><br> Frontier</h1>
            <p style="max-width: 500px; font-size: 1.2rem; color: rgba(255,255,255,0.6);">
                The world’s first decentralized AI mesh network. Scalable, secure, and beyond human speed.
            </p>
            <div style="margin-top: 40px; display: flex; gap: 20px;">
                <button style="padding: 15px 30px; background: var(--cyan); border: none; font-family: var(--font-display); font-weight: bold; cursor: pointer;">GET STARTED</button>
                <button style="padding: 15px 30px; background: transparent; border: 1px solid white; color: white; font-family: var(--font-display); cursor: pointer;">WHITEPAPER</button>
            </div>
        </div>
    </section>

    <section id="features">
        <h2 style="font-family: var(--font-display); font-size: 2.5rem;">Core Protocols</h2>
        <div class="features-grid">
            <div class="feature-card">
                <h3 style="font-family: var(--font-display); margin-bottom: 15px;">Quantum Sync</h3>
                <p>Instantaneous data reconciliation across distributed nodes with zero latency.</p>
            </div>
            <div class="feature-card">
                <h3 style="font-family: var(--font-display); margin-bottom: 15px;">Neural Guard</h3>
                <p>Self-evolving AI security layers that predict threats before they manifest.</p>
            </div>
            <div class="feature-card">
                <h3 style="font-family: var(--font-display); margin-bottom: 15px;">Edge Compute</h3>
                <p>Localized processing power that brings the cloud to the device level.</p>
            </div>
        </div>
    </section>

    <section id="faq">
        <h2 style="font-family: var(--font-display); margin-bottom: 30px;">Intelligence Briefing</h2>
        <div class="faq-item">
            <div class="faq-question">What is Nexus? <span>+</span></div>
            <div class="faq-answer">Nexus is a distributed intelligence network designed to bridge the gap between human intent and machine execution.</div>
        </div>
        <div class="faq-item">
            <div class="faq-question">How secure is the protocol? <span>+</span></div>
            <div class="faq-answer">Our protocol utilizes 512-bit quantum-resistant encryption on every data packet.</div>
        </div>
    </section>

    <script>
        // 1. THREE.JS BACKGROUND
        const canvas = document.querySelector('#bg-canvas');
        const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 5;

        const particlesGeometry = new THREE.BufferGeometry();
        const count = 3000;
        const positions = new Float32Array(count * 3);
        for(let i = 0; i < count * 3; i++) positions[i] = (Math.random() - 0.5) * 15;
        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

        const particlesMaterial = new THREE.PointsMaterial({ size: 0.015, color: 0x00f5ff, transparent: true, opacity: 0.8 });
        const points = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(points);

        let mouseX = 0, mouseY = 0;
        window.addEventListener('mousemove', (e) => {
            mouseX = (e.clientX / window.innerWidth) - 0.5;
            mouseY = (e.clientY / window.innerHeight) - 0.5;
            gsap.to('#cursor-dot', { x: e.clientX, y: e.clientY, duration: 0.1 });
        });

        function animate() {
            requestAnimationFrame(animate);
            points.rotation.y += 0.001;
            points.rotation.x += (mouseY * 0.05 - points.rotation.x) * 0.1;
            points.rotation.y += (mouseX * 0.05 - points.rotation.y) * 0.1;
            renderer.render(scene, camera);
        }
        
        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }
        window.addEventListener('resize', onWindowResize);
        onWindowResize();
        animate();

        // 2. LOADER & GSAP ANIMATIONS
        window.addEventListener('load', () => {
            let tl = gsap.timeline();
            tl.to("#loader-bar", { width: "100%", duration: 1.5, ease: "power4.inOut" });
            tl.to("#loader", { yPercent: -100, duration: 0.8, ease: "expo.inOut" });
            
            // Hero Entry
            tl.from(".hero-title", { y: 100, opacity: 0, duration: 1, ease: "power4.out" }, "-=0.2");
            tl.from(".hero-content p", { opacity: 0, x: -20, duration: 0.8 }, "-=0.6");
        });

        // 3. SCROLL ANIMATIONS
        gsap.registerPlugin(ScrollTrigger);
        gsap.utils.toArray(".feature-card").forEach(card => {
            gsap.from(card, {
                scrollTrigger: { trigger: card, start: "top 90%" },
                opacity: 0, y: 50, duration: 1
            });
        });

        // 4. FAQ LOGIC
        document.querySelectorAll('.faq-item').forEach(item => {
            item.addEventListener('click', () => {
                item.classList.toggle('active');
                const sign = item.querySelector('span');
                sign.textContent = item.classList.contains('active') ? '-' : '+';
            });
        });
    </script>
</body>
</html>
