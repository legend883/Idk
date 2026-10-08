(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Photo slots: show the stone placeholder until a real photo exists.
  document.querySelectorAll(".photo img").forEach((img) => {
    const fig = img.closest(".photo");
    const miss = () => fig.classList.add("is-missing");
    if (img.complete && !img.naturalWidth) miss();
    img.addEventListener("error", miss);
    img.addEventListener("load", () => fig.classList.remove("is-missing"));
  });

  // Header state + mobile menu
  const header = document.querySelector(".site-header");
  const onScroll = () => header.classList.toggle("is-stuck", scrollY > 8);
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  const menuBtn = document.querySelector(".menu-btn");
  const nav = document.getElementById("nav");
  menuBtn?.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    menuBtn.setAttribute("aria-expanded", String(open));
    menuBtn.querySelector("span").textContent = open ? "Close" : "Menu";
    document.body.style.overflow = open ? "hidden" : "";
  });

  document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

  // Work filters
  const filters = document.querySelectorAll(".filters button");
  filters.forEach((btn) =>
    btn.addEventListener("click", () => {
      filters.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      const f = btn.dataset.filter;
      document.querySelectorAll(".gallery .item").forEach((it) => {
        it.hidden = f !== "all" && it.dataset.cat !== f;
      });
      if (window.ScrollTrigger) ScrollTrigger.refresh();
    })
  );

  // Consultation form
  const form = document.querySelector("form.form");
  if (form) {
    const check = (input) => {
      const field = input.closest(".field");
      const ok = input.checkValidity() && (!input.required || input.value.trim() !== "");
      field.classList.toggle("has-error", !ok);
      input.setAttribute("aria-invalid", String(!ok));
      return ok;
    };
    form.querySelectorAll("input[required], input[type=email]").forEach((i) =>
      i.addEventListener("blur", () => i.value && check(i))
    );
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const inputs = [...form.querySelectorAll("input[required], input[type=email]")];
      const bad = inputs.filter((i) => !check(i));
      if (bad.length) return bad[0].focus();
      const btn = form.querySelector("button[type=submit]");
      btn.disabled = true;
      btn.firstChild.textContent = "Sending… ";
      // TODO when live: POST new FormData(form) to the client's form endpoint.
      setTimeout(() => {
        form.classList.add("is-done");
        form.querySelector(".done").focus();
      }, 700);
    });
  }

  // ── Motion ──
  if (reduce || !window.gsap) return;
  gsap.registerPlugin(ScrollTrigger, SplitText);

  const CUT = getComputedStyle(document.documentElement).getPropertyValue("--cut-shadow").trim();
  const flat = "0 0 0 rgba(255,255,255,0), 0 0 0 rgba(0,0,0,0)";

  // Signature: headings chisel in letter by letter, then the cut deepens.
  const chisel = (el, delay = 0, trigger = true) => {
    const split = SplitText.create(el, { type: "words,chars", charsClass: "char" });
    const finalShadow = getComputedStyle(el).textShadow;
    const tl = gsap.timeline({
      delay,
      scrollTrigger: trigger ? { trigger: el, start: "top 85%", once: true } : undefined,
    });
    tl.from(split.chars, {
      opacity: 0,
      yPercent: -22,
      filter: "blur(4px)",
      duration: 0.7,
      ease: "expo.out",
      stagger: { each: Math.min(0.045, 0.9 / split.chars.length) },
    }).fromTo(el, { textShadow: flat }, { textShadow: finalShadow === "none" ? CUT : finalShadow, duration: 0.9, ease: "power2.out", clearProps: "textShadow" }, "<0.15");
    return tl;
  };

  document.fonts.ready.then(() => {
    const hero = document.querySelector('[data-chisel="hero"]');
    if (hero) {
      chisel(hero, 0.1, false);
      gsap.from(".slab .inscr span", { opacity: 0, y: 8, duration: 0.8, ease: "expo.out", stagger: 0.12, delay: 0.55 });
      gsap.from(".slab .rule", { scaleX: 0, transformOrigin: "left", duration: 1.1, ease: "expo.out", delay: 0.7 });
      gsap.from(".hero-in", { opacity: 0, y: 14, duration: 0.9, ease: "expo.out", stagger: 0.1, delay: 0.85 });
      gsap.from(".hero-photo", { clipPath: "inset(100% 0 0 0)", duration: 1.4, ease: "expo.inOut", delay: 0.2 });
      gsap.to(".hero-photo img", { yPercent: 8, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
    }
    document.querySelectorAll("[data-chisel]:not([data-chisel=hero])").forEach((el) => chisel(el));

    // Brick courses lay in course by course.
    document.querySelectorAll(".courses").forEach((c) =>
      gsap.from(c.children, {
        scaleX: 0,
        transformOrigin: (i) => (i % 2 ? "right" : "left"),
        duration: 1.1,
        ease: "expo.out",
        stagger: 0.14,
        scrollTrigger: { trigger: c, start: "top 92%", once: true },
      })
    );

    gsap.set(".reveal", { opacity: 0, y: 22 });
    ScrollTrigger.batch(".reveal", {
      start: "top 90%",
      once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, duration: 0.9, ease: "expo.out", stagger: 0.08, overwrite: true }),
    });
  });
})();
