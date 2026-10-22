/**
 * Pinkal Rathod – Personal Portfolio
 * Main Interactive JavaScript (Theme, Animated Typing, Smooth Scrolling, Scrollspy, Mobile Nav)
 */

document.addEventListener('DOMContentLoaded', () => {
    // 0. Progressive enhancement flag: triggers smooth scroll reveals
    document.documentElement.classList.add('js-ready');

    // 1. Dark / Light Mode Toggle
    initThemeToggle();

    // 2. Animated Typing Effect
    initTypingEffect();

    // 3. Back to Top Button
    initBackToTop();

    // 4. Mobile Nav auto-close
    initMobileNav();

    // 5. Active Link Highlight on Scroll
    initScrollSpy();

    // 6. Premium Custom Cursor
    initCustomCursor();

    // 7. Modern Viewport Scroll Reveal & Stagger Animations
    initScrollReveal();
});

/**
 * Initializes Theme Toggle (Dark Navy / Light Mode)
 */
function initThemeToggle() {
    const htmlEl = document.documentElement;
    const bodyEl = document.body;
    const toggleBtns = [
        document.getElementById('themeToggle'),
        document.getElementById('themeToggleMobile')
    ].filter(Boolean);

    // Retrieve saved theme or fallback to dark
    const savedTheme = localStorage.getItem('pr_portfolio_theme') || 'dark';
    setTheme(savedTheme);

    toggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const currentTheme = htmlEl.getAttribute('data-theme') || 'dark';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
        });
    });

    function setTheme(theme) {
        htmlEl.setAttribute('data-theme', theme);
        bodyEl.className = theme === 'dark' ? 'theme-dark' : 'theme-light';
        localStorage.setItem('pr_portfolio_theme', theme);

        // Update button icons
        toggleBtns.forEach(btn => {
            const icon = btn.querySelector('i');
            if (icon) {
                if (theme === 'dark') {
                    icon.className = 'fa-solid fa-sun';
                    btn.setAttribute('title', 'Switch to Light Mode');
                } else {
                    icon.className = 'fa-solid fa-moon';
                    btn.setAttribute('title', 'Switch to Dark Mode');
                }
            }
        });
    }
}

/**
 * Typing Text Effect for Hero Header
 * Rotates through the 5 specified core technical disciplines
 */
function initTypingEffect() {
    const typingEl = document.getElementById('typingText');
    if (!typingEl) return;

    let titles = [
        "Python Development",
        "Django Web Development",
        "Flutter App Development",
        "Android Development",
        "Frontend Development"
    ];

    try {
        const customData = typingEl.getAttribute('data-titles');
        if (customData) {
            titles = JSON.parse(customData);
        }
    } catch (e) {
        // Fallback to default
    }

    let titleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const typingSpeed = 80;
    const deletingSpeed = 40;
    const pauseTime = 1800;

    function type() {
        const currentTitle = titles[titleIndex];

        if (isDeleting) {
            typingEl.textContent = currentTitle.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingEl.textContent = currentTitle.substring(0, charIndex + 1);
            charIndex++;
        }

        let speed = isDeleting ? deletingSpeed : typingSpeed;

        if (!isDeleting && charIndex === currentTitle.length) {
            speed = pauseTime;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            titleIndex = (titleIndex + 1) % titles.length;
            speed = 400;
        }

        setTimeout(type, speed);
    }

    type();
}

/**
 * Back to Top Floating Button
 */
function initBackToTop() {
    const backToTopBtn = document.getElementById('backToTop');
    if (!backToTopBtn) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    });

    backToTopBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Auto-close mobile navbar when a link is clicked
 */
function initMobileNav() {
    const navCollapse = document.getElementById('navbarNav');
    if (!navCollapse) return;

    const navLinks = navCollapse.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth < 992 && navCollapse.classList.contains('show')) {
                const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
                if (bsCollapse) {
                    bsCollapse.hide();
                }
            }
        });
    });
}

/**
 * Smooth Active Section Highlighting
 */
function initScrollSpy() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.main-navbar .nav-link[href^="#"]');

    if (!sections.length || !navLinks.length) return;

    window.addEventListener('scroll', () => {
        let currentSectionId = '';
        const scrollPosition = window.scrollY + 140;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });
}

