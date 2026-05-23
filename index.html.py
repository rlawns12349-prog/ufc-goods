<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FIGHTGOODS — MMA 굿즈 플랫폼</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Bebas+Neue&display=swap" rel="stylesheet">
<style>
:root {
  --red: #e63946;
  --red-dark: #b5262e;
  --red-glow: rgba(230,57,70,0.15);
  --bg: #0a0a0a;
  --bg2: #111111;
  --bg3: #181818;
  --bg4: #1f1f1f;
  --border: #2a2a2a;
  --border2: #333;
  --text: #f0f0f0;
  --text2: #aaa;
  --text3: #666;
  --nav-h: 64px;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Noto Sans KR', sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
}

/* ── NAVBAR ── */
.navbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  height: var(--nav-h);
  background: rgba(10,10,10,0.92);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; padding: 0 40px;
  gap: 0;
}
.nav-logo {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 26px;
  letter-spacing: 2px;
  color: var(--red);
  margin-right: 40px;
  cursor: pointer;
}
.nav-logo span { color: var(--text); }
.nav-links { display: flex; gap: 4px; flex: 1; }
.nav-link {
  padding: 8px 16px;
  font-size: 13px;
  color: var(--text3);
  cursor: pointer;
  border-radius: 6px;
  transition: color .2s, background .2s;
  white-space: nowrap;
  background: none; border: none; font-family: inherit;
}
.nav-link:hover { color: var(--text); background: var(--bg3); }
.nav-link.active { color: var(--red); }
.nav-right { display: flex; align-items: center; gap: 12px; margin-left: auto; }
.nav-search {
  display: flex; align-items: center; gap: 8px;
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 8px; padding: 7px 14px; width: 200px;
  font-size: 13px; color: var(--text3); cursor: text;
}
.nav-search:hover { border-color: var(--border2); }
.cart-btn {
  position: relative; cursor: pointer;
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 14px;
  font-size: 13px; color: var(--text);
  display: flex; align-items: center; gap: 6px;
  transition: border-color .2s;
  white-space: nowrap;
}
.cart-btn:hover { border-color: var(--red); }
.cart-count {
  background: var(--red); color: #fff;
  width: 18px; height: 18px; border-radius: 50%;
  font-size: 10px; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
}
.login-btn {
  padding: 8px 18px; border-radius: 8px;
  background: var(--red); color: #fff;
  font-size: 13px; font-weight: 700;
  cursor: pointer; border: none; font-family: inherit;
  transition: background .2s;
}
.login-btn:hover { background: var(--red-dark); }

/* ── PAGE WRAPPER ── */
.page-wrap {
  margin-top: var(--nav-h);
  display: none;
}
.page-wrap.active { display: block; }

/* ── HERO ── */
.hero {
  position: relative;
  height: 520px;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a0608 40%, #0a0a0a 100%);
  overflow: hidden;
  display: flex; align-items: center;
}
.hero::before {
  content: '';
  position: absolute; inset: 0;
  background: repeating-linear-gradient(
    -45deg, transparent, transparent 40px,
    rgba(230,57,70,0.03) 40px, rgba(230,57,70,0.03) 41px
  );
}
.hero-content {
  position: relative; z-index: 2;
  padding: 0 80px;
  max-width: 700px;
}
.hero-live {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(230,57,70,0.15); border: 1px solid rgba(230,57,70,0.4);
  border-radius: 20px; padding: 6px 16px;
  font-size: 12px; font-weight: 700; color: var(--red);
  margin-bottom: 20px;
  animation: pulse-border 2s infinite;
}
@keyframes pulse-border {
  0%,100% { border-color: rgba(230,57,70,0.4); }
  50% { border-color: rgba(230,57,70,0.8); }
}
.hero-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--red); animation: blink 1.2s infinite; }
@keyframes blink { 0%,100%{opacity:1;} 50%{opacity:.3;} }
.hero-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 72px; line-height: 0.95;
  letter-spacing: 2px;
  margin-bottom: 16px;
}
.hero-title .accent { color: var(--red); }
.hero-sub { font-size: 15px; color: var(--text2); line-height: 1.7; margin-bottom: 32px; }
.hero-btns { display: flex; gap: 12px; }
.btn-red {
  padding: 14px 32px; border-radius: 10px;
  background: var(--red); color: #fff;
  font-size: 14px; font-weight: 700;
  cursor: pointer; border: none; font-family: inherit;
  transition: background .2s, transform .1s;
}
.btn-red:hover { background: var(--red-dark); }
.btn-red:active { transform: scale(.98); }
.btn-outline {
  padding: 14px 32px; border-radius: 10px;
  background: transparent; color: var(--text);
  font-size: 14px; font-weight: 500;
  cursor: pointer; border: 1px solid var(--border2); font-family: inherit;
  transition: border-color .2s, background .2s;
}
.btn-outline:hover { border-color: var(--text2); background: var(--bg3); }
.hero-right {
  position: absolute; right: 0; top: 0; bottom: 0; width: 45%;
  display: flex; align-items: center; justify-content: center;
}
.hero-graphic {
  width: 360px; height: 360px;
  background: radial-gradient(circle at center, rgba(230,57,70,0.2) 0%, transparent 65%);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 180px;
  animation: float 4s ease-in-out infinite;
}
@keyframes float { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-16px);} }

/* ── SECTION COMMON ── */
.section { padding: 60px 80px; }
.section-head {
  display: flex; align-items: baseline; gap: 16px;
  margin-bottom: 32px;
}
.section-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 32px; letter-spacing: 1px;
}
.section-label {
  font-size: 11px; font-weight: 700; color: var(--red);
  text-transform: uppercase; letter-spacing: 1.5px;
}
.section-more {
  margin-left: auto; font-size: 13px; color: var(--text3);
  cursor: pointer; border: none; background: none;
  font-family: inherit; transition: color .2s;
}
.section-more:hover { color: var(--red); }

/* ── RESULT BANNER ── */
.result-banner {
  margin: 0 80px 40px;
  background: linear-gradient(135deg, #1a0608, #110305);
  border: 1px solid rgba(230,57,70,0.4);
  border-radius: 16px; padding: 28px 36px;
  cursor: pointer; transition: border-color .2s;
}
.result-banner:hover { border-color: var(--red); }
.result-banner-top {
  display: flex; align-items: center; gap: 12px;
  margin-bottom: 20px;
}
.result-event { font-size: 13px; color: var(--text2); }
.result-main {
  display: grid; grid-template-columns: 1fr auto 1fr;
  align-items: center; gap: 32px;
}
.result-fighter { text-align: center; }
.result-fighter .name {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 42px; letter-spacing: 1px; line-height: 1;
}
.result-fighter.winner .name { color: var(--red); }
.result-fighter .org { font-size: 12px; color: var(--text3); margin-top: 4px; }
.result-center { text-align: center; }
.result-method-big {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 28px; color: var(--red); letter-spacing: 1px;
}
.result-detail { font-size: 12px; color: var(--text3); margin-top: 4px; }
.result-banner-cta {
  display: flex; gap: 12px; margin-top: 24px;
  padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.06);
}

