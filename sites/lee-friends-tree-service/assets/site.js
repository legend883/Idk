// Mobile menu and the preview quote form.
(function () {
  var nav = document.querySelector(".nav");
  var toggle = document.querySelector(".nav-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  // Until the photo files are in assets/photos, show a plain block instead of a broken image.
  document.querySelectorAll(".shot img").forEach(function (img) {
    function miss() { img.closest(".shot").classList.add("missing"); }
    if (img.complete && !img.naturalWidth) miss();
    img.addEventListener("error", miss);
  });

  var form = document.getElementById("quote");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var phone = form.querySelector("#f-phone");
      var err = form.querySelector("#e-phone");
      var status = form.querySelector(".form-status");
      var ok = phone.value.replace(/\D/g, "").length >= 10;
      phone.setAttribute("aria-invalid", ok ? "false" : "true");
      err.hidden = ok;
      if (!ok) { phone.focus(); return; }
      // Preview only: the form is not connected to an inbox yet.
      status.textContent = "This preview form isn't connected yet. Please call (770) 466-5112 and we'll get you a quote.";
    });
  }
})();
