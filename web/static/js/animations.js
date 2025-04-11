import { gsap } from "gsap";

// Анимация шапки при скролле
window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    gsap.to(header, {
        height: window.scrollY > 20 ? "60px" : "80px",
        boxShadow: window.scrollY > 20 ? "0 4px 12px rgba(0,0,0,0.1)" : "none",
        duration: 0.3
    });
});

// Skeleton-загрузка
export function showSkeleton() {
    gsap.fromTo(".skeleton",
        { opacity: 0.3 },
        { opacity: 0.6, duration: 1, repeat: -1, yoyo: true }
    );
}