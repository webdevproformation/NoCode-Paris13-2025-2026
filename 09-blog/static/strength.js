(function () {
  // ---- 1) Toggle show/hide password ----
  document.querySelectorAll("[data-toggle-password]").forEach(btn => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-toggle-password");
      const input = document.getElementById(id);
      if (!input) return;

      const isPassword = input.type === "password";
      input.type = isPassword ? "text" : "password";

      btn.setAttribute("aria-pressed", String(isPassword));
      btn.setAttribute("aria-label", isPassword ? "Masquer le mot de passe" : "Afficher le mot de passe");
      btn.textContent = isPassword ? "Masquer" : "Afficher";
    });
  });

  // ---- 2) Strength meter ----
  function fallbackScore(pwd) {
    // Score 0-4 (heuristique simple)
    let score = 0;
    if (!pwd) return 0;

    const length = pwd.length;
    const hasLower = /[a-z]/.test(pwd);
    const hasUpper = /[A-Z]/.test(pwd);
    const hasDigit = /\d/.test(pwd);
    const hasSymbol = /[^A-Za-z0-9]/.test(pwd);

    const variety = [hasLower, hasUpper, hasDigit, hasSymbol].filter(Boolean).length;

    if (length >= 8) score++;
    if (length >= 12) score++;
    if (variety >= 2) score++;
    if (variety >= 3 && length >= 12) score++;

    return Math.max(0, Math.min(4, score));
  }

  function labelFor(score) {
    return ["Très faible", "Faible", "Moyen", "Bon", "Fort"][score] || "—";
  }

  function colorFor(score) {
    return ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#27ae60"][score] || "#bdc3c7";
  }

  function updateMeter(input) {
    const pwd = input.value || "";
    const meter = document.querySelector(`[data-meter-for="${input.id}"]`);
    if (!meter) return;

    const bar = meter.querySelector(".password-meter-bar");
    const text = meter.querySelector(".password-meter-text");
    if (!bar || !text) return;

    // zxcvbn si présent (score 0-4), sinon fallback
    let score = 0;
    if (window.zxcvbn) {
      score = window.zxcvbn(pwd).score; // 0..4
    } else {
      score = fallbackScore(pwd);
    }

    const percent = (score / 4) * 100;
    bar.style.width = percent + "%";
    bar.style.backgroundColor = colorFor(score);
    bar.setAttribute("aria-valuenow", String(score));
    text.textContent = "Force : " + labelFor(score);
  }

  document.querySelectorAll("[data-password-input]").forEach(input => {
    input.addEventListener("input", () => updateMeter(input));
    updateMeter(input);
  });
})();