/* ── PRODUCT GRID ── */
.product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}
.product-card {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 14px; overflow: hidden;
  cursor: pointer; transition: border-color .2s, transform .2s;
}
.product-card:hover { border-color: var(--red); transform: translateY(-4px); }
.product-img {
  height: 200px;
  background: linear-gradient(135deg, #1e1e2e, #2a1e2a);
  display: flex; align-items: center; justify-content: center;
  font-size: 64px; position: relative;
}
.product-badge {
  position: absolute; top: 12px; right: 12px;
  padding: 4px 10px; border-radius: 6px;
  font-size: 10px; font-weight: 700;
}
.badge-hot { background: var(--red); color: #fff; }
.badge-limited { background: #ff6b35; color: #fff; }
.badge-new { background: #2d6a4f; color: #95d5b2; }
.product-body { padding: 16px; }
.product-name { font-size: 14px; font-weight: 500; margin-bottom: 6px; line-height: 1.4; }
.product-fighter { font-size: 11px; color: var(--text3); margin-bottom: 8px; }
.product-bottom {
  display: flex; align-items: center; justify-content: space-between;
}
.product-price { font-size: 18px; font-weight: 700; color: var(--red); }
.product-stock { font-size: 11px; color: var(--text3); }

/* ── FIGHTERS SECTION ── */
.fighter-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;
}
.fighter-card {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 14px; padding: 24px;
  cursor: pointer; transition: border-color .2s, background .2s;
  display: flex; gap: 20px; align-items: flex-start;
}
.fighter-card:hover { border-color: var(--red); background: var(--bg4); }
.fighter-avatar {
  width: 72px; height: 72px; border-radius: 50%;
  background: var(--bg4); border: 2px solid var(--border2);
  display: flex; align-items: center; justify-content: center;
  font-size: 34px; flex-shrink: 0;
}
.fighter-info { flex: 1; min-width: 0; }
.fighter-name { font-size: 18px; font-weight: 700; margin-bottom: 4px; }
.fighter-meta { font-size: 12px; color: var(--text3); margin-bottom: 8px; }
.fighter-record {
  display: flex; gap: 12px; margin-bottom: 10px;
}
.record-stat { text-align: center; }
.record-val { font-size: 20px; font-weight: 700; }
.record-label { font-size: 10px; color: var(--text3); }
.fighter-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }
.tag {
  padding: 3px 10px; border-radius: 20px;
  background: var(--red-glow); border: 1px solid rgba(230,57,70,0.3);
  color: var(--red); font-size: 11px;
}
.fighter-goods-count { font-size: 11px; color: var(--text3); }

/* ── RANKING TABLE ── */
.ranking-tabs {
  display: flex; gap: 0; background: var(--bg3);
  border: 1px solid var(--border); border-radius: 10px;
  padding: 4px; width: fit-content; margin-bottom: 24px;
}
.ranking-tab {
  padding: 8px 20px; border-radius: 7px;
  font-size: 13px; cursor: pointer; transition: all .2s;
  background: none; border: none; color: var(--text3); font-family: inherit;
}
.ranking-tab.active { background: var(--red); color: #fff; font-weight: 700; }
.rank-table { width: 100%; border-collapse: collapse; }
.rank-table th {
  text-align: left; padding: 10px 16px;
  font-size: 11px; color: var(--text3); font-weight: 500;
  border-bottom: 1px solid var(--border);
  text-transform: uppercase; letter-spacing: 0.8px;
}
.rank-table td {
  padding: 14px 16px; border-bottom: 1px solid var(--border);
  font-size: 14px;
}
.rank-table tr:last-child td { border-bottom: none; }
.rank-table tr:hover td { background: var(--bg3); }
.rank-num { font-weight: 700; color: var(--text3); width: 40px; }
.rank-num.top { color: var(--red); font-size: 16px; }
.rank-change { font-size: 11px; }
.rank-change.up { color: #2d6a4f; }
.rank-change.down { color: var(--red); }
.rank-change.same { color: var(--text3); }

/* ── PRODUCT DETAIL PAGE ── */
.detail-layout {
  display: grid; grid-template-columns: 1fr 1fr; gap: 60px;
  padding: 60px 80px; min-height: calc(100vh - var(--nav-h));
  align-items: start;
}
.detail-images { position: sticky; top: calc(var(--nav-h) + 24px); }
.main-img {
  width: 100%; aspect-ratio: 1;
  background: linear-gradient(135deg, #1e1e2e, #2a1520);
  border-radius: 16px; border: 1px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  font-size: 120px; margin-bottom: 12px;
}
.thumb-row { display: flex; gap: 10px; }
.thumb {
  width: 70px; height: 70px; border-radius: 8px;
  background: var(--bg3); border: 1px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  font-size: 28px; cursor: pointer; transition: border-color .2s;
}
.thumb.active { border-color: var(--red); }
.thumb:hover { border-color: var(--border2); }
.detail-info { padding-top: 8px; }
.detail-fighter-tag {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--red-glow); border: 1px solid rgba(230,57,70,0.3);
  border-radius: 6px; padding: 5px 12px;
  font-size: 12px; color: var(--red); margin-bottom: 16px; cursor: pointer;
}
.detail-name { font-size: 28px; font-weight: 700; line-height: 1.3; margin-bottom: 12px; }
.detail-price { font-size: 36px; font-weight: 700; color: var(--red); margin-bottom: 8px; }
.detail-review { display: flex; align-items: center; gap: 8px; margin-bottom: 24px; }
.stars { color: #f4a261; font-size: 14px; }
.review-count { font-size: 13px; color: var(--text3); }
.detail-divider { height: 1px; background: var(--border); margin: 24px 0; }
.option-label { font-size: 13px; color: var(--text2); margin-bottom: 10px; font-weight: 500; }
.option-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; }
.opt-btn {
  padding: 10px 20px; border-radius: 8px;
  border: 1px solid var(--border2); background: var(--bg3);
  color: var(--text2); font-size: 13px; cursor: pointer;
  font-family: inherit; transition: all .2s;
}
.opt-btn:hover { border-color: var(--red); color: var(--red); background: var(--red-glow); }
.opt-btn.selected { border-color: var(--red); color: var(--red); background: var(--red-glow); }
.qty-row {
  display: flex; align-items: center; gap: 16px; margin-bottom: 20px;
}
.qty-label { font-size: 13px; color: var(--text2); font-weight: 500; width: 60px; }
.qty-ctrl { display: flex; align-items: center; gap: 0; border: 1px solid var(--border2); border-radius: 8px; overflow: hidden; }
.qty-btn {
  width: 38px; height: 38px; display: flex; align-items: center; justify-content: center;
  cursor: pointer; background: var(--bg3); border: none; color: var(--text);
  font-size: 18px; font-family: inherit; transition: background .2s;
}
.qty-btn:hover { background: var(--bg4); }
.qty-val { width: 48px; text-align: center; font-size: 15px; font-weight: 700; border: none; background: var(--bg3); color: var(--text); padding: 0 8px; line-height: 38px; }
.price-summary {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 10px; padding: 16px 20px; margin-bottom: 20px;
}
.price-row {
  display: flex; justify-content: space-between; align-items: center;
  font-size: 13px; padding: 4px 0;
}
.price-row .plabel { color: var(--text3); }
.price-row.total { font-size: 16px; font-weight: 700; padding-top: 10px; margin-top: 6px; border-top: 1px solid var(--border); }
.price-row.total .pval { color: var(--red); }
.btn-row { display: flex; gap: 12px; }
.btn-buy {
  flex: 2; padding: 16px; background: var(--red); color: #fff;
  font-size: 15px; font-weight: 700; border: none; border-radius: 10px;
  cursor: pointer; font-family: inherit; transition: background .2s;
}
.btn-buy:hover { background: var(--red-dark); }
.btn-cart {
  flex: 1; padding: 16px; background: transparent; color: var(--text);
  font-size: 15px; font-weight: 500; border: 1px solid var(--border2);
  border-radius: 10px; cursor: pointer; font-family: inherit; transition: all .2s;
}
.btn-cart:hover { border-color: var(--text2); background: var(--bg3); }

/* ── BREADCRUMB ── */
.breadcrumb {
  padding: 20px 80px 0;
  display: flex; align-items: center; gap: 8px;
  font-size: 12px; color: var(--text3);
}
.breadcrumb span { cursor: pointer; }
.breadcrumb span:hover { color: var(--text); }
.breadcrumb .sep { color: var(--border2); }
.breadcrumb .current { color: var(--text2); }

/* ── FIGHTER DETAIL PAGE ── */
.fighter-detail-hero {
  background: linear-gradient(180deg, #1a0608 0%, #0a0a0a 100%);
  padding: 60px 80px 40px;
}
.fighter-detail-top {
  display: flex; gap: 48px; align-items: flex-start;
}
.fighter-detail-avatar {
  width: 140px; height: 140px; border-radius: 50%;
  background: var(--bg3); border: 3px solid var(--red);
  display: flex; align-items: center; justify-content: center;
  font-size: 72px; flex-shrink: 0;
}
.fighter-detail-meta { flex: 1; }
.fighter-detail-name {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 56px; letter-spacing: 2px; line-height: 1;
  margin-bottom: 8px;
}
.fighter-detail-org { font-size: 14px; color: var(--text3); margin-bottom: 16px; }
.stats-row { display: flex; gap: 24px; margin-bottom: 20px; }
.stat-box {
  background: rgba(255,255,255,0.04); border: 1px solid var(--border);
  border-radius: 10px; padding: 14px 20px; text-align: center; min-width: 80px;
}
.stat-val { font-size: 28px; font-weight: 700; }
.stat-label { font-size: 10px; color: var(--text3); margin-top: 2px; letter-spacing: 0.5px; }
.fighter-detail-body { padding: 0 80px 60px; display: grid; grid-template-columns: 1fr 340px; gap: 48px; margin-top: 40px; }
.tl-wrap { }
.tl-title { font-family: 'Bebas Neue', sans-serif; font-size: 24px; letter-spacing: 1px; margin-bottom: 24px; }
.tl-item {
  display: flex; gap: 20px; padding-bottom: 28px;
  position: relative;
}
.tl-item::before {
  content: ''; position: absolute;
  left: 9px; top: 24px; bottom: 0;
  width: 2px; background: var(--border);
}
.tl-item:last-child::before { display: none; }
.tl-dot {
  width: 20px; height: 20px; border-radius: 50%;
  border: 2px solid var(--border2); background: var(--bg);
  flex-shrink: 0; margin-top: 4px; position: relative; z-index: 1;
}
.tl-dot.highlight { border-color: var(--red); background: var(--red); }
.tl-content-wrap { flex: 1; }
.tl-year { font-size: 11px; color: var(--text3); margin-bottom: 4px; }
.tl-event { font-size: 15px; font-weight: 500; margin-bottom: 6px; }
.tl-desc { font-size: 13px; color: var(--text3); line-height: 1.6; margin-bottom: 8px; }
.tl-goods-link {
  font-size: 12px; color: var(--red); cursor: pointer;
  display: inline-flex; align-items: center; gap: 4px;
}
.tl-goods-link:hover { text-decoration: underline; }
.fighter-goods-sidebar { }
.fighter-goods-box {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 14px; padding: 24px; position: sticky;
  top: calc(var(--nav-h) + 24px);
}
.fgs-title { font-size: 14px; font-weight: 700; margin-bottom: 16px; }
.mini-product {
  display: flex; gap: 12px; align-items: center;
  padding: 10px 0; border-bottom: 1px solid var(--border);
  cursor: pointer;
}
.mini-product:last-of-type { border-bottom: none; }
.mini-product:hover .mini-name { color: var(--red); }
.mini-img {
  width: 56px; height: 56px; border-radius: 8px;
  background: var(--bg4); display: flex; align-items: center; justify-content: center;
  font-size: 26px; flex-shrink: 0;
}
.mini-name { font-size: 13px; margin-bottom: 4px; }
.mini-price { font-size: 14px; font-weight: 700; color: var(--red); }

/* ── CART PAGE ── */
.cart-layout {
  display: grid; grid-template-columns: 1fr 360px; gap: 40px;
  padding: 40px 80px 60px;
}
.cart-items { }
.cart-head {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 28px; letter-spacing: 1px; margin-bottom: 24px;
}
.cart-item {
  display: flex; gap: 20px; align-items: center;
  padding: 20px 0; border-bottom: 1px solid var(--border);
}
.cart-img {
  width: 100px; height: 100px; border-radius: 10px;
  background: linear-gradient(135deg, #1e1e2e, #2a1520);
  display: flex; align-items: center; justify-content: center;
  font-size: 44px; flex-shrink: 0;
}
.cart-item-info { flex: 1; }
.cart-item-name { font-size: 15px; font-weight: 500; margin-bottom: 4px; }
.cart-item-opt { font-size: 12px; color: var(--text3); margin-bottom: 12px; }
.cart-item-bottom { display: flex; align-items: center; justify-content: space-between; }
.remove-btn {
  font-size: 12px; color: var(--text3); cursor: pointer;
  background: none; border: none; font-family: inherit;
  transition: color .2s; padding: 0;
}
.remove-btn:hover { color: var(--red); }
.cart-item-price { font-size: 18px; font-weight: 700; color: var(--red); }
.cart-summary {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 16px; padding: 28px;
  position: sticky; top: calc(var(--nav-h) + 24px);
  height: fit-content;
}
.summary-title { font-size: 16px; font-weight: 700; margin-bottom: 20px; }
.summary-row {
  display: flex; justify-content: space-between;
  font-size: 14px; padding: 8px 0;
}
.summary-row .slabel { color: var(--text3); }
.summary-divider { height: 1px; background: var(--border); margin: 12px 0; }
.summary-total {
  display: flex; justify-content: space-between;
  font-size: 18px; font-weight: 700; margin-bottom: 20px;
}
.summary-total .tval { color: var(--red); }
.coupon-row {
  display: flex; gap: 8px; margin-bottom: 20px;
}
.coupon-input {
  flex: 1; padding: 10px 14px;
  background: var(--bg4); border: 1px solid var(--border2);
  border-radius: 8px; color: var(--text); font-size: 13px; font-family: inherit;
}
.coupon-input::placeholder { color: var(--text3); }
.coupon-input:focus { outline: none; border-color: var(--red); }
.coupon-btn {
  padding: 10px 16px; border-radius: 8px;
  background: var(--bg4); border: 1px solid var(--border2);
  color: var(--text); font-size: 13px; cursor: pointer; font-family: inherit;
  transition: border-color .2s;
  white-space: nowrap;
}
.coupon-btn:hover { border-color: var(--red); }

/* ── PAYMENT PAGE ── */
.payment-layout {
  display: grid; grid-template-columns: 1fr 400px; gap: 48px;
  padding: 40px 80px 60px;
}
.payment-head { font-family: 'Bebas Neue', sans-serif; font-size: 28px; letter-spacing: 1px; margin-bottom: 28px; }
.payment-section-title { font-size: 14px; font-weight: 700; margin-bottom: 14px; color: var(--text2); }
.payment-block { margin-bottom: 32px; }
.pay-methods { display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; }
.pay-method {
  padding: 14px 8px; border-radius: 10px;
  border: 1px solid var(--border2); background: var(--bg3);
  text-align: center; font-size: 13px; font-weight: 500;
  cursor: pointer; transition: all .2s; font-family: inherit; color: var(--text2);
}
.pay-method:hover { border-color: var(--red); color: var(--red); background: var(--red-glow); }
.pay-method.selected { border-color: var(--red); color: var(--red); background: var(--red-glow); }
.address-box {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 10px; padding: 16px 20px;
}
.address-row { font-size: 14px; margin-bottom: 4px; }
.address-detail { font-size: 12px; color: var(--text3); }
.order-summary-card {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 16px; padding: 28px;
  position: sticky; top: calc(var(--nav-h) + 24px);
}
.os-item {
  display: flex; gap: 12px; align-items: center;
  padding: 12px 0; border-bottom: 1px solid var(--border);
}
.os-img {
  width: 56px; height: 56px; border-radius: 8px;
  background: var(--bg4); display: flex; align-items: center; justify-content: center;
  font-size: 26px; flex-shrink: 0;
}
.os-info { flex: 1; }
.os-name { font-size: 13px; margin-bottom: 3px; }
.os-opt { font-size: 11px; color: var(--text3); }
.os-price { font-size: 14px; font-weight: 700; color: var(--red); }

/* ── ORDER COMPLETE ── */
.confirm-wrap {
  max-width: 640px; margin: 0 auto;
  padding: 80px 40px;
  text-align: center;
}
.confirm-icon {
  width: 96px; height: 96px; border-radius: 50%;
  background: rgba(45,106,79,0.2); border: 2px solid #2d6a4f;
  display: flex; align-items: center; justify-content: center;
  font-size: 48px; margin: 0 auto 28px;
  animation: pop .4s cubic-bezier(0.34,1.56,0.64,1);
}
@keyframes pop { from{transform:scale(0);opacity:0;} to{transform:scale(1);opacity:1;} }
.confirm-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 48px; letter-spacing: 2px; margin-bottom: 8px;
}
.confirm-sub { font-size: 14px; color: var(--text3); margin-bottom: 40px; }
.confirm-box {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 14px; padding: 24px 28px; text-align: left; margin-bottom: 32px;
}
.confirm-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 10px 0; border-bottom: 1px solid var(--border);
  font-size: 14px;
}
.confirm-row:last-child { border-bottom: none; }
.confirm-row .clabel { color: var(--text3); }
.confirm-row .cval { font-weight: 500; }
.confirm-btns { display: flex; gap: 12px; justify-content: center; }

/* ── TOAST ── */
.toast {
  position: fixed; bottom: 32px; left: 50%; transform: translateX(-50%) translateY(80px);
  background: var(--bg3); border: 1px solid var(--border2);
  border-radius: 10px; padding: 14px 24px;
  font-size: 14px; font-weight: 500;
  z-index: 999; opacity: 0;
  transition: transform .3s, opacity .3s;
  white-space: nowrap;
}
.toast.show { transform: translateX(-50%) translateY(0); opacity: 1; }

/* ── UTIL ── */
.tag-row { display: flex; gap: 6px; flex-wrap: wrap; }
.chip {
  padding: 4px 12px; border-radius: 20px;
  font-size: 11px; border: 1px solid var(--border);
  color: var(--text3); background: var(--bg3);
  cursor: pointer; transition: all .2s; font-family: inherit;
}
.chip.active { border-color: var(--red); color: var(--red); background: var(--red-glow); }
.chip:hover { border-color: var(--border2); color: var(--text); }

/* ── AUTH MODAL ── */
.modal-overlay { position:fixed;inset:0;background:rgba(0,0,0,0.75);z-index:500;display:none;align-items:center;justify-content:center;backdrop-filter:blur(4px); }
.modal-overlay.show { display:flex; }
.modal { background:var(--bg3);border:1px solid var(--border2);border-radius:20px;padding:40px;width:100%;max-width:420px;position:relative;animation:modalIn .25s cubic-bezier(0.34,1.56,0.64,1); }
@keyframes modalIn { from{transform:scale(0.9);opacity:0;} to{transform:scale(1);opacity:1;} }
.modal-close { position:absolute;top:16px;right:20px;background:none;border:none;color:var(--text3);font-size:22px;cursor:pointer;line-height:1; }
.modal-close:hover { color:var(--text); }
.modal-title { font-family:'Bebas Neue',sans-serif;font-size:32px;letter-spacing:1px;margin-bottom:4px; }
.modal-sub { font-size:13px;color:var(--text3);margin-bottom:24px; }
.modal-tabs { display:flex;background:var(--bg4);border-radius:8px;padding:3px;margin-bottom:22px; }
.modal-tab { flex:1;padding:8px;border-radius:6px;font-size:13px;text-align:center;cursor:pointer;color:var(--text3);transition:all .2s;background:none;border:none;font-family:inherit; }
.modal-tab.active { background:var(--red);color:#fff;font-weight:700; }
.form-group { margin-bottom:14px; }
.form-label { font-size:12px;color:var(--text2);margin-bottom:5px;font-weight:500; }
.form-input { width:100%;padding:11px 14px;background:var(--bg4);border:1px solid var(--border2);border-radius:8px;color:var(--text);font-size:14px;font-family:inherit;outline:none;transition:border-color .2s; }
.form-input:focus { border-color:var(--red); }
.form-hint { font-size:11px;margin-top:4px; }
.form-hint.err { color:var(--red); }
.form-hint.ok { color:var(--green-light); }
.btn-primary { width:100%;padding:13px;background:var(--red);color:#fff;font-size:14px;font-weight:700;border:none;border-radius:10px;cursor:pointer;font-family:inherit;margin-bottom:8px;transition:background .2s; }
.btn-primary:hover { background:var(--red-dark); }
.btn-primary.full { width:100%; }
.social-row { display:flex;gap:8px;margin-top:10px; }
.social-btn { flex:1;padding:10px;border-radius:8px;border:1px solid var(--border2);background:var(--bg4);color:var(--text2);font-size:12px;font-weight:700;cursor:pointer;font-family:inherit;transition:all .2s; }
.social-btn:hover { border-color:var(--border);color:var(--text); }
.modal-divider { display:flex;align-items:center;gap:10px;margin:14px 0;font-size:11px;color:var(--text3); }
.modal-divider::before,.modal-divider::after { content:'';flex:1;height:1px;background:var(--border); }
.user-btn { display:flex;align-items:center;gap:8px;padding:6px 14px;border-radius:8px;background:var(--bg3);border:1px solid var(--border);cursor:pointer;font-size:13px;transition:border-color .2s; }
.user-btn:hover { border-color:var(--border2); }
.user-avatar { width:26px;height:26px;border-radius:50%;background:var(--red);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff; }
:root { --green-light: #95d5b2; }

.mypage-menu-item { padding:14px 20px;font-size:13px;cursor:pointer;transition:background .15s;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:10px; }
.mypage-menu-item:last-child { border-bottom:none; }
.mypage-menu-item:hover { background:var(--bg4); }
.mypage-menu-item.active { color:var(--red);font-weight:500; }
.faq-item { background:var(--bg3);border:1px solid var(--border);border-radius:10px;margin-bottom:8px;overflow:hidden; }
.faq-q { padding:16px 20px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-size:14px;font-weight:500;transition:background .15s; }
.faq-q:hover { background:var(--bg4); }
.faq-a { padding:0 20px;max-height:0;overflow:hidden;transition:max-height .3s,padding .3s;font-size:13px;color:var(--text2);line-height:1.7; }
.faq-a.open { max-height:200px;padding:12px 20px 16px; }
.faq-chevron { transition:transform .3s;font-size:12px;color:var(--text3); }
.faq-chevron.open { transform:rotate(180deg); }
.cal-cell { min-height:72px;background:var(--bg3);border:1px solid var(--border);border-radius:6px;padding:8px;cursor:pointer;transition:border-color .2s; }
.cal-cell:hover { border-color:var(--border2); }
.cal-cell.has-event { border-color:rgba(230,57,70,0.4); }
.cal-date { font-size:12px;color:var(--text3);margin-bottom:4px; }
.cal-event { font-size:10px;background:var(--red-glow);border:1px solid rgba(230,57,70,0.3);color:var(--red);padding:2px 5px;border-radius:4px;line-height:1.4; }
</style>
</head>
<body>

<!-- ════ NAVBAR ════ -->
<nav class="navbar">
  <div class="nav-logo" onclick="showPage('home')">FIGHT<span>GOODS</span></div>
  <div class="nav-links">
    <button class="nav-link active" onclick="showPage('home');setActiveNav(this)">굿즈 홈</button>
    <button class="nav-link" onclick="showPage('ranking');setActiveNav(this)">종합 랭킹</button>
    <button class="nav-link" onclick="showPage('fighters');setActiveNav(this)">선수 정보</button>
    <button class="nav-link" onclick="showPage('results');setActiveNav(this)">경기 정보</button>
    <button class="nav-link" onclick="showPage('community');setActiveNav(this)">커뮤니티</button>
    <button class="nav-link" onclick="showPage('notice');setActiveNav(this)">공지사항</button>
    <button class="nav-link" onclick="showPage('faq');setActiveNav(this)">고객지원</button>
    <button class="nav-link" onclick="showPage('mypage');setActiveNav(this)">마이페이지</button>
  </div>
  <div class="nav-right">
    <div style="position:relative;">
      <div class="nav-search" style="display:flex;align-items:center;gap:6px;">
        <span>🔍</span>
        <input id="search-input" placeholder="상품 또는 선수 검색" style="background:none;border:none;outline:none;color:var(--text);font-size:13px;font-family:inherit;width:150px;" oninput="onSearch(this.value)" onfocus="onSearch(this.value)" onblur="setTimeout(closeSearch,200)">
      </div>
      <div id="search-dropdown" style="display:none;position:absolute;top:calc(100% + 6px);left:0;right:0;background:var(--bg3);border:1px solid var(--border2);border-radius:10px;overflow:hidden;z-index:300;"></div>
    </div>
    <div class="cart-btn" onclick="showPage('cart')">
      🛒 장바구니 <div class="cart-count" id="cart-count">1</div>
    </div>
    <div id="nav-auth"></div>
  </div>
</nav>

<!-- ════ AUTH MODAL ════ -->
<div class="modal-overlay" id="auth-modal">
  <div class="modal">
    <button class="modal-close" onclick="closeModal()">&#x2715;</button>
    <div class="modal-title">FIGHTGOODS</div>
    <div class="modal-sub">MMA 서사 기반 굿즈 플랫폼</div>
    <div class="modal-tabs">
      <button class="modal-tab active" id="tab-login" onclick="switchAuthTab('login')">로그인</button>
      <button class="modal-tab" id="tab-signup" onclick="switchAuthTab('signup')">회원가입</button>
    </div>
    <div id="form-login">
      <div class="form-group"><div class="form-label">이메일</div><input class="form-input" id="login-email" type="email" placeholder="이메일 입력"></div>
      <div class="form-group"><div class="form-label">비밀번호</div><input class="form-input" id="login-pw" type="password" placeholder="비밀번호 입력" onkeydown="if(event.key==='Enter')doLogin()"><div id="login-err" class="form-hint err" style="display:none;"></div></div>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <label style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text3);cursor:pointer;"><input type="checkbox"> 로그인 상태 유지</label>
        <span style="font-size:12px;color:var(--text3);cursor:pointer;" onclick="showToast('비밀번호 재설정 이메일을 발송했습니다')">비밀번호 찾기</span>
      </div>
      <button class="btn-primary full" onclick="doLogin()">로그인</button>
      <div class="modal-divider">소셜 로그인</div>
      <div class="social-row">
        <button class="social-btn" onclick="doSocialLogin('카카오')">카카오</button>
        <button class="social-btn" onclick="doSocialLogin('구글')">구글</button>
        <button class="social-btn" onclick="doSocialLogin('네이버')">네이버</button>
      </div>
    </div>
    <div id="form-signup" style="display:none;">
      <div class="form-group"><div class="form-label">이메일</div><input class="form-input" id="su-email" type="email" placeholder="이메일 입력" oninput="checkEmail(this.value)"><div id="su-email-hint" class="form-hint"></div></div>
      <div class="form-group"><div class="form-label">닉네임</div><input class="form-input" id="su-nick" placeholder="닉네임 (2~10자)" oninput="checkNick(this.value)"><div id="su-nick-hint" class="form-hint"></div></div>
      <div class="form-group"><div class="form-label">비밀번호</div><input class="form-input" id="su-pw" type="password" placeholder="영문+숫자+특수문자 8자 이상" oninput="checkPw(this.value)"><div id="pw-strength-bar" style="height:4px;border-radius:2px;margin-top:5px;transition:width .3s,background .3s;width:0;"></div><div id="su-pw-hint" class="form-hint"></div></div>
      <div class="form-group"><div class="form-label">비밀번호 확인</div><input class="form-input" id="su-pw2" type="password" placeholder="비밀번호 재입력" oninput="checkPw2(this.value)"><div id="su-pw2-hint" class="form-hint"></div></div>
      <div style="margin-bottom:14px;">
        <label style="display:flex;align-items:center;gap:8px;font-size:13px;cursor:pointer;margin-bottom:8px;"><input type="checkbox" id="agree-terms"> 이용약관 및 개인정보처리방침 동의 <span style="color:var(--red);">(필수)</span></label>
        <label style="display:flex;align-items:center;gap:8px;font-size:13px;cursor:pointer;"><input type="checkbox"> 마케팅 수신 동의 (선택)</label>
      </div>
      <div id="su-err" class="form-hint err" style="display:none;margin-bottom:10px;"></div>
      <button class="btn-primary full" onclick="doSignup()">회원가입</button>
    </div>
  </div>
</div>

<!-- ════ HOME PAGE ════ -->
<div class="page-wrap active" id="page-home">
  <!-- HERO -->
  <div class="hero">
    <div class="hero-content">
      <div class="hero-live"><div class="hero-dot"></div>UFC 298 LIVE 진행 중</div>
      <div class="hero-title">MMA<br><span class="accent">서사를</span><br>입어라</div>
      <div class="hero-sub">선수의 이야기가 담긴 굿즈.<br>경기 직후 가장 먼저 만나는 챔피언의 흔적.</div>
      <div class="hero-btns">
        <button class="btn-red" onclick="showPage('results');setActiveNav(document.querySelectorAll('.nav-link')[3])">경기 결과 보기</button>
        <button class="btn-outline" onclick="showPage('fighters');setActiveNav(document.querySelectorAll('.nav-link')[2])">선수 탐색하기</button>
      </div>
    </div>
    <div class="hero-right">
      <div class="hero-graphic">🥊</div>
    </div>
  </div>

  <!-- RESULT BANNER -->
  <div class="result-banner" onclick="showPage('results');setActiveNav(document.querySelectorAll('.nav-link')[3])">
    <div class="result-banner-top">
      <span class="badge badge-hot" style="padding:4px 12px;border-radius:6px;">방금 종료</span>
      <span class="result-event">UFC 298 · 2025.05.17 메인이벤트</span>
    </div>
    <div class="result-main">
      <div class="result-fighter winner">
        <div class="name">홍길동</div>
        <div class="org">UFC · 웰터급 챔피언</div>
      </div>
      <div class="result-center">
        <div class="result-method-big">KO 승</div>
        <div class="result-detail">1라운드 2분 34초</div>
        <div style="font-size:22px;color:var(--text3);margin:8px 0;">VS</div>
      </div>
      <div class="result-fighter">
        <div class="name">맥스 홀로웨이</div>
        <div class="org">UFC · 웰터급</div>
      </div>
    </div>
    <div class="result-banner-cta">
      <button class="btn-red" onclick="event.stopPropagation();showPage('product')">연계 굿즈 바로구매 →</button>
      <button class="btn-outline" onclick="event.stopPropagation();showPage('fighter-detail')">홍길동 선수 스토리 보기</button>
    </div>
  </div>

  <!-- POPULAR GOODS -->
  <div class="section">
    <div class="section-head">
      <div class="section-label">인기 굿즈</div>
      <div class="section-title">지금 가장 핫한 굿즈</div>
      <button class="section-more" onclick="showPage('ranking');setActiveNav(document.querySelectorAll('.nav-link')[1])">전체 보기 →</button>
    </div>
    <div style="display:flex;gap:8px;margin-bottom:20px;" id="product-filters">
      <button class="chip active" data-cat="전체" onclick="filterProducts(this)">전체</button>
      <button class="chip" data-cat="티셔츠" onclick="filterProducts(this)">티셔츠</button>
      <button class="chip" data-cat="포스터" onclick="filterProducts(this)">포스터</button>
      <button class="chip" data-cat="포토카드" onclick="filterProducts(this)">포토카드</button>
      <button class="chip" data-cat="후디" onclick="filterProducts(this)">후디</button>
    </div>
    <div class="product-grid" id="home-product-grid">
      <div class="product-card" onclick="showPage('product')">
        <div class="product-img">👕<span class="product-badge badge-hot">🔥 HOT</span></div>
        <div class="product-body">
          <div class="product-name">홍길동 챔피언 등극 기념 티셔츠</div>
          <div class="product-fighter">홍길동 · UFC 웰터급</div>
          <div class="product-bottom"><div class="product-price">₩45,000</div><div class="product-stock">재고 12개</div></div>
        </div>
      </div>
      <div class="product-card" onclick="showPage('product')">
        <div class="product-img">🖼️<span class="product-badge badge-limited">한정 50개</span></div>
        <div class="product-body">
          <div class="product-name">챔피언 벨트 아트 포스터</div>
          <div class="product-fighter">홍길동 · UFC 웰터급</div>
          <div class="product-bottom"><div class="product-price">₩18,000</div><div class="product-stock">한정 50개</div></div>
        </div>
      </div>
      <div class="product-card" onclick="showPage('product')">
        <div class="product-img">📸<span class="product-badge badge-new">NEW</span></div>
        <div class="product-body">
          <div class="product-name">등극 순간 포토카드 세트</div>
          <div class="product-fighter">홍길동 · UFC 웰터급</div>
          <div class="product-bottom"><div class="product-price">₩12,000</div><div class="product-stock">재고 있음</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- FIGHTERS PREVIEW -->
  <div class="section" style="padding-top:0;">
    <div class="section-head">
      <div class="section-label">선수 서사</div>
      <div class="section-title">그들의 이야기</div>
      <button class="section-more" onclick="showPage('fighters');setActiveNav(document.querySelectorAll('.nav-link')[2])">전체 선수 보기 →</button>
    </div>
    <div class="fighter-grid">
      <div class="fighter-card" onclick="showPage('fighter-detail')">
        <div class="fighter-avatar">🥊</div>
        <div class="fighter-info">
          <div class="fighter-name">홍길동</div>
          <div class="fighter-meta">웰터급 · UFC · 데뷔 2019</div>
          <div class="fighter-record">
            <div class="record-stat"><div class="record-val">12</div><div class="record-label">승</div></div>
            <div class="record-stat"><div class="record-val">3</div><div class="record-label">패</div></div>
            <div class="record-stat"><div class="record-val">0</div><div class="record-label">무</div></div>
          </div>
          <div class="fighter-tags"><span class="tag">챔피언 등극</span><span class="tag">체급 조절</span></div>
          <div class="fighter-goods-count">관련 굿즈 3개</div>
        </div>
      </div>
      <div class="fighter-card">
        <div class="fighter-avatar">💪</div>
        <div class="fighter-info">
          <div class="fighter-name">이철수</div>
          <div class="fighter-meta">헤비급 · 블랙컴뱃 · 데뷔 2020</div>
          <div class="fighter-record">
            <div class="record-stat"><div class="record-val">8</div><div class="record-label">승</div></div>
            <div class="record-stat"><div class="record-val">1</div><div class="record-label">패</div></div>
            <div class="record-stat"><div class="record-val">0</div><div class="record-label">무</div></div>
          </div>
          <div class="fighter-tags"><span class="tag">부상 극복</span><span class="tag">무명 시절</span></div>
          <div class="fighter-goods-count">관련 굿즈 1개</div>
        </div>
      </div>
      <div class="fighter-card">
        <div class="fighter-avatar">⚡</div>
        <div class="fighter-info">
          <div class="fighter-name">박영희</div>
          <div class="fighter-meta">밴텀급 · ZFN · 데뷔 2022</div>
          <div class="fighter-record">
            <div class="record-stat"><div class="record-val">6</div><div class="record-label">승</div></div>
            <div class="record-stat"><div class="record-val">0</div><div class="record-label">패</div></div>
            <div class="record-stat"><div class="record-val">0</div><div class="record-label">무</div></div>
          </div>
          <div class="fighter-tags"><span class="tag">신인왕</span><span class="tag">연승 스트릭</span></div>
          <div class="fighter-goods-count">관련 굿즈 2개</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════ RESULTS PAGE ════ -->
<div class="page-wrap" id="page-results">
  <div class="section">
    <div class="section-head">
      <div class="section-label">경기 정보</div>
      <div class="section-title">경기 결과 피드</div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 320px;gap:32px;align-items:start;">
      <div>
        <!-- main result -->
        <div class="result-banner" style="margin:0 0 20px;" onclick="showPage('fighter-detail')">
          <div class="result-banner-top">
            <span class="badge badge-hot" style="padding:4px 12px;border-radius:6px;">방금 종료</span>
            <span class="result-event">UFC 298 · 2025.05.17 메인이벤트</span>
          </div>
          <div class="result-main">
            <div class="result-fighter winner"><div class="name">홍길동</div><div class="org">UFC · 웰터급 챔피언</div></div>
            <div class="result-center"><div class="result-method-big">KO 승</div><div class="result-detail">1라운드 2분 34초</div><div style="font-size:22px;color:var(--text3);margin:8px 0;">VS</div></div>
            <div class="result-fighter"><div class="name">맥스 홀로웨이</div><div class="org">UFC · 웰터급</div></div>
          </div>
          <div class="result-banner-cta">
            <button class="btn-red" onclick="event.stopPropagation();showPage('product')">연계 굿즈 바로구매 →</button>
            <button class="btn-outline" onclick="event.stopPropagation();showPage('fighter-detail')">선수 스토리 보기</button>
          </div>
        </div>
        <!-- past results -->
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:20px 24px;margin-bottom:12px;opacity:.7;cursor:pointer;" onclick="showPage('fighter-detail')">
          <div style="font-size:12px;color:var(--text3);margin-bottom:10px;">ZFN 38 · 2025.05.10</div>
          <div style="display:flex;justify-content:space-between;align-items:center;">
            <div style="font-size:16px;font-weight:700;">이철수 <span style="font-size:13px;color:var(--text3);font-weight:400;">vs</span> 김용재</div>
            <div style="font-size:13px;color:#2d6a4f;font-weight:700;">판정 승</div>
          </div>
        </div>
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:20px 24px;opacity:.5;cursor:pointer;">
          <div style="font-size:12px;color:var(--text3);margin-bottom:10px;">UFC 297 · 2025.04.28</div>
          <div style="display:flex;justify-content:space-between;align-items:center;">
            <div style="font-size:16px;font-weight:700;">박영희 <span style="font-size:13px;color:var(--text3);font-weight:400;">vs</span> 최강희</div>
            <div style="font-size:13px;color:var(--red);font-weight:700;">KO 승</div>
          </div>
        </div>
      </div>
      <!-- upcoming -->
      <div>
        <div style="font-size:12px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:1px;margin-bottom:14px;">출시 예정 굿즈</div>
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:16px 20px;margin-bottom:12px;">
          <div style="font-size:11px;color:var(--text3);margin-bottom:4px;">UFC 308 예정 · D-14</div>
          <div style="font-size:14px;font-weight:500;margin-bottom:10px;">홍길동 UFC 308 출전 기념 굿즈</div>
          <button class="btn-red" style="padding:8px 16px;font-size:12px;">알림 신청</button>
        </div>
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:16px 20px;opacity:.7;">
          <div style="font-size:11px;color:var(--text3);margin-bottom:4px;">ZFN 40 예정 · D-21</div>
          <div style="font-size:14px;font-weight:500;margin-bottom:10px;">이철수 연속 KO 기념 포스터</div>
          <button class="btn-outline" style="padding:8px 16px;font-size:12px;">알림 신청</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════ FIGHTERS PAGE ════ -->
<div class="page-wrap" id="page-fighters">
  <div class="section">
    <div class="section-head">
      <div class="section-label">선수 정보</div>
      <div class="section-title">계약 선수 전체</div>
    </div>
    <div class="tag-row" style="margin-bottom:24px;">
      <button class="chip active">전체</button>
      <button class="chip">웰터급</button>
      <button class="chip">헤비급</button>
      <button class="chip">밴텀급</button>
      <button class="chip">UFC</button>
      <button class="chip">블랙컴뱃</button>
      <button class="chip">ZFN</button>
      <button class="chip">현역</button>
    </div>
    <div class="fighter-grid">
      <div class="fighter-card" onclick="showPage('fighter-detail')">
        <div class="fighter-avatar">🥊</div>
        <div class="fighter-info">
          <div class="fighter-name">홍길동</div>
          <div class="fighter-meta">웰터급 · UFC · 데뷔 2019.03.15</div>
          <div class="fighter-record">
            <div class="record-stat"><div class="record-val">12</div><div class="record-label">승</div></div>
            <div class="record-stat"><div class="record-val">3</div><div class="record-label">패</div></div>
            <div class="record-stat"><div class="record-val">77%</div><div class="record-label">피니시율</div></div>
          </div>
          <div class="fighter-tags"><span class="tag">챔피언 등극</span><span class="tag">체급 조절</span></div>
          <div class="fighter-goods-count">관련 굿즈 3개</div>
        </div>
      </div>
      <div class="fighter-card">
        <div class="fighter-avatar">💪</div>
        <div class="fighter-info">
          <div class="fighter-name">이철수</div>
          <div class="fighter-meta">헤비급 · 블랙컴뱃 · 데뷔 2020.07.22</div>
          <div class="fighter-record">
            <div class="record-stat"><div class="record-val">8</div><div class="record-label">승</div></div>
            <div class="record-stat"><div class="record-val">1</div><div class="record-label">패</div></div>
            <div class="record-stat"><div class="record-val">62%</div><div class="record-label">피니시율</div></div>
          </div>
          <div class="fighter-tags"><span class="tag">부상 극복</span><span class="tag">무명 시절</span></div>
          <div class="fighter-goods-count">관련 굿즈 1개</div>
        </div>
      </div>
      <div class="fighter-card">
        <div class="fighter-avatar">⚡</div>
        <div class="fighter-info">
          <div class="fighter-name">박영희</div>
          <div class="fighter-meta">밴텀급 · ZFN · 데뷔 2022.11.05</div>
          <div class="fighter-record">
            <div class="record-stat"><div class="record-val">6</div><div class="record-label">승</div></div>
            <div class="record-stat"><div class="record-val">0</div><div class="record-label">패</div></div>
            <div class="record-stat"><div class="record-val">83%</div><div class="record-label">피니시율</div></div>
          </div>
          <div class="fighter-tags"><span class="tag">신인왕</span><span class="tag">연승 스트릭</span></div>
          <div class="fighter-goods-count">관련 굿즈 2개</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════ FIGHTER DETAIL PAGE ════ -->
<div class="page-wrap" id="page-fighter-detail">
  <div class="breadcrumb">
    <span onclick="showPage('fighters');setActiveNav(document.querySelectorAll('.nav-link')[2])">선수 정보</span>
    <span class="sep">›</span><span class="current">홍길동</span>
  </div>
  <div class="fighter-detail-hero">
    <div class="fighter-detail-top">
      <div class="fighter-detail-avatar">🥊</div>
      <div class="fighter-detail-meta">
        <div class="fighter-detail-name">홍길동</div>
        <div class="fighter-detail-org">UFC · 웰터급 챔피언 · 데뷔 2019.03.15</div>
        <div class="stats-row">
          <div class="stat-box"><div class="stat-val">12</div><div class="stat-label">승</div></div>
          <div class="stat-box"><div class="stat-val">3</div><div class="stat-label">패</div></div>
          <div class="stat-box"><div class="stat-val">0</div><div class="stat-label">무</div></div>
          <div class="stat-box"><div class="stat-val">77%</div><div class="stat-label">피니시율</div></div>
          <div class="stat-box"><div class="stat-val">5</div><div class="stat-label">KO</div></div>
        </div>
        <button class="btn-red" onclick="showPage('product')">관련 굿즈 바로가기 →</button>
      </div>
    </div>
  </div>
  <div class="fighter-detail-body">
    <div class="tl-wrap">
      <div class="tl-title">성장 타임라인</div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-content-wrap">
          <div class="tl-year">2019</div>
          <div class="tl-event">데뷔 · 무명 시절</div>
          <div class="tl-desc">아무도 주목하지 않던 지방 팀 소속. 연속 KO로 이름을 알리기 시작했다.</div>
          <div class="tl-goods-link" onclick="showPage('product')">이 스토리의 굿즈 보기 →</div>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-content-wrap">
          <div class="tl-year">2021</div>
          <div class="tl-event">체급 조절 도전</div>
          <div class="tl-desc">웰터급으로 체급을 올리며 고비를 맞았지만, 6개월의 재활과 훈련으로 복귀했다.</div>
          <div class="tl-goods-link" onclick="showPage('product')">이 스토리의 굿즈 보기 →</div>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-dot highlight"></div>
        <div class="tl-content-wrap">
          <div class="tl-year">2023 🏆</div>
          <div class="tl-event">챔피언 등극</div>
          <div class="tl-desc">UFC 298에서 KO 1라운드 피니시. 한국 MMA 역사상 첫 UFC 웰터급 챔피언.</div>
          <div class="tl-goods-link" onclick="showPage('product')">이 스토리의 굿즈 보기 →</div>
        </div>
      </div>
    </div>
    <div class="fighter-goods-sidebar">
      <div class="fighter-goods-box">
        <div class="fgs-title">홍길동 관련 굿즈</div>
        <div class="mini-product" onclick="showPage('product')">
          <div class="mini-img">👕</div>
          <div><div class="mini-name">챔피언 등극 기념 티셔츠</div><div class="mini-price">₩45,000</div></div>
        </div>
        <div class="mini-product" onclick="showPage('product')">
          <div class="mini-img">🖼️</div>
          <div><div class="mini-name">챔피언 벨트 아트 포스터</div><div class="mini-price">₩18,000</div></div>
        </div>
        <div class="mini-product" onclick="showPage('product')">
          <div class="mini-img">📸</div>
          <div><div class="mini-name">등극 순간 포토카드 세트</div><div class="mini-price">₩12,000</div></div>
        </div>
        <button class="btn-red" style="margin-top:16px;width:100%;" onclick="showPage('product')">굿즈 전체 보기</button>
      </div>
    </div>
  </div>
</div>

<!-- ════ RANKING PAGE ════ -->
<div class="page-wrap" id="page-ranking">
  <div class="section">
    <div class="section-head">
      <div class="section-label">종합 랭킹</div>
      <div class="section-title">인기 굿즈 순위</div>
    </div>
    <div class="ranking-tabs">
      <button class="ranking-tab active" onclick="switchRankTab(this,'sales')">판매량순</button>
      <button class="ranking-tab" onclick="switchRankTab(this,'views')">조회수순</button>
    </div>
    <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;overflow:hidden;">
      <table class="rank-table">
        <thead><tr>
          <th style="width:60px;">순위</th><th>상품</th><th>선수</th>
          <th style="text-align:right;">판매량</th><th style="text-align:right;">가격</th>
        </tr></thead>
        <tbody>
          <tr onclick="showPage('product')" style="cursor:pointer;">
            <td><div class="rank-num top">1<div class="rank-change up">▲2</div></div></td>
            <td><div style="font-size:14px;font-weight:500;">챔피언 등극 기념 티셔츠</div></td>
            <td style="color:var(--text3);font-size:13px;">홍길동</td>
            <td style="text-align:right;font-size:14px;font-weight:700;">1,284</td>
            <td style="text-align:right;color:var(--red);font-weight:700;">₩45,000</td>
          </tr>
          <tr onclick="showPage('product')" style="cursor:pointer;">
            <td><div class="rank-num top">2<div class="rank-change same">—</div></div></td>
            <td><div style="font-size:14px;font-weight:500;">챔피언 벨트 아트 포스터</div></td>
            <td style="color:var(--text3);font-size:13px;">홍길동</td>
            <td style="text-align:right;font-size:14px;font-weight:700;">893</td>
            <td style="text-align:right;color:var(--red);font-weight:700;">₩18,000</td>
          </tr>
          <tr onclick="showPage('product')" style="cursor:pointer;">
            <td><div class="rank-num top">3<div class="rank-change up">▲1</div></div></td>
            <td><div style="font-size:14px;font-weight:500;">등극 순간 포토카드 세트</div></td>
            <td style="color:var(--text3);font-size:13px;">홍길동</td>
            <td style="text-align:right;font-size:14px;font-weight:700;">712</td>
            <td style="text-align:right;color:var(--red);font-weight:700;">₩12,000</td>
          </tr>
          <tr onclick="showPage('product')" style="cursor:pointer;">
            <td><div class="rank-num">4<div class="rank-change down">▼1</div></div></td>
            <td><div style="font-size:14px;font-weight:500;">이철수 부상 극복 기념 후디</div></td>
            <td style="color:var(--text3);font-size:13px;">이철수</td>
            <td style="text-align:right;font-size:14px;font-weight:700;">445</td>
            <td style="text-align:right;color:var(--red);font-weight:700;">₩68,000</td>
          </tr>
          <tr onclick="showPage('product')" style="cursor:pointer;">
            <td><div class="rank-num">5<div class="rank-change up">▲3</div></div></td>
            <td><div style="font-size:14px;font-weight:500;">박영희 무패 스트릭 머그컵</div></td>
            <td style="color:var(--text3);font-size:13px;">박영희</td>
            <td style="text-align:right;font-size:14px;font-weight:700;">321</td>
            <td style="text-align:right;color:var(--red);font-weight:700;">₩16,000</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ════ PRODUCT DETAIL PAGE ════ -->
<div class="page-wrap" id="page-product">
  <div class="breadcrumb">
    <span onclick="showPage('home');setActiveNav(document.querySelectorAll('.nav-link')[0])">굿즈 홈</span>
    <span class="sep">›</span>
    <span onclick="showPage('fighter-detail')">홍길동</span>
    <span class="sep">›</span>
    <span class="current">챔피언 등극 기념 티셔츠</span>
  </div>
  <div class="detail-layout">
    <div class="detail-images">
      <div class="main-img">👕</div>
      <div class="thumb-row">
        <div class="thumb active">👕</div>
        <div class="thumb">📐</div>
        <div class="thumb">🏷️</div>
        <div class="thumb">📦</div>
      </div>
    </div>
    <div class="detail-info">
      <div class="detail-fighter-tag" onclick="showPage('fighter-detail')">🥊 홍길동 · UFC 웰터급 챔피언</div>
      <div class="detail-name">홍길동 챔피언 등극 기념 티셔츠</div>
      <div class="detail-price" id="display-price">₩45,000</div>
      <div class="detail-review">
        <div class="stars">★★★★★</div>
        <div style="font-size:14px;font-weight:700;">4.8</div>
        <div class="review-count">(23개 리뷰)</div>
      </div>
      <div class="detail-divider"></div>
      <div class="option-label">사이즈</div>
      <div class="option-row" id="size-opts">
        <button class="opt-btn" onclick="selectOpt(this,'size-opts')">S</button>
        <button class="opt-btn selected" onclick="selectOpt(this,'size-opts')">M</button>
        <button class="opt-btn" onclick="selectOpt(this,'size-opts')">L</button>
        <button class="opt-btn" onclick="selectOpt(this,'size-opts')">XL</button>
      </div>
      <div class="option-label">색상</div>
      <div class="option-row" id="color-opts">
        <button class="opt-btn selected" onclick="selectOpt(this,'color-opts')">블랙</button>
        <button class="opt-btn" onclick="selectOpt(this,'color-opts')">화이트</button>
        <button class="opt-btn" onclick="selectOpt(this,'color-opts')">레드</button>
      </div>
      <div class="qty-row">
        <div class="qty-label">수량</div>
        <div class="qty-ctrl">
          <button class="qty-btn" onclick="changeQty(-1)">−</button>
          <div class="qty-val" id="qty-val">1</div>
          <button class="qty-btn" onclick="changeQty(1)">+</button>
        </div>
      </div>
      <div class="price-summary">
        <div class="price-row"><span class="plabel">상품금액</span><span id="price-sub">₩45,000</span></div>
        <div class="price-row"><span class="plabel">배송비</span><span>₩3,000</span></div>
        <div class="price-row total"><span>총 결제금액</span><span class="pval" id="price-total">₩48,000</span></div>
      </div>
      <div class="btn-row">
        <button class="btn-buy" onclick="showPage('payment')">바로구매</button>
        <button class="btn-cart" onclick="addToCart()">장바구니 담기</button>
      </div>
      <div class="detail-divider"></div>
      <div style="font-size:13px;color:var(--text3);line-height:1.8;">
        소재: 코튼 100% · 제조국: 한국<br>
        배송: 영업일 기준 2~3일 소요<br>
        교환/반품: 수령 후 7일 이내 가능
      </div>
      <div style="height:1px;background:var(--border);margin:24px 0;"></div>
      <div style="font-size:14px;font-weight:700;margin-bottom:16px;">구매 후기</div>
      <div id="review-list">
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:10px;padding:16px 18px;margin-bottom:10px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
            <div style="width:32px;height:32px;border-radius:50%;background:var(--bg4);display:flex;align-items:center;justify-content:center;">👤</div>
            <span style="font-size:13px;font-weight:500;">fight_fan92</span>
            <span style="color:#f4a261;font-size:12px;">★★★★★</span>
            <span style="font-size:11px;color:var(--text3);margin-left:auto;">2025.05.18</span>
          </div>
          <div style="font-size:13px;color:var(--text2);line-height:1.6;">퀄리티 대박이에요. 챔피언 등극 순간이 프린트되어 있어서 감동이 두 배입니다.</div>
        </div>
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:10px;padding:16px 18px;margin-bottom:10px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
            <div style="width:32px;height:32px;border-radius:50%;background:var(--bg4);display:flex;align-items:center;justify-content:center;">👤</div>
            <span style="font-size:13px;font-weight:500;">goods_collector</span>
            <span style="color:#f4a261;font-size:12px;">★★★★★</span>
            <span style="font-size:11px;color:var(--text3);margin-left:auto;">2025.05.17</span>
          </div>
          <div style="font-size:13px;color:var(--text2);line-height:1.6;">배송도 빠르고 원단이 부드러워요. 사이즈는 딱 맞게 왔습니다.</div>
        </div>
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:10px;padding:16px 18px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
            <div style="width:32px;height:32px;border-radius:50%;background:var(--bg4);display:flex;align-items:center;justify-content:center;">👤</div>
            <span style="font-size:13px;font-weight:500;">ufc_lover</span>
            <span style="color:#f4a261;font-size:12px;">★★★★☆</span>
            <span style="font-size:11px;color:var(--text3);margin-left:auto;">2025.05.15</span>
          </div>
          <div style="font-size:13px;color:var(--text2);line-height:1.6;">디자인은 정말 마음에 드는데 배송이 하루 늦었어요. 재구매 의사 있습니다!</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════ CART PAGE ════ -->
<div class="page-wrap" id="page-cart">
  <div class="cart-layout">
    <div class="cart-items">
      <div class="cart-head">장바구니</div>
      <div class="cart-item">
        <div class="cart-img">👕</div>
        <div class="cart-item-info">
          <div class="cart-item-name">홍길동 챔피언 등극 기념 티셔츠</div>
          <div class="cart-item-opt">사이즈: M · 색상: 블랙</div>
          <div class="cart-item-bottom">
            <div style="display:flex;align-items:center;gap:0;border:1px solid var(--border2);border-radius:8px;overflow:hidden;">
              <button class="qty-btn" onclick="changeCartQty(-1)" style="width:36px;height:36px;">−</button>
              <div class="qty-val" id="cart-qty" style="width:44px;height:36px;display:flex;align-items:center;justify-content:center;background:var(--bg3);">1</div>
              <button class="qty-btn" onclick="changeCartQty(1)" style="width:36px;height:36px;">+</button>
            </div>
            <div class="cart-item-price" id="cart-item-price">₩45,000</div>
          </div>
          <button class="remove-btn" style="margin-top:8px;">삭제</button>
        </div>
      </div>
    </div>
    <div>
      <div class="cart-summary">
        <div class="summary-title">주문 요약</div>
        <div class="coupon-row">
          <input class="coupon-input" placeholder="쿠폰 코드 입력" id="coupon-input">
          <button class="coupon-btn" onclick="applyCoupon()">적용</button>
        </div>
        <div class="summary-row"><span class="slabel">상품금액</span><span id="cart-sub-total">₩45,000</span></div>
        <div class="summary-row" id="discount-row" style="display:none;color:#2d6a4f;"><span class="slabel">할인</span><span id="discount-amt">-₩0</span></div>
        <div class="summary-row"><span class="slabel">배송비</span><span>₩3,000</span></div>
        <div class="summary-divider"></div>
        <div class="summary-total"><span>총 결제금액</span><span class="tval" id="cart-grand-total">₩48,000</span></div>
        <button class="btn-red" onclick="showPage('payment')" style="width:100%;">결제하기</button>
      </div>
    </div>
  </div>
</div>

<!-- ════ SCHEDULE PAGE ════ -->
<div class="page-wrap" id="page-schedule">
  <div class="section">
    <div class="section-head">
      <div class="section-label">경기 정보</div>
      <div class="section-title">경기 일정 &amp; 결과</div>
    </div>
    <div style="margin-bottom:24px;">
      <div class="ranking-tabs" style="margin-bottom:0;">
        <button class="ranking-tab active" onclick="switchScheduleTab(this,'calendar')">캘린더</button>
        <button class="ranking-tab" onclick="switchScheduleTab(this,'results')">경기 결과</button>
        <button class="ranking-tab" onclick="switchScheduleTab(this,'preview')">대결 프리뷰</button>
        <button class="ranking-tab" onclick="switchScheduleTab(this,'highlight')">하이라이트</button>
      </div>
    </div>
    <div id="sched-calendar">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
        <button class="btn-outline" style="padding:8px 16px;font-size:13px;" onclick="changeMonth(-1)">← 이전달</button>
        <div style="font-family:'Bebas Neue',sans-serif;font-size:24px;" id="cal-month-label"></div>
        <button class="btn-outline" style="padding:8px 16px;font-size:13px;" onclick="changeMonth(1)">다음달 →</button>
      </div>
      <div id="cal-grid" style="display:grid;grid-template-columns:repeat(7,1fr);gap:2px;"></div>
    </div>
    <div id="sched-results" style="display:none;">
      <div style="background:linear-gradient(135deg,#1a0608,#110305);border:1px solid rgba(230,57,70,0.4);border-radius:16px;padding:24px 32px;margin-bottom:16px;cursor:pointer;" onclick="showPage('fighter-detail')">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:16px;"><span style="background:var(--red);color:#fff;padding:3px 10px;border-radius:6px;font-size:11px;font-weight:700;">방금 종료</span><span style="font-size:13px;color:var(--text2);">UFC 298 · 2025.05.17</span></div>
        <div style="display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:24px;margin-bottom:16px;">
          <div style="text-align:center;"><div style="font-family:'Bebas Neue',sans-serif;font-size:36px;color:var(--red);">홍길동</div><div style="font-size:12px;color:var(--text3);">UFC 웰터급 챔피언</div></div>
          <div style="text-align:center;"><div style="font-family:'Bebas Neue',sans-serif;font-size:22px;color:var(--red);">KO 승</div><div style="font-size:11px;color:var(--text3);">1R 2:34</div></div>
          <div style="text-align:center;"><div style="font-family:'Bebas Neue',sans-serif;font-size:36px;">맥스 홀로웨이</div><div style="font-size:12px;color:var(--text3);">UFC 웰터급</div></div>
        </div>
        <button class="btn-red" style="padding:10px 24px;font-size:13px;" onclick="event.stopPropagation();showPage('product')">연계 굿즈 바로구매 →</button>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:18px 24px;margin-bottom:10px;cursor:pointer;">
        <div style="font-size:11px;color:var(--text3);margin-bottom:8px;">ZFN 38 · 2025.05.10</div>
        <div style="display:flex;justify-content:space-between;"><span style="font-size:15px;font-weight:500;">이철수 vs 김용재</span><span style="color:#95d5b2;font-weight:700;">판정 승</span></div>
      </div>
    </div>
    <div id="sched-preview" style="display:none;">
      <div style="background:linear-gradient(135deg,#1a0608,#110305);border:1px solid rgba(230,57,70,0.3);border-radius:14px;padding:28px;">
        <div style="font-size:11px;color:var(--red);font-weight:700;margin-bottom:16px;">UFC 308 · D-14 예정</div>
        <div style="display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:24px;margin-bottom:20px;">
          <div style="text-align:center;"><div style="font-family:'Bebas Neue',sans-serif;font-size:32px;">홍길동</div><div style="font-size:12px;color:var(--text3);">12W 3L · 챔피언</div><div style="display:flex;gap:6px;justify-content:center;margin-top:8px;"><span style="font-size:11px;padding:2px 8px;background:var(--bg4);border:1px solid var(--border);border-radius:10px;color:var(--text3);">KO 전문</span><span style="font-size:11px;padding:2px 8px;background:var(--bg4);border:1px solid var(--border);border-radius:10px;color:var(--text3);">강한 턱</span></div></div>
          <div style="font-family:'Bebas Neue',sans-serif;font-size:32px;color:var(--text3);text-align:center;">VS</div>
          <div style="text-align:center;"><div style="font-family:'Bebas Neue',sans-serif;font-size:32px;">볼코노프스키</div><div style="font-size:12px;color:var(--text3);">26W 3L · 전 챔피언</div><div style="display:flex;gap:6px;justify-content:center;margin-top:8px;"><span style="font-size:11px;padding:2px 8px;background:var(--bg4);border:1px solid var(--border);border-radius:10px;color:var(--text3);">레슬링</span><span style="font-size:11px;padding:2px 8px;background:var(--bg4);border:1px solid var(--border);border-radius:10px;color:var(--text3);">스태미나</span></div></div>
        </div>
        <div style="display:flex;gap:10px;"><button class="btn-red" style="padding:10px 20px;font-size:13px;" onclick="showPage('product')">홍길동 예고 굿즈 →</button><button class="btn-outline" style="padding:10px 20px;font-size:13px;" onclick="showToast('✓ 경기 알림이 신청되었습니다')">경기 알림 신청</button></div>
      </div>
    </div>
    <div id="sched-highlight" style="display:none;">
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;overflow:hidden;margin-bottom:16px;">
        <div style="height:200px;background:linear-gradient(135deg,#1a1a2e,#16213e);display:flex;align-items:center;justify-content:center;font-size:56px;position:relative;cursor:pointer;" onclick="showToast('공식 유튜브 링크로 이동합니다')">
          🎬<div style="position:absolute;width:60px;height:60px;border-radius:50%;background:rgba(230,57,70,0.9);display:flex;align-items:center;justify-content:center;font-size:24px;">▶</div>
        </div>
        <div style="padding:14px 18px;"><div style="font-size:14px;font-weight:500;margin-bottom:4px;">UFC 298 홍길동 KO 하이라이트</div><div style="font-size:12px;color:var(--text3);margin-bottom:10px;">공식 UFC 유튜브 · 2025.05.17</div><button class="btn-red" style="padding:8px 18px;font-size:12px;" onclick="showPage('product')">관련 굿즈 보기 →</button></div>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;overflow:hidden;">
        <div style="height:200px;background:linear-gradient(135deg,#1e2a1e,#162116);display:flex;align-items:center;justify-content:center;font-size:56px;position:relative;cursor:pointer;" onclick="showToast('공식 유튜브 링크로 이동합니다')">
          🎬<div style="position:absolute;width:60px;height:60px;border-radius:50%;background:rgba(230,57,70,0.9);display:flex;align-items:center;justify-content:center;font-size:24px;">▶</div>
        </div>
        <div style="padding:14px 18px;"><div style="font-size:14px;font-weight:500;margin-bottom:4px;">ZFN 38 이철수 판정 하이라이트</div><div style="font-size:12px;color:var(--text3);">ZFN 공식 유튜브 · 2025.05.10</div></div>
      </div>
    </div>
  </div>
</div>

<!-- ════ NOTICE PAGE ════ -->
<div class="page-wrap" id="page-notice">
  <div class="section">
    <div class="section-head"><div class="section-label">공지사항</div><div class="section-title">공지사항</div></div>
    <div style="max-width:800px;">
      <div style="display:flex;gap:14px;align-items:flex-start;padding:18px 0;border-bottom:1px solid var(--border);cursor:pointer;">
        <span style="background:rgba(230,57,70,0.15);color:var(--red);border:1px solid rgba(230,57,70,0.3);font-size:10px;font-weight:700;padding:2px 8px;border-radius:4px;flex-shrink:0;margin-top:2px;">공지</span>
        <div><div style="font-size:14px;font-weight:500;margin-bottom:4px;">[필독] 5월 배송 지연 안내</div><div style="font-size:11px;color:var(--text3);">2025.05.15</div></div>
      </div>
      <div style="display:flex;gap:14px;align-items:flex-start;padding:18px 0;border-bottom:1px solid var(--border);cursor:pointer;">
        <span style="background:rgba(230,57,70,0.15);color:var(--red);border:1px solid rgba(230,57,70,0.3);font-size:10px;font-weight:700;padding:2px 8px;border-radius:4px;flex-shrink:0;margin-top:2px;">공지</span>
        <div><div style="font-size:14px;font-weight:500;margin-bottom:4px;">UFC 298 연계 굿즈 출시 안내</div><div style="font-size:11px;color:var(--text3);">2025.05.17</div></div>
      </div>
      <div style="display:flex;gap:14px;align-items:flex-start;padding:18px 0;border-bottom:1px solid var(--border);cursor:pointer;">
        <div style="width:34px;"></div>
        <div><div style="font-size:14px;font-weight:500;margin-bottom:4px;">시스템 점검 예정 안내 (5/20 02:00~04:00)</div><div style="font-size:11px;color:var(--text3);">2025.05.13</div></div>
      </div>
      <div style="display:flex;gap:14px;align-items:flex-start;padding:18px 0;border-bottom:1px solid var(--border);cursor:pointer;">
        <div style="width:34px;"></div>
        <div><div style="font-size:14px;font-weight:500;margin-bottom:4px;">이용약관 개정 안내 (2025.06.01 시행)</div><div style="font-size:11px;color:var(--text3);">2025.05.01</div></div>
      </div>
      <div style="display:flex;gap:14px;align-items:flex-start;padding:18px 0;cursor:pointer;">
        <div style="width:34px;"></div>
        <div><div style="font-size:14px;font-weight:500;margin-bottom:4px;">FIGHTGOODS 서비스 오픈 안내</div><div style="font-size:11px;color:var(--text3);">2025.04.01</div></div>
      </div>
    </div>
  </div>
</div>

<!-- ════ FAQ PAGE ════ -->
<div class="page-wrap" id="page-faq">
  <div class="section">
    <div class="section-head"><div class="section-label">고객지원</div><div class="section-title">FAQ &amp; 1:1 문의</div></div>
    <div style="display:grid;grid-template-columns:1fr 340px;gap:40px;align-items:start;">
      <div>
        <div style="display:flex;align-items:center;gap:10px;background:var(--bg3);border:1px solid var(--border2);border-radius:10px;padding:12px 18px;margin-bottom:16px;">
          <span>🔍</span><input id="faq-search" placeholder="궁금한 점을 검색하세요" oninput="filterFaq()" style="flex:1;background:none;border:none;outline:none;color:var(--text);font-size:14px;font-family:inherit;">
        </div>
        <div style="display:flex;gap:8px;margin-bottom:20px;" id="faq-cats">
          <button class="chip active" data-cat="전체" onclick="filterFaqCat(this)">전체</button>
          <button class="chip" data-cat="배송" onclick="filterFaqCat(this)">배송</button>
          <button class="chip" data-cat="교환반품" onclick="filterFaqCat(this)">교환/반품</button>
          <button class="chip" data-cat="결제" onclick="filterFaqCat(this)">결제</button>
          <button class="chip" data-cat="굿즈" onclick="filterFaqCat(this)">굿즈</button>
        </div>
        <div id="faq-list"></div>
      </div>
      <div>
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:24px;">
          <div style="font-size:14px;font-weight:700;margin-bottom:16px;">1:1 문의 접수</div>
          <div style="font-size:12px;color:var(--text3);margin-bottom:16px;line-height:1.7;">운영시간: 평일 10:00~18:00<br>운영시간 외에는 챗봇이 자동 응답합니다.</div>
          <select style="width:100%;padding:10px 14px;background:var(--bg4);border:1px solid var(--border2);border-radius:8px;color:var(--text);font-size:13px;font-family:inherit;margin-bottom:10px;outline:none;">
            <option>문의 유형 선택</option><option>상품 불량</option><option>오배송</option><option>미배송</option><option>결제 오류</option><option>기타</option>
          </select>
          <textarea placeholder="문의 내용을 입력해주세요" style="width:100%;padding:10px 14px;background:var(--bg4);border:1px solid var(--border2);border-radius:8px;color:var(--text);font-size:13px;font-family:inherit;resize:vertical;min-height:100px;margin-bottom:10px;outline:none;"></textarea>
          <button class="btn-red" style="width:100%;padding:12px;" onclick="showToast('✓ 문의가 접수되었습니다. 접수번호: #20250517-CS042')">문의 접수</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════ MYPAGE ════ -->
<div class="page-wrap" id="page-mypage">
  <div style="display:grid;grid-template-columns:240px 1fr;gap:32px;padding:40px 80px 60px;">
    <div style="position:sticky;top:calc(var(--nav-h) + 24px);height:fit-content;">
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:24px;margin-bottom:16px;text-align:center;" id="mypage-profile-box">
        <div id="mypage-avatar" style="width:72px;height:72px;border-radius:50%;background:var(--red);display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:700;color:#fff;margin:0 auto 12px;">?</div>
        <div id="mypage-name" style="font-size:16px;font-weight:700;margin-bottom:4px;">로그인이 필요합니다</div>
        <div id="mypage-email" style="font-size:12px;color:var(--text3);"></div>
        <div id="mypage-point" style="font-size:13px;color:var(--red);font-weight:700;margin-top:8px;"></div>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;overflow:hidden;">
        <div class="mypage-menu-item active" id="menu-orders" onclick="switchMypageTab('orders')">📦 구매내역</div>
        <div class="mypage-menu-item" id="menu-profile" onclick="switchMypageTab('profile')">👤 정보수정</div>
        <div class="mypage-menu-item" id="menu-delivery" onclick="switchMypageTab('delivery')">🚚 배송조회</div>
        <div class="mypage-menu-item" id="menu-withdraw" onclick="switchMypageTab('withdraw')">⚠️ 계정탈퇴</div>
      </div>
    </div>
    <div id="mypage-content" style="min-height:400px;"></div>
  </div>
</div>

<!-- ════ PAYMENT PAGE ════ -->
<div class="page-wrap" id="page-payment">
  <div class="payment-layout">
    <div>
      <div class="payment-head">결제</div>
      <div class="payment-block">
        <div class="payment-section-title">배송지 정보</div>
        <div class="address-box">
          <div class="address-row" style="font-weight:500;">홍길동 · 010-1234-5678</div>
          <div class="address-detail" style="margin-top:6px;">서울특별시 성북구 안암로 145, 101동 1302호</div>
          <button class="btn-outline" style="margin-top:12px;padding:8px 16px;font-size:12px;">배송지 변경</button>
        </div>
      </div>
      <div class="payment-block">
        <div class="payment-section-title">결제 수단</div>
        <div class="pay-methods" id="pay-methods">
          <button class="pay-method" onclick="selectPay(this)">신용/체크카드</button>
          <button class="pay-method selected" onclick="selectPay(this)">카카오페이</button>
          <button class="pay-method" onclick="selectPay(this)">토스페이</button>
          <button class="pay-method" onclick="selectPay(this)">네이버페이</button>
          <button class="pay-method" onclick="selectPay(this)" style="grid-column:span 4;">무통장입금 (가상계좌)</button>
        </div>
      </div>
      <div class="payment-block">
        <div class="payment-section-title">할인 적용</div>
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:10px;padding:16px 20px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
            <span style="font-size:13px;color:var(--text2);">보유 적립금</span>
            <span style="font-size:14px;font-weight:700;">1,500 P</span>
          </div>
          <div style="display:flex;gap:8px;">
            <input class="coupon-input" placeholder="사용할 포인트 입력 (100P 단위)" style="flex:1;">
            <button class="coupon-btn">적용</button>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="order-summary-card">
        <div style="font-size:16px;font-weight:700;margin-bottom:16px;">주문 상품</div>
        <div class="os-item">
          <div class="os-img">👕</div>
          <div class="os-info">
            <div class="os-name">홍길동 챔피언 등극 기념 티셔츠</div>
            <div class="os-opt">M · 블랙 · 1개</div>
          </div>
          <div class="os-price">₩45,000</div>
        </div>
        <div style="margin-top:16px;">
          <div class="summary-row"><span class="slabel" style="font-size:13px;">상품금액</span><span>₩45,000</span></div>
          <div class="summary-row"><span class="slabel" style="font-size:13px;">배송비</span><span>₩3,000</span></div>
          <div class="summary-divider"></div>
          <div class="summary-total"><span>총 결제금액</span><span class="tval">₩48,000</span></div>
          <button class="btn-buy" onclick="doConfirm()">결제하기</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════ ORDER CONFIRM PAGE ════ -->
<div class="page-wrap" id="page-confirm">
  <div class="confirm-wrap">
    <div class="confirm-icon">✓</div>
    <div class="confirm-title">결제 완료!</div>
    <div class="confirm-sub">주문 확인 이메일이 발송되었습니다</div>
    <div class="confirm-box" id="confirm-detail-area">
      <div class="confirm-row"><span class="clabel">주문번호</span><span class="cval">#20250517-0042</span></div>
      <div class="confirm-row"><span class="clabel">상품</span><span class="cval">홍길동 챔피언 기념 티셔츠 (M) ×1</span></div>
      <div class="confirm-row"><span class="clabel">결제금액</span><span class="cval" style="color:var(--red);">₩48,000</span></div>
      <div class="confirm-row"><span class="clabel">결제수단</span><span class="cval">카카오페이</span></div>
      <div class="confirm-row"><span class="clabel">배송지</span><span class="cval">서울특별시 성북구</span></div>
      <div class="confirm-row"><span class="clabel">예상 배송일</span><span class="cval">2025년 5월 20일</span></div>
    </div>
    <div class="confirm-btns">
      <button class="btn-red" onclick="showPage('home');setActiveNav(document.querySelectorAll('.nav-link')[0])">쇼핑 계속하기</button>
      <button class="btn-outline">주문 내역 확인</button>
    </div>
  </div>
</div>

<!-- ════ COMMUNITY PAGE ════ -->
<div class="page-wrap" id="page-community">
  <div class="section">
    <div class="section-head">
      <div class="section-label">커뮤니티</div>
      <div class="section-title">팬 커뮤니티</div>
    </div>

    <div style="display:grid;grid-template-columns:1fr 320px;gap:32px;align-items:start;">
      <!-- LEFT: BOARD -->
      <div>
        <!-- Tabs -->
        <div class="ranking-tabs" style="margin-bottom:20px;">
          <button class="ranking-tab active" onclick="switchBoardTab(this,'free')">자유게시판</button>
          <button class="ranking-tab" onclick="switchBoardTab(this,'review')">구매 후기</button>
          <button class="ranking-tab" onclick="switchBoardTab(this,'flex')">굿즈 자랑</button>
          <button class="ranking-tab" onclick="switchBoardTab(this,'match')">경기 토론</button>
        </div>

        <!-- Write button -->
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
          <div style="display:flex;gap:8px;">
            <button class="chip active">최신순</button>
            <button class="chip">인기순</button>
          </div>
          <button class="btn-red" style="padding:9px 20px;font-size:13px;" onclick="toggleWriteForm()">글쓰기 +</button>
        </div>

        <!-- Write form (hidden by default) -->
        <div id="write-form" style="display:none;background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:20px;margin-bottom:20px;">
          <input id="post-title" placeholder="제목을 입력하세요" style="width:100%;padding:10px 14px;background:var(--bg4);border:1px solid var(--border2);border-radius:8px;color:var(--text);font-size:14px;font-family:inherit;margin-bottom:10px;">
          <textarea id="post-body" placeholder="내용을 입력하세요" style="width:100%;padding:10px 14px;background:var(--bg4);border:1px solid var(--border2);border-radius:8px;color:var(--text);font-size:13px;font-family:inherit;resize:vertical;min-height:100px;margin-bottom:12px;"></textarea>
          <div style="display:flex;gap:8px;justify-content:flex-end;">
            <button class="btn-outline" style="padding:8px 20px;font-size:13px;" onclick="toggleWriteForm()">취소</button>
            <button class="btn-red" style="padding:8px 20px;font-size:13px;" onclick="submitPost()">등록</button>
          </div>
        </div>

        <!-- Post list -->
        <div id="post-list"></div>
      </div>

      <!-- RIGHT: SIDEBAR -->
      <div style="display:flex;flex-direction:column;gap:20px;">

        <!-- 선수 Q&A -->
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:22px;">
          <div style="font-size:11px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">이벤트</div>
          <div style="font-size:16px;font-weight:700;margin-bottom:6px;">선수 Q&A</div>
          <div style="font-size:12px;color:var(--text3);line-height:1.7;margin-bottom:14px;">홍길동 선수에게 질문을 남겨보세요.<br>질문 접수: ~2025.06.15 · 답변 공개: 7.01</div>
          <div style="background:var(--bg4);border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-bottom:10px;">
            <div style="font-size:13px;margin-bottom:6px;">"챔피언 벨트 따고 제일 먼저 한 일이 뭔가요?"</div>
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="font-size:11px;color:var(--text3);">fan_kim · 좋아요 142</span>
              <button style="font-size:11px;color:var(--red);background:none;border:none;cursor:pointer;font-family:inherit;" onclick="showToast('❤️ 좋아요!')">❤️ 142</button>
            </div>
          </div>
          <div style="background:var(--bg4);border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-bottom:14px;">
            <div style="font-size:13px;margin-bottom:6px;">"체급 조절 당시 가장 힘들었던 점은?"</div>
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="font-size:11px;color:var(--text3);">mma_lover · 좋아요 87</span>
              <button style="font-size:11px;color:var(--red);background:none;border:none;cursor:pointer;font-family:inherit;" onclick="showToast('❤️ 좋아요!')">❤️ 87</button>
            </div>
          </div>
          <button class="btn-outline" style="width:100%;padding:9px;font-size:13px;" onclick="showToast('✓ 질문이 접수되었습니다 (+30P)')">질문 남기기 (+30P)</button>
        </div>

        <!-- 굿즈 투표 -->
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:22px;">
          <div style="font-size:11px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">투표 진행 중</div>
          <div style="font-size:16px;font-weight:700;margin-bottom:4px;">다음 굿즈 투표</div>
          <div style="font-size:11px;color:var(--text3);margin-bottom:16px;">마감: 2025.06.01 · 참여 시 +50P</div>
          <div id="vote-options">
            <div class="vote-item" data-idx="0" onclick="castVote(0)" style="margin-bottom:10px;cursor:pointer;">
              <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px;">
                <span>챔피언 후드 집업</span><span id="vpct-0">48%</span>
              </div>
              <div style="height:6px;background:var(--bg4);border-radius:3px;overflow:hidden;">
                <div id="vbar-0" style="height:100%;width:48%;background:var(--red);border-radius:3px;transition:width .4s;"></div>
              </div>
            </div>
            <div class="vote-item" data-idx="1" onclick="castVote(1)" style="margin-bottom:10px;cursor:pointer;">
              <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px;">
                <span>등극 기념 키링 세트</span><span id="vpct-1">31%</span>
              </div>
              <div style="height:6px;background:var(--bg4);border-radius:3px;overflow:hidden;">
                <div id="vbar-1" style="height:100%;width:31%;background:var(--border2);border-radius:3px;transition:width .4s;"></div>
              </div>
            </div>
            <div class="vote-item" data-idx="2" onclick="castVote(2)" style="cursor:pointer;">
              <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px;">
                <span>포토북</span><span id="vpct-2">21%</span>
              </div>
              <div style="height:6px;background:var(--bg4);border-radius:3px;overflow:hidden;">
                <div id="vbar-2" style="height:100%;width:21%;background:var(--border2);border-radius:3px;transition:width .4s;"></div>
              </div>
            </div>
          </div>
          <div style="font-size:11px;color:var(--text3);margin-top:12px;text-align:right;">총 2,341명 참여</div>
        </div>

        <!-- 경기 승부 예측 -->
        <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:22px;">
          <div style="font-size:11px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">승부 예측 · +100P</div>
          <div style="font-size:14px;font-weight:700;margin-bottom:4px;">UFC 308 메인이벤트</div>
          <div style="font-size:11px;color:var(--text3);margin-bottom:14px;">홍길동 vs 알렉산더 볼코노프스키</div>
          <div style="display:flex;gap:8px;">
            <button class="pay-method" onclick="castPredict(this,'홍길동')" style="flex:1;padding:12px 8px;">홍길동 승</button>
            <button class="pay-method" onclick="castPredict(this,'볼코노프스키')" style="flex:1;padding:12px 8px;">볼코노프스키 승</button>
          </div>
        </div>

      </div>
    </div>
  </div>
</div>

<!-- TOAST -->
<div class="toast" id="toast"></div>

<script>
let qty = 1;
let cartQty = 1;
const BASE_PRICE = 45000;
const SHIPPING = 3000;

function showPage(name) {
  document.querySelectorAll('.page-wrap').forEach(p => p.classList.remove('active'));
  const el = document.getElementById('page-' + name);
  if (el) { el.classList.add('active'); window.scrollTo({top:0,behavior:'smooth'}); }
  if (name === 'mypage') renderMypage();
  if (name === 'product') { addRecentViewed(PRODUCTS[0]); }
  if (name === 'schedule') renderCalendar();
  if (name === 'faq') renderFaq(FAQ_DATA);
}

function setActiveNav(el) {
  document.querySelectorAll('.nav-link').forEach(n => n.classList.remove('active'));
  el.classList.add('active');
}

function selectOpt(btn, groupId) {
  document.querySelectorAll('#' + groupId + ' .opt-btn').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
}

function selectPay(btn) {
  document.querySelectorAll('#pay-methods .pay-method').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
}

function changeQty(delta) {
  qty = Math.max(1, Math.min(99, qty + delta));
  document.getElementById('qty-val').textContent = qty;
  const sub = BASE_PRICE * qty;
  document.getElementById('price-sub').textContent = '₩' + sub.toLocaleString();
  document.getElementById('price-total').textContent = '₩' + (sub + SHIPPING).toLocaleString();
}

function changeCartQty(delta) {
  cartQty = Math.max(1, Math.min(99, cartQty + delta));
  document.getElementById('cart-qty').textContent = cartQty;
  const sub = BASE_PRICE * cartQty;
  document.getElementById('cart-item-price').textContent = '₩' + sub.toLocaleString();
  document.getElementById('cart-sub-total').textContent = '₩' + sub.toLocaleString();
  const disc = parseInt(document.getElementById('discount-amt')?.textContent?.replace(/[^0-9]/g,'')) || 0;
  document.getElementById('cart-grand-total').textContent = '₩' + (sub + SHIPPING - disc).toLocaleString();
}

let couponApplied = false;
function applyCoupon() {
  if (couponApplied) return;
  const val = document.getElementById('coupon-input').value.trim().toUpperCase();
  if (val === 'FIGHT10') {
    couponApplied = true;
    const disc = Math.floor(BASE_PRICE * cartQty * 0.1);
    const row = document.getElementById('discount-row');
    row.style.display = 'flex';
    document.getElementById('discount-amt').textContent = '-₩' + disc.toLocaleString();
    const sub = BASE_PRICE * cartQty;
    document.getElementById('cart-grand-total').textContent = '₩' + (sub + SHIPPING - disc).toLocaleString();
    showToast('🎉 쿠폰 적용 완료! 10% 할인되었습니다');
  } else {
    showToast('유효하지 않은 쿠폰 코드입니다');
  }
}

function addToCart() {
  const count = document.getElementById('cart-count');
  count.textContent = parseInt(count.textContent) + 1;
  showToast('✓ 장바구니에 담겼습니다');
}

function switchRankTab(el, type) {
  document.querySelectorAll('.ranking-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}

// ── COMMUNITY ──
const defaultPosts = [
  { id:1, title:'홍길동 KO 진짜 소름...', body:'1라운드에 저렇게 끝낼 줄 몰랐다 ㄷㄷ 챔피언 등극 티셔츠 바로 샀음', author:'fight_fan92', likes:47, comments:12, time:'방금' },
  { id:2, title:'챔피언 벨트 포스터 받았어요 후기', body:'퀄리티 생각보다 훨씬 좋음. 액자 끼워서 걸었는데 진짜 인테리어 됨', author:'goods_collector', likes:38, comments:8, time:'10분 전' },
  { id:3, title:'이철수 다음 경기 언제임?', body:'ZFN 39 나오는지 아는 사람?', author:'mma_nerd', likes:15, comments:23, time:'1시간 전' },
  { id:4, title:'박영희 무패 언제까지 가나', body:'6연승 진짜 대단하다. 굿즈 없어서 아쉽', author:'zfn_watcher', likes:29, comments:6, time:'3시간 전' },
];
let posts = [...defaultPosts];
let nextId = 5;
let voted = false;
let predicted = false;
const voteData = [48, 31, 21];

function renderPosts() {
  const list = document.getElementById('post-list');
  if (!list) return;
  list.innerHTML = posts.map(p => `
    <div style="background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:18px 20px;margin-bottom:12px;cursor:pointer;transition:border-color .2s;" onmouseover="this.style.borderColor='var(--border2)'" onmouseout="this.style.borderColor='var(--border)'">
      <div style="font-size:15px;font-weight:500;margin-bottom:6px;">${p.title}</div>
      <div style="font-size:13px;color:var(--text3);margin-bottom:12px;line-height:1.6;">${p.body}</div>
      <div style="display:flex;align-items:center;gap:16px;font-size:12px;color:var(--text3);">
        <span>${p.author}</span><span>${p.time}</span>
        <span style="margin-left:auto;display:flex;gap:12px;">
          <button onclick="likePost(event,${p.id})" style="background:none;border:none;color:var(--text3);cursor:pointer;font-size:12px;font-family:inherit;transition:color .2s;" onmouseover="this.style.color='var(--red)'" onmouseout="this.style.color='var(--text3)'">❤️ ${p.likes}</button>
          <span>💬 ${p.comments}</span>
        </span>
      </div>
    </div>
  `).join('');
}

function likePost(e, id) {
  e.stopPropagation();
  const p = posts.find(x => x.id === id);
  if (p) { p.likes++; renderPosts(); }
}

function toggleWriteForm() {
  const f = document.getElementById('write-form');
  f.style.display = f.style.display === 'none' ? 'block' : 'none';
}

function submitPost() {
  const title = document.getElementById('post-title').value.trim();
  const body = document.getElementById('post-body').value.trim();
  if (!title) { showToast('제목을 입력해주세요'); return; }
  posts.unshift({ id: nextId++, title, body: body || '내용 없음', author: '나', likes: 0, comments: 0, time: '방금' });
  renderPosts();
  document.getElementById('post-title').value = '';
  document.getElementById('post-body').value = '';
  toggleWriteForm();
  showToast('✓ 게시글이 등록되었습니다');
}

function switchBoardTab(el, type) {
  document.querySelectorAll('.ranking-tabs .ranking-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
}

function castVote(idx) {
  if (voted) { showToast('이미 투표하셨습니다'); return; }
  voted = true;
  voteData[idx] += 5;
  const total = voteData.reduce((a,b) => a+b, 0);
  voteData.forEach((v, i) => {
    const pct = Math.round(v / total * 100);
    document.getElementById('vpct-' + i).textContent = pct + '%';
    document.getElementById('vbar-' + i).style.width = pct + '%';
    document.getElementById('vbar-' + i).style.background = i === idx ? 'var(--red)' : 'var(--border2)';
  });
  showToast('✓ 투표 완료! (+50P)');
}

function castPredict(btn, name) {
  if (predicted) { showToast('이미 예측하셨습니다'); return; }
  predicted = true;
  document.querySelectorAll('#page-community .pay-method').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
  showToast('✓ ' + name + ' 승 예측 완료! (+100P)');
}

// init
renderPosts();

document.querySelectorAll('.chip').forEach(c => {
  c.addEventListener('click', function() {
    document.querySelectorAll('.chip').forEach(x => x.classList.remove('active'));
    this.classList.add('active');
  });
});
// thumb click
document.querySelectorAll('.thumb').forEach(t => {
  t.addEventListener('click', function() {
    document.querySelectorAll('.thumb').forEach(x => x.classList.remove('active'));
    this.classList.add('active');
  });
});

// ── AUTH (localStorage) ──
let currentUser = null;

function loadAuth() {
  try { const u = localStorage.getItem('fg_user'); if (u) currentUser = JSON.parse(u); } catch(e) {}
  renderNavAuth();
  if (document.getElementById('page-mypage').classList.contains('active')) renderMypage();
}

function saveAuth(user) {
  currentUser = user;
  localStorage.setItem('fg_user', JSON.stringify(user));
  renderNavAuth();
}

function renderNavAuth() {
  const el = document.getElementById('nav-auth');
  if (!el) return;
  if (currentUser) {
    el.innerHTML = `
      <div class="user-btn" style="display:flex;align-items:center;gap:8px;padding:6px 14px;border-radius:8px;background:var(--bg3);border:1px solid var(--border);cursor:pointer;font-size:13px;" onclick="showPage('mypage');setActiveNav(document.querySelectorAll('.nav-link')[7])">
        <div class="user-avatar" style="width:26px;height:26px;border-radius:50%;background:var(--red);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">${currentUser.nick[0]}</div>
        <span>${currentUser.nick}</span>
      </div>
      <button style="padding:8px 14px;border-radius:8px;background:transparent;color:var(--text);font-size:13px;border:1px solid var(--border2);cursor:pointer;font-family:inherit;" onclick="doLogout()">로그아웃</button>`;
  } else {
    el.innerHTML = `<button class="login-btn" onclick="openModal('login')">로그인</button>`;
  }
}

function openModal(tab) {
  document.getElementById('auth-modal').classList.add('show');
  switchAuthTab(tab || 'login');
}
function closeModal() {
  document.getElementById('auth-modal').classList.remove('show');
}
function switchAuthTab(tab) {
  document.getElementById('tab-login').classList.toggle('active', tab === 'login');
  document.getElementById('tab-signup').classList.toggle('active', tab === 'signup');
  document.getElementById('form-login').style.display = tab === 'login' ? 'block' : 'none';
  document.getElementById('form-signup').style.display = tab === 'signup' ? 'block' : 'none';
}

function doLogin() {
  const email = document.getElementById('login-email').value.trim();
  const pw = document.getElementById('login-pw').value;
  const err = document.getElementById('login-err');
  if (!email || !pw) { err.textContent = '이메일과 비밀번호를 입력해주세요.'; err.style.display = 'block'; return; }
  try {
    const users = JSON.parse(localStorage.getItem('fg_users') || '[]');
    const user = users.find(u => u.email === email && u.pw === pw);
    if (!user) { err.textContent = '이메일 또는 비밀번호가 올바르지 않습니다.'; err.style.display = 'block'; return; }
    saveAuth(user);
    closeModal();
    showToast('✓ 로그인 완료! 환영합니다, ' + user.nick + '님');
    err.style.display = 'none';
  } catch(e) { err.textContent = '오류가 발생했습니다.'; err.style.display = 'block'; }
}

function doSocialLogin(provider) {
  const nick = provider + '유저' + Math.floor(Math.random() * 1000);
  const user = { email: nick + '@social.com', nick, pw: '', point: 500 };
  saveAuth(user);
  closeModal();
  showToast('✓ ' + provider + ' 로그인 완료! 환영합니다, ' + nick + '님');
}

function doLogout() {
  currentUser = null;
  localStorage.removeItem('fg_user');
  renderNavAuth();
  showToast('로그아웃 되었습니다');
}

function checkEmail(v) {
  const h = document.getElementById('su-email-hint');
  if (!v) { h.textContent = ''; return; }
  const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
  if (!valid) { h.className = 'form-hint err'; h.textContent = '올바른 이메일 형식이 아닙니다.'; return; }
  const users = JSON.parse(localStorage.getItem('fg_users') || '[]');
  if (users.find(u => u.email === v)) { h.className = 'form-hint err'; h.textContent = '이미 사용 중인 이메일입니다.'; }
  else { h.className = 'form-hint ok'; h.textContent = '사용 가능한 이메일입니다.'; }
}
function checkNick(v) {
  const h = document.getElementById('su-nick-hint');
  if (!v) { h.textContent = ''; return; }
  if (v.length < 2 || v.length > 10) { h.className = 'form-hint err'; h.textContent = '닉네임은 2~10자여야 합니다.'; return; }
  h.className = 'form-hint ok'; h.textContent = '사용 가능한 닉네임입니다.';
}
function checkPw(v) {
  const bar = document.getElementById('pw-strength-bar');
  const h = document.getElementById('su-pw-hint');
  const score = [/.{8,}/.test(v), /[A-Za-z]/.test(v), /[0-9]/.test(v), /[^A-Za-z0-9]/.test(v)].filter(Boolean).length;
  const colors = ['', '#e63946', '#f4a261', '#2d6a4f', '#2d6a4f'];
  const labels = ['', '약함', '보통', '강함', '매우 강함'];
  bar.style.width = (score * 25) + '%';
  bar.style.background = colors[score] || 'transparent';
  h.className = score >= 3 ? 'form-hint ok' : 'form-hint err';
  h.textContent = v ? labels[score] : '';
}
function checkPw2(v) {
  const h = document.getElementById('su-pw2-hint');
  const pw = document.getElementById('su-pw').value;
  if (!v) { h.textContent = ''; return; }
  if (v === pw) { h.className = 'form-hint ok'; h.textContent = '비밀번호가 일치합니다.'; }
  else { h.className = 'form-hint err'; h.textContent = '비밀번호가 일치하지 않습니다.'; }
}
function doSignup() {
  const email = document.getElementById('su-email').value.trim();
  const nick = document.getElementById('su-nick').value.trim();
  const pw = document.getElementById('su-pw').value;
  const pw2 = document.getElementById('su-pw2').value;
  const agree = document.getElementById('agree-terms').checked;
  const err = document.getElementById('su-err');
  if (!email || !nick || !pw || !pw2) { err.textContent = '모든 항목을 입력해주세요.'; err.style.display = 'block'; return; }
  if (pw !== pw2) { err.textContent = '비밀번호가 일치하지 않습니다.'; err.style.display = 'block'; return; }
  if (pw.length < 8) { err.textContent = '비밀번호는 8자 이상이어야 합니다.'; err.style.display = 'block'; return; }
  if (!agree) { err.textContent = '이용약관에 동의해주세요.'; err.style.display = 'block'; return; }
  try {
    const users = JSON.parse(localStorage.getItem('fg_users') || '[]');
    if (users.find(u => u.email === email)) { err.textContent = '이미 사용 중인 이메일입니다.'; err.style.display = 'block'; return; }
    const user = { email, nick, pw, point: 0 };
    users.push(user);
    localStorage.setItem('fg_users', JSON.stringify(users));
    saveAuth(user);
    closeModal();
    showToast('✓ 회원가입 완료! 환영합니다, ' + nick + '님');
    err.style.display = 'none';
  } catch(e) { err.textContent = '오류가 발생했습니다.'; err.style.display = 'block'; }
}

// close modal on overlay click
document.getElementById('auth-modal').addEventListener('click', function(e) {
  if (e.target === this) closeModal();
});

loadAuth();


// ── PRODUCT DATA ──
const PRODUCTS = [
  {id:1, name:'홍길동 챔피언 등극 기념 티셔츠', fighter:'홍길동 · UFC 웰터급', price:45000, icon:'👕', badge:'hot', stock:'재고 12개', cat:'티셔츠'},
  {id:2, name:'챔피언 벨트 아트 포스터', fighter:'홍길동 · UFC 웰터급', price:18000, icon:'🖼️', badge:'limited', stock:'한정 50개', cat:'포스터'},
  {id:3, name:'등극 순간 포토카드 세트', fighter:'홍길동 · UFC 웰터급', price:12000, icon:'📸', badge:'new', stock:'재고 있음', cat:'포토카드'},
  {id:4, name:'이철수 부상 극복 기념 후디', fighter:'이철수 · 블랙컴뱃 헤비급', price:68000, icon:'🎽', badge:'', stock:'재고 5개', cat:'후디'},
  {id:5, name:'박영희 무패 스트릭 머그컵', fighter:'박영희 · ZFN 밴텀급', price:16000, icon:'☕', badge:'new', stock:'재고 30개', cat:'포토카드'},
];
const FIGHTERS_DATA = [
  {icon:'🥊', name:'홍길동', meta:'웰터급 · UFC · 데뷔 2019.03.15', w:12, l:3, finish:'77%', tags:['챔피언 등극','체급 조절'], goods:3, org:'UFC', cls:'웰터급', active:true},
  {icon:'💪', name:'이철수', meta:'헤비급 · 블랙컴뱃 · 데뷔 2020.07.22', w:8, l:1, finish:'62%', tags:['부상 극복','무명 시절'], goods:1, org:'블랙컴뱃', cls:'헤비급', active:true},
  {icon:'⚡', name:'박영희', meta:'밴텀급 · ZFN · 데뷔 2022.11.05', w:6, l:0, finish:'83%', tags:['신인왕','연승 스트릭'], goods:2, org:'ZFN', cls:'밴텀급', active:true},
];
const FAQ_DATA = [
  {cat:'배송', q:'배송은 얼마나 걸리나요?', a:'결제 완료 후 영업일 2~3일 이내에 발송됩니다. 주말·공휴일은 제외됩니다.'},
  {cat:'배송', q:'배송비는 얼마인가요?', a:'기본 배송비는 3,000원이며, 50,000원 이상 구매 시 무료 배송입니다.'},
  {cat:'교환반품', q:'교환·반품은 어떻게 하나요?', a:'상품 수령 후 7일 이내에 마이페이지 > 구매내역에서 신청 가능합니다. 단순 변심의 경우 왕복 배송비가 발생합니다.'},
  {cat:'교환반품', q:'불량품을 받았어요.', a:'수령 후 7일 이내에 1:1 문의로 사진과 함께 접수해 주시면 무료로 교환 처리해 드립니다.'},
  {cat:'결제', q:'어떤 결제 수단을 지원하나요?', a:'신용/체크카드, 카카오페이, 토스페이, 네이버페이, 무통장입금(가상계좌)을 지원합니다.'},
  {cat:'결제', q:'결제 후 취소할 수 있나요?', a:'배송 시작 전까지 마이페이지 > 구매내역에서 취소 가능합니다. 카드 결제는 3~5영업일 내 환불됩니다.'},
  {cat:'굿즈', q:'한정판 상품은 어떻게 구매하나요?', a:'출시 예정 상품 페이지에서 알림 신청을 하시면 출시 당일 알림을 받으실 수 있습니다.'},
  {cat:'굿즈', q:'사이즈 가이드는 어디서 확인하나요?', a:'상품 상세 페이지 하단에 사이즈 가이드 이미지가 제공됩니다.'},
];
const CAL_EVENTS = {'2025-5-3':'ZFN 38','2025-5-10':'블랙컴뱃 15','2025-5-17':'UFC 298','2025-5-24':'ZFN 39','2025-5-31':'UFC 299'};

// ── RECENT VIEWED ──
let recentViewed = [];
function addRecentViewed(p) {
  recentViewed = recentViewed.filter(x => x.id !== p.id);
  recentViewed.unshift(p);
  if (recentViewed.length > 10) recentViewed.pop();
  renderRecentViewed();
}
function renderRecentViewed() {
  const el = document.getElementById('recent-viewed-wrap');
  if (!el || !recentViewed.length) return;
  el.innerHTML = '<div style="display:flex;gap:16px;overflow-x:auto;padding-bottom:8px;">' +
    recentViewed.map(p => `<div onclick="showPage('product')" style="flex-shrink:0;width:140px;cursor:pointer;">
      <div style="height:140px;background:linear-gradient(135deg,#1e1e2e,#2a1e2a);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:48px;border:1px solid var(--border);margin-bottom:8px;">${p.icon}</div>
      <div style="font-size:12px;margin-bottom:4px;">${p.name}</div>
      <div style="font-size:13px;font-weight:700;color:var(--red);">₩${p.price.toLocaleString()}</div>
    </div>`).join('') + '</div>';
}

// ── PRODUCT FILTER ──
function filterProducts(btn) {
  document.querySelectorAll('#product-filters .chip').forEach(c => c.classList.remove('active'));
  btn.classList.add('active');
  const cat = btn.dataset.cat;
  const filtered = cat === '전체' ? PRODUCTS : PRODUCTS.filter(p => p.cat === cat);
  renderProductGrid('home-product-grid', filtered);
}
function renderProductGrid(id, list) {
  const badgeMap = {hot:'<span class="p-badge badge-hot" style="position:absolute;top:12px;right:12px;padding:4px 10px;border-radius:6px;font-size:10px;font-weight:700;background:var(--red);color:#fff;">🔥 HOT</span>', limited:'<span style="position:absolute;top:12px;right:12px;padding:4px 10px;border-radius:6px;font-size:10px;font-weight:700;background:#ff6b35;color:#fff;">한정판</span>', new:'<span style="position:absolute;top:12px;right:12px;padding:4px 10px;border-radius:6px;font-size:10px;font-weight:700;background:#2d6a4f;color:#95d5b2;">NEW</span>'};
  const el = document.getElementById(id);
  if (!el) return;
  el.innerHTML = list.map(p => `<div class="product-card" onclick="goProduct(${p.id})">
    <div class="product-img">${p.icon}${badgeMap[p.badge]||''}</div>
    <div class="product-body"><div class="product-name">${p.name}</div><div class="product-fighter">${p.fighter}</div>
    <div class="product-bottom"><div class="product-price">₩${p.price.toLocaleString()}</div><div class="product-stock">${p.stock}</div></div></div>
  </div>`).join('');
}
function goProduct(id) {
  const p = PRODUCTS.find(x => x.id === id) || PRODUCTS[0];
  addRecentViewed(p);
  showPage('product');
}

// ── FIGHTER FILTER ──
function filterFighters(btn) {
  if (btn) {
    document.querySelectorAll('#page-fighters .filter-chip').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
  }
  const activeBtn = document.querySelector('#page-fighters .filter-chip.active');
  const f = activeBtn ? activeBtn.dataset.f : 'all';
  const filtered = f === 'all' ? FIGHTERS_DATA : FIGHTERS_DATA.filter(d => d.cls === f || d.org === f || (f === '현역' && d.active));
  const el = document.getElementById('fighters-grid');
  if (!el) return;
  el.innerHTML = filtered.length ? filtered.map(d => `<div class="fighter-card" onclick="showPage('fighter-detail')">
    <div class="fighter-avatar">${d.icon}</div>
    <div class="fighter-info">
      <div class="fighter-name">${d.name}</div>
      <div class="fighter-meta">${d.meta}</div>
      <div class="fighter-record">
        <div class="record-stat"><div class="record-val">${d.w}</div><div class="record-label">승</div></div>
        <div class="record-stat"><div class="record-val">${d.l}</div><div class="record-label">패</div></div>
        <div class="record-stat"><div class="record-val">${d.finish}</div><div class="record-label">피니시율</div></div>
      </div>
      <div class="fighter-tags">${d.tags.map(t=>'<span class="tag">'+t+'</span>').join('')}</div>
      <div class="fighter-goods-count">관련 굿즈 ${d.goods}개</div>
    </div>
  </div>`).join('') : '<div style="grid-column:span 3;text-align:center;padding:40px;color:var(--text3);">검색 결과가 없습니다</div>';
}

// ── SEARCH ──
const SEARCH_DATA = [
  ...PRODUCTS.map(p => ({label: p.name, page: 'product', type: '상품'})),
  ...FIGHTERS_DATA.map(f => ({label: f.name, page: 'fighter-detail', type: '선수'})),
];
function onSearch(v) {
  const dd = document.getElementById('search-dropdown');
  if (!v.trim()) { dd.style.display = 'none'; return; }
  const results = SEARCH_DATA.filter(d => d.label.toLowerCase().includes(v.toLowerCase())).slice(0, 8);
  if (!results.length) { dd.style.display = 'none'; return; }
  dd.innerHTML = results.map(r => `<div onclick="goSearchResult('${r.page}')" style="padding:10px 14px;font-size:13px;cursor:pointer;display:flex;gap:8px;align-items:center;" onmouseover="this.style.background='var(--bg4)'" onmouseout="this.style.background=''"><span style="font-size:10px;color:var(--text3);width:30px;">${r.type}</span>${r.label}</div>`).join('');
  dd.style.display = 'block';
}
function goSearchResult(page) {
  document.getElementById('search-input').value = '';
  closeSearch();
  showPage(page);
}
function closeSearch() {
  const dd = document.getElementById('search-dropdown');
  if (dd) dd.style.display = 'none';
}

// ── CALENDAR ──
let calYear = 2025, calMonth = 4;
function renderCalendar() {
  const label = calYear + '년 ' + (calMonth+1) + '월';
  const el = document.getElementById('cal-month-label');
  if (el) el.textContent = label;
  const grid = document.getElementById('cal-grid');
  if (!grid) return;
  const days = ['일','월','화','수','목','금','토'];
  let html = days.map(d => '<div style="text-align:center;padding:8px;font-size:11px;color:var(--text3);font-weight:700;">'+d+'</div>').join('');
  const first = new Date(calYear, calMonth, 1).getDay();
  const total = new Date(calYear, calMonth+1, 0).getDate();
  for (let i = 0; i < first; i++) html += '<div></div>';
  for (let d = 1; d <= total; d++) {
    const key = calYear+'-'+(calMonth+1)+'-'+d;
    const ev = CAL_EVENTS[key];
    html += '<div class="cal-cell '+(ev?'has-event':'')+'" onclick="'+( ev ? "showToast('"+ev+" 알림 신청됨')" : '' )+'"><div class="cal-date">'+d+'</div>'+(ev?'<div class="cal-event">'+ev+'</div>':'')+'</div>';
  }
  grid.innerHTML = html;
}
function changeMonth(delta) {
  calMonth += delta;
  if (calMonth < 0) { calMonth = 11; calYear--; }
  if (calMonth > 11) { calMonth = 0; calYear++; }
  renderCalendar();
}
function switchScheduleTab(el, tab) {
  document.querySelectorAll('#page-schedule .ranking-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  ['calendar','results','preview','highlight'].forEach(t => {
    const d = document.getElementById('sched-'+t);
    if (d) d.style.display = t === tab ? 'block' : 'none';
  });
}

// ── FAQ ──
function renderFaq(data) {
  const el = document.getElementById('faq-list');
  if (!el) return;
  el.innerHTML = data.map((f, i) => `<div class="faq-item">
    <div class="faq-q" onclick="toggleFaq(${i})"><span>[${f.cat}] ${f.q}</span><span class="faq-chevron" id="fc-${i}">▼</span></div>
    <div class="faq-a" id="fa-${i}">${f.a}</div>
  </div>`).join('');
}
function toggleFaq(i) {
  document.getElementById('fa-'+i).classList.toggle('open');
  document.getElementById('fc-'+i).classList.toggle('open');
}
function filterFaq() {
  const v = document.getElementById('faq-search').value;
  renderFaq(FAQ_DATA.filter(f => f.q.includes(v) || f.a.includes(v)));
}
function filterFaqCat(btn) {
  document.querySelectorAll('#faq-cats .chip').forEach(c => c.classList.remove('active'));
  btn.classList.add('active');
  const cat = btn.dataset.cat;
  renderFaq(cat === '전체' ? FAQ_DATA : FAQ_DATA.filter(f => f.cat === cat));
}

// ── MYPAGE ──
function renderMypage() {
  const av = document.getElementById('mypage-avatar');
  const nm = document.getElementById('mypage-name');
  const em = document.getElementById('mypage-email');
  const pt = document.getElementById('mypage-point');
  if (!av) return;
  if (currentUser) {
    av.textContent = currentUser.nick[0];
    nm.textContent = currentUser.nick;
    em.textContent = currentUser.email;
    pt.textContent = '적립금: ' + (currentUser.point || 0) + ' P';
  } else {
    av.textContent = '?';
    nm.textContent = '로그인이 필요합니다';
    em.textContent = '';
    pt.textContent = '';
  }
  switchMypageTab('orders');
}
function switchMypageTab(tab) {
  ['orders','profile','delivery','withdraw'].forEach(t => {
    const el = document.getElementById('menu-'+t);
    if (el) el.classList.toggle('active', t === tab);
  });
  const content = document.getElementById('mypage-content');
  if (!content) return;
  if (!currentUser) {
    content.innerHTML = '<div style="text-align:center;padding:60px 20px;color:var(--text3);"><div style="font-size:48px;margin-bottom:16px;">🔐</div><div style="margin-bottom:16px;">로그인 후 이용 가능합니다</div><button class="btn-primary" style="width:auto;padding:12px 32px;" onclick="openModal('login')">로그인</button></div>';
    return;
  }
  if (tab === 'orders') {
    const orders = currentUser.orders || [];
    if (!orders.length) {
      content.innerHTML = '<div style="font-family:'Bebas Neue',sans-serif;font-size:24px;letter-spacing:1px;margin-bottom:20px;">구매 내역</div><div style="text-align:center;padding:60px 20px;color:var(--text3);"><div style="font-size:48px;margin-bottom:12px;">📦</div><div>구매 내역이 없습니다</div></div>';
      return;
    }
    content.innerHTML = '<div style="font-family:'Bebas Neue',sans-serif;font-size:24px;letter-spacing:1px;margin-bottom:20px;">구매 내역</div>' +
      orders.map(o => `<div style="background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:20px 24px;margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;padding-bottom:12px;border-bottom:1px solid var(--border);">
          <div style="font-size:12px;color:var(--text3);">${o.num} · ${o.date}</div>
          <span style="font-size:12px;font-weight:700;padding:4px 10px;border-radius:6px;background:rgba(230,57,70,0.15);color:var(--red);">${o.status}</span>
        </div>
        <div style="display:flex;gap:14px;align-items:center;">
          <div style="width:60px;height:60px;border-radius:8px;background:var(--bg4);display:flex;align-items:center;justify-content:center;font-size:28px;flex-shrink:0;">👕</div>
          <div style="flex:1;"><div style="font-size:14px;font-weight:500;margin-bottom:4px;">${o.name}</div><div style="font-size:11px;color:var(--text3);">1개</div></div>
          <div style="font-size:15px;font-weight:700;color:var(--red);">₩${o.price.toLocaleString()}</div>
        </div>
        <div style="display:flex;gap:8px;margin-top:14px;">
          <button class="btn-outline" style="padding:7px 14px;font-size:12px;" onclick="showToast('배송 조회 페이지로 이동합니다')">배송 조회</button>
          <button class="btn-outline" style="padding:7px 14px;font-size:12px;" onclick="showToast('교환/반품 신청이 접수되었습니다')">교환/반품</button>
          <button class="btn-outline" style="padding:7px 14px;font-size:12px;border-color:var(--red);color:var(--red);" onclick="cancelOrder(this)">주문 취소</button>
        </div>
      </div>`).join('');
  } else if (tab === 'profile') {
    content.innerHTML = `<div style="font-family:'Bebas Neue',sans-serif;font-size:24px;letter-spacing:1px;margin-bottom:20px;">정보 수정</div>
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:28px;max-width:480px;">
        <div class="form-group"><div class="form-label">닉네임</div><input class="form-input" id="edit-nick" value="${currentUser.nick}"></div>
        <div class="form-group"><div class="form-label">이메일</div><input class="form-input" value="${currentUser.email}" disabled style="opacity:.5;"></div>
        <button class="btn-primary" style="margin-top:8px;" onclick="saveProfile()">저장</button>
      </div>`;
  } else if (tab === 'delivery') {
    content.innerHTML = `<div style="font-family:'Bebas Neue',sans-serif;font-size:24px;letter-spacing:1px;margin-bottom:20px;">배송 조회</div>
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:28px;max-width:480px;">
        <div class="form-group"><div class="form-label">운송장 번호</div>
          <div style="display:flex;gap:8px;"><input class="form-input" id="track-num" placeholder="운송장 번호 입력"><button class="coupon-btn" onclick="trackDelivery()">조회</button></div>
        </div>
        <div id="track-result"></div>
      </div>`;
  } else if (tab === 'withdraw') {
    content.innerHTML = `<div style="font-family:'Bebas Neue',sans-serif;font-size:24px;letter-spacing:1px;margin-bottom:20px;">계정 탈퇴</div>
      <div style="background:var(--bg3);border:1px solid rgba(230,57,70,0.3);border-radius:14px;padding:28px;max-width:480px;">
        <div style="font-size:14px;color:var(--text2);line-height:1.8;margin-bottom:20px;">탈퇴 시 모든 구매 내역 및 적립금이 삭제됩니다.<br>진행 중인 주문이 있을 경우 탈퇴가 제한됩니다.</div>
        <select style="width:100%;padding:10px 14px;background:var(--bg4);border:1px solid var(--border2);border-radius:8px;color:var(--text);font-size:13px;font-family:inherit;margin-bottom:16px;outline:none;">
          <option>서비스 불만족</option><option>개인정보 우려</option><option>이용 빈도 낮음</option><option>기타</option>
        </select>
        <button class="btn-outline full" style="border-color:var(--red);color:var(--red);" onclick="doWithdraw()">탈퇴하기</button>
      </div>`;
  }
}
function cancelOrder(btn) {
  btn.closest('div[style]').remove();
  showToast('주문이 취소되었습니다');
}
function saveProfile() {
  const nick = document.getElementById('edit-nick').value.trim();
  if (!nick || nick.length < 2) { showToast('올바른 닉네임을 입력해주세요'); return; }
  try {
    let users = JSON.parse(localStorage.getItem('fg_users') || '[]');
    const u = users.find(x => x.email === currentUser.email);
    if (u) { u.nick = nick; localStorage.setItem('fg_users', JSON.stringify(users)); }
    currentUser.nick = nick;
    localStorage.setItem('fg_user', JSON.stringify(currentUser));
    renderNavAuth(); renderMypage();
    showToast('✓ 정보가 수정되었습니다');
  } catch(e) { showToast('오류가 발생했습니다'); }
}
function trackDelivery() {
  const n = document.getElementById('track-num').value.trim();
  if (!n) { showToast('운송장 번호를 입력해주세요'); return; }
  document.getElementById('track-result').innerHTML = `<div style="margin-top:16px;">
    <div style="font-size:13px;font-weight:700;margin-bottom:12px;color:#95d5b2;">CJ대한통운 · ${n}</div>
    ${['집화 완료','간선 이동 중','배송 출발','배송 완료'].map((s,i) => `
    <div style="display:flex;gap:12px;align-items:center;padding:8px 0;border-bottom:1px solid var(--border);">
      <div style="width:10px;height:10px;border-radius:50%;background:${i<3?'var(--red)':'var(--border2)'};flex-shrink:0;"></div>
      <span style="font-size:13px;${i>=3?'color:var(--text3);':''}">${s}</span>
      ${i<3?'<span style="font-size:11px;color:var(--text3);margin-left:auto;">2025.05.'+(17+i)+'</span>':''}
    </div>`).join('')}
  </div>`;
}
function doWithdraw() {
  if (!confirm('정말 탈퇴하시겠습니까?')) return;
  try {
    let users = JSON.parse(localStorage.getItem('fg_users') || '[]');
    users = users.filter(u => u.email !== currentUser.email);
    localStorage.setItem('fg_users', JSON.stringify(users));
  } catch(e) {}
  doLogout();
  showToast('탈퇴가 처리되었습니다');
}

// ── CONFIRM: save order to user ──
const _origConfirmClick = document.querySelector('[onclick*="confirm"]');
function doConfirm() {
  const method = document.querySelector('#pay-methods .pay-method.selected')?.textContent || '카카오페이';
  const num = '#' + new Date().getFullYear() + String(new Date().getMonth()+1).padStart(2,'0') + String(new Date().getDate()).padStart(2,'0') + '-' + (Math.floor(Math.random()*9000)+1000);
  const d = new Date(); d.setDate(d.getDate()+3);
  document.getElementById('confirm-detail-area').innerHTML = `
    <div class="confirm-row"><span class="clabel">주문번호</span><span>${num}</span></div>
    <div class="confirm-row"><span class="clabel">상품</span><span>홍길동 챔피언 기념 티셔츠 (M) ×1</span></div>
    <div class="confirm-row"><span class="clabel">결제금액</span><span style="color:var(--red);">₩48,000</span></div>
    <div class="confirm-row"><span class="clabel">결제수단</span><span>${method}</span></div>
    <div class="confirm-row"><span class="clabel">예상 배송일</span><span>${d.getMonth()+1}월 ${d.getDate()}일</span></div>`;
  if (currentUser) {
    try {
      let users = JSON.parse(localStorage.getItem('fg_users') || '[]');
      const u = users.find(x => x.email === currentUser.email);
      if (u) {
        u.orders = u.orders || [];
        u.orders.unshift({num, name:'홍길동 챔피언 기념 티셔츠 (M)', price:48000, status:'배송 준비 중', date: new Date().toLocaleDateString('ko-KR')});
        u.point = (u.point||0) + 480;
        localStorage.setItem('fg_users', JSON.stringify(users));
        currentUser = u;
        localStorage.setItem('fg_user', JSON.stringify(currentUser));
      }
    } catch(e) {}
  }
  showPage('confirm');
}

// ── INIT ──
renderProductGrid('home-product-grid', PRODUCTS);
filterFighters();
renderCalendar();
renderFaq(FAQ_DATA);

</script>
</body>
</html>
