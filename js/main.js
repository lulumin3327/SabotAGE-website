const $ = (s, r = document) => [...r.querySelectorAll(s)];
$('.menu-btn').forEach(b => b.onclick = () => { const u = document.getElementById('menu'); const o = u.classList.toggle('open'); b.setAttribute('aria-expanded', o) });
// 篩選：.chips[data-target=#id]，按鈕 data-f，項目 data-cat
$('.chips[data-target]').forEach(g => {
  const items = $('[data-cat]', document.querySelector(g.dataset.target));
  $('.chip', g).forEach(c => c.onclick = () => {
    $('.chip', g).forEach(x => x.setAttribute('aria-pressed', x === c));
    items.forEach(i => i.hidden = c.dataset.f !== 'all' && i.dataset.cat !== c.dataset.f)
  })
});
// 分頁籤
$('[data-tabs]').forEach(t => $('[role=tab]', t).forEach(b => b.onclick = () => {
  $('[role=tab]', t).forEach(x => x.setAttribute('aria-selected', x === b));
  $('[role=tabpanel]').forEach(p => { if (p.dataset.group === t.dataset.tabs) p.hidden = p.id !== b.dataset.t })
}));
// 現實／特殊空間
$('[data-space]').forEach(b => b.onclick = () => {
  document.body.dataset.space = b.dataset.space;
  $('[data-space]').forEach(x => x.setAttribute('aria-pressed', x === b))
});
// 地塊
const map = document.getElementById('tilemap');
if (map) {
  $('button', map).forEach(b => b.onclick = () => {
    $('button', map).forEach(x => x.setAttribute('aria-pressed', x === b));
    document.getElementById('tile-name').textContent = b.dataset.n;
    document.getElementById('tile-state').textContent = map.classList.contains('damaged') ? '目前狀態：損毀（待補說明）' : '目前狀態：完好（待補說明）'
  });
  const t = document.getElementById('toggle-state');
  t.onclick = () => { const d = map.classList.toggle('damaged'); t.textContent = d ? '切換為完好' : '切換為損毀'; t.setAttribute('aria-pressed', d) }
}