/**
 * 6. Premium Custom Cursor System
 * Hardware-accelerated with requestAnimationFrame, lerp smoothing,
 * adaptive dark/light themes, interactive hover states, and touch detection.
 */
function initCustomCursor() {
    const dot = document.getElementById('cursorDot');
    const ring = document.getElementById('cursorRing');
    if (!dot || !ring) return;

    // Check touch devices, narrow screens, or reduced motion
    const isTouchOrSmall = () => {
        return window.matchMedia('(hover: none) and (pointer: coarse), (max-width: 991.98px)').matches;
    };
    const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (isTouchOrSmall() || isReducedMotion) {
        dot.style.display = 'none';
        ring.style.display = 'none';
        return;
    }

    let mouseX = -100;
    let mouseY = -100;
    let ringX = -100;
    let ringY = -100;
    let isVisible = false;
    let isRunning = false;
    let rafId = null;

    // Smooth lerp easing factor for outer ring
    const lerpFactor = 0.16;

    function render() {
        const dx = mouseX - ringX;
        const dy = mouseY - ringY;

        ringX += dx * lerpFactor;
        ringY += dy * lerpFactor;

        // Precise centering with translate(-50%, -50%)
        dot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
        ring.style.transform = `translate3d(${ringX.toFixed(2)}px, ${ringY.toFixed(2)}px, 0) translate(-50%, -50%)`;

        // If ring has settled and cursor is outside window, stop RAF loop to conserve CPU
        if (!isVisible && Math.abs(dx) < 0.1 && Math.abs(dy) < 0.1) {
            isRunning = false;
            cancelAnimationFrame(rafId);
            return;
        }

        if (isRunning) {
            rafId = requestAnimationFrame(render);
        }
    }

    function startLoop() {
        if (!isRunning) {
            isRunning = true;
            rafId = requestAnimationFrame(render);
        }
    }

    // Mouse Movement
    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;

        if (!isVisible) {
            isVisible = true;
            dot.classList.add('cursor-visible');
            ring.classList.add('cursor-visible');
            if (ringX < 0 && ringY < 0) {
                ringX = mouseX;
                ringY = mouseY;
            }
            startLoop();
        } else if (!isRunning) {
            startLoop();
        }
    }, { passive: true });

    // Window boundaries
    document.addEventListener('mouseleave', () => {
        isVisible = false;
        dot.classList.remove('cursor-visible');
        ring.classList.remove('cursor-visible');
        ring.classList.remove('cursor-hover', 'cursor-card-hover', 'cursor-input-focus', 'cursor-click');
        dot.classList.remove('cursor-hover', 'cursor-card-hover', 'cursor-input-focus', 'cursor-click');
    });

    document.addEventListener('mouseenter', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        isVisible = true;
        dot.classList.add('cursor-visible');
        ring.classList.add('cursor-visible');
        startLoop();
    });

    window.addEventListener('blur', () => {
        isVisible = false;
        dot.classList.remove('cursor-visible');
        ring.classList.remove('cursor-visible');
        ring.classList.remove('cursor-hover', 'cursor-card-hover', 'cursor-input-focus', 'cursor-click');
        dot.classList.remove('cursor-hover', 'cursor-card-hover', 'cursor-input-focus', 'cursor-click');
    });

    // Tactile Click Feedback
    window.addEventListener('mousedown', (e) => {
        if (e.button === 0) {
            dot.classList.add('cursor-click');
            ring.classList.add('cursor-click');
        }
    });

    window.addEventListener('mouseup', () => {
        dot.classList.remove('cursor-click');
        ring.classList.remove('cursor-click');
    });

    // Interactive Hover States (Delegated for 60fps performance across dynamic and static elements)
    document.addEventListener('mouseover', (e) => {
        const target = e.target;
        if (!target) return;

        // 1. Text Inputs, Textareas, Selects
        if (target.closest('input:not([type="submit"]):not([type="button"]), textarea, select, .modern-form-control, .form-control')) {
            ring.classList.add('cursor-input-focus');
            dot.classList.add('cursor-input-focus');
            ring.classList.remove('cursor-hover', 'cursor-card-hover');
            dot.classList.remove('cursor-hover', 'cursor-card-hover');
            return;
        }

        // 2. Clickable Links, Buttons, Interactive Badges
        if (target.closest('a, button, .btn, .btn-primary-gradient, .btn-outline-glass, .btn-social, .btn-linkedin, .btn-icon, .nav-link, .navbar-brand, .theme-toggle-btn, .btn-back-to-top, .tech-chip, .badge-tag, .breadcrumb-item a, [role="button"], input[type="submit"], input[type="button"]')) {
            ring.classList.add('cursor-hover');
            dot.classList.add('cursor-hover');
            ring.classList.remove('cursor-input-focus', 'cursor-card-hover');
            dot.classList.remove('cursor-input-focus', 'cursor-card-hover');
            return;
        }

        // 3. Clickable Cards, Artwork, Timelines, Profile Cards
        if (target.closest('.project-card, .skill-card, .discipline-card, .timeline-item, .contact-item, .contact-info-card, .profile-card, .about-portrait-card, .about-portrait-wrapper, .hero-card-wrapper, .project-artwork, .bio-narrative-card, .resume-sheet')) {
            ring.classList.add('cursor-card-hover');
            dot.classList.add('cursor-card-hover');
            ring.classList.remove('cursor-hover', 'cursor-input-focus');
            dot.classList.remove('cursor-hover', 'cursor-input-focus');
            return;
        }

        // 4. Default State (normal background/text)
        ring.classList.remove('cursor-hover', 'cursor-card-hover', 'cursor-input-focus');
        dot.classList.remove('cursor-hover', 'cursor-card-hover', 'cursor-input-focus');
    }, { passive: true });

    // Responsive resize listener (handles window resize or orientation changes)
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            if (isTouchOrSmall()) {
                dot.style.display = 'none';
                ring.style.display = 'none';
                isRunning = false;
                cancelAnimationFrame(rafId);
            } else {
                dot.style.display = '';
                ring.style.display = '';
            }
        }, 150);
    }, { passive: true });
}

