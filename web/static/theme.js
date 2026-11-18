// Shared light/dark theme toggle for both front-ends.
// The pre-paint theme is applied by a tiny inline script in each page's <head>;
// this file only wires up the toggle button (requires the DOM, loaded at body end).
(function () {
    'use strict';
    var root = document.documentElement;
    var KEY = 'cl-theme';
    var btn = document.getElementById('theme-toggle');
    if (!btn) { return; }

    function current() {
        return root.getAttribute('data-theme') ||
            (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    }

    function updateIcon() {
        var isDark = current() === 'dark';
        btn.textContent = isDark ? '☀' : '☾'; // ☀ / ☾
        btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
    }

    btn.addEventListener('click', function () {
        var next = current() === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        try { localStorage.setItem(KEY, next); } catch (e) {}
        updateIcon();
    });

    updateIcon();
})();
