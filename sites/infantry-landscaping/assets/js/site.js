(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Photo slots: show the placeholder art until a real photo exists.
  document.querySelectorAll(".photo img").forEach((img) => {
    const fig = img.closest(".photo");
    const miss = () => fig.classList.add("is-missing");
    if (img.complete && !img.naturalWidth) miss();
    img.addEventListener("error", miss);
    img.addEventListener("load", () => fig.classList.remove("is-missing"));
  });

  const header = document.querySelector(".site-header");
  const onScroll = () => header.classList.toggle("is-stuck", scrollY > 8);
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  const menuBtn = document.querySelector(".menu-btn");
  const nav = document.getElementById("nav");
  menuBtn?.addEventListener("click", () => {
    document.documentElement.style.setProperty("--header-h", header.getBoundingClientRect().bottom + "px");
    const open = nav.classList.toggle("is-open");
    menuBtn.setAttribute("aria-expanded", String(open));
    menuBtn.querySelector("span").textContent = open ? "Close" : "Menu";
    document.body.style.overflow = open ? "hidden" : "";
  });

  document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

  const filters = document.querySelectorAll(".filters button");
  filters.forEach((btn) =>
    btn.addEventListener("click", () => {
      filters.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      const f = btn.dataset.filter;
      document.querySelectorAll(".gallery .item").forEach((it) => (it.hidden = f !== "all" && it.dataset.cat !== f));
      if (window.ScrollTrigger) ScrollTrigger.refresh();
    })
  );

  const form = document.querySelector("form.form");
  if (form) {
    const check = (input) => {
      const ok = input.checkValidity() && (!input.required || input.value.trim() !== "");
      input.closest(".field").classList.toggle("has-error", !ok);
      input.setAttribute("aria-invalid", String(!ok));
      return ok;
    };
    form.querySelectorAll("input[required], input[type=email]").forEach((i) => i.addEventListener("blur", () => i.value && check(i)));
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const bad = [...form.querySelectorAll("input[required], input[type=email]")].filter((i) => !check(i));
      if (bad.length) return bad[0].focus();
      const btn = form.querySelector("button[type=submit]");
      btn.disabled = true;
      btn.firstChild.textContent = "Sending… ";
      // When live: POST new FormData(form) to the client's form endpoint.
      setTimeout(() => {
        form.classList.add("is-done");
        form.querySelector(".done").focus();
      }, 700);
    });
  }

  if (reduce || !window.gsap) return;
  gsap.registerPlugin(ScrollTrigger, SplitText);

  // Headings rise in word by word.
  const rise = (el, delay = 0, trigger = true) => {
    const split = SplitText.create(el, { type: "lines,words", mask: "lines" });
    return gsap.from(split.words, {
      yPercent: 110,
      duration: 1,
      ease: "expo.out",
      stagger: 0.05,
      delay,
      scrollTrigger: trigger ? { trigger: el, start: "top 88%", once: true } : undefined,
    });
  };

  document.fonts.ready.then(() => {
    const hero = document.querySelector('[data-split="hero"]');
    if (hero) {
      rise(hero, 0.15, false);
      gsap.from(".hero .kick-script, .hero .accent-bar", { opacity: 0, x: -16, duration: 0.9, ease: "expo.out" });
      gsap.from(".hero-in", { opacity: 0, y: 16, duration: 0.9, ease: "expo.out", stagger: 0.1, delay: 0.55 });
      gsap.from(".hero--panel .panel", { opacity: 0, y: 30, duration: 1.1, ease: "expo.out" });
      gsap.fromTo(".hero-photo img, .hero-photo", { scale: 1.08 }, { scale: 1, duration: 1.8, ease: "expo.out" });
    }
    document.querySelectorAll("[data-split]:not([data-split=hero])").forEach((el) => rise(el));

    document.querySelectorAll(".joint").forEach((j) =>
      gsap.from(j, { clipPath: "inset(0 100% 0 0)", duration: 1.4, ease: "expo.inOut", scrollTrigger: { trigger: j, start: "top 92%", once: true } })
    );
    gsap.from(".trust .t", { opacity: 0, y: 14, duration: 0.8, ease: "expo.out", stagger: 0.08, scrollTrigger: { trigger: ".trust", start: "top 95%", once: true } });

    gsap.set(".reveal", { opacity: 0, y: 24 });
    ScrollTrigger.batch(".reveal", {
      start: "top 90%",
      once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, duration: 0.9, ease: "expo.out", stagger: 0.08, overwrite: true }),
    });
  });
})();
