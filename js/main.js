(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".nav-dd").forEach(function (dd) {
    var btn = dd.querySelector(".nav-dd-toggle");
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = dd.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      document.querySelectorAll(".nav-dd").forEach(function (other) {
        if (other !== dd) {
          other.classList.remove("is-open");
          var ob = other.querySelector(".nav-dd-toggle");
          if (ob) ob.setAttribute("aria-expanded", "false");
        }
      });
    });
  });

  document.addEventListener("click", function () {
    document.querySelectorAll(".nav-dd.is-open").forEach(function (dd) {
      dd.classList.remove("is-open");
      var btn = dd.querySelector(".nav-dd-toggle");
      if (btn) btn.setAttribute("aria-expanded", "false");
    });
  });

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    document.querySelectorAll(".reveal").forEach(function (el) {
      io.observe(el);
    });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) {
      el.classList.add("is-visible");
    });
  }

  document.querySelectorAll("[data-share-url]").forEach(function (input) {
    input.value = window.location.href;
    input.addEventListener("focus", function () {
      input.select();
    });
  });
})();