/**
 * 7. Modern Viewport Scroll Reveal & Stagger System
 * Uses IntersectionObserver for 60fps buttery smooth scroll entrances.
 */
function initScrollReveal() {
    // If user prefers reduced motion or browser doesn't support IntersectionObserver
    if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        document.querySelectorAll('.reveal-on-scroll, .modern-glass-card, .project-card, .skill-card, .timeline-item, .contact-item, .bio-narrative-card, .resume-sheet').forEach(el => {
            el.classList.add('is-revealed');
        });
        return;
    }

    // Select candidate elements for smooth reveal across all pages
    const revealSelectors = [
        '.page-header',
        '.section-header',
        '.section-tag',
        '.hero-section .hero-text-col > *',
        '.hero-card-wrapper',
        '.modern-glass-card',
        '.project-card',
        '.skill-card',
        '.skill-category-block',
        '.discipline-card',
        '.timeline-item',
        '.contact-item',
        '.contact-info-card',
        '.contact-form-card',
        '.bio-narrative-card',
        '.resume-sheet',
        '.academic-quick-box',
        '.projects-meta-bar'
    ];

    const elements = document.querySelectorAll(revealSelectors.join(', '));

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-revealed');
                obs.unobserve(entry.target); // Unobserve to save CPU/battery
            }
        });
    }, {
        threshold: 0.08,
        rootMargin: '0px 0px -30px 0px'
    });

    elements.forEach((el) => {
        // Add reveal-on-scroll class if not already present
        if (!el.classList.contains('reveal-on-scroll')) {
            el.classList.add('reveal-on-scroll');
        }

        // Automatic subtle stagger for sibling grid columns and cards
        const colParent = el.closest('[class*="col-"]');
        if (colParent && colParent.parentElement && colParent.parentElement.classList.contains('row')) {
            const cols = Array.from(colParent.parentElement.children);
            const colIdx = cols.indexOf(colParent);
            if (colIdx >= 0) {
                const delayNum = (colIdx % 4) + 1;
                el.classList.add(`reveal-delay-${delayNum}`);
            }
        } else {
            const parent = el.parentElement;
            if (parent && (parent.classList.contains('row') || parent.classList.contains('d-flex'))) {
                const siblings = Array.from(parent.children);
                const childIdx = siblings.indexOf(el);
                if (childIdx > 0 && childIdx < 6) {
                    el.classList.add(`reveal-delay-${childIdx}`);
                }
            }
        }

        observer.observe(el);
    });
}


