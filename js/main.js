// js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Hero Slider (only on index.html)
    const heroSection = document.querySelector('.hero-slider');
    const dots = document.querySelectorAll('.slider-dot');
    if (heroSection && dots.length) {
        const images = [
            'images/hero1.jpg',
            'images/hero2.jpg',
            'images/hero3.jpg',
            'images/hero4.jpg',
            'images/hero5.jpg',
            'images/hero6.jpg',
            'images/hero7.jpg'
        ];
        let current = 0;

        function updateSlide(index) {
            heroSection.style.backgroundImage = `url('${images[index]}')`;
            dots.forEach((dot, i) => {
                dot.classList.toggle('bg-white', i === index);
                dot.classList.toggle('bg-gray-400', i !== index);
            });
            current = index;
        }

        // Click dots
        dots.forEach((dot, i) => dot.addEventListener('click', () => updateSlide(i)));

        // Auto-advance
        setInterval(() => {
            updateSlide((current + 1) % images.length);
        }, 5000);
    }

    // Highlight active page in navigation (simple example)
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});
