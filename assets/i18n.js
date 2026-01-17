/**
 * Simple i18n (internationalization) utility for Kids Games
 * 
 * Usage:
 * 1. Include this script in your HTML: <script src="assets/i18n.js"></script>
 * 2. Define translations object in your game script
 * 3. Call initI18n(translations) to initialize
 * 4. Use data-i18n attributes in HTML elements
 * 5. Use t(key) function to get translated strings in JavaScript
 */

class I18n {
    constructor() {
        this.currentLang = localStorage.getItem('kidsGamesLang') || 'en';
        this.translations = {};
        this.gameName = '';
    }

    init(translations, gameName = 'game') {
        this.translations = translations;
        this.gameName = gameName;
        
        // Add language switcher if not exists
        if (!document.querySelector('.lang-switcher')) {
            this.addLanguageSwitcher();
        }
        
        // Apply saved language
        this.switchLanguage(this.currentLang);
        
        // Set up lang buttons
        this.setupLangButtons();
    }

    addLanguageSwitcher() {
        const switcher = document.createElement('div');
        switcher.className = 'lang-switcher';
        switcher.innerHTML = `
            <button class="lang-btn" data-lang="en">English</button>
            <button class="lang-btn" data-lang="ja">日本語</button>
        `;
        
        // Add styles
        const style = document.createElement('style');
        style.textContent = `
            .lang-switcher {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 10000;
                display: flex;
                gap: 5px;
                background: rgba(0, 0, 0, 0.8);
                padding: 8px;
                border-radius: 20px;
                border: 2px solid #333;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            }

            .lang-btn {
                background: linear-gradient(145deg, #2a2a2a, #1a1a1a);
                color: #999;
                border: 2px solid #333;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 15px;
                cursor: pointer;
                transition: all 0.3s;
                font-family: 'Arial', sans-serif;
            }

            .lang-btn:hover {
                border-color: #ffd700;
                color: #ffd700;
            }

            .lang-btn.active {
                background: linear-gradient(145deg, #ffd700, #ffed4e);
                color: #000;
                border-color: #ffd700;
                box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
            }

            @media (max-width: 768px) {
                .lang-switcher {
                    top: 10px;
                    right: 10px;
                    padding: 5px;
                }
                .lang-btn {
                    padding: 6px 12px;
                    font-size: 12px;
                }
            }
        `;
        
        document.head.appendChild(style);
        document.body.insertBefore(switcher, document.body.firstChild);
    }

    setupLangButtons() {
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                this.switchLanguage(btn.dataset.lang);
            });
        });
    }

    switchLanguage(lang) {
        this.currentLang = lang;
        localStorage.setItem('kidsGamesLang', lang);
        localStorage.setItem(`${this.gameName}Lang`, lang);
        
        // Update active button
        document.querySelectorAll('.lang-btn').forEach(btn => {
            if (btn.dataset.lang === lang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
        
        // Update all translatable elements
        this.updateTranslations();
        
        // Dispatch event for custom handling
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
    }

    updateTranslations() {
        // Update elements with data-i18n attribute
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.dataset.i18n;
            const text = this.t(key);
            if (text) {
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    el.placeholder = text;
                } else {
                    el.textContent = text;
                }
            }
        });

        // Update elements with data-i18n-html attribute (for HTML content)
        document.querySelectorAll('[data-i18n-html]').forEach(el => {
            const key = el.dataset.i18nHtml;
            const text = this.t(key);
            if (text) {
                el.innerHTML = text;
            }
        });
    }

    t(key) {
        const keys = key.split('.');
        let value = this.translations[this.currentLang];
        
        for (const k of keys) {
            if (value && value[k] !== undefined) {
                value = value[k];
            } else {
                console.warn(`Translation key not found: ${key} for language: ${this.currentLang}`);
                return key;
            }
        }
        
        return value;
    }

    getCurrentLang() {
        return this.currentLang;
    }
}

// Create global instance
const i18n = new I18n();

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = I18n;
}
