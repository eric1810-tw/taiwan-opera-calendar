/* 台灣戲曲演出行事曆前端邏輯。 */
let eventsData = [];
let currentFilter = 'all';
let currentRegion = 'all';
let currentType = 'all';
let currentKeyword = '';
let reportReturnFocus = null;

const eventsContainer = document.getElementById('eventsContainer');
const emptyView = document.getElementById('emptyView');
const filteredStats = document.getElementById('filteredStats');
const regionSelect = document.getElementById('regionSelect');
const typeSelect = document.getElementById('typeSelect');
const keywordSearch = document.getElementById('keywordSearch');
const chips = [...document.querySelectorAll('#multiRowChips .chip')];
const namedQuickFilters = chips.map(chip => chip.dataset.filter)
  .filter(filter => filter !== 'all' && !filter.startsWith('其他'))
  .flatMap(filter => filter.split('*'));
const loadingView = document.getElementById('loadingView');
const loadError = document.getElementById('loadError');
const reportModal = document.getElementById('reportModal');

function escapeHTML(value) {
  return String(value ?? '').replace(/[&<>"']/g, character => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  })[character]);
}

function safeExternalURL(value) {
  try {
    const url = new URL(String(value || ''), location.href);
    return url.protocol === 'https:' ? url.href : '#';
  } catch (_) {
    return '#';
  }
}

function getTaiwanToday() {
  const testDate = new URLSearchParams(location.search).get('today');
  if (['localhost', '127.0.0.1'].includes(location.hostname) && /^\d{4}-\d{2}-\d{2}$/.test(testDate || '')) {
    return testDate;
  }
  const parts = new Intl.DateTimeFormat('en-US', {
    timeZone: 'Asia/Taipei', year: 'numeric', month: '2-digit', day: '2-digit'
  }).formatToParts(new Date());
  const part = type => parts.find(item => item.type === type).value;
  return `${part('year')}-${part('month')}-${part('day')}`;
}

function dateDifference(later, earlier) {
  const [ly, lm, ld] = later.split('-').map(Number);
  const [ey, em, ed] = earlier.split('-').map(Number);
  return (Date.UTC(ly, lm - 1, ld) - Date.UTC(ey, em - 1, ed)) / 86400000;
}

function isISODate(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const [year, month, day] = value.split('-').map(Number);
  const date = new Date(Date.UTC(year, month - 1, day));
  return date.getUTCFullYear() === year && date.getUTCMonth() === month - 1 && date.getUTCDate() === day;
}

function getDaysBadge(event) {
  const today = getTaiwanToday();
  const endDate = event.endDate || event.date;
  const daysAway = Math.max(0, dateDifference(event.date, today));
  if (event.date <= today && endDate >= today) {
    const hasContinuousDateRange = /\d{1,2}日?\s*[–—~～至到]\s*(?:\d{1,2}月?\s*)?\d{1,2}/.test(event.dateFormatted || '');
    const label = hasContinuousDateRange || event.date === today ? '演出中' : '期間內・詳見場次日期';
    return `<span class="text-[10px] font-bold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded border border-emerald-200">${label}</span>`;
  }
  if (daysAway <= 7) {
    return `<span class="text-[10px] font-bold text-[#d80b72] bg-red-100/80 px-2 py-0.5 rounded border border-red-200">🔥 還有 ${daysAway} 天</span>`;
  }
  if (daysAway <= 21) {
    return `<span class="text-[10px] font-bold text-amber-800 bg-amber-100/70 px-2 py-0.5 rounded border border-amber-200">倒數 ${daysAway} 天</span>`;
  }
  return `<span class="text-[10px] font-bold text-stone-500 bg-stone-100 px-2 py-0.5 rounded">${daysAway} 天後</span>`;
}

function getVerificationLabel(event) {
  if (event.verifyStatus !== 'verified') return escapeHTML(event.verifyLabel || '⏳ 待核實');
  try {
    const source = new URL(event.sourceUrl || event.link);
    return source.protocol === 'https:' && event.verifyLabel
      ? escapeHTML(event.verifyLabel)
      : '⏳ 演出來源頁待補';
  } catch (_) {
    return '⏳ 演出來源頁待補';
  }
}

function changeTheme(themeName) {
  if (!['crimson-classic', 'purple-regal', 'literati-ink'].includes(themeName)) return;
  document.documentElement.setAttribute('data-theme', themeName);
  try { localStorage.setItem('opera-theme', themeName); } catch (_) { /* 儲存空間停用時仍可切換主題。 */ }
  document.querySelectorAll('[data-theme-choice]').forEach(button => {
    const selected = button.dataset.themeChoice === themeName;
    button.classList.toggle('theme-selected', selected);
    button.setAttribute('aria-pressed', String(selected));
  });
}

function matchesQuickFilter(event, filter) {
  if (filter === 'all') return true;
  const fields = [...(event.tags || []), event.troupe, event.artist, event.genre];
  if (filter.startsWith('其他')) {
    const genre = filter.replace('其他', '');
    if (event.genre !== genre && !fields.some(value => typeof value === 'string' && value.includes(filter))) return false;
    return !namedQuickFilters.some(name => fields.some(value => typeof value === 'string' && value.includes(name)));
  }
  return filter.split('*').some(alias => fields.some(value => typeof value === 'string' && value.includes(alias)));
}

function renderEvents() {
  const filtered = [...eventsData]
    .sort((a, b) => a.date.localeCompare(b.date) || a.title.localeCompare(b.title, 'zh-Hant'))
    .filter(event => {
      if (!matchesQuickFilter(event, currentFilter)) return false;
      if (currentRegion !== 'all' && (!event.region || !event.region.includes(currentRegion))) return false;
      if (currentType !== 'all' && event.badgeType !== currentType) return false;
      if (currentKeyword) {
        const searchable = [event.title, event.troupe, event.artist, event.location, event.date, event.dateFormatted,
          event.time, event.description, event.genre, event.region, ...(event.tags || [])]
          .map(value => String(value ?? '').toLocaleLowerCase('zh-TW')).join(' ');
        if (!currentKeyword.split(/\s+/).every(term => searchable.includes(term))) return false;
      }
      return true;
    });

  const verifiedCount = filtered.filter(event => event.verifyStatus === 'verified').length;
  const pendingCount = filtered.filter(event => event.verifyStatus === 'pending').length;
  const communityCount = filtered.filter(event => event.verifyStatus === 'community').length;
  filteredStats.textContent = `共 ${filtered.length} 筆節目卡片：已核實 ${verifiedCount}・待確認 ${pendingCount}・社群來源 ${communityCount}`;
  if (!filtered.length) {
    eventsContainer.innerHTML = '';
    emptyView.classList.remove('hidden');
    return;
  }

  emptyView.classList.add('hidden');
  eventsContainer.innerHTML = filtered.map(event => `
    <article class="opera-card rounded-2xl p-4 transition duration-200 flex flex-col justify-between">
      <div>
        <div class="flex items-center justify-between gap-1.5 mb-1.5">
          <div class="flex items-center gap-1.5 flex-wrap">
            <span class="text-xs font-bold text-[#d80b72] bg-[#d80b72]/10 px-2.5 py-0.5 rounded-full border border-[#d80b72]/20">${escapeHTML(event.troupe || '主辦單位待核實')}</span>
            <span class="text-[10px] font-semibold ${event.verifyStatus === 'verified' && getVerificationLabel(event).startsWith('🛡️') ? 'text-emerald-700 bg-emerald-50 border-emerald-200' : 'text-amber-800 bg-amber-50 border-amber-200'} px-2 py-0.5 rounded-full border">${getVerificationLabel(event)}</span>
          </div>
          <div class="shrink-0">${getDaysBadge(event)}</div>
        </div>
        <h2 class="text-base font-bold serif-title text-stone-900 leading-snug mb-1">${escapeHTML(event.title)}</h2>
        ${event.verifyStatus === 'pending' ? '<p class="text-[11px] font-bold text-amber-900 bg-amber-100 border border-amber-200 rounded-lg px-2 py-1 mb-2">自動發現候選・尚未核實劇種與演出資訊</p>' : ''}
        <div class="text-xs text-stone-700 font-medium mb-2 bg-stone-50 px-2 py-1 rounded-lg"><span class="text-amber-800 font-semibold">🎭 主演：</span><span>${escapeHTML(event.artist)}</span></div>
        <div class="space-y-1 text-xs text-stone-600 mb-2.5">
          <div class="flex items-start gap-1"><span class="text-[#d80b72] font-semibold shrink-0">🗓️ 日期時間：</span><span class="font-medium text-stone-800">${escapeHTML(event.dateFormatted)} ｜ ${escapeHTML(event.time)}</span></div>
          <div class="flex items-start gap-1"><span class="text-[#d80b72] font-semibold shrink-0">📍 演出地點：</span><a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(event.location || '')}" target="_blank" rel="noopener noreferrer" class="text-stone-700 underline decoration-stone-300 hover:text-[#d80b72]">${escapeHTML(event.location || '演出地點待核實')}</a></div>
        </div>
        <p class="text-xs text-stone-500 leading-relaxed mb-3">${escapeHTML(event.description || '由文化部公開資料發現，詳細內容待人工核對官方公告。')}</p>
      </div>
      <div class="pt-2 border-t border-stone-100 flex items-center justify-between gap-2 mt-auto">
        <button type="button" data-report-title="${escapeHTML(event.title)}" class="report-event text-[11px] text-stone-400 hover:text-[#d80b72] py-1">⚠️ 回報資訊有誤</button>
        <a href="${escapeHTML(safeExternalURL(event.link))}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-xs font-bold px-3.5 py-1.5 rounded-xl accent-btn shadow-sm transition active:scale-95">
          <span>${escapeHTML(event.verifyStatus === 'pending' ? '查看來源線索' : (event.linkLabel || '官方購票 / 詳情'))}</span>
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>
      </div>
    </article>`).join('');
  eventsContainer.querySelectorAll('.report-event').forEach(button => {
    button.addEventListener('click', () => openReportModal(button.dataset.reportTitle, button));
  });
}

function selectFilter(selectedChip) {
  chips.forEach(chip => {
    const selected = chip === selectedChip;
    chip.classList.toggle('chip-active', selected);
    chip.classList.toggle('bg-white', !selected);
    chip.classList.toggle('text-stone-700', !selected);
    chip.classList.toggle('border-stone-300', !selected);
    chip.setAttribute('aria-pressed', String(selected));
  });
  currentFilter = selectedChip.dataset.filter;
  renderEvents();
}

function resetAllFilters() {
  currentRegion = 'all';
  currentType = 'all';
  currentKeyword = '';
  regionSelect.value = 'all';
  typeSelect.value = 'all';
  keywordSearch.value = '';
  selectFilter(chips.find(chip => chip.dataset.filter === 'all'));
}

function openReportModal(showTitle, trigger = document.activeElement) {
  reportReturnFocus = trigger;
  document.getElementById('reportTargetTitle').textContent = `針對演出：${showTitle}`;
  reportModal.classList.remove('hidden');
  reportModal.setAttribute('aria-hidden', 'false');
  document.getElementById('reportReason').focus();
}

function closeReportDialog() {
  reportModal.classList.add('hidden');
  reportModal.setAttribute('aria-hidden', 'true');
  if (reportReturnFocus && document.contains(reportReturnFocus)) reportReturnFocus.focus();
}

function submitReport(event) {
  event.preventDefault();
  const reason = document.getElementById('reportReason').value;
  const detail = document.getElementById('reportDetail').value;
  const target = document.getElementById('reportTargetTitle').textContent;
  const issueTitle = encodeURIComponent(`[演出回報] ${target} - ${reason}`);
  const issueBody = encodeURIComponent(`### 回報目標\n${target}\n\n### 原因\n${reason}\n\n### 詳情與來源\n${detail}`);
  window.location.assign(`https://github.com/eric1810-tw/taiwan-opera-calendar/issues/new?title=${issueTitle}&body=${issueBody}`);
}

function validateEvent(event) {
  const requiredText = ['id', 'date', 'dateFormatted', 'time', 'troupe', 'genre', 'artist', 'title', 'location', 'description', 'link'];
  const validGenres = new Set(['歌仔戲', '布袋戲', '音樂劇', '其他歌仔戲', '其他布袋戲', '其他音樂劇']);
  const validStatuses = new Set(['verified', 'community', 'pending']);
  const validBadges = new Set(['ticket', 'free', 'temple', 'plan']);
  const validRegions = new Set(['北部', '中部', '南部', '東部', '未分類']);
  if (!event || typeof event !== 'object' || Array.isArray(event)) return '不是物件';
  if (requiredText.some(key => typeof event[key] !== 'string')) return '必要文字欄位缺漏或型態錯誤';
  if (!isISODate(event.date)) return 'date 不是有效 YYYY-MM-DD 日期';
  if (event.endDate !== undefined && (!isISODate(event.endDate) || event.endDate < event.date)) return 'endDate 無效或早於 date';
  if (!validGenres.has(event.genre) || !validStatuses.has(event.verifyStatus)
    || !validBadges.has(event.badgeType) || !validRegions.has(event.region)) return '劇種、來源狀態、類型或地區無效';
  if (!Number.isInteger(event.daysAway) || event.daysAway < 0) return 'daysAway 無效';
  if (!Array.isArray(event.tags) || event.tags.some(tag => typeof tag !== 'string')) return 'tags 必須為字串陣列';
  return null;
}

async function loadSchedule() {
  loadingView.classList.remove('hidden');
  loadError.classList.add('hidden');
  eventsContainer.classList.remove('hidden');
  emptyView.classList.add('hidden');
  loadLastUpdated();
  try {
    const response = await fetch('./data/schedule.json', { cache: 'no-cache' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    if (!Array.isArray(data)) throw new Error('資料根節點不是陣列');
    const valid = [];
    data.forEach((event, index) => {
      const reason = validateEvent(event);
      if (reason) {
        console.warn(`略過格式錯誤的場次 id=${event?.id ?? `index:${index}`}：${reason}`);
      } else {
        valid.push(event);
      }
    });
    if (!valid.length) throw new Error('沒有任何格式正確的場次');
    const today = getTaiwanToday();
    eventsData = valid.filter(event => (event.endDate || event.date) >= today);
    loadingView.classList.add('hidden');
    eventsContainer.classList.remove('hidden');
    renderEvents();
  } catch (error) {
    console.error('Schedule load failed:', error);
    loadingView.classList.add('hidden');
    document.getElementById('loadErrorMessage').textContent = location.protocol === 'file:'
      ? '直接以 file:// 開啟無法讀取 JSON。'
      : '網路暫時無法載入演出資料，請稍後重試。';
    loadError.classList.remove('hidden');
  }
}

async function loadLastUpdated() {
  const label = document.getElementById('lastUpdated');
  try {
    const response = await fetch('./data/metadata.json', { cache: 'no-cache' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const metadata = await response.json();
    const timestamp = new Date(metadata.lastUpdated);
    if (!Number.isFinite(timestamp.getTime())) throw new Error('更新時間無效');
    const formatted = new Intl.DateTimeFormat('zh-TW', {
      timeZone: 'Asia/Taipei', year: 'numeric', month: '2-digit', day: '2-digit',
      hour: '2-digit', minute: '2-digit', hourCycle: 'h23'
    }).format(timestamp);
    label.textContent = `資料最後更新時間：${formatted}（台灣時間）`;
  } catch (error) {
    console.warn('Last-updated metadata unavailable:', error);
    label.textContent = '資料最後更新時間：目前無法取得';
  }
}

chips.forEach(chip => chip.addEventListener('click', () => selectFilter(chip)));
regionSelect.addEventListener('change', event => { currentRegion = event.target.value; renderEvents(); });
typeSelect.addEventListener('change', event => { currentType = event.target.value; renderEvents(); });
keywordSearch.addEventListener('input', event => {
  currentKeyword = event.target.value.trim().toLocaleLowerCase('zh-TW');
  renderEvents();
});
document.getElementById('resetFilters').addEventListener('click', resetAllFilters);
document.getElementById('retryLoad').addEventListener('click', loadSchedule);
document.getElementById('openGeneralReport').addEventListener('click', event => openReportModal('一般演出提報', event.currentTarget));
document.getElementById('closeReportModal').addEventListener('click', closeReportDialog);
document.getElementById('cancelReport').addEventListener('click', closeReportDialog);
document.getElementById('reportForm').addEventListener('submit', submitReport);
document.querySelectorAll('[data-theme-choice]').forEach(button => {
  button.addEventListener('click', () => changeTheme(button.dataset.themeChoice));
});
reportModal.addEventListener('click', event => { if (event.target === reportModal) closeReportDialog(); });
document.addEventListener('keydown', event => {
  if (reportModal.classList.contains('hidden')) return;
  if (event.key === 'Escape') {
    closeReportDialog();
    return;
  }
  if (event.key === 'Tab') {
    const focusable = [...reportModal.querySelectorAll('button, input, select, textarea, a[href], [tabindex]:not([tabindex="-1"])')]
      .filter(element => !element.disabled && element.getClientRects().length);
    if (!focusable.length) {
      event.preventDefault();
      reportModal.focus();
      return;
    }
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && (document.activeElement === first || !reportModal.contains(document.activeElement))) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && (document.activeElement === last || !reportModal.contains(document.activeElement))) {
      event.preventDefault();
      first.focus();
    }
  }
});

try {
  const savedTheme = localStorage.getItem('opera-theme');
  if (savedTheme) changeTheme(savedTheme);
} catch (_) { /* 儲存空間停用時使用預設主題。 */ }
loadSchedule();
