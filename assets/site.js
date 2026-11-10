(function () {
  var c = window.EW_CONFIG || {};
  document.querySelectorAll("[data-plan]").forEach(function (a) {
    var link = c.stripe && c.stripe[a.getAttribute("data-plan")];
    if (link) { a.href = link; }
  });
  var f = document.getElementById("lead-form");
  if (!f) return;
  var msg = document.getElementById("form-msg");
  f.addEventListener("submit", function (e) {
    var d = new FormData(f);
    if (c.formEndpoint) { f.action = c.formEndpoint; f.method = "POST"; return; }
    e.preventDefault();
    if (c.email) {
      var body = "";
      d.forEach(function (v, k) { body += k + " : " + v + "\n"; });
      window.location.href = "mailto:" + c.email + "?subject=" +
        encodeURIComponent("Demande de maquette gratuite") + "&body=" + encodeURIComponent(body);
      msg.textContent = "Votre messagerie s'ouvre : envoyez le message pour valider la demande.";
    } else {
      msg.textContent = "Le formulaire sera actif très prochainement.";
    }
  });
})();
