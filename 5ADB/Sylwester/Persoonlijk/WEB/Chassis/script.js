document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".contact-form");
    if (form) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Bedankt voor uw bericht! We nemen zo snel mogelijk contact met u op.");
            form.reset();
        });
    }
});

// DARK MODE
const toggle = document.getElementById("theme-toggle");

function applyTheme(mode) {
    if (mode === "dark") {
        document.body.classList.add("dark");
        toggle.textContent = "☀️";
    } else {
        document.body.classList.remove("dark");
        toggle.textContent = "🌙";
    }
}

toggle.addEventListener("click", () => {
    const newMode = document.body.classList.contains("dark") ? "light" : "dark";
    localStorage.setItem("theme", newMode);
    applyTheme(newMode);
});

// Load saved theme
applyTheme(localStorage.getItem("theme") || "light");


// LANGUAGE SYSTEM
const langSelect = document.getElementById("lang-select");

async function loadLanguage(lang) {
    const res = await fetch("lang.json");
    const data = await res.json();

    for (const id in data[lang]) {
        const el = document.getElementById(id);
        if (el) el.textContent = data[lang][id];
    }

    localStorage.setItem("lang", lang);
}

langSelect.addEventListener("change", () => {
    loadLanguage(langSelect.value);
});

// Load saved language
const savedLang = localStorage.getItem("lang") || "nl";
langSelect.value = savedLang;
loadLanguage(savedLang);