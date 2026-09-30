#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const schedulePath = path.join(__dirname, '..', 'data', 'schedule.json');
const events = JSON.parse(fs.readFileSync(schedulePath, 'utf8'));
const dateToken = /(?:(20\d{2})\s*[/年.-]\s*)?(\d{1,2})\s*[/月.-]\s*(\d{1,2})/g;
const rangeSeparator = /[–—~～至到]/;

function isISODate(value) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const [year, month, day] = value.split('-').map(Number);
  const date = new Date(Date.UTC(year, month - 1, day));
  return date.getUTCFullYear() === year && date.getUTCMonth() === month - 1 && date.getUTCDate() === day;
}

function addDays(value, amount) {
  const [year, month, day] = value.split('-').map(Number);
  const date = new Date(Date.UTC(year, month - 1, day + amount));
  return date.toISOString().slice(0, 10);
}

function parseEventDates(event) {
  const text = String(event.dateFormatted || '').split('(原公告', 1)[0].split('（原公告', 1)[0];
  const matches = [...text.matchAll(dateToken)];
  const dates = [];
  let previous = null;
  for (const match of matches) {
    let year = Number(match[1] || (previous || event.date).slice(0, 4));
    const month = Number(match[2]);
    const day = Number(match[3]);
    if (previous && !match[1] && (year * 100 + month) < (Number(previous.slice(0, 4)) * 100 + Number(previous.slice(5, 7)))) {
      year += 1;
    }
    const current = `${year.toString().padStart(4, '0')}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
    if (!isISODate(current) || (previous && current < previous)) return null;
    dates.push(current);
    previous = current;
  }
  if (dates.length < 2 || dates[0] !== event.date) return null;
  const ranges = [];
  for (let index = 1; index < matches.length; index += 1) {
    const previousMatch = matches[index - 1];
    const separator = text.slice(previousMatch.index + previousMatch[0].length, matches[index].index);
    if (rangeSeparator.test(separator)) ranges.push([dates[index - 1], dates[index]]);
  }
  return { dates, ranges };
}

function isScheduledToday(event, today) {
  const parsed = parseEventDates(event);
  if (!parsed) return today === event.date || today === (event.endDate || event.date);
  if (parsed.dates.includes(today)) return true;
  return parsed.ranges.some(([start, end]) => start <= today && today <= end);
}

function labelFor(event, today) {
  if (event.date <= today && (event.endDate || event.date) >= today) {
    return isScheduledToday(event, today) ? '演出中' : '期間內・詳見場次日期';
  }
  return '不在活動期間';
}

let failures = 0;
const multiDayEvents = events.filter(event => event.endDate && event.endDate !== event.date);
console.log(`多日場次：${multiDayEvents.length} 筆`);
for (const event of multiDayEvents) {
  console.log(`\n${event.id} | ${event.title} | ${event.dateFormatted}`);
  for (let today = event.date; today <= event.endDate; today = addDays(today, 1)) {
    const label = labelFor(event, today);
    console.log(`${today} -> ${label}`);
  }
}

function requireLabel(description, predicate, expected) {
  const event = multiDayEvents.find(predicate.event);
  const actual = event ? labelFor(event, predicate.date) : '找不到場次';
  console.log(`\n驗收 ${description}: ${actual}`);
  if (actual !== expected) {
    console.error(`FAIL: 預期 ${expected}，實際 ${actual}`);
    failures += 1;
  }
}

requireLabel('火燒紅蓮寺 2026-10-11', {
  event: event => event.title.includes('火燒紅蓮寺'), date: '2026-10-11'
}, '演出中');
requireLabel('10/30、11/01 的 2026-10-31', {
  event: event => event.dateFormatted.includes('10/30') && event.dateFormatted.includes('11/01') && !rangeSeparator.test(event.dateFormatted),
  date: '2026-10-31'
}, '期間內・詳見場次日期');
requireLabel('10/30、11/01 的 2026-11-01', {
  event: event => event.dateFormatted.includes('10/30') && event.dateFormatted.includes('11/01') && !rangeSeparator.test(event.dateFormatted),
  date: '2026-11-01'
}, '演出中');
requireLabel('10/03、10/04 的 2026-10-04', {
  event: event => event.dateFormatted.includes('10/03') && event.dateFormatted.includes('10/04') && event.dateFormatted.includes('、'),
  date: '2026-10-04'
}, '演出中');

for (const event of multiDayEvents) {
  const parsed = parseEventDates(event);
  if (parsed && parsed.ranges.length) {
    for (let today = event.date; today <= event.endDate; today = addDays(today, 1)) {
      if (labelFor(event, today) !== '演出中') {
        console.error(`FAIL: 連續區間未標示演出中：${event.id} ${today}`);
        failures += 1;
      }
    }
  }
}

if (failures) process.exitCode = 1;
else console.log('\n所有日期徽章驗收通過');
