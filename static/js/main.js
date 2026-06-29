/* =============================================
   AnimaMagni — Main JavaScript
   Scroll effects · Navbar · Particles · Reveal
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

    // ─── NAVBAR SCROLL ───────────────────────────────
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 30);
    }, { passive: true });


    // ─── HAMBURGER MENU ──────────────────────────────
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobileMenu');
    if (hamburger && mobileMenu) {
        hamburger.addEventListener('click', () => {
            mobileMenu.classList.toggle('open');
        });
    }


    // ─── HERO LOGO REVEAL (A then M on scroll) ───────
    const heroLogoWrap = document.querySelector('.hero-logo-wrap');
    if (heroLogoWrap) {
        // Show A immediately
        setTimeout(() => {
            heroLogoWrap.classList.add('revealed-a');
        }, 400);

        // Show M when user scrolls or after delay
        const revealM = () => {
            heroLogoWrap.classList.add('revealed-m');
        };

        let mRevealed = false;
        window.addEventListener('scroll', () => {
            if (!mRevealed && window.scrollY > 60) {
                mRevealed = true;
                revealM();
            }
        }, { passive: true });

        // Also reveal M after 2.5s even without scroll
        setTimeout(() => {
            if (!mRevealed) { mRevealed = true; revealM(); }
        }, 2500);
    }


    // ─── SCROLL REVEAL ───────────────────────────────
    const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(el => observer.observe(el));

    // Stagger children
    document.querySelectorAll('.stagger').forEach(parent => {
        Array.from(parent.children).forEach((child, i) => {
            child.style.setProperty('--i', i);
        });
    });


    // ─── FLOATING PARTICLES ──────────────────────────
    const particleContainer = document.querySelector('.hero-particles');
    if (particleContainer) {
        const colors = ['#9b6dff', '#c8c8c8', '#7c5cbf'];
        const count = 30;

        for (let i = 0; i < count; i++) {
            const p = document.createElement('div');
            p.classList.add('particle');
            p.style.cssText = `
                left: ${Math.random() * 100}%;
                width: ${Math.random() * 3 + 1}px;
                height: ${Math.random() * 3 + 1}px;
                background: ${colors[Math.floor(Math.random() * colors.length)]};
                animation-duration: ${Math.random() * 15 + 10}s;
                animation-delay: ${Math.random() * 10}s;
                border-radius: 50%;
            `;
            particleContainer.appendChild(p);
        }
    }


    // ─── PARALLAX HERO BG ────────────────────────────
    const heroBg = document.querySelector('.hero-bg');
    if (heroBg) {
        window.addEventListener('scroll', () => {
            const y = window.scrollY;
            heroBg.style.transform = `translateY(${y * 0.3}px)`;
        }, { passive: true });
    }


    // ─── SMOOTH SCROLL FOR ANCHOR LINKS ──────────────
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', e => {
            const target = document.querySelector(link.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });


    // ─── AUTO-DISMISS MESSAGES ───────────────────────
    document.querySelectorAll('.message').forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = '0';
            msg.style.transform = 'translateY(-8px)';
            msg.style.transition = '0.4s ease';
            setTimeout(() => msg.remove(), 400);
        }, 5000);
    });


    // ─── TYPING CURSOR EFFECT (hero subtitle) ────────
    const typingEl = document.querySelector('.typing-text');
    if (typingEl) {
        const words = typingEl.dataset.words ? typingEl.dataset.words.split('|') : [];
        if (words.length > 1) {
            let wi = 0, ci = 0, deleting = false;
            const type = () => {
                const word = words[wi];
                if (!deleting) {
                    typingEl.textContent = word.slice(0, ++ci);
                    if (ci === word.length) { deleting = true; setTimeout(type, 1800); return; }
                } else {
                    typingEl.textContent = word.slice(0, --ci);
                    if (ci === 0) { deleting = false; wi = (wi + 1) % words.length; }
                }
                setTimeout(type, deleting ? 60 : 110);
            };
            setTimeout(type, 800);
        }
    }

});
