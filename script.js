function setLens(mode){
  document.body.setAttribute('data-lens', mode);
  document.getElementById('btn-exec').classList.toggle('active', mode === 'exec');
  document.getElementById('btn-builder').classList.toggle('active', mode === 'builder');
  document.getElementById('lede-exec').classList.toggle('active', mode === 'exec');
  document.getElementById('lede-builder').classList.toggle('active', mode === 'builder');
}

function toggleCase(headEl){
  var caseEl = headEl.parentElement;
  var isOpen = caseEl.classList.contains('open');
  caseEl.classList.toggle('open');
  headEl.querySelector('.case-toggle').textContent = isOpen ? '+' : '−';
}

function loadEmbed(btn, id, url){
  var wrap = document.getElementById(id);
  if(wrap.classList.contains('show')){
    wrap.classList.remove('show');
    wrap.innerHTML = '';
    btn.textContent = 'View live dashboard';
    return;
  }
  wrap.innerHTML = '<iframe src="' + url + '" loading="lazy" allowfullscreen></iframe>';
  wrap.classList.add('show');
  btn.textContent = 'Hide dashboard';
}

/* Stat counters, animate once on scroll into view */
(function(){
  var stats = document.querySelectorAll('.stat .num');
  var done = false;
  function animate(){
    if(done) return;
    var strip = document.querySelector('.stat-strip');
    if(!strip) return;
    var rect = strip.getBoundingClientRect();
    if(rect.top > window.innerHeight * 0.9) return;
    done = true;
    stats.forEach(function(el){
      var target = parseFloat(el.getAttribute('data-count'));
      var prefix = el.getAttribute('data-prefix') || '';
      var suffix = el.getAttribute('data-suffix') || '';
      var isDecimal = target % 1 !== 0;
      var duration = 900; var startTime = null;
      function step(ts){
        if(!startTime) startTime = ts;
        var progress = Math.min((ts - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        var current = target * eased;
        el.textContent = prefix + (isDecimal ? current.toFixed(1) : Math.round(current)) + suffix;
        if(progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
    window.removeEventListener('scroll', animate);
  }
  window.addEventListener('scroll', animate);
  animate();
})();

/* Whole-band reveal on scroll — one motion per section, not per card */
(function(){
  var els = document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    els.forEach(function(el){ io.observe(el); });
  } else {
    els.forEach(function(el){ el.classList.add('in'); });
  }
})();

/* Subtle hero parallax */
(function(){
  var el = document.getElementById('hero-parallax');
  if(!el) return;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduced) return;
  window.addEventListener('scroll', function(){
    var y = window.scrollY;
    if(y < 600){
      el.style.transform = 'translateY(' + (y * 0.16) + 'px)';
      el.style.opacity = Math.max(1 - y / 520, 0);
    }
  });
})();

/* Magnetic cursor dot — desktop only, one deliberate interaction moment */
(function(){
  if(window.matchMedia('(hover: none)').matches) return;
  var dot = document.createElement('div');
  dot.id = 'cursor-dot';
  document.body.appendChild(dot);
  var shown = false;
  window.addEventListener('mousemove', function(e){
    dot.style.left = e.clientX + 'px';
    dot.style.top = e.clientY + 'px';
    if(!shown){ dot.classList.add('show'); shown = true; }
  });
  var targets = document.querySelectorAll('a, button, .case-head');
  targets.forEach(function(t){
    t.addEventListener('mouseenter', function(){ dot.classList.add('big'); });
    t.addEventListener('mouseleave', function(){ dot.classList.remove('big'); });
  });
})();
