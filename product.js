/* Screen gallery and keyboard-accessible image viewer. No external services. */
const tabs = [...document.querySelectorAll('[role="tab"]')];
function selectTab(tab) {
  for (const item of tabs) {
    const active = item === tab;
    item.setAttribute('aria-selected', String(active));
    item.tabIndex = active ? 0 : -1;
    document.getElementById(item.getAttribute('aria-controls')).hidden = !active;
  }
}
for (const tab of tabs) {
  tab.addEventListener('click', () => selectTab(tab));
  tab.addEventListener('keydown', event => {
    let next;
    if (event.key === 'ArrowRight') next = (tabs.indexOf(tab) + 1) % tabs.length;
    if (event.key === 'ArrowLeft') next = (tabs.indexOf(tab) + tabs.length - 1) % tabs.length;
    if (event.key === 'Home') next = 0;
    if (event.key === 'End') next = tabs.length - 1;
    if (next !== undefined) { event.preventDefault(); selectTab(tabs[next]); tabs[next].focus(); }
  });
}
const viewer = document.querySelector('#image-viewer');
let opener;
for (const button of document.querySelectorAll('[data-zoom]')) {
  button.addEventListener('click', () => {
    const source = button.querySelector('img');
    const enlarged = viewer.querySelector('img');
    enlarged.src = source.src;
    enlarged.alt = source.alt;
    viewer.querySelector('p').textContent = source.alt;
    opener = button;
    viewer.showModal();
  });
}
viewer.querySelector('button').addEventListener('click', () => viewer.close());
viewer.addEventListener('click', event => { if (event.target === viewer) viewer.close(); });
viewer.addEventListener('close', () => opener?.focus({preventScroll:true}));

// Start only on screen; pause when hidden or explicitly paused by the visitor.
const assistantShapes = document.querySelector('.morph-collection');
const motionToggle = document.querySelector('[data-morph-toggle]');
if (assistantShapes && motionToggle) {
  const observer = new IntersectionObserver(entries => {
    assistantShapes.classList.toggle('morph-running', entries[0].isIntersecting);
  }, {threshold: 0.15});
  observer.observe(assistantShapes);
  const syncVisibility = () => assistantShapes.classList.toggle('morph-suspended', document.hidden);
  syncVisibility();
  document.addEventListener('visibilitychange', syncVisibility);
  motionToggle.addEventListener('click', () => {
    const paused = assistantShapes.classList.toggle('morph-paused');
    motionToggle.setAttribute('aria-pressed', String(paused));
    motionToggle.textContent = paused ? motionToggle.dataset.resumeLabel : motionToggle.dataset.pauseLabel;
  });
}
