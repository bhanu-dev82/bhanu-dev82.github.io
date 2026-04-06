document.addEventListener('DOMContentLoaded', function () {
    const html = document.documentElement;
    const header = document.querySelector('#header');
    let headerH = header ? header.offsetHeight : 64;
    const loadingScreen = document.getElementById('loadingScreen');

    // --- Loading Screen ---
    if (loadingScreen) {
        setTimeout(() => {
            loadingScreen.style.opacity = '0';
            setTimeout(() => loadingScreen.style.display = 'none', 500);
        }, 400);
    }

    // --- Smooth Scrolling ---
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (!target) return;
            e.preventDefault();
            window.scrollTo({ top: target.getBoundingClientRect().top + window.pageYOffset - headerH, behavior: 'smooth' });
            const navMenu = document.getElementById('navLinks');
            const navToggle = document.getElementById('navToggle');
            if (navMenu && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                if (navToggle) navToggle.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    });

    // --- Mobile Nav Toggle ---
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navLinks');
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            navMenu.classList.toggle('active');
            this.innerHTML = navMenu.classList.contains('active')
                ? '<i class="fas fa-times"></i>'
                : '<i class="fas fa-bars"></i>';
        });
    }

    // --- Footer Year ---
    const yearEl = document.getElementById('currentYear');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    // --- Active Nav Link on Scroll ---
    const sections = document.querySelectorAll('main section[id]');
    const navLinks = document.querySelectorAll('header nav ul li a');
    function updateActiveLink() {
        let current = '';
        sections.forEach(s => {
            if (window.scrollY >= s.offsetTop - headerH - 80) current = s.id;
        });
        navLinks.forEach(a => {
            a.classList.toggle('active', a.getAttribute('href') === `#${current}`);
        });
    }
    window.addEventListener('scroll', updateActiveLink, { passive: true });
    setTimeout(updateActiveLink, 200);

    // --- Theme Toggle ---
    const themeBtn = document.getElementById('theme-toggle');
    function applyTheme(theme) {
        html.setAttribute('data-theme', theme);
        if (themeBtn) themeBtn.innerHTML = theme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        localStorage.setItem('theme', theme);
        setTimeout(() => { initParticles(); initPlexus(); }, 60);
    }
    function getCSSVar(v) { return getComputedStyle(html).getPropertyValue(v).trim(); }

    const saved = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(saved || (prefersDark ? 'dark' : 'light'));

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            applyTheme(html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
        });
    }

    // --- Background Particles ---
    function initParticles() {
        if (typeof particlesJS === 'undefined' || !document.getElementById('particles-js')) return;
        if (window.pJSDom && window.pJSDom[0] && window.pJSDom[0].pJS) {
            window.pJSDom[0].pJS.fn.vendors.destroypJS();
            window.pJSDom = [];
        }
        const color = getCSSVar('--particle-color') || '#7c6af7';
        particlesJS('particles-js', {
            particles: {
                number: { value: 35, density: { enable: true, value_area: 900 } },
                color: { value: color },
                shape: { type: 'circle' },
                opacity: { value: 0.25, random: true },
                size: { value: 2, random: true },
                line_linked: { enable: false },
                move: { enable: true, speed: 0.6, random: true, out_mode: 'out' }
            },
            interactivity: { events: { onhover: { enable: false }, onclick: { enable: false } } },
            retina_detect: true
        });
    }

    // --- Hero Plexus Canvas ---
    const canvas = document.getElementById('hero-plexus-canvas');
    let ctx, particles = [], rafId;

    function initPlexus() {
        if (!canvas) return;
        ctx = canvas.getContext('2d');
        if (rafId) cancelAnimationFrame(rafId);
        resizePlexus();
        createParticles();
        animatePlexus();
    }

    function resizePlexus() {
        if (!canvas) return;
        const hero = document.getElementById('hero');
        canvas.width = hero ? hero.offsetWidth : window.innerWidth;
        canvas.height = hero ? hero.offsetHeight : window.innerHeight;
    }

    class Dot {
        constructor() { this.reset(); }
        reset() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.vx = (Math.random() - 0.5) * 0.3;
            this.vy = (Math.random() - 0.5) * 0.3;
            this.r = Math.random() * 1.5 + 0.5;
            this.color = getCSSVar('--plexus-particle') || '#7c6af7';
        }
        update() {
            this.x += this.vx; this.y += this.vy;
            if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
            if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.fill();
        }
    }

    function createParticles() {
        particles = [];
        const count = Math.min(80, Math.floor((canvas.width * canvas.height) / 10000));
        for (let i = 0; i < count; i++) particles.push(new Dot());
    }

    function drawLines() {
        const maxDist = 120;
        const lineColor = getCSSVar('--plexus-line') || 'rgba(124,106,247,0.15)';
        const rgb = lineColor.match(/[\d.]+/g);
        const base = rgb ? `${rgb[0]},${rgb[1]},${rgb[2]}` : '124,106,247';
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const d = Math.sqrt(dx * dx + dy * dy);
                if (d < maxDist) {
                    ctx.strokeStyle = `rgba(${base},${(1 - d / maxDist) * 0.5})`;
                    ctx.lineWidth = 0.4;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }
    }

    function animatePlexus() {
        rafId = requestAnimationFrame(animatePlexus);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => { p.update(); p.draw(); });
        drawLines();
    }

    if (canvas) {
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => { cancelAnimationFrame(rafId); initPlexus(); }, 250);
        });
    }

    // --- Scroll Fade-in ---
    const fadeEls = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); } });
    }, { threshold: 0.08 });
    fadeEls.forEach(el => observer.observe(el));

    // --- Resize: update header height ---
    window.addEventListener('resize', () => { if (header) headerH = header.offsetHeight; }, { passive: true });
});
