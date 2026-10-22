





import base64
from pathlib import Path

import streamlit as st

portrait_image = base64.b64encode(
    (Path(__file__).parent / 'ing' / 'IMG_3240.jpeg').read_bytes()
).decode('ascii')

st.set_page_config(
    page_title='김하은 | 나를 소개합니다',
    page_icon='💜',
    layout='wide',
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Outfit:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #352b46;
        --muted: #756b83;
        --line: rgba(111, 83, 146, 0.16);
    }
    .stApp {
        background:
            radial-gradient(ellipse at 8% 5%, rgba(255,255,255,.88), transparent 35%),
            radial-gradient(ellipse at 92% 24%, rgba(231,199,246,.72), transparent 34%),
            linear-gradient(135deg, #eee5ff 0%, #f8e8f3 52%, #e6e4ff 100%);
        color: var(--ink);
        font-family: 'Gowun Dodum', sans-serif;
    }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { max-width: 1080px; padding: 2.2rem 1.5rem 4rem; }
    [data-testid="stMarkdownContainer"] { color: var(--ink); }
    .topline {
        display:flex; justify-content:space-between; align-items:center;
        padding-bottom:1.15rem; border-bottom:1px solid var(--line);
        color:var(--muted); font-family:'Outfit',sans-serif; font-size:.84rem;
    }
    .topline strong { color:var(--ink); }
    .hero { display:grid; grid-template-columns:1.25fr .75fr; gap:2rem; align-items:center; padding:3.5rem 0 2.8rem; }
    .eyebrow {
        display:inline-block; margin-bottom:1.15rem; padding:.42rem .8rem;
        border:1px solid rgba(140,105,197,.24); border-radius:999px;
        background:rgba(255,255,255,.48); color:#73529e;
        font-family:'Outfit',sans-serif; font-size:.76rem; font-weight:600;
    }
    h1 { margin:0; color:#342744; font-size:clamp(2.7rem,7vw,5rem); line-height:1.12; font-weight:700; }
    h1 span { color:#8b68bb; }
    .hero-copy { max-width:540px; margin:1.25rem 0 1.6rem; color:#625770; font-size:1.08rem; line-height:1.9; }
    .hero-tags { display:flex; flex-wrap:wrap; gap:.55rem; }
    .hero-tags span { padding:.48rem .76rem; border-radius:8px; background:rgba(255,255,255,.62); color:#5c4a70; font-size:.86rem; }
    .portrait {
        position:relative; overflow:hidden; min-height:310px; border-radius:18px;
        border:1px solid rgba(255,255,255,.8);
        background:linear-gradient(145deg,#d9c2f1,#f3d7e9 58%,#c9c7f5);
        box-shadow:0 22px 55px rgba(83,58,116,.15);
    }
    .portrait img { position:absolute; inset:0; box-sizing:border-box; width:100%; height:100%; padding:1rem; object-fit:contain; }
    .portrait-label {
        position:absolute; right:1rem; bottom:1rem; padding:.65rem .9rem;
        border-radius:10px; background:rgba(255,255,255,.82); color:#58436f;
        font-family:'Outfit',sans-serif; font-weight:700;
    }
    .closing-kuromi { display:inline-block; margin-left:.35rem; font-size:.85rem; vertical-align:middle; }
    .section-head {
        display:flex; align-items:end; justify-content:space-between; gap:1rem;
        margin:2.2rem 0 1.1rem; padding-bottom:.8rem; border-bottom:1px solid var(--line);
    }
    .section-head h2 { margin:0; color:#3b2d4d; font-size:1.55rem; }
    .section-head p { margin:0; color:var(--muted); font-size:.88rem; }
    .info-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1rem; }
    .info-card {
        min-height:170px; padding:1.2rem 1.25rem; border:1px solid rgba(255,255,255,.8);
        border-radius:12px; background:rgba(255,255,255,.55);
    }
    .info-card .label { color:#9476b2; font-family:'Outfit',sans-serif; font-size:.78rem; font-weight:700; }
    .info-card h3 { margin:.65rem 0 .45rem; color:#3b2d4d; font-size:1.13rem; }
    .info-card p { margin:0; color:#6e6379; font-size:.91rem; line-height:1.7; }
    .career {
        display:grid; grid-template-columns:.85fr 1.15fr; gap:1.5rem; padding:1.5rem;
        border-radius:14px; background:linear-gradient(115deg,rgba(122,89,165,.95),rgba(167,117,171,.93)); color:#fff;
    }
    .career h2 { margin:.25rem 0 .65rem; color:#fff; font-size:1.45rem; }
    .career p { margin:0; color:rgba(255,255,255,.86); line-height:1.8; }
    .career .label { color:#f3dafa; font-family:'Outfit',sans-serif; font-size:.75rem; font-weight:700; }
    .steps { display:grid; grid-template-columns:repeat(3,1fr); gap:.7rem; }
    .step { padding:.95rem; border:1px solid rgba(255,255,255,.24); border-radius:9px; background:rgba(255,255,255,.1); }
    .step b { display:block; margin-bottom:.4rem; color:#fff; font-size:.92rem; }
    .step span { color:rgba(255,255,255,.8); font-size:.82rem; line-height:1.6; }
    .interests { display:flex; flex-wrap:wrap; gap:.7rem; }
    .interest { padding:.7rem 1rem; border:1px solid rgba(255,255,255,.85); border-radius:9px; background:rgba(255,255,255,.55); color:#5d4c70; font-size:.92rem; }
    .closing { margin-top:2.5rem; padding:1.3rem; border-top:1px solid var(--line); color:#776982; text-align:center; font-size:.94rem; line-height:1.8; }
    .closing strong { color:#72539a; }
    @media (max-width:720px) {
        .block-container { padding:1.4rem 1rem 2.5rem; }
        .hero { grid-template-columns:1fr; gap:1.5rem; padding:2.5rem 0 1.6rem; }
        .portrait { min-height:250px; }
        .info-grid, .career { grid-template-columns:1fr; }
        .info-card { min-height:auto; }
        .steps { grid-template-columns:1fr; }
        .section-head { align-items:start; flex-direction:column; gap:.3rem; }
    }
    </style>

    <div class="topline"><strong>HAEUN'S NOTEBOOK</strong><span>MY INTRODUCTION &nbsp; / &nbsp; 2026</span></div>
    <section class="hero">
      <div>
        <span class="eyebrow">IT STUDENT · FUTURE SECURITY EXPERT</span>
        <h1>안녕하세요,<br /><span>김하은</span>입니다.</h1>
        <p class="hero-copy">새로운 것을 배우고 나만의 가능성을 키워가는<br />경복비즈니스학교 IT과 3학년 김하은입니다.</p>
        <div class="hero-tags"><span>경복비즈니스학교</span><span>IT과 3학년</span><span>정보보안</span></div>
      </div>
      <div class="portrait">
                <img src="data:image/jpeg;base64,IMAGE_DATA" alt="김하은 사진" />
                <span class="portrait-label">♡ HAEUN</span>
      </div>
    </section>

    <div class="section-head"><h2>About me</h2><p>제가 좋아하는 것, 그리고 소중하게 생각하는 것</p></div>
    <section class="info-grid">
      <article class="info-card"><span class="label">01 / SCHOOL</span><h3>배움으로 한 걸음씩</h3><p>경복비즈니스학교 IT과 3학년으로, IT 분야의 지식과 실무 역량을 차근차근 쌓고 있어요.</p></article>
      <article class="info-card"><span class="label">02 / MY TIME</span><h3>친구와 수다, OTT 한 편</h3><p>친구들과 통화하며 이야기 나누기, 좋아하는 콘텐츠를 보며 쉬는 시간이 큰 즐거움이에요.</p></article>
      <article class="info-card"><span class="label">03 / MY WAY</span><h3>꾸준히 배우고 성장하기</h3><p>작은 경험도 배움으로 만들고, 제가 세운 목표를 직접 현실로 만들어가는 사람이 되고 싶어요.</p></article>
    </section>

    <div class="section-head"><h2>My future</h2><p>꿈을 계획으로, 계획을 나만의 기업으로</p></div>
    <section class="career">
      <div><span class="label">MY CAREER GOAL</span><h2>정보보안 전문가</h2><p>프리랜서로 다양한 경험과 신뢰를 쌓고, 개인사업을 성장시켜 언젠가는 나만의 기업을 만드는 것이 목표예요.</p></div>
      <div class="steps">
        <div class="step"><b>01 · 실력 쌓기</b><span>보안 기초와 전문 지식을 꾸준히 익히기</span></div>
        <div class="step"><b>02 · 경험 넓히기</b><span>프리랜서 활동으로 프로젝트 경험 만들기</span></div>
        <div class="step"><b>03 · 꿈 키우기</b><span>개인사업을 성장시켜 나만의 기업 세우기</span></div>
      </div>
    </section>

    <div class="section-head"><h2>Things I like</h2><p>하은이를 기분 좋게 만드는 것들</p></div>
    <div class="interests"><span class="interest">친구들과 통화하기</span><span class="interest">OTT 시청하기</span><span class="interest">쿠로미</span><span class="interest">IT와 정보보안 알아가기</span></div>
    <div class="closing"><strong>“꾸준히 배우고, 직접 도전하며, 신뢰받는 보안 전문가로 성장하기.”</strong><span class="closing-kuromi" aria-label="쿠로미">😈💜</span><br />저의 꿈을 향해 오늘도 한 걸음씩 나아가고 있습니다. 반가워요!</div>
    """.replace('IMAGE_DATA', portrait_image),
    unsafe_allow_html=True,
)
