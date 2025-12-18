// Theme Management System
// Handles dark/light mode toggle and persistence

class ThemeManager {
    constructor() {
        this.currentTheme = this.getStoredTheme() || 'light';
        this.init();
    }

    init() {
        // Apply stored theme
        this.applyTheme(this.currentTheme);

        // Create toggle button
        this.createToggleButton();

        // Listen for system theme changes
        this.watchSystemTheme();
    }

    getStoredTheme() {
        return localStorage.getItem('career-recommender-theme');
    }

    setStoredTheme(theme) {
        localStorage.setItem('career-recommender-theme', theme);
    }

    applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        this.currentTheme = theme;
        this.setStoredTheme(theme);
        this.updateToggleButton();
    }

    toggleTheme() {
        const newTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        this.applyTheme(newTheme);

        // Add animation effect
        document.body.style.transition = 'background-color 0.5s ease';
    }

    createToggleButton() {
        const button = document.createElement('button');
        button.className = 'theme-toggle';
        button.setAttribute('aria-label', 'Toggle theme');
        button.setAttribute('title', 'Toggle Dark/Light Mode');
        button.innerHTML = `<span class="icon">🌙</span>`;

        button.addEventListener('click', () => this.toggleTheme());

        document.body.appendChild(button);
        this.toggleButton = button;
    }

    updateToggleButton() {
        if (!this.toggleButton) return;

        const icon = this.toggleButton.querySelector('.icon');

        if (this.currentTheme === 'dark') {
            icon.textContent = '☀️';
            this.toggleButton.setAttribute('title', 'Switch to Light Mode');
        } else {
            icon.textContent = '🌙';
            this.toggleButton.setAttribute('title', 'Switch to Dark Mode');
        }
    }

    watchSystemTheme() {
        // Check if user prefers dark mode
        const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');

        // Only apply system theme if no stored preference
        if (!this.getStoredTheme()) {
            this.applyTheme(darkModeQuery.matches ? 'dark' : 'light');
        }

        // Listen for system theme changes
        darkModeQuery.addEventListener('change', (e) => {
            if (!this.getStoredTheme()) {
                this.applyTheme(e.matches ? 'dark' : 'light');
            }
        });
    }
}

// Initialize theme manager when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.themeManager = new ThemeManager();
    });
} else {
    window.themeManager = new ThemeManager();
}
