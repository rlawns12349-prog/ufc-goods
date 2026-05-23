<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FIGHTGOODS</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&family=Bebas+Neue&display=swap" rel="stylesheet">
<style>
:root{--red:#e63946;--rg:rgba(230,57,70,0.15);--bg:#0a0a0a;--bg2:#111;--bg3:#181818;--bg4:#1f1f1f;--bd:#2a2a2a;--bd2:#333;--t:#f0f0f0;--t2:#aaa;--t3:#666;--nh:64px;--green:#2d6a4f;--gl:#95d5b2;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Noto Sans KR',sans-serif;background:var(--bg);color:var(--t);min-height:100vh;}
/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nh);background:rgba(10,10,10,.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--bd);display:flex;align-items:center;padding:0 40px;gap:0;}
.logo{font-family:'Bebas Neue',sans-serif;font-size:26px;letter-spacing:2px;color:var(--red);margin-right:32px;cursor:pointer;}
.logo span{color:var(--t);}
.nav-links{display:flex;gap:2px;flex:1;overflow-x:auto;}
.nl{padding:8px 12px;font-size:13px;color:var(--t3);cursor:pointer;border-radius:6px;background:none;border:none;font-family:inherit;white-space:nowrap;transition:color .2s,background .2s;}
.nl:hover{color:var(--t);background:var(--bg3);}
.nl.on{color:var(--red);}
.nav-r{display:flex;align-items:center;gap:10px;margin-left:auto;flex-shrink:0;}
.srch-wrap{position:relative;}
.srch-box{display:flex;align-items:center;gap:6px;background:var(--bg3);border:1px solid var(--bd);border-radius:8px;padding:7px 12px;width:190px;}
.srch-box input{background:none;border:none;outline:none;color:var(--t);font-size:13px;font-family:inherit;width:140px;}
.srch-dd{position:absolute;top:calc(100% + 6px);left:0;right:0;background:var(--bg3);border:1px solid var(--bd2);border-radius:10px;overflow:hidden;display:none;z-index:200;}
.srch-dd.on{display:block;}
.si{padding:10px 14px;font-size:13px;cursor:pointer;}
.si:hover{background:var(--bg4);}
.cart-btn{cursor:pointer;background:var(--bg3);border:1px solid var(--bd);border-radius:8px;padding:8px 14px;font-size:13px;color:var(--t);display:flex;align-items:center;gap:6px;transition:border-color .2s;white-space:nowrap;}
.cart-btn:hover{border-color:var(--red);}
.cb{background:var(--red);color:#fff;width:18px;height:18px;border-radius:50%;font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center;}
/* PAGES */
.pw{margin-top:var(--nh);display:none;}
.pw.on{display:block;}
/* MODAL */
.ov{position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:300;display:none;align-items:center;justify-content:center;backdrop-filter:blur(4px);}
.ov.on{display:flex;}
.modal{background:var(--bg3);border:1px solid var(--bd2);border-radius:20px;padding:36px;width:100%;max-width:420px;position:relative;animation:mIn .25s cubic-bezier(.34,1.56,.64,1);}
@keyframes mIn{from{transform:scale(.9);opacity:0;}to{transform:scale(1);opacity:1;}}
.mc{position:absolute;top:14px;right:18px;background:none;border:none;color:var(--t3);font-size:22px;cursor:pointer;}
.mc:hover{color:var(--t);}
.mtabs{display:flex;background:var(--bg4);border-radius:8px;padding:3px;margin-bottom:20px;}
.mt{flex:1;padding:8px;border-radius:6px;font-size:13px;text-align:center;cursor:pointer;color:var(--t3);background:none;border:none;font-family:inherit;transition:all .2s;}
.mt.on{background:var(--red);color:#fff;font-weight:700;}
.fg{margin-bottom:13px;}
.fl{font-size:12px;color:var(--t2);margin-bottom:5px;font-weight:500;}
.fi{width:100%;padding:11px 14px;background:var(--bg4);border:1px solid var(--bd2);border-radius:8px;color:var(--t);font-size:14px;font-family:inherit;outline:none;transition:border-color .2s;}
.fi:focus{border-color:var(--red);}
.fh{font-size:11px;margin-top:4px;}
.fh.err{color:var(--red);}
.fh.ok{color:var(--gl);}
.social-row{display:flex;gap:8px;margin-top:10px;}
.sb{flex:1;padding:10px;border-radius:8px;border:1px solid var(--bd2);background:var(--bg4);color:var(--t2);font-size:12px;font-weight:700;cursor:pointer;font-family:inherit;}
.sb:hover{border-color:var(--bd);color:var(--t);}
.mdiv{display:flex;align-items:center;gap:10px;margin:14px 0;font-size:11px;color:var(--t3);}
.mdiv::before,.mdiv::after{content:'';flex:1;height:1px;background:var(--bd);}
/* BUTTONS */
.br{padding:13px 28px;border-radius:10px;background:var(--red);color:#fff;font-size:14px;font-weight:700;cursor:pointer;border:none;font-family:inherit;transition:background .2s;}
.br:hover{background:#b5262e;}
.br.sm{padding:9px 18px;font-size:13px;}
.br.full{width:100%;}
.bo{padding:13px 28px;border-radius:10px;background:transparent;color:var(--t);font-size:14px;font-weight:500;cursor:pointer;border:1px solid var(--bd2);font-family:inherit;transition:all .2s;}
.bo:hover{border-color:var(--t2);background:var(--bg3);}
.bo.sm{padding:9px 16px;font-size:13px;}
.bo.full{width:100%;}
/* HERO */
.hero{position:relative;height:500px;background:linear-gradient(135deg,#0a0a0a 0%,#1a0608 40%,#0a0a0a 100%);overflow:hidden;display:flex;align-items:center;}
.hero::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(-45deg,transparent,transparent 40px,rgba(230,57,70,.03) 40px,rgba(230,57,70,.03) 41px);}
.hc{position:relative;z-index:2;padding:0 80px;max-width:660px;}
.hlive{display:inline-flex;align-items:center;gap:8px;background:rgba(230,57,70,.15);border:1px solid rgba(230,57,70,.4);border-radius:20px;padding:6px 16px;font-size:12px;font-weight:700;color:var(--red);margin-bottom:20px;}
.hdot{width:8px;height:8px;border-radius:50%;background:var(--red);animation:blink 1.2s infinite;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:.3;}}
.ht{font-family:'Bebas Neue',sans-serif;font-size:68px;line-height:.95;letter-spacing:2px;margin-bottom:16px;}
.ht .ac{color:var(--red);}
.hs{font-size:15px;color:var(--t2);line-height:1.7;margin-bottom:28px;}
.hbtns{display:flex;gap:12px;}
.hgfx{position:absolute;right:0;top:0;bottom:0;width:45%;display:flex;align-items:center;justify-content:center;}
.hgfx-inner{width:340px;height:340px;background:radial-gradient(circle at center,rgba(230,57,70,.2) 0%,transparent 65%);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:160px;animation:float 4s ease-in-out infinite;}
@keyframes float{0%,100%{transform:translateY(0);}50%{transform:translateY(-14px);}}
/* SECTION */
.sec{padding:56px 80px;}
.sh{display:flex;align-items:baseline;gap:16px;margin-bottom:28px;}
.sl{font-size:11px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:1.5px;}
.st{font-family:'Bebas Neue',sans-serif;font-size:30px;letter-spacing:1px;}
.sm{margin-left:auto;font-size:13px;color:var(--t3);cursor:pointer;border:none;background:none;font-family:inherit;}
.sm:hover{color:var(--red);}
/* RESULT BANNER */
.rb{margin:0 80px 36px;background:linear-gradient(135deg,#1a0608,#110305);border:1px solid rgba(230,57,70,.4);border-radius:16px;padding:26px 32px;cursor:pointer;transition:border-color .2s;}
.rb:hover{border-color:var(--red);}
.rb-top{display:flex;align-items:center;gap:12px;margin-bottom:18px;}
.rb-main{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:28px;}
.rf{text-align:center;}
.rf .rn{font-family:'Bebas Neue',sans-serif;font-size:40px;letter-spacing:1px;line-height:1;}
.rf.win .rn{color:var(--red);}
.rf .ro{font-size:12px;color:var(--t3);margin-top:4px;}
.rc{text-align:center;}
.rm{font-family:'Bebas Neue',sans-serif;font-size:26px;color:var(--red);letter-spacing:1px;}
.rd{font-size:12px;color:var(--t3);margin-top:4px;}
.rb-cta{display:flex;gap:12px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,.06);}
/* PRODUCT */
.pg{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;}
.pc{background:var(--bg3);border:1px solid var(--bd);border-radius:14px;overflow:hidden;cursor:pointer;transition:border-color .2s,transform .2s;}
.pc:hover{border-color:var(--red);transform:translateY(-4px);}
.pi{height:190px;background:linear-gradient(135deg,#1e1e2e,#2a1e2a);display:flex;align-items:center;justify-content:center;font-size:60px;position:relative;}
.pbadge{position:absolute;top:10px;right:10px;padding:3px 9px;border-radius:6px;font-size:10px;font-weight:700;}
.bh{background:var(--red);color:#fff;}
.bl{background:#ff6b35;color:#fff;}
.bn{background:var(--green);color:var(--gl);}
.pb{padding:14px;}
.pn{font-size:14px;font-weight:500;margin-bottom:5px;line-height:1.4;}
.pf{font-size:11px;color:var(--t3);margin-bottom:7px;}
.pp{display:flex;align-items:center;justify-content:space-between;}
.pr{font-size:17px;font-weight:700;color:var(--red);}
.ps{font-size:11px;color:var(--t3);}
/* FIGHTER */
.fg-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;}
.fc{background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:22px;cursor:pointer;transition:border-color .2s,background .2s;display:flex;gap:18px;}
.fc:hover{border-color:var(--red);background:var(--bg4);}
.fav{width:68px;height:68px;border-radius:50%;background:var(--bg4);border:2px solid var(--bd2);display:flex;align-items:center;justify-content:center;font-size:32px;flex-shrink:0;}
.fi2{flex:1;}
.fn{font-size:17px;font-weight:700;margin-bottom:3px;}
.fm{font-size:12px;color:var(--t3);margin-bottom:7px;}
.frec{display:flex;gap:10px;margin-bottom:8px;}
.frs{text-align:center;}
.frv{font-size:18px;font-weight:700;}
.frl{font-size:10px;color:var(--t3);}
.ftags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:8px;}
.ftag{padding:3px 10px;border-radius:20px;background:var(--rg);border:1px solid rgba(230,57,70,.3);color:var(--red);font-size:11px;}
.fg-cnt{font-size:11px;color:var(--t3);}
/* TABS */
.tabs{display:flex;background:var(--bg3);border:1px solid var(--bd);border-radius:10px;padding:4px;width:fit-content;margin-bottom:22px;}
.tab{padding:8px 18px;border-radius:7px;font-size:13px;cursor:pointer;background:none;border:none;color:var(--t3);font-family:inherit;transition:all .2s;}
.tab.on{background:var(--red);color:#fff;font-weight:700;}
/* RANKING */
.rtbl{width:100%;border-collapse:collapse;}
.rtbl th{text-align:left;padding:10px 16px;font-size:11px;color:var(--t3);font-weight:500;border-bottom:1px solid var(--bd);text-transform:uppercase;letter-spacing:.8px;}
.rtbl td{padding:13px 16px;border-bottom:1px solid var(--bd);font-size:14px;}
.rtbl tr:last-child td{border-bottom:none;}
.rtbl tr:hover td{background:var(--bg3);}
.rch{font-size:11px;}
.rch.up{color:var(--gl);}
.rch.dn{color:var(--red);}
.rch.eq{color:var(--t3);}
/* PRODUCT DETAIL */
.dl{display:grid;grid-template-columns:1fr 1fr;gap:56px;padding:56px 80px;align-items:start;}
.dimg{position:sticky;top:calc(var(--nh) + 20px);}
.mi{width:100%;aspect-ratio:1;background:linear-gradient(135deg,#1e1e2e,#2a1520);border-radius:16px;border:1px solid var(--bd);display:flex;align-items:center;justify-content:center;font-size:110px;margin-bottom:12px;}
.tr{display:flex;gap:10px;}
.th{width:66px;height:66px;border-radius:8px;background:var(--bg3);border:1px solid var(--bd);display:flex;align-items:center;justify-content:center;font-size:26px;cursor:pointer;transition:border-color .2s;}
.th.on{border-color:var(--red);}
.dtag{display:inline-flex;align-items:center;gap:6px;background:var(--rg);border:1px solid rgba(230,57,70,.3);border-radius:6px;padding:5px 12px;font-size:12px;color:var(--red);margin-bottom:14px;cursor:pointer;}
.dnm{font-size:26px;font-weight:700;line-height:1.3;margin-bottom:10px;}
.dpr{font-size:34px;font-weight:700;color:var(--red);margin-bottom:8px;}
.drev{display:flex;align-items:center;gap:8px;margin-bottom:20px;}
.divr{height:1px;background:var(--bd);margin:20px 0;}
.ol{font-size:13px;color:var(--t2);margin-bottom:9px;font-weight:500;}
.or{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px;}
.ob{padding:9px 18px;border-radius:8px;border:1px solid var(--bd2);background:var(--bg3);color:var(--t2);font-size:13px;cursor:pointer;font-family:inherit;transition:all .2s;}
.ob:hover,.ob.on{border-color:var(--red);color:var(--red);background:var(--rg);}
.qr{display:flex;align-items:center;gap:14px;margin-bottom:18px;}
.ql{font-size:13px;color:var(--t2);font-weight:500;width:56px;}
.qc{display:flex;border:1px solid var(--bd2);border-radius:8px;overflow:hidden;}
.qb{width:36px;height:36px;display:flex;align-items:center;justify-content:center;cursor:pointer;background:var(--bg3);border:none;color:var(--t);font-size:18px;font-family:inherit;}
.qb:hover{background:var(--bg4);}
.qv{width:44px;text-align:center;font-size:14px;font-weight:700;background:var(--bg3);color:var(--t);line-height:36px;}
.ps2{background:var(--bg3);border:1px solid var(--bd);border-radius:10px;padding:14px 18px;margin-bottom:18px;}
.pr2{display:flex;justify-content:space-between;font-size:13px;padding:3px 0;}
.pr2 .pl{color:var(--t3);}
.pr2.tot{font-size:15px;font-weight:700;padding-top:10px;margin-top:6px;border-top:1px solid var(--bd);}
.pr2.tot .pv{color:var(--red);}
.brow{display:flex;gap:12px;}
.bbuy{flex:2;padding:15px;background:var(--red);color:#fff;font-size:15px;font-weight:700;border:none;border-radius:10px;cursor:pointer;font-family:inherit;}
.bbuy:hover{background:#b5262e;}
.bcart{flex:1;padding:15px;background:transparent;color:var(--t);font-size:15px;font-weight:500;border:1px solid var(--bd2);border-radius:10px;cursor:pointer;font-family:inherit;}
.bcart:hover{border-color:var(--t2);background:var(--bg3);}
/* CART */
.cl{display:grid;grid-template-columns:1fr 340px;gap:36px;padding:36px 80px 56px;}
.cart-item{display:flex;gap:18px;align-items:center;padding:18px 0;border-bottom:1px solid var(--bd);}
.cimg{width:90px;height:90px;border-radius:10px;background:linear-gradient(135deg,#1e1e2e,#2a1520);display:flex;align-items:center;justify-content:center;font-size:40px;flex-shrink:0;}
.csum{background:var(--bg3);border:1px solid var(--bd);border-radius:16px;padding:24px;position:sticky;top:calc(var(--nh)+20px);height:fit-content;}
.srow{display:flex;justify-content:space-between;font-size:14px;padding:7px 0;}
.srow .sl2{color:var(--t3);}
.sdiv{height:1px;background:var(--bd);margin:10px 0;}
.stot{display:flex;justify-content:space-between;font-size:17px;font-weight:700;margin-bottom:18px;}
.stot .sv{color:var(--red);}
.ci2{flex:1;padding:9px 12px;background:var(--bg4);border:1px solid var(--bd2);border-radius:8px;color:var(--t);font-size:13px;font-family:inherit;outline:none;}
.ci2:focus{border-color:var(--red);}
.cbtn{padding:9px 13px;border-radius:8px;background:var(--bg4);border:1px solid var(--bd2);color:var(--t);font-size:13px;cursor:pointer;font-family:inherit;white-space:nowrap;}
.cbtn:hover{border-color:var(--red);}
/* PAYMENT */
.payl{display:grid;grid-template-columns:1fr 380px;gap:44px;padding:36px 80px 56px;}
.pm{display:grid;grid-template-columns:repeat(4,1fr);gap:9px;}
.pmb{padding:13px 6px;border-radius:10px;border:1px solid var(--bd2);background:var(--bg3);text-align:center;font-size:13px;font-weight:500;cursor:pointer;font-family:inherit;color:var(--t2);transition:all .2s;}
.pmb:hover,.pmb.on{border-color:var(--red);color:var(--red);background:var(--rg);}
.abox{background:var(--bg3);border:1px solid var(--bd);border-radius:10px;padding:14px 18px;}
.osc{background:var(--bg3);border:1px solid var(--bd);border-radius:16px;padding:24px;position:sticky;top:calc(var(--nh)+20px);}
.osi{display:flex;gap:12px;align-items:center;padding:11px 0;border-bottom:1px solid var(--bd);}
.osimg{width:52px;height:52px;border-radius:8px;background:var(--bg4);display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;}
/* CONFIRM */
.conf{max-width:600px;margin:0 auto;padding:72px 36px;text-align:center;}
.cicon{width:90px;height:90px;border-radius:50%;background:rgba(45,106,79,.2);border:2px solid var(--green);display:flex;align-items:center;justify-content:center;font-size:44px;margin:0 auto 24px;animation:pop .4s cubic-bezier(.34,1.56,.64,1);}
@keyframes pop{from{transform:scale(0);opacity:0;}to{transform:scale(1);opacity:1;}}
.ctit{font-family:'Bebas Neue',sans-serif;font-size:44px;letter-spacing:2px;margin-bottom:8px;}
.cbox{background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:22px 26px;text-align:left;margin:28px 0;}
.crow{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid var(--bd);font-size:14px;}
.crow:last-child{border-bottom:none;}
.crow .ck{color:var(--t3);}
/* MYPAGE */
.mpl{display:grid;grid-template-columns:220px 1fr;gap:28px;padding:36px 80px 56px;}
.mpside{position:sticky;top:calc(var(--nh)+20px);height:fit-content;}
.mpprof{background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:22px;margin-bottom:14px;text-align:center;}
.mpav{width:68px;height:68px;border-radius:50%;background:var(--red);display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;color:#fff;margin:0 auto 10px;}
.mpmenu{background:var(--bg3);border:1px solid var(--bd);border-radius:14px;overflow:hidden;}
.mmi{padding:13px 18px;font-size:13px;cursor:pointer;border-bottom:1px solid var(--bd);display:flex;align-items:center;gap:8px;transition:background .15s;}
.mmi:last-child{border-bottom:none;}
.mmi:hover{background:var(--bg4);}
.mmi.on{color:var(--red);font-weight:500;}
/* COMMUNITY */
.board-post{background:var(--bg3);border:1px solid var(--bd);border-radius:12px;padding:16px 18px;margin-bottom:11px;cursor:pointer;transition:border-color .2s;}
.board-post:hover{border-color:var(--bd2);}
/* FAQ */
.faq-item{background:var(--bg3);border:1px solid var(--bd);border-radius:10px;margin-bottom:8px;overflow:hidden;}
.faq-q{padding:15px 18px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-size:14px;font-weight:500;}
.faq-q:hover{background:var(--bg4);}
.faq-a{padding:0 18px;max-height:0;overflow:hidden;transition:max-height .3s,padding .3s;font-size:13px;color:var(--t2);line-height:1.7;}
.faq-a.on{max-height:200px;padding:10px 18px 16px;}
.fch{transition:transform .3s;color:var(--t3);font-size:12px;}
.fch.on{transform:rotate(180deg);}
/* CALENDAR */
.cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;}
.cal-cell{min-height:68px;background:var(--bg3);border:1px solid var(--bd);border-radius:6px;padding:7px;cursor:pointer;transition:border-color .2s;}
.cal-cell:hover{border-color:var(--bd2);}
.cal-cell.ev{border-color:rgba(230,57,70,.4);}
.cal-d{font-size:11px;color:var(--t3);margin-bottom:3px;}
.cal-e{font-size:10px;background:var(--rg);border:1px solid rgba(230,57,70,.3);color:var(--red);padding:2px 5px;border-radius:4px;line-height:1.4;}
/* CHIPS */
.chip{padding:4px 11px;border-radius:20px;font-size:11px;border:1px solid var(--bd);color:var(--t3);background:var(--bg3);cursor:pointer;font-family:inherit;transition:all .2s;}
.chip.on{border-color:var(--red);color:var(--red);background:var(--rg);}
.chip:hover{border-color:var(--bd2);color:var(--t);}
/* NOTICE */
.ni{display:flex;gap:14px;padding:16px 0;border-bottom:1px solid var(--bd);cursor:pointer;}
.ni:hover .ntit{color:var(--red);}
.npin{background:var(--rg);color:var(--red);border:1px solid rgba(230,57,70,.3);font-size:10px;font-weight:700;padding:2px 7px;border-radius:4px;flex-shrink:0;margin-top:2px;}
.ntit{font-size:14px;font-weight:500;margin-bottom:3px;transition:color .2s;}
/* TOAST */
.toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(80px);background:var(--bg3);border:1px solid var(--bd2);border-radius:10px;padding:13px 22px;font-size:14px;font-weight:500;z-index:999;opacity:0;transition:transform .3s,opacity .3s;white-space:nowrap;pointer-events:none;}
.toast.on{transform:translateX(-50%) translateY(0);opacity:1;}
/* BREADCRUMB */
.bc{padding:18px 80px 0;display:flex;align-items:center;gap:8px;font-size:12px;color:var(--t3);}
.bc span{cursor:pointer;}
.bc span:hover{color:var(--t);}
.bc .sep{color:var(--bd2);}
/* FIGHTER DETAIL */
.fdh{background:linear-gradient(180deg,#1a0608 0%,#0a0a0a 100%);padding:56px 80px 36px;}
.fdtop{display:flex;gap:44px;align-items:flex-start;}
.fdav{width:130px;height:130px;border-radius:50%;background:var(--bg3);border:3px solid var(--red);display:flex;align-items:center;justify-content:center;font-size:64px;flex-shrink:0;}
.fdnm{font-family:'Bebas Neue',sans-serif;font-size:52px;letter-spacing:2px;line-height:1;margin-bottom:7px;}
.srow2{display:flex;gap:20px;margin-bottom:18px;}
.sbox{background:rgba(255,255,255,.04);border:1px solid var(--bd);border-radius:10px;padding:13px 18px;text-align:center;min-width:76px;}
.sv2{font-size:26px;font-weight:700;}
.slb{font-size:10px;color:var(--t3);margin-top:2px;}
.fdb{padding:0 80px 56px;display:grid;grid-template-columns:1fr 320px;gap:44px;margin-top:36px;}
.tl-item{display:flex;gap:18px;padding-bottom:24px;position:relative;}
.tl-item::before{content:'';position:absolute;left:8px;top:22px;bottom:0;width:2px;background:var(--bd);}
.tl-item:last-child::before{display:none;}
.tl-dot{width:18px;height:18px;border-radius:50%;border:2px solid var(--bd2);background:var(--bg);flex-shrink:0;margin-top:4px;position:relative;z-index:1;}
.tl-dot.hi{border-color:var(--red);background:var(--red);}
.gbox{background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:22px;position:sticky;top:calc(var(--nh)+20px);}
.mprod{display:flex;gap:11px;align-items:center;padding:9px 0;border-bottom:1px solid var(--bd);cursor:pointer;}
.mprod:last-of-type{border-bottom:none;}
.mprod:hover .mpn{color:var(--red);}
.mpimg{width:52px;height:52px;border-radius:8px;background:var(--bg4);display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;}
.mpn{font-size:13px;margin-bottom:3px;transition:color .2s;}
.mpp{font-size:13px;font-weight:700;color:var(--red);}
/* REVIEW */
.rev-item{background:var(--bg3);border:1px solid var(--bd);border-radius:10px;padding:15px 17px;margin-bottom:9px;}
.rev-top{display:flex;align-items:center;gap:9px;margin-bottom:7px;}
/* USER BTN */
.ubtn{display:flex;align-items:center;gap:7px;padding:6px 13px;border-radius:8px;background:var(--bg3);border:1px solid var(--bd);cursor:pointer;font-size:13px;}
.ubtn:hover{border-color:var(--bd2);}
.uav{width:24px;height:24px;border-radius:50%;background:var(--red);display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:#fff;}
.lbtn{padding:8px 16px;border-radius:8px;background:var(--red);color:#fff;font-size:13px;font-weight:700;cursor:pointer;border:none;font-family:inherit;}
.lbtn:hover{background:#b5262e;}
</style>
</head>
<body>

<!-- NAVBAR -->
<nav>
  <div class="logo" onclick="go('home')">FIGHT<span>GOODS</span></div>
  <div class="nav-links">
    <button class="nl on" onclick="go('home');nav(this)">굿즈 홈</button>
    <button class="nl" onclick="go('ranking');nav(this)">종합 랭킹</button>
    <button class="nl" onclick="go('fighters');nav(this)">선수 정보</button>
    <button class="nl" onclick="go('schedule');nav(this)">경기 정보</button>
    <button class="nl" onclick="go('community');nav(this)">커뮤니티</button>
    <button class="nl" onclick="go('notice');nav(this)">공지사항</button>
    <button class="nl" onclick="go('faq');nav(this)">고객지원</button>
    <button class="nl" onclick="go('mypage');nav(this)">마이페이지</button>
  </div>
  <div class="nav-r">
    <div class="srch-wrap">
      <div class="srch-box"><span>🔍</span><input id="si" placeholder="검색" oninput="srch(this.value)" onfocus="srch(this.value)" onblur="setTimeout(closeSrch,200)"></div>
      <div class="srch-dd" id="sdd"></div>
    </div>
    <div class="cart-btn" onclick="go('cart')">🛒 장바구니 <div class="cb" id="cc">0</div></div>
    <div id="nauth"></div>
  </div>
</nav>

<!-- AUTH MODAL -->
<div class="ov" id="aov">
  <div class="modal">
    <button class="mc" onclick="closeAuth()">&#x2715;</button>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:30px;letter-spacing:1px;margin-bottom:3px;">FIGHTGOODS</div>
    <div style="font-size:13px;color:var(--t3);margin-bottom:22px;">MMA 서사 기반 굿즈 플랫폼</div>
    <div class="mtabs">
      <button class="mt on" id="tlog" onclick="atab('login')">로그인</button>
      <button class="mt" id="tsig" onclick="atab('signup')">회원가입</button>
    </div>
    <!-- LOGIN -->
    <div id="flog">
      <div class="fg"><div class="fl">이메일</div><input class="fi" id="le" type="email" placeholder="이메일 입력"></div>
      <div class="fg"><div class="fl">비밀번호</div><input class="fi" id="lp" type="password" placeholder="비밀번호 입력" onkeydown="if(event.key==='Enter')doLogin()"><div id="lerr" class="fh err" style="display:none;"></div></div>
      <div style="display:flex;justify-content:space-between;margin-bottom:14px;">
        <label style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--t3);cursor:pointer;"><input type="checkbox"> 로그인 상태 유지</label>
        <span style="font-size:12px;color:var(--t3);cursor:pointer;" onclick="toast('비밀번호 재설정 이메일이 발송되었습니다')">비밀번호 찾기</span>
      </div>
      <button class="br full" onclick="doLogin()">로그인</button>
      <div class="mdiv">소셜 로그인</div>
      <div class="social-row">
        <button class="sb" onclick="socialLogin('카카오')">카카오</button>
        <button class="sb" onclick="socialLogin('구글')">구글</button>
        <button class="sb" onclick="socialLogin('네이버')">네이버</button>
      </div>
    </div>
    <!-- SIGNUP -->
    <div id="fsig" style="display:none;">
      <div class="fg"><div class="fl">이메일</div><input class="fi" id="se" type="email" placeholder="이메일 입력" oninput="chkEmail(this.value)"><div id="seh" class="fh"></div></div>
      <div class="fg"><div class="fl">닉네임</div><input class="fi" id="sn" placeholder="닉네임 (2~10자)" oninput="chkNick(this.value)"><div id="snh" class="fh"></div></div>
      <div class="fg"><div class="fl">비밀번호</div><input class="fi" id="sp" type="password" placeholder="영문+숫자+특수문자 8자 이상" oninput="chkPw(this.value)"><div id="pwbar" style="height:4px;border-radius:2px;margin-top:5px;width:0;transition:width .3s,background .3s;"></div><div id="sph" class="fh"></div></div>
      <div class="fg"><div class="fl">비밀번호 확인</div><input class="fi" id="sp2" type="password" placeholder="비밀번호 재입력" oninput="chkPw2(this.value)"><div id="sp2h" class="fh"></div></div>
      <div style="margin-bottom:13px;">
        <label style="display:flex;align-items:center;gap:7px;font-size:13px;cursor:pointer;margin-bottom:7px;"><input type="checkbox" id="agr"> 이용약관 및 개인정보처리방침 동의 <span style="color:var(--red);">(필수)</span></label>
        <label style="display:flex;align-items:center;gap:7px;font-size:13px;cursor:pointer;"><input type="checkbox"> 마케팅 수신 동의 (선택)</label>
      </div>
      <div id="serr" class="fh err" style="display:none;margin-bottom:9px;"></div>
      <button class="br full" onclick="doSignup()">회원가입</button>
    </div>
  </div>
</div>

<!-- HOME -->
<div class="pw on" id="p-home">
  <div class="hero">
    <div class="hc">
      <div class="hlive"><div class="hdot"></div>UFC 298 LIVE 진행 중</div>
      <div class="ht">MMA<br><span class="ac">서사를</span><br>입어라</div>
      <div class="hs">선수의 이야기가 담긴 굿즈.<br>경기 직후 가장 먼저 만나는 챔피언의 흔적.</div>
      <div class="hbtns">
        <button class="br" onclick="go('schedule');nav(document.querySelectorAll('.nl')[3])">경기 결과 보기</button>
        <button class="bo" onclick="go('fighters');nav(document.querySelectorAll('.nl')[2])">선수 탐색하기</button>
      </div>
    </div>
    <div class="hgfx"><div class="hgfx-inner">🥊</div></div>
  </div>
  <div class="rb" onclick="go('schedule');nav(document.querySelectorAll('.nl')[3])">
    <div class="rb-top"><span style="background:var(--red);color:#fff;padding:3px 10px;border-radius:6px;font-size:11px;font-weight:700;">방금 종료</span><span style="font-size:13px;color:var(--t2);">UFC 298 · 2025.05.17</span></div>
    <div class="rb-main">
      <div class="rf win"><div class="rn">홍길동</div><div class="ro">UFC · 웰터급 챔피언</div></div>
      <div class="rc"><div class="rm">KO 승</div><div class="rd">1라운드 2분 34초</div><div style="font-size:20px;color:var(--t3);margin:6px 0;">VS</div></div>
      <div class="rf"><div class="rn">맥스 홀로웨이</div><div class="ro">UFC · 웰터급</div></div>
    </div>
    <div class="rb-cta">
      <button class="br" onclick="event.stopPropagation();go('product')">연계 굿즈 바로구매 →</button>
      <button class="bo" onclick="event.stopPropagation();go('fighter-detail')">홍길동 선수 스토리 보기</button>
    </div>
  </div>
  <div class="sec">
    <div class="sh"><div class="sl">인기 굿즈</div><div class="st">지금 가장 핫한 굿즈</div><button class="sm" onclick="go('ranking');nav(document.querySelectorAll('.nl')[1])">전체 보기 →</button></div>
    <div style="display:flex;gap:8px;margin-bottom:18px;" id="pf">
      <button class="chip on" data-c="전체" onclick="filterP(this)">전체</button>
      <button class="chip" data-c="티셔츠" onclick="filterP(this)">티셔츠</button>
      <button class="chip" data-c="포스터" onclick="filterP(this)">포스터</button>
      <button class="chip" data-c="포토카드" onclick="filterP(this)">포토카드</button>
      <button class="chip" data-c="후디" onclick="filterP(this)">후디</button>
    </div>
    <div class="pg" id="hpg"></div>
  </div>
  <div class="sec" style="padding-top:0;">
    <div class="sh"><div class="sl">선수 서사</div><div class="st">그들의 이야기</div><button class="sm" onclick="go('fighters');nav(document.querySelectorAll('.nl')[2])">전체 보기 →</button></div>
    <div class="fg-grid" id="hfg"></div>
  </div>
  <div class="sec" style="padding-top:0;">
    <div class="sh"><div class="sl">최근 본 상품</div><div class="st">다시 보기</div></div>
    <div id="rv"><div style="text-align:center;padding:36px;color:var(--t3);"><div style="font-size:36px;margin-bottom:8px;">👀</div>아직 본 상품이 없어요</div></div>
  </div>
</div>

<!-- RANKING -->
<div class="pw" id="p-ranking">
  <div class="sec">
    <div class="sh"><div class="sl">종합 랭킹</div><div class="st">인기 굿즈 순위</div></div>
    <div style="display:flex;gap:12px;margin-bottom:18px;align-items:center;">
      <div class="tabs">
        <button class="tab on" onclick="tabOn(this,this.parentNode)">판매량순</button>
        <button class="tab" onclick="tabOn(this,this.parentNode)">조회수순</button>
      </div>
      <div style="display:flex;gap:6px;">
        <button class="chip on" onclick="chipOn(this,'.pchip')">일간</button>
        <button class="chip pchip" onclick="chipOn(this,'.pchip')">주간</button>
        <button class="chip pchip" onclick="chipOn(this,'.pchip')">월간</button>
      </div>
    </div>
    <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:14px;overflow:hidden;">
      <table class="rtbl">
        <thead><tr><th style="width:56px;">순위</th><th>상품</th><th>선수</th><th style="text-align:right;">판매량</th><th style="text-align:right;">가격</th></tr></thead>
        <tbody id="rtb"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- FIGHTERS -->
<div class="pw" id="p-fighters">
  <div class="sec">
    <div class="sh"><div class="sl">선수 정보</div><div class="st">계약 선수 전체</div></div>
    <div style="display:flex;gap:10px;margin-bottom:22px;flex-wrap:wrap;align-items:center;">
      <input id="fsrch" placeholder="🔍 선수 이름 검색" oninput="filterF()" style="padding:8px 12px;background:var(--bg3);border:1px solid var(--bd2);border-radius:8px;color:var(--t);font-size:13px;font-family:inherit;outline:none;width:190px;">
      <div style="display:flex;gap:6px;flex-wrap:wrap;" id="ff">
        <button class="chip on" data-f="전체" onclick="chipOn(this,'#ff .chip');filterF()">전체</button>
        <button class="chip" data-f="웰터급" onclick="chipOn(this,'#ff .chip');filterF()">웰터급</button>
        <button class="chip" data-f="헤비급" onclick="chipOn(this,'#ff .chip');filterF()">헤비급</button>
        <button class="chip" data-f="밴텀급" onclick="chipOn(this,'#ff .chip');filterF()">밴텀급</button>
        <button class="chip" data-f="UFC" onclick="chipOn(this,'#ff .chip');filterF()">UFC</button>
        <button class="chip" data-f="블랙컴뱃" onclick="chipOn(this,'#ff .chip');filterF()">블랙컴뱃</button>
        <button class="chip" data-f="ZFN" onclick="chipOn(this,'#ff .chip');filterF()">ZFN</button>
      </div>
    </div>
    <div class="fg-grid" id="fgrid"></div>
  </div>
</div>

<!-- FIGHTER DETAIL -->
<div class="pw" id="p-fighter-detail">
  <div class="bc"><span onclick="go('fighters');nav(document.querySelectorAll('.nl')[2])">선수 정보</span><span class="sep">›</span><span style="color:var(--t2);">홍길동</span></div>
  <div class="fdh">
    <div class="fdtop">
      <div class="fdav">🥊</div>
      <div>
        <div class="fdnm">홍길동</div>
        <div style="font-size:13px;color:var(--t3);margin-bottom:14px;">UFC · 웰터급 챔피언 · 데뷔 2019.03.15</div>
        <div class="srow2">
          <div class="sbox"><div class="sv2">12</div><div class="slb">승</div></div>
          <div class="sbox"><div class="sv2">3</div><div class="slb">패</div></div>
          <div class="sbox"><div class="sv2">0</div><div class="slb">무</div></div>
          <div class="sbox"><div class="sv2">77%</div><div class="slb">피니시율</div></div>
        </div>
        <button class="br" onclick="go('product')">관련 굿즈 바로가기 →</button>
      </div>
    </div>
  </div>
  <div class="fdb">
    <div>
      <div style="font-family:'Bebas Neue',sans-serif;font-size:22px;letter-spacing:1px;margin-bottom:22px;">성장 타임라인</div>
      <div class="tl-item"><div class="tl-dot"></div><div><div style="font-size:11px;color:var(--t3);">2019</div><div style="font-size:15px;font-weight:500;margin:3px 0 5px;">데뷔 · 무명 시절</div><div style="font-size:13px;color:var(--t3);line-height:1.6;margin-bottom:7px;">아무도 주목하지 않던 지방 팀 소속. 연속 KO로 이름을 알리기 시작했다.</div><span style="font-size:12px;color:var(--red);cursor:pointer;" onclick="go('product')">이 스토리의 굿즈 보기 →</span></div></div>
      <div class="tl-item"><div class="tl-dot"></div><div><div style="font-size:11px;color:var(--t3);">2021</div><div style="font-size:15px;font-weight:500;margin:3px 0 5px;">체급 조절 도전</div><div style="font-size:13px;color:var(--t3);line-height:1.6;margin-bottom:7px;">웰터급으로 체급을 올리며 고비를 맞았지만 6개월 재활 후 복귀했다.</div><span style="font-size:12px;color:var(--red);cursor:pointer;" onclick="go('product')">이 스토리의 굿즈 보기 →</span></div></div>
      <div class="tl-item"><div class="tl-dot hi"></div><div><div style="font-size:11px;color:var(--t3);">2023 🏆</div><div style="font-size:15px;font-weight:500;margin:3px 0 5px;">챔피언 등극</div><div style="font-size:13px;color:var(--t3);line-height:1.6;margin-bottom:7px;">UFC 298에서 KO 1라운드 피니시. 한국 MMA 역사상 첫 UFC 웰터급 챔피언.</div><span style="font-size:12px;color:var(--red);cursor:pointer;" onclick="go('product')">이 스토리의 굿즈 보기 →</span></div></div>
    </div>
    <div>
      <div class="gbox">
        <div style="font-size:14px;font-weight:700;margin-bottom:14px;">홍길동 관련 굿즈</div>
        <div class="mprod" onclick="go('product')"><div class="mpimg">👕</div><div><div class="mpn">챔피언 등극 기념 티셔츠</div><div class="mpp">₩45,000</div></div></div>
        <div class="mprod" onclick="go('product')"><div class="mpimg">🖼️</div><div><div class="mpn">챔피언 벨트 아트 포스터</div><div class="mpp">₩18,000</div></div></div>
        <div class="mprod" onclick="go('product')"><div class="mpimg">📸</div><div><div class="mpn">등극 순간 포토카드 세트</div><div class="mpp">₩12,000</div></div></div>
        <button class="br" style="width:100%;margin-top:14px;" onclick="go('product')">굿즈 전체 보기</button>
      </div>
    </div>
  </div>
</div>

<!-- SCHEDULE -->
<div class="pw" id="p-schedule">
  <div class="sec">
    <div class="sh"><div class="sl">경기 정보</div><div class="st">경기 일정 &amp; 결과</div></div>
    <div class="tabs" style="margin-bottom:24px;">
      <button class="tab on" onclick="tabOn(this,this.parentNode);schTab('cal')">캘린더</button>
      <button class="tab" onclick="tabOn(this,this.parentNode);schTab('res')">경기 결과</button>
      <button class="tab" onclick="tabOn(this,this.parentNode);schTab('pre')">대결 프리뷰</button>
      <button class="tab" onclick="tabOn(this,this.parentNode);schTab('hi')">하이라이트</button>
    </div>
    <div id="st-cal">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;">
        <button class="bo sm" onclick="calM(-1)">← 이전달</button>
        <div style="font-family:'Bebas Neue',sans-serif;font-size:22px;" id="cml"></div>
        <button class="bo sm" onclick="calM(1)">다음달 →</button>
      </div>
      <div class="cal-grid" id="cg"></div>
    </div>
    <div id="st-res" style="display:none;">
      <div class="rb" style="margin:0 0 14px;" onclick="go('fighter-detail')">
        <div class="rb-top"><span style="background:var(--red);color:#fff;padding:3px 10px;border-radius:6px;font-size:11px;font-weight:700;">방금 종료</span><span style="font-size:13px;color:var(--t2);">UFC 298 · 2025.05.17</span></div>
        <div class="rb-main">
          <div class="rf win"><div class="rn">홍길동</div><div class="ro">UFC 웰터급</div></div>
          <div class="rc"><div class="rm">KO 승</div><div class="rd">1R 2:34</div><div style="font-size:18px;color:var(--t3);margin:4px 0;">VS</div></div>
          <div class="rf"><div class="rn">맥스 홀로웨이</div><div class="ro">UFC 웰터급</div></div>
        </div>
        <div class="rb-cta"><button class="br" onclick="event.stopPropagation();go('product')">연계 굿즈 바로구매 →</button></div>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:12px;padding:16px 22px;cursor:pointer;">
        <div style="font-size:11px;color:var(--t3);margin-bottom:7px;">ZFN 38 · 2025.05.10</div>
        <div style="display:flex;justify-content:space-between;"><span style="font-size:15px;font-weight:500;">이철수 vs 김용재</span><span style="color:var(--gl);font-weight:700;">판정 승</span></div>
      </div>
    </div>
    <div id="st-pre" style="display:none;">
      <div style="background:linear-gradient(135deg,#1a0608,#110305);border:1px solid rgba(230,57,70,.3);border-radius:14px;padding:26px;">
        <div style="font-size:11px;color:var(--red);font-weight:700;margin-bottom:14px;">UFC 308 · D-14 예정</div>
        <div style="display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:22px;margin-bottom:18px;">
          <div style="text-align:center;"><div style="font-family:'Bebas Neue',sans-serif;font-size:30px;">홍길동</div><div style="font-size:12px;color:var(--t3);">12W 3L · 챔피언</div><div style="display:flex;gap:5px;justify-content:center;margin-top:7px;"><span style="font-size:11px;padding:2px 7px;background:var(--bg4);border:1px solid var(--bd);border-radius:10px;color:var(--t3);">KO 전문</span><span style="font-size:11px;padding:2px 7px;background:var(--bg4);border:1px solid var(--bd);border-radius:10px;color:var(--t3);">강한 턱</span></div></div>
          <div style="font-family:'Bebas Neue',sans-serif;font-size:30px;color:var(--t3);">VS</div>
          <div style="text-align:center;"><div style="font-family:'Bebas Neue',sans-serif;font-size:30px;">볼코노프스키</div><div style="font-size:12px;color:var(--t3);">26W 3L · 전 챔피언</div><div style="display:flex;gap:5px;justify-content:center;margin-top:7px;"><span style="font-size:11px;padding:2px 7px;background:var(--bg4);border:1px solid var(--bd);border-radius:10px;color:var(--t3);">레슬링</span><span style="font-size:11px;padding:2px 7px;background:var(--bg4);border:1px solid var(--bd);border-radius:10px;color:var(--t3);">스태미나</span></div></div>
        </div>
        <div style="display:flex;gap:10px;"><button class="br sm" onclick="go('product')">홍길동 예고 굿즈 →</button><button class="bo sm" onclick="toast('✓ 경기 알림이 신청되었습니다')">경기 알림 신청</button></div>
      </div>
    </div>
    <div id="st-hi" style="display:none;">
      <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:14px;overflow:hidden;margin-bottom:14px;">
        <div style="height:190px;background:linear-gradient(135deg,#1a1a2e,#16213e);display:flex;align-items:center;justify-content:center;font-size:52px;position:relative;cursor:pointer;" onclick="toast('공식 유튜브 링크로 이동합니다')">🎬<div style="position:absolute;width:56px;height:56px;border-radius:50%;background:rgba(230,57,70,.9);display:flex;align-items:center;justify-content:center;font-size:22px;">▶</div></div>
        <div style="padding:13px 16px;"><div style="font-size:14px;font-weight:500;margin-bottom:3px;">UFC 298 홍길동 KO 하이라이트</div><div style="font-size:12px;color:var(--t3);margin-bottom:9px;">공식 UFC 유튜브 · 2025.05.17</div><button class="br sm" onclick="go('product')">관련 굿즈 보기 →</button></div>
      </div>
    </div>
  </div>
</div>

<!-- PRODUCT DETAIL -->
<div class="pw" id="p-product">
  <div class="bc"><span onclick="go('home');nav(document.querySelectorAll('.nl')[0])">굿즈 홈</span><span class="sep">›</span><span onclick="go('fighter-detail')">홍길동</span><span class="sep">›</span><span style="color:var(--t2);">챔피언 등극 기념 티셔츠</span></div>
  <div class="dl">
    <div class="dimg">
      <div class="mi" id="mimg">👕</div>
      <div class="tr">
        <div class="th on" onclick="selThumb(this,'👕')">👕</div>
        <div class="th" onclick="selThumb(this,'📐')">📐</div>
        <div class="th" onclick="selThumb(this,'🏷️')">🏷️</div>
        <div class="th" onclick="selThumb(this,'📦')">📦</div>
      </div>
    </div>
    <div>
      <div class="dtag" onclick="go('fighter-detail')">🥊 홍길동 · UFC 웰터급 챔피언</div>
      <div class="dnm">홍길동 챔피언 등극 기념 티셔츠</div>
      <div class="dpr" id="dpr">₩45,000</div>
      <div class="drev"><span style="color:#f4a261;font-size:14px;">★★★★★</span><span style="font-size:14px;font-weight:700;">4.8</span><span style="font-size:13px;color:var(--t3);">(23개 리뷰)</span></div>
      <div class="divr"></div>
      <div class="ol">사이즈</div>
      <div class="or" id="so">
        <button class="ob" onclick="selOpt(this,'so')">S</button>
        <button class="ob on" onclick="selOpt(this,'so')">M</button>
        <button class="ob" onclick="selOpt(this,'so')">L</button>
        <button class="ob" onclick="selOpt(this,'so')">XL</button>
      </div>
      <div class="ol">색상</div>
      <div class="or" id="co">
        <button class="ob on" onclick="selOpt(this,'co')">블랙</button>
        <button class="ob" onclick="selOpt(this,'co')">화이트</button>
        <button class="ob" onclick="selOpt(this,'co')">레드</button>
      </div>
      <div class="qr"><div class="ql">수량</div><div class="qc"><button class="qb" onclick="chgQ(-1)">−</button><div class="qv" id="qv">1</div><button class="qb" onclick="chgQ(1)">+</button></div></div>
      <div class="ps2">
        <div class="pr2"><span class="pl">상품금액</span><span id="psub">₩45,000</span></div>
        <div class="pr2"><span class="pl">배송비</span><span>₩3,000</span></div>
        <div class="pr2 tot"><span>총 결제금액</span><span class="pv" id="ptot">₩48,000</span></div>
      </div>
      <div class="brow"><button class="bbuy" onclick="buyNow()">바로구매</button><button class="bcart" onclick="addCart()">장바구니 담기</button></div>
      <div class="divr"></div>
      <div style="font-size:13px;color:var(--t3);line-height:1.8;">소재: 코튼 100% · 제조국: 한국<br>배송: 영업일 기준 2~3일 소요<br>교환/반품: 수령 후 7일 이내 가능</div>
      <div class="divr"></div>
      <div style="font-size:14px;font-weight:700;margin-bottom:14px;">구매 후기</div>
      <div class="rev-item"><div class="rev-top"><div style="width:30px;height:30px;border-radius:50%;background:var(--bg4);display:flex;align-items:center;justify-content:center;">👤</div><span style="font-size:13px;font-weight:500;">fight_fan92</span><span style="color:#f4a261;font-size:12px;">★★★★★</span><span style="font-size:11px;color:var(--t3);margin-left:auto;">2025.05.18</span></div><div style="font-size:13px;color:var(--t2);line-height:1.6;">퀄리티 대박이에요. 챔피언 등극 순간이 프린트되어 있어서 감동이 두 배입니다.</div></div>
      <div class="rev-item"><div class="rev-top"><div style="width:30px;height:30px;border-radius:50%;background:var(--bg4);display:flex;align-items:center;justify-content:center;">👤</div><span style="font-size:13px;font-weight:500;">goods_collector</span><span style="color:#f4a261;font-size:12px;">★★★★★</span><span style="font-size:11px;color:var(--t3);margin-left:auto;">2025.05.17</span></div><div style="font-size:13px;color:var(--t2);line-height:1.6;">배송도 빠르고 원단이 부드러워요. 사이즈 딱 맞게 왔습니다.</div></div>
      <div class="rev-item"><div class="rev-top"><div style="width:30px;height:30px;border-radius:50%;background:var(--bg4);display:flex;align-items:center;justify-content:center;">👤</div><span style="font-size:13px;font-weight:500;">ufc_lover</span><span style="color:#f4a261;font-size:12px;">★★★★☆</span><span style="font-size:11px;color:var(--t3);margin-left:auto;">2025.05.15</span></div><div style="font-size:13px;color:var(--t2);line-height:1.6;">디자인은 정말 마음에 드는데 배송이 하루 늦었어요. 재구매 의사 있습니다!</div></div>
    </div>
  </div>
</div>

<!-- CART -->
<div class="pw" id="p-cart">
  <div class="cl">
    <div>
      <div style="font-family:'Bebas Neue',sans-serif;font-size:26px;letter-spacing:1px;margin-bottom:22px;">장바구니</div>
      <div id="citems"></div>
    </div>
    <div>
      <div class="csum">
        <div style="font-size:15px;font-weight:700;margin-bottom:18px;">주문 요약</div>
        <div style="display:flex;gap:8px;margin-bottom:14px;"><input class="ci2" placeholder="쿠폰 코드 (FIGHT10)" id="cpn"><button class="cbtn" onclick="applyCpn()">적용</button></div>
        <div class="srow"><span class="sl2">상품금액</span><span id="csub">₩0</span></div>
        <div class="srow" id="disc-row" style="display:none;color:var(--gl);"><span class="sl2">할인</span><span id="disc-amt"></span></div>
        <div class="srow"><span class="sl2">배송비</span><span id="cship">₩3,000</span></div>
        <div class="sdiv"></div>
        <div class="stot"><span>총 결제금액</span><span class="sv" id="ctot">₩0</span></div>
        <button class="br full" onclick="go('payment')">결제하기</button>
      </div>
    </div>
  </div>
</div>

<!-- PAYMENT -->
<div class="pw" id="p-payment">
  <div class="payl">
    <div>
      <div style="font-family:'Bebas Neue',sans-serif;font-size:26px;letter-spacing:1px;margin-bottom:24px;">결제</div>
      <div style="margin-bottom:26px;"><div style="font-size:14px;font-weight:700;margin-bottom:11px;color:var(--t2);">배송지 정보</div><div class="abox" id="padr"><div style="font-size:13px;color:var(--t3);">로그인 후 배송지가 자동으로 불러와집니다.</div></div><button class="bo sm" style="margin-top:9px;" onclick="toast('배송지 변경')">배송지 변경</button></div>
      <div style="margin-bottom:26px;"><div style="font-size:14px;font-weight:700;margin-bottom:11px;color:var(--t2);">결제 수단</div>
        <div class="pm" id="pmethods">
          <button class="pmb" onclick="selPay(this)">신용/체크카드</button>
          <button class="pmb on" onclick="selPay(this)">카카오페이</button>
          <button class="pmb" onclick="selPay(this)">토스페이</button>
          <button class="pmb" onclick="selPay(this)">네이버페이</button>
          <button class="pmb" onclick="selPay(this)" style="grid-column:span 4;">무통장입금</button>
        </div>
      </div>
      <div style="margin-bottom:26px;"><div style="font-size:14px;font-weight:700;margin-bottom:11px;color:var(--t2);">적립금 사용</div>
        <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:10px;padding:14px 18px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:9px;"><span style="font-size:13px;color:var(--t2);">보유 적립금</span><span style="font-size:14px;font-weight:700;" id="ppt">0 P</span></div>
          <div style="display:flex;gap:8px;"><input class="ci2" id="puse" placeholder="사용할 포인트 (100P 단위)"><button class="cbtn" onclick="usePoint()">적용</button></div>
        </div>
      </div>
    </div>
    <div>
      <div class="osc">
        <div style="font-size:15px;font-weight:700;margin-bottom:14px;">주문 상품</div>
        <div id="pitems"></div>
        <div style="margin-top:14px;" id="ptotals"></div>
        <button class="br full" style="margin-top:14px;" onclick="doConfirm()">결제하기</button>
      </div>
    </div>
  </div>
</div>

<!-- CONFIRM -->
<div class="pw" id="p-confirm">
  <div class="conf">
    <div class="cicon">✓</div>
    <div class="ctit">결제 완료!</div>
    <div style="font-size:13px;color:var(--t3);margin-bottom:4px;">주문 확인 이메일이 발송되었습니다</div>
    <div class="cbox" id="cdet"></div>
    <div style="display:flex;gap:12px;justify-content:center;">
      <button class="br" onclick="go('home');nav(document.querySelectorAll('.nl')[0])">쇼핑 계속하기</button>
      <button class="bo" onclick="go('mypage');nav(document.querySelectorAll('.nl')[7])">주문 내역 확인</button>
    </div>
  </div>
</div>

<!-- MYPAGE -->
<div class="pw" id="p-mypage">
  <div class="mpl">
    <div class="mpside">
      <div class="mpprof">
        <div class="mpav" id="mpav">?</div>
        <div style="font-size:15px;font-weight:700;margin-bottom:3px;" id="mpnm">로그인이 필요합니다</div>
        <div style="font-size:12px;color:var(--t3);" id="mpem"></div>
        <div style="font-size:13px;color:var(--red);font-weight:700;margin-top:7px;" id="mppt"></div>
      </div>
      <div class="mpmenu">
        <div class="mmi on" id="mm-orders" onclick="mpTab('orders')">📦 구매내역</div>
        <div class="mmi" id="mm-profile" onclick="mpTab('profile')">👤 정보수정</div>
        <div class="mmi" id="mm-delivery" onclick="mpTab('delivery')">🚚 배송조회</div>
        <div class="mmi" id="mm-withdraw" onclick="mpTab('withdraw')">⚠️ 계정탈퇴</div>
      </div>
    </div>
    <div id="mpc" style="min-height:400px;"></div>
  </div>
</div>

<!-- COMMUNITY -->
<div class="pw" id="p-community">
  <div class="sec">
    <div class="sh"><div class="sl">커뮤니티</div><div class="st">팬 커뮤니티</div></div>
    <div style="display:grid;grid-template-columns:1fr 300px;gap:28px;align-items:start;">
      <div>
        <div class="tabs" style="margin-bottom:18px;">
          <button class="tab on" onclick="tabOn(this,this.parentNode)">자유게시판</button>
          <button class="tab" onclick="tabOn(this,this.parentNode)">구매 후기</button>
          <button class="tab" onclick="tabOn(this,this.parentNode)">굿즈 자랑</button>
          <button class="tab" onclick="tabOn(this,this.parentNode)">경기 토론</button>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
          <div style="display:flex;gap:7px;"><button class="chip on" onclick="sortP('r',this)">최신순</button><button class="chip" onclick="sortP('l',this)">인기순</button></div>
          <button class="br sm" onclick="toggleWrite()">글쓰기 +</button>
        </div>
        <div id="wf" style="display:none;background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:18px;margin-bottom:18px;">
          <input id="wt" placeholder="제목" style="width:100%;padding:10px 13px;background:var(--bg4);border:1px solid var(--bd2);border-radius:8px;color:var(--t);font-size:14px;font-family:inherit;margin-bottom:9px;outline:none;">
          <textarea id="wb" placeholder="내용을 입력하세요" style="width:100%;padding:10px 13px;background:var(--bg4);border:1px solid var(--bd2);border-radius:8px;color:var(--t);font-size:13px;font-family:inherit;resize:vertical;min-height:80px;margin-bottom:9px;outline:none;"></textarea>
          <div style="display:flex;gap:8px;justify-content:flex-end;"><button class="bo sm" onclick="toggleWrite()">취소</button><button class="br sm" onclick="submitPost()">등록</button></div>
        </div>
        <div id="posts"></div>
      </div>
      <div style="display:flex;flex-direction:column;gap:18px;">
        <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:20px;">
          <div style="font-size:11px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:1px;margin-bottom:5px;">이벤트</div>
          <div style="font-size:15px;font-weight:700;margin-bottom:5px;">선수 Q&A</div>
          <div style="font-size:12px;color:var(--t3);line-height:1.7;margin-bottom:13px;">홍길동 선수에게 질문을 남겨보세요.<br>접수: ~2025.06.15</div>
          <div style="background:var(--bg4);border:1px solid var(--bd);border-radius:9px;padding:11px 13px;margin-bottom:8px;"><div style="font-size:13px;margin-bottom:5px;">"챔피언 벨트 따고 제일 먼저 한 일?"</div><div style="display:flex;justify-content:space-between;"><span style="font-size:11px;color:var(--t3);">fan_kim</span><button style="font-size:11px;color:var(--red);background:none;border:none;cursor:pointer;" onclick="toast('❤️ 좋아요!')">❤️ 142</button></div></div>
          <button class="bo full sm" onclick="toast('✓ 질문이 접수되었습니다 (+30P)')">질문 남기기 (+30P)</button>
        </div>
        <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:20px;">
          <div style="font-size:11px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:1px;margin-bottom:5px;">투표 진행 중</div>
          <div style="font-size:15px;font-weight:700;margin-bottom:3px;">다음 굿즈 투표</div>
          <div style="font-size:11px;color:var(--t3);margin-bottom:14px;">마감: 2025.06.01 · 참여 시 +50P</div>
          <div id="votearea"></div>
          <div style="font-size:11px;color:var(--t3);margin-top:9px;text-align:right;">총 2,341명 참여</div>
        </div>
        <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:20px;">
          <div style="font-size:11px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:1px;margin-bottom:5px;">승부 예측 · +100P</div>
          <div style="font-size:14px;font-weight:700;margin-bottom:3px;">UFC 308 메인이벤트</div>
          <div style="font-size:11px;color:var(--t3);margin-bottom:13px;">홍길동 vs 볼코노프스키</div>
          <div style="display:flex;gap:8px;">
            <button class="pmb" id="pa" onclick="predict('홍길동')">홍길동 승</button>
            <button class="pmb" id="pb" onclick="predict('볼코노프스키')">볼코노프스키 승</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- NOTICE -->
<div class="pw" id="p-notice">
  <div class="sec">
    <div class="sh"><div class="sl">공지사항</div><div class="st">공지사항</div></div>
    <div style="max-width:760px;">
      <div class="ni"><span class="npin">공지</span><div><div class="ntit">[필독] 5월 배송 지연 안내</div><div style="font-size:11px;color:var(--t3);">2025.05.15</div></div></div>
      <div class="ni"><span class="npin">공지</span><div><div class="ntit">UFC 298 연계 굿즈 출시 안내</div><div style="font-size:11px;color:var(--t3);">2025.05.17</div></div></div>
      <div class="ni"><div style="width:32px;"></div><div><div class="ntit">시스템 점검 예정 (5/20 02:00~04:00)</div><div style="font-size:11px;color:var(--t3);">2025.05.13</div></div></div>
      <div class="ni"><div style="width:32px;"></div><div><div class="ntit">이용약관 개정 안내 (2025.06.01 시행)</div><div style="font-size:11px;color:var(--t3);">2025.05.01</div></div></div>
      <div class="ni" style="border-bottom:none;"><div style="width:32px;"></div><div><div class="ntit">FIGHTGOODS 서비스 오픈 안내</div><div style="font-size:11px;color:var(--t3);">2025.04.01</div></div></div>
    </div>
  </div>
</div>

<!-- FAQ -->
<div class="pw" id="p-faq">
  <div class="sec">
    <div class="sh"><div class="sl">고객지원</div><div class="st">FAQ &amp; 1:1 문의</div></div>
    <div style="display:grid;grid-template-columns:1fr 320px;gap:36px;align-items:start;">
      <div>
        <div style="display:flex;align-items:center;gap:9px;background:var(--bg3);border:1px solid var(--bd2);border-radius:10px;padding:11px 16px;margin-bottom:14px;"><span>🔍</span><input id="fqs" placeholder="궁금한 점을 검색하세요" oninput="filterFaq()" style="flex:1;background:none;border:none;outline:none;color:var(--t);font-size:14px;font-family:inherit;"></div>
        <div style="display:flex;gap:7px;margin-bottom:18px;" id="fqcats">
          <button class="chip on" data-c="전체" onclick="chipOn(this,'#fqcats .chip');filterFaq()">전체</button>
          <button class="chip" data-c="배송" onclick="chipOn(this,'#fqcats .chip');filterFaq()">배송</button>
          <button class="chip" data-c="교환반품" onclick="chipOn(this,'#fqcats .chip');filterFaq()">교환/반품</button>
          <button class="chip" data-c="결제" onclick="chipOn(this,'#fqcats .chip');filterFaq()">결제</button>
          <button class="chip" data-c="굿즈" onclick="chipOn(this,'#fqcats .chip');filterFaq()">굿즈</button>
        </div>
        <div id="fql"></div>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:22px;">
        <div style="font-size:14px;font-weight:700;margin-bottom:14px;">1:1 문의 접수</div>
        <div style="font-size:12px;color:var(--t3);margin-bottom:14px;line-height:1.7;">운영시간: 평일 10:00~18:00<br>운영시간 외 챗봇 자동 응답</div>
        <select style="width:100%;padding:10px 13px;background:var(--bg4);border:1px solid var(--bd2);border-radius:8px;color:var(--t);font-size:13px;font-family:inherit;margin-bottom:9px;outline:none;"><option>문의 유형 선택</option><option>상품 불량</option><option>오배송</option><option>미배송</option><option>결제 오류</option><option>기타</option></select>
        <textarea placeholder="문의 내용을 입력해주세요" style="width:100%;padding:10px 13px;background:var(--bg4);border:1px solid var(--bd2);border-radius:8px;color:var(--t);font-size:13px;font-family:inherit;resize:vertical;min-height:90px;margin-bottom:9px;outline:none;"></textarea>
        <button class="br full" onclick="toast('✓ 문의가 접수되었습니다. 접수번호: #20250517-CS042')">문의 접수</button>
      </div>
    </div>
  </div>
</div>

<div class="toast" id="tst"></div>

<script>
const PRODS=[
  {id:1,n:'홍길동 챔피언 등극 기념 티셔츠',f:'홍길동 · UFC 웰터급',p:45000,ic:'👕',b:'h',s:'재고 12개',c:'티셔츠'},
  {id:2,n:'챔피언 벨트 아트 포스터',f:'홍길동 · UFC 웰터급',p:18000,ic:'🖼️',b:'l',s:'한정 50개',c:'포스터'},
  {id:3,n:'등극 순간 포토카드 세트',f:'홍길동 · UFC 웰터급',p:12000,ic:'📸',b:'n',s:'재고 있음',c:'포토카드'},
  {id:4,n:'이철수 부상 극복 기념 후디',f:'이철수 · 블랙컴뱃 헤비급',p:68000,ic:'🎽',b:'',s:'재고 5개',c:'후디'},
  {id:5,n:'박영희 무패 스트릭 머그컵',f:'박영희 · ZFN 밴텀급',p:16000,ic:'☕',b:'n',s:'재고 30개',c:'포토카드'},
];
const FIGHTERS=[
  {ic:'🥊',n:'홍길동',m:'웰터급 · UFC · 데뷔 2019',w:12,l:3,fp:'77%',tags:['챔피언 등극','체급 조절'],g:3,org:'UFC',cls:'웰터급'},
  {ic:'💪',n:'이철수',m:'헤비급 · 블랙컴뱃 · 데뷔 2020',w:8,l:1,fp:'62%',tags:['부상 극복','무명 시절'],g:1,org:'블랙컴뱃',cls:'헤비급'},
  {ic:'⚡',n:'박영희',m:'밴텀급 · ZFN · 데뷔 2022',w:6,l:0,fp:'83%',tags:['신인왕','연승 스트릭'],g:2,org:'ZFN',cls:'밴텀급'},
];
const RNKS=[
  {r:1,ch:'up',n:'챔피언 등극 기념 티셔츠',f:'홍길동',s:1284,p:45000},
  {r:2,ch:'eq',n:'챔피언 벨트 아트 포스터',f:'홍길동',s:893,p:18000},
  {r:3,ch:'up',n:'등극 순간 포토카드 세트',f:'홍길동',s:712,p:12000},
  {r:4,ch:'dn',n:'이철수 부상 극복 기념 후디',f:'이철수',s:445,p:68000},
  {r:5,ch:'up',n:'박영희 무패 스트릭 머그컵',f:'박영희',s:321,p:16000},
];
const FAQS=[
  {c:'배송',q:'배송은 얼마나 걸리나요?',a:'결제 완료 후 영업일 2~3일 이내 발송됩니다.'},
  {c:'배송',q:'배송비는 얼마인가요?',a:'기본 3,000원이며 5만원 이상 구매 시 무료입니다.'},
  {c:'교환반품',q:'교환·반품은 어떻게 하나요?',a:'수령 후 7일 이내 마이페이지에서 신청 가능합니다.'},
  {c:'교환반품',q:'불량품을 받았어요.',a:'1:1 문의로 사진과 함께 접수해 주시면 무료 교환 처리해 드립니다.'},
  {c:'결제',q:'어떤 결제 수단을 지원하나요?',a:'카드, 카카오페이, 토스페이, 네이버페이, 무통장입금을 지원합니다.'},
  {c:'결제',q:'결제 후 취소할 수 있나요?',a:'배송 시작 전까지 마이페이지 구매내역에서 취소 가능합니다.'},
  {c:'굿즈',q:'한정판 상품은 어떻게 구매하나요?',a:'출시 예정 상품에서 알림 신청을 하시면 출시 당일 알림을 받으실 수 있습니다.'},
];
const CEVENTS={'2025-5-3':'ZFN 38','2025-5-10':'블랙컴뱃 15','2025-5-17':'UFC 298','2025-5-24':'ZFN 39'};
const DPOST=[
  {id:1,t:'홍길동 KO 진짜 소름...', b:'1라운드에 저렇게 끝낼 줄 몰랐다 ㄷㄷ', a:'fight_fan',l:47,cm:12,tm:'방금'},
  {id:2,t:'챔피언 벨트 포스터 후기', b:'퀄리티 생각보다 훨씬 좋음. 액자 끼워서 인테리어 됨', a:'goods_collector',l:38,cm:8,tm:'10분 전'},
  {id:3,t:'이철수 다음 경기 언제임?', b:'ZFN 39 나오는지 아는 사람?', a:'mma_nerd',l:15,cm:23,tm:'1시간 전'},
];
const VOTES=[{l:'챔피언 후드 집업',v:48},{l:'등극 기념 키링',v:31},{l:'포토북',v:21}];

// STATE
let qty=1,cartItems=[],couponApplied=false,cartDisc=0;
let recentViewed=[],posts=[...DPOST],nxtPid=4;
let calY=2025,calM=4,voted=false,predicted=false;
let currentUser=null;

// ── UTILS ──
function go(name){
  document.querySelectorAll('.pw').forEach(p=>p.classList.remove('on'));
  const el=document.getElementById('p-'+name);
  if(el) el.classList.add('on');
  window.scrollTo({top:0,behavior:'smooth'});
  if(name==='mypage') renderMp();
  if(name==='cart') renderCart();
  if(name==='payment') renderPayment();
  if(name==='schedule') renderCal();
  if(name==='faq') renderFaq(FAQS);
  if(name==='community') renderVote();
  if(name==='product'){ addRV(PRODS[0]); }
}
function nav(el){
  document.querySelectorAll('.nl').forEach(n=>n.classList.remove('on'));
  if(el) el.classList.add('on');
}
function tabOn(el,parent){
  parent.querySelectorAll('.tab').forEach(t=>t.classList.remove('on'));
  el.classList.add('on');
}
function chipOn(el,sel){
  document.querySelectorAll(sel).forEach(c=>c.classList.remove('on'));
  el.classList.add('on');
}
let toastT;
function toast(msg){
  const t=document.getElementById('tst');
  t.textContent=msg; t.classList.add('on');
  clearTimeout(toastT);
  toastT=setTimeout(()=>t.classList.remove('on'),2500);
}

// ── AUTH ──
function loadAuth(){
  try{ const u=localStorage.getItem('fg_user'); if(u) currentUser=JSON.parse(u); }catch(e){}
  renderNav();
}
function saveAuth(u){ currentUser=u; localStorage.setItem('fg_user',JSON.stringify(u)); renderNav(); }
function renderNav(){
  const el=document.getElementById('nauth');
  if(!el) return;
  if(currentUser){
    el.innerHTML=`<div class="ubtn" onclick="go('mypage');nav(document.querySelectorAll('.nl')[7])"><div class="uav">${currentUser.nick[0]}</div><span>${currentUser.nick}</span></div><button style="padding:8px 13px;border-radius:8px;background:transparent;color:var(--t);font-size:13px;border:1px solid var(--bd2);cursor:pointer;font-family:inherit;" onclick="doLogout()">로그아웃</button>`;
    const pa=document.getElementById('padr');
    if(pa) pa.innerHTML=`<div style="font-size:14px;font-weight:500;">${currentUser.nick} · 010-1234-5678</div><div style="font-size:12px;color:var(--t3);margin-top:5px;">서울특별시 성북구 안암로 145</div>`;
    const pp=document.getElementById('ppt'); if(pp) pp.textContent=(currentUser.point||0)+' P';
  } else {
    el.innerHTML=`<button class="lbtn" onclick="openAuth()">로그인</button>`;
  }
}
function openAuth(tab){ document.getElementById('aov').classList.add('on'); atab(tab||'login'); }
function closeAuth(){ document.getElementById('aov').classList.remove('on'); }
function atab(t){
  document.getElementById('tlog').classList.toggle('on',t==='login');
  document.getElementById('tsig').classList.toggle('on',t==='signup');
  document.getElementById('flog').style.display=t==='login'?'block':'none';
  document.getElementById('fsig').style.display=t==='signup'?'block':'none';
}
document.getElementById('aov').addEventListener('click',function(e){ if(e.target===this) closeAuth(); });

function doLogin(){
  const e=document.getElementById('le').value.trim(), p=document.getElementById('lp').value;
  const err=document.getElementById('lerr');
  if(!e||!p){ err.textContent='이메일과 비밀번호를 입력해주세요.'; err.style.display='block'; return; }
  try{
    const users=JSON.parse(localStorage.getItem('fg_users')||'[]');
    const u=users.find(x=>x.email===e&&x.pw===p);
    if(!u){ err.textContent='이메일 또는 비밀번호가 올바르지 않습니다.'; err.style.display='block'; return; }
    saveAuth(u); closeAuth(); toast('✓ 로그인 완료! 환영합니다, '+u.nick+'님'); err.style.display='none';
  }catch(ex){ err.textContent='오류가 발생했습니다.'; err.style.display='block'; }
}
function socialLogin(prov){
  const nick=prov+'유저'+Math.floor(Math.random()*1000);
  const u={email:nick+'@social.com',nick,pw:'',point:500,orders:[]};
  saveAuth(u); closeAuth(); toast('✓ '+prov+' 로그인 완료! 환영합니다, '+nick+'님');
}
function doLogout(){ currentUser=null; localStorage.removeItem('fg_user'); renderNav(); toast('로그아웃 되었습니다'); }
function chkEmail(v){
  const h=document.getElementById('seh'); if(!v){h.textContent='';return;}
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)){h.className='fh err';h.textContent='올바른 이메일 형식이 아닙니다.';return;}
  const users=JSON.parse(localStorage.getItem('fg_users')||'[]');
  if(users.find(u=>u.email===v)){h.className='fh err';h.textContent='이미 사용 중인 이메일입니다.';}
  else{h.className='fh ok';h.textContent='사용 가능한 이메일입니다.';}
}
function chkNick(v){
  const h=document.getElementById('snh'); if(!v){h.textContent='';return;}
  if(v.length<2||v.length>10){h.className='fh err';h.textContent='닉네임은 2~10자여야 합니다.';return;}
  h.className='fh ok';h.textContent='사용 가능한 닉네임입니다.';
}
function chkPw(v){
  const bar=document.getElementById('pwbar'),h=document.getElementById('sph');
  const sc=[/.{8,}/.test(v),/[A-Za-z]/.test(v),/[0-9]/.test(v),/[^A-Za-z0-9]/.test(v)].filter(Boolean).length;
  const cols=['','#e63946','#f4a261','#2d6a4f','#2d6a4f'],lbs=['','약함','보통','강함','매우 강함'];
  bar.style.width=(sc*25)+'%'; bar.style.background=cols[sc]||'transparent';
  h.className=sc>=3?'fh ok':'fh err'; h.textContent=v?lbs[sc]:'';
}
function chkPw2(v){
  const h=document.getElementById('sp2h'),pw=document.getElementById('sp').value; if(!v){h.textContent='';return;}
  if(v===pw){h.className='fh ok';h.textContent='비밀번호가 일치합니다.';}
  else{h.className='fh err';h.textContent='비밀번호가 일치하지 않습니다.';}
}
function doSignup(){
  const e=document.getElementById('se').value.trim(),n=document.getElementById('sn').value.trim();
  const p=document.getElementById('sp').value,p2=document.getElementById('sp2').value;
  const agr=document.getElementById('agr').checked,err=document.getElementById('serr');
  if(!e||!n||!p||!p2){err.textContent='모든 항목을 입력해주세요.';err.style.display='block';return;}
  if(p!==p2){err.textContent='비밀번호가 일치하지 않습니다.';err.style.display='block';return;}
  if(p.length<8){err.textContent='비밀번호는 8자 이상이어야 합니다.';err.style.display='block';return;}
  if(!agr){err.textContent='이용약관에 동의해주세요.';err.style.display='block';return;}
  try{
    const users=JSON.parse(localStorage.getItem('fg_users')||'[]');
    if(users.find(u=>u.email===e)){err.textContent='이미 사용 중인 이메일입니다.';err.style.display='block';return;}
    const u={email:e,nick:n,pw:p,point:0,orders:[]};
    users.push(u); localStorage.setItem('fg_users',JSON.stringify(users));
    saveAuth(u); closeAuth(); toast('✓ 회원가입 완료! 환영합니다, '+n+'님'); err.style.display='none';
  }catch(ex){err.textContent='오류가 발생했습니다.';err.style.display='block';}
}

// ── PRODUCTS ──
function prodHTML(p){
  const bm={h:'<span class="pbadge bh">🔥 HOT</span>',l:'<span class="pbadge bl">한정판</span>',n:'<span class="pbadge bn">NEW</span>'};
  return`<div class="pc" onclick="go('product')"><div class="pi">${p.ic}${bm[p.b]||''}</div><div class="pb"><div class="pn">${p.n}</div><div class="pf">${p.f}</div><div class="pp"><div class="pr">₩${p.p.toLocaleString()}</div><div class="ps">${p.s}</div></div></div></div>`;
}
function renderProds(el,list){ const e=document.getElementById(el); if(e) e.innerHTML=list.map(prodHTML).join(''); }
function filterP(btn){
  chipOn(btn,'#pf .chip');
  const c=btn.dataset.c;
  renderProds('hpg',c==='전체'?PRODS:PRODS.filter(p=>p.c===c));
}

// ── FIGHTERS ──
function fighterHTML(f){
  return`<div class="fc" onclick="go('fighter-detail')"><div class="fav">${f.ic}</div><div class="fi2"><div class="fn">${f.n}</div><div class="fm">${f.m}</div><div class="frec"><div class="frs"><div class="frv">${f.w}</div><div class="frl">승</div></div><div class="frs"><div class="frv">${f.l}</div><div class="frl">패</div></div><div class="frs"><div class="frv">${f.fp}</div><div class="frl">피니시율</div></div></div><div class="ftags">${f.tags.map(t=>`<span class="ftag">${t}</span>`).join('')}</div><div class="fg-cnt">관련 굿즈 ${f.g}개</div></div></div>`;
}
function renderFighters(list){
  const e=document.getElementById('fgrid'); if(!e) return;
  e.innerHTML=list.length?list.map(fighterHTML).join(''):'<div style="grid-column:span 3;text-align:center;padding:40px;color:var(--t3);">검색 결과가 없습니다</div>';
}
function filterF(){
  const q=(document.getElementById('fsrch')||{}).value||'';
  const ac=document.querySelector('#ff .chip.on');
  const f=ac?ac.dataset.f:'전체';
  const res=FIGHTERS.filter(x=>{
    const mq=!q||x.n.includes(q);
    const mf=f==='전체'||x.cls===f||x.org===f;
    return mq&&mf;
  });
  renderFighters(res);
  // also update home fighter grid
  const hf=document.getElementById('hfg'); if(hf) hf.innerHTML=FIGHTERS.map(fighterHTML).join('');
}

// ── RANKING ──
function renderRank(){
  const cm={up:'▲ up',dn:'▼ dn',eq:'— eq'};
  document.getElementById('rtb').innerHTML=RNKS.map(r=>`
    <tr onclick="go('product')" style="cursor:pointer;">
      <td><div style="font-weight:700;${r.r<=3?'color:var(--red);font-size:15px;':''}">${r.r}<div class="rch ${r.ch}">${{up:'▲',dn:'▼',eq:'—'}[r.ch]}</div></div></td>
      <td><div style="font-size:14px;font-weight:500;">${r.n}</div></td>
      <td style="color:var(--t3);font-size:13px;">${r.f}</td>
      <td style="text-align:right;font-size:14px;font-weight:700;">${r.s.toLocaleString()}</td>
      <td style="text-align:right;color:var(--red);font-weight:700;">₩${r.p.toLocaleString()}</td>
    </tr>`).join('');
}

// ── PRODUCT DETAIL ──
function selOpt(btn,gid){
  document.querySelectorAll('#'+gid+' .ob').forEach(b=>b.classList.remove('on'));
  btn.classList.add('on');
}
function selThumb(btn,ic){
  document.querySelectorAll('.th').forEach(t=>t.classList.remove('on'));
  btn.classList.add('on');
  document.getElementById('mimg').textContent=ic;
}
function chgQ(d){
  qty=Math.max(1,Math.min(99,qty+d));
  document.getElementById('qv').textContent=qty;
  const sub=45000*qty;
  document.getElementById('psub').textContent='₩'+sub.toLocaleString();
  document.getElementById('ptot').textContent='₩'+(sub+3000).toLocaleString();
}
function buyNow(){
  if(!currentUser){openAuth('login');toast('로그인이 필요합니다');return;}
  go('payment');
}
function addCart(){
  const sz=document.querySelector('#so .ob.on')?.textContent||'M';
  const cl=document.querySelector('#co .ob.on')?.textContent||'블랙';
  const ex=cartItems.find(i=>i.sz===sz&&i.cl===cl);
  if(ex) ex.qty+=qty; else cartItems.push({id:1,n:'홍길동 챔피언 등극 기념 티셔츠',ic:'👕',p:45000,sz,cl,qty});
  updateCC(); toast('✓ 장바구니에 담겼습니다');
}
function updateCC(){ document.getElementById('cc').textContent=cartItems.reduce((s,i)=>s+i.qty,0); }

// ── CART ──
function renderCart(){
  const w=document.getElementById('citems');
  if(!cartItems.length){
    w.innerHTML='<div style="text-align:center;padding:56px;color:var(--t3);"><div style="font-size:40px;margin-bottom:10px;">🛒</div>장바구니가 비어있습니다</div>';
    updCartTot(); return;
  }
  w.innerHTML=cartItems.map((it,i)=>`
    <div class="cart-item">
      <div class="cimg">${it.ic}</div>
      <div style="flex:1;">
        <div style="font-size:14px;font-weight:500;margin-bottom:3px;">${it.n}</div>
        <div style="font-size:12px;color:var(--t3);margin-bottom:10px;">${it.sz} · ${it.cl}</div>
        <div style="display:flex;align-items:center;justify-content:space-between;">
          <div style="display:flex;border:1px solid var(--bd2);border-radius:8px;overflow:hidden;">
            <button class="qb" onclick="cqty(${i},-1)">−</button>
            <div class="qv" style="width:40px;height:36px;line-height:36px;">${it.qty}</div>
            <button class="qb" onclick="cqty(${i},1)">+</button>
          </div>
          <div style="font-size:15px;font-weight:700;color:var(--red);">₩${(it.p*it.qty).toLocaleString()}</div>
        </div>
        <button onclick="rmCart(${i})" style="font-size:12px;color:var(--t3);background:none;border:none;cursor:pointer;margin-top:7px;font-family:inherit;">삭제</button>
      </div>
    </div>`).join('');
  updCartTot();
}
function cqty(i,d){ cartItems[i].qty=Math.max(1,cartItems[i].qty+d); updateCC(); renderCart(); }
function rmCart(i){ cartItems.splice(i,1); updateCC(); renderCart(); }
function updCartTot(){
  const sub=cartItems.reduce((s,i)=>s+i.p*i.qty,0);
  const ship=sub>0?3000:0;
  document.getElementById('csub').textContent='₩'+sub.toLocaleString();
  document.getElementById('cship').textContent='₩'+ship.toLocaleString();
  document.getElementById('ctot').textContent='₩'+(sub+ship-cartDisc).toLocaleString();
}
function applyCpn(){
  if(couponApplied){toast('이미 쿠폰이 적용되었습니다');return;}
  const v=document.getElementById('cpn').value.trim().toUpperCase();
  if(v==='FIGHT10'){
    couponApplied=true;
    const sub=cartItems.reduce((s,i)=>s+i.p*i.qty,0);
    cartDisc=Math.floor(sub*.1);
    document.getElementById('disc-row').style.display='flex';
    document.getElementById('disc-amt').textContent='-₩'+cartDisc.toLocaleString();
    updCartTot(); toast('🎉 쿠폰 적용! 10% 할인');
  } else toast('유효하지 않은 쿠폰 코드입니다');
}

// ── PAYMENT ──
function renderPayment(){
  const items=cartItems.length?cartItems:[{ic:'👕',n:'홍길동 챔피언 등극 기념 티셔츠',sz:'M',cl:'블랙',qty:1,p:45000}];
  const sub=items.reduce((s,i)=>s+i.p*i.qty,0);
  document.getElementById('pitems').innerHTML=items.map(i=>`
    <div class="osi"><div class="osimg">${i.ic}</div><div style="flex:1;"><div style="font-size:13px;margin-bottom:2px;">${i.n}</div><div style="font-size:11px;color:var(--t3);">${i.sz} · ${i.cl} · ${i.qty}개</div></div><div style="font-size:13px;font-weight:700;color:var(--red);">₩${(i.p*i.qty).toLocaleString()}</div></div>`).join('');
  document.getElementById('ptotals').innerHTML=`
    <div class="srow"><span class="sl2" style="font-size:13px;">상품금액</span><span>₩${sub.toLocaleString()}</span></div>
    <div class="srow"><span class="sl2" style="font-size:13px;">배송비</span><span>₩3,000</span></div>
    <div class="sdiv"></div>
    <div class="stot"><span>총 결제금액</span><span class="sv">₩${(sub+3000).toLocaleString()}</span></div>`;
  if(currentUser){ const pp=document.getElementById('ppt'); if(pp) pp.textContent=(currentUser.point||0)+' P'; }
}
function selPay(btn){ document.querySelectorAll('#pmethods .pmb').forEach(b=>b.classList.remove('on')); btn.classList.add('on'); }
function usePoint(){ if(!currentUser){toast('로그인이 필요합니다');return;} const p=parseInt(document.getElementById('puse').value)||0; if(p%100!==0){toast('100P 단위로 입력해주세요');return;} if(p>(currentUser.point||0)){toast('보유 포인트가 부족합니다');return;} toast('✓ '+p+'P 적용되었습니다'); }
function doConfirm(){
  const method=document.querySelector('#pmethods .pmb.on')?.textContent||'카카오페이';
  const num='#'+new Date().getFullYear()+String(new Date().getMonth()+1).padStart(2,'0')+String(new Date().getDate()).padStart(2,'0')+'-'+(Math.floor(Math.random()*9000)+1000);
  const dd=new Date(); dd.setDate(dd.getDate()+3);
  document.getElementById('cdet').innerHTML=`
    <div class="crow"><span class="ck">주문번호</span><span>${num}</span></div>
    <div class="crow"><span class="ck">상품</span><span>홍길동 챔피언 기념 티셔츠 (M) ×1</span></div>
    <div class="crow"><span class="ck">결제금액</span><span style="color:var(--red);">₩48,000</span></div>
    <div class="crow"><span class="ck">결제수단</span><span>${method}</span></div>
    <div class="crow"><span class="ck">예상 배송일</span><span>${dd.getMonth()+1}월 ${dd.getDate()}일</span></div>`;
  if(currentUser){
    try{
      let us=JSON.parse(localStorage.getItem('fg_users')||'[]');
      const u=us.find(x=>x.email===currentUser.email);
      if(u){ u.orders=u.orders||[]; u.orders.unshift({num,name:'홍길동 챔피언 기념 티셔츠 (M)',price:48000,status:'배송 준비 중',date:new Date().toLocaleDateString('ko-KR')}); u.point=(u.point||0)+480; localStorage.setItem('fg_users',JSON.stringify(us)); currentUser=u; localStorage.setItem('fg_user',JSON.stringify(u)); }
    }catch(ex){}
  }
  cartItems=[]; couponApplied=false; cartDisc=0; updateCC();
  go('confirm');
}

// ── MYPAGE ──
function renderMp(){
  const av=document.getElementById('mpav'),nm=document.getElementById('mpnm'),em=document.getElementById('mpem'),pt=document.getElementById('mppt');
  if(!av) return;
  if(currentUser){ av.textContent=currentUser.nick[0]; nm.textContent=currentUser.nick; em.textContent=currentUser.email; pt.textContent='적립금: '+(currentUser.point||0)+' P'; }
  else { av.textContent='?'; nm.textContent='로그인이 필요합니다'; em.textContent=''; pt.textContent=''; }
  mpTab('orders');
}
function mpTab(t){
  ['orders','profile','delivery','withdraw'].forEach(x=>{ const e=document.getElementById('mm-'+x); if(e) e.classList.toggle('on',x===t); });
  const c=document.getElementById('mpc'); if(!c) return;
  if(!currentUser){ c.innerHTML='<div style="text-align:center;padding:56px;color:var(--t3);"><div style="font-size:40px;margin-bottom:14px;">🔐</div><div style="margin-bottom:14px;">로그인 후 이용 가능합니다</div><button class="br" onclick="openAuth('login')">로그인</button></div>'; return; }
  if(t==='orders'){
    const ords=currentUser.orders||[];
    c.innerHTML='<div style="font-family:'Bebas Neue',sans-serif;font-size:22px;letter-spacing:1px;margin-bottom:18px;">구매 내역</div>'+(ords.length?ords.map(o=>`
      <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:12px;padding:18px 22px;margin-bottom:11px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:11px;padding-bottom:11px;border-bottom:1px solid var(--bd);">
          <div style="font-size:12px;color:var(--t3);">${o.num} · ${o.date}</div>
          <span style="font-size:12px;font-weight:700;padding:3px 9px;border-radius:6px;background:rgba(230,57,70,.15);color:var(--red);">${o.status}</span>
        </div>
        <div style="display:flex;gap:12px;align-items:center;">
          <div style="width:56px;height:56px;border-radius:8px;background:var(--bg4);display:flex;align-items:center;justify-content:center;font-size:26px;">👕</div>
          <div style="flex:1;"><div style="font-size:14px;font-weight:500;margin-bottom:3px;">${o.name}</div><div style="font-size:11px;color:var(--t3);">1개</div></div>
          <div style="font-size:14px;font-weight:700;color:var(--red);">₩${o.price.toLocaleString()}</div>
        </div>
        <div style="display:flex;gap:7px;margin-top:12px;">
          <button class="bo sm" onclick="toast('배송 조회')">배송 조회</button>
          <button class="bo sm" onclick="toast('교환/반품 신청 접수됨')">교환/반품</button>
          <button style="padding:9px 14px;border-radius:8px;background:transparent;color:var(--red);font-size:13px;border:1px solid var(--red);cursor:pointer;font-family:inherit;" onclick="this.closest('div[style]').remove();toast('주문이 취소되었습니다')">주문 취소</button>
        </div>
      </div>`).join(''):'<div style="text-align:center;padding:40px;color:var(--t3);"><div style="font-size:36px;margin-bottom:10px;">📦</div>구매 내역이 없습니다</div>');
  } else if(t==='profile'){
    c.innerHTML=`<div style="font-family:'Bebas Neue',sans-serif;font-size:22px;letter-spacing:1px;margin-bottom:18px;">정보 수정</div>
      <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:26px;max-width:460px;">
        <div class="fg"><div class="fl">닉네임</div><input class="fi" id="enick" value="${currentUser.nick}"></div>
        <div class="fg"><div class="fl">이메일</div><input class="fi" value="${currentUser.email}" disabled style="opacity:.5;"></div>
        <button class="br" style="margin-top:6px;" onclick="savePrf()">저장</button>
      </div>`;
  } else if(t==='delivery'){
    c.innerHTML=`<div style="font-family:'Bebas Neue',sans-serif;font-size:22px;letter-spacing:1px;margin-bottom:18px;">배송 조회</div>
      <div style="background:var(--bg3);border:1px solid var(--bd);border-radius:14px;padding:26px;max-width:460px;">
        <div class="fg"><div class="fl">운송장 번호</div><div style="display:flex;gap:8px;"><input class="fi" id="trk" placeholder="운송장 번호 입력"><button class="cbtn" onclick="trackDel()">조회</button></div></div>
        <div id="trres"></div>
      </div>`;
  } else if(t==='withdraw'){
    c.innerHTML=`<div style="font-family:'Bebas Neue',sans-serif;font-size:22px;letter-spacing:1px;margin-bottom:18px;">계정 탈퇴</div>
      <div style="background:var(--bg3);border:1px solid rgba(230,57,70,.3);border-radius:14px;padding:26px;max-width:460px;">
        <div style="font-size:14px;color:var(--t2);line-height:1.8;margin-bottom:18px;">탈퇴 시 모든 구매 내역 및 적립금이 삭제됩니다.</div>
        <select style="width:100%;padding:10px 13px;background:var(--bg4);border:1px solid var(--bd2);border-radius:8px;color:var(--t);font-size:13px;font-family:inherit;margin-bottom:14px;outline:none;"><option>서비스 불만족</option><option>개인정보 우려</option><option>이용 빈도 낮음</option><option>기타</option></select>
        <button class="bo full" style="border-color:var(--red);color:var(--red);" onclick="doWtdr()">탈퇴하기</button>
      </div>`;
  }
}
function savePrf(){
  const n=document.getElementById('enick').value.trim();
  if(!n||n.length<2){toast('올바른 닉네임을 입력해주세요');return;}
  try{ let us=JSON.parse(localStorage.getItem('fg_users')||'[]'); const u=us.find(x=>x.email===currentUser.email); if(u){u.nick=n;localStorage.setItem('fg_users',JSON.stringify(us));} currentUser.nick=n; localStorage.setItem('fg_user',JSON.stringify(currentUser)); renderNav(); renderMp(); toast('✓ 정보가 수정되었습니다'); }catch(ex){toast('오류가 발생했습니다');}
}
function trackDel(){
  const n=document.getElementById('trk').value.trim(); if(!n){toast('운송장 번호를 입력해주세요');return;}
  document.getElementById('trres').innerHTML=`<div style="margin-top:14px;"><div style="font-size:13px;font-weight:700;margin-bottom:10px;color:var(--gl);">CJ대한통운 · ${n}</div>${['집화 완료','간선 이동 중','배송 출발','배송 완료'].map((s,i)=>`<div style="display:flex;gap:11px;align-items:center;padding:7px 0;border-bottom:1px solid var(--bd);"><div style="width:9px;height:9px;border-radius:50%;background:${i<3?'var(--red)':'var(--bd2)'};flex-shrink:0;"></div><span style="font-size:13px;${i>=3?'color:var(--t3);':''}">${s}</span>${i<3?`<span style="font-size:11px;color:var(--t3);margin-left:auto;">2025.05.${17+i}</span>`:''}</div>`).join('')}</div>`;
}
function doWtdr(){
  if(!confirm('정말 탈퇴하시겠습니까?')) return;
  try{ let us=JSON.parse(localStorage.getItem('fg_users')||'[]'); us=us.filter(u=>u.email!==currentUser.email); localStorage.setItem('fg_users',JSON.stringify(us)); }catch(ex){}
  doLogout(); toast('탈퇴가 처리되었습니다');
}

// ── SEARCH ──
const SDATA=[...PRODS.map(p=>({l:p.n,pg:'product',t:'상품'})),...FIGHTERS.map(f=>({l:f.n,pg:'fighter-detail',t:'선수'}))];
function srch(v){
  const dd=document.getElementById('sdd');
  if(!v.trim()){dd.classList.remove('on');return;}
  const res=SDATA.filter(d=>d.l.includes(v)).slice(0,7);
  if(!res.length){dd.classList.remove('on');return;}
  dd.innerHTML=res.map(r=>`<div class="si" onclick="goSrch('${r.pg}')"><span style="font-size:10px;color:var(--t3);margin-right:7px;">${r.t}</span>${r.l}</div>`).join('');
  dd.classList.add('on');
}
function goSrch(pg){ document.getElementById('si').value=''; closeSrch(); go(pg); }
function closeSrch(){ document.getElementById('sdd').classList.remove('on'); }

// ── CALENDAR ──
function renderCal(){
  const ml=document.getElementById('cml'); if(ml) ml.textContent=calY+'년 '+(calM+1)+'월';
  const g=document.getElementById('cg'); if(!g) return;
  const days=['일','월','화','수','목','금','토'];
  let h=days.map(d=>`<div style="text-align:center;padding:7px;font-size:11px;color:var(--t3);font-weight:700;">${d}</div>`).join('');
  const first=new Date(calY,calM,1).getDay(),tot=new Date(calY,calM+1,0).getDate();
  for(let i=0;i<first;i++) h+='<div></div>';
  for(let d=1;d<=tot;d++){
    const k=calY+'-'+(calM+1)+'-'+d,ev=CEVENTS[k];
    h+=`<div class="cal-cell ${ev?'ev':''}" ${ev?`onclick="toast('${ev} 알림 신청됨')"`:''}><div class="cal-d">${d}</div>${ev?`<div class="cal-e">${ev}</div>`:''}</div>`;
  }
  g.innerHTML=h;
}
function calM2(d){ calM+=d; if(calM<0){calM=11;calY--;} if(calM>11){calM=0;calY++;} renderCal(); }
function calM(d){ calM2(d); }
function schTab(t){
  ['cal','res','pre','hi'].forEach(x=>{ const e=document.getElementById('st-'+x); if(e) e.style.display=x===t?'block':'none'; });
}

// ── COMMUNITY ──
let postSortR=true;
function renderPosts(list){
  const el=document.getElementById('posts'); if(!el) return;
  el.innerHTML=(list||posts).map(p=>`
    <div class="board-post">
      <div style="font-size:15px;font-weight:500;margin-bottom:5px;">${p.t}</div>
      <div style="font-size:13px;color:var(--t3);margin-bottom:11px;line-height:1.6;">${p.b}</div>
      <div style="display:flex;align-items:center;gap:14px;font-size:12px;color:var(--t3);">
        <span>${p.a}</span><span>${p.tm}</span>
        <span style="margin-left:auto;display:flex;gap:11px;">
          <button onclick="likeP(event,${p.id})" style="background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;font-family:inherit;">❤️ ${p.l}</button>
          <span>💬 ${p.cm}</span>
        </span>
      </div>
    </div>`).join('');
}
function likeP(e,id){ e.stopPropagation(); if(!currentUser){toast('로그인이 필요합니다');return;} const p=posts.find(x=>x.id===id); if(p){p.l++;renderPosts();} }
function toggleWrite(){ if(!currentUser){openAuth('login');toast('로그인이 필요합니다');return;} const f=document.getElementById('wf'); f.style.display=f.style.display==='none'?'block':'none'; }
function submitPost(){
  const t=document.getElementById('wt').value.trim(),b=document.getElementById('wb').value.trim();
  if(!t){toast('제목을 입력해주세요');return;}
  posts.unshift({id:nxtPid++,t,b:b||'내용 없음',a:currentUser?.nick||'익명',l:0,cm:0,tm:'방금'});
  renderPosts(); document.getElementById('wt').value=''; document.getElementById('wb').value=''; document.getElementById('wf').style.display='none'; toast('✓ 게시글이 등록되었습니다');
}
function sortP(type,btn){ chipOn(btn,'#p-community .chip'); const s=[...posts].sort((a,b)=>type==='l'?b.l-a.l:b.id-a.id); renderPosts(s); }
function renderVote(){
  const tot=VOTES.reduce((s,v)=>s+v.v,0);
  document.getElementById('votearea').innerHTML=VOTES.map((v,i)=>{
    const pct=Math.round(v.v/tot*100);
    return`<div onclick="castVote(${i})" style="margin-bottom:9px;cursor:pointer;"><div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:4px;"><span>${v.l}</span><span id="vp${i}">${pct}%</span></div><div style="height:5px;background:var(--bg4);border-radius:3px;overflow:hidden;"><div id="vb${i}" style="height:100%;width:${pct}%;background:${i===0?'var(--red)':'var(--bd2)'};border-radius:3px;transition:width .4s;"></div></div></div>`;
  }).join('');
}
function castVote(idx){
  if(!currentUser){openAuth('login');toast('로그인이 필요합니다');return;}
  if(voted){toast('이미 투표하셨습니다');return;}
  voted=true; VOTES[idx].v+=5;
  const tot=VOTES.reduce((s,v)=>s+v.v,0);
  VOTES.forEach((v,i)=>{ const p=Math.round(v.v/tot*100); const vp=document.getElementById('vp'+i),vb=document.getElementById('vb'+i); if(vp) vp.textContent=p+'%'; if(vb){vb.style.width=p+'%';vb.style.background=i===idx?'var(--red)':'var(--bd2)';} });
  toast('✓ 투표 완료! (+50P)');
}
function predict(n){
  if(!currentUser){openAuth('login');toast('로그인이 필요합니다');return;}
  if(predicted){toast('이미 예측하셨습니다');return;}
  predicted=true;
  document.getElementById('pa').classList.toggle('on',n==='홍길동');
  document.getElementById('pb').classList.toggle('on',n==='볼코노프스키');
  toast('✓ '+n+' 승 예측 완료! (+100P)');
}

// ── FAQ ──
function renderFaq(data){
  const el=document.getElementById('fql'); if(!el) return;
  el.innerHTML=data.map((f,i)=>`<div class="faq-item"><div class="faq-q" onclick="toggleFaq(${i})"><span>[${f.c}] ${f.q}</span><span class="fch" id="fc${i}">▼</span></div><div class="faq-a" id="fa${i}">${f.a}</div></div>`).join('');
}
function toggleFaq(i){ document.getElementById('fa'+i).classList.toggle('on'); document.getElementById('fc'+i).classList.toggle('on'); }
function filterFaq(){
  const v=(document.getElementById('fqs')||{}).value||'';
  const ac=document.querySelector('#fqcats .chip.on'); const cat=ac?ac.dataset.c:'전체';
  renderFaq(FAQS.filter(f=>(cat==='전체'||f.c===cat)&&(!v||f.q.includes(v)||f.a.includes(v))));
}

// ── RECENT VIEWED ──
function addRV(p){
  recentViewed=recentViewed.filter(x=>x.id!==p.id); recentViewed.unshift(p); if(recentViewed.length>10) recentViewed.pop();
  const el=document.getElementById('rv'); if(!el) return;
  el.innerHTML='<div style="display:flex;gap:14px;overflow-x:auto;padding-bottom:6px;">'+recentViewed.map(x=>`<div onclick="go('product')" style="flex-shrink:0;width:130px;cursor:pointer;"><div style="height:130px;background:linear-gradient(135deg,#1e1e2e,#2a1e2a);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:44px;border:1px solid var(--bd);margin-bottom:7px;">${x.ic}</div><div style="font-size:12px;margin-bottom:3px;">${x.n}</div><div style="font-size:13px;font-weight:700;color:var(--red);">₩${x.p.toLocaleString()}</div></div>`).join('')+'</div>';
}

// ── INIT ──
loadAuth();
renderProds('hpg',PRODS);
document.getElementById('hfg').innerHTML=FIGHTERS.map(fighterHTML).join('');
renderFighters(FIGHTERS);
renderRank();
renderCal();
renderFaq(FAQS);
renderPosts();
renderVote();
</script>
</body>
</html>