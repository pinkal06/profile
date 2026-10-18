/**
 * Pinkal Rathod – Personal Portfolio
 * Main Interactive JavaScript (Theme, Animated Typing, Smooth Scrolling, Scrollspy, Mobile Nav)
 */

document.addEventListener('DOMContentLoaded', () => {
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
