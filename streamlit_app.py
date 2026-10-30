import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="김하은 | 취업 포트폴리오",
    page_icon="💜",
    layout="wide",
)

sections = {
    "자기소개": "about",
    "아르바이트": "experience",
    "동아리": "club",
    "수상경력": "awards",
    "학생회": "student-council",
    "생활기록부": "core-profile",
}
selected_section = st.sidebar.radio("포트폴리오", sections, label_visibility="collapsed")

APP_DIR = Path(__file__).parent
html = (APP_DIR / "index.html").read_text(encoding="utf-8")
profile_image = base64.b64encode((APP_DIR / "ing" / "IMG_3586.jpeg").read_bytes()).decode("ascii")
html = html.replace("ing/IMG_3586.jpeg", f"data:image/jpeg;base64,{profile_image}")
styles = (APP_DIR / "styles.css").read_text(encoding="utf-8")
script = (APP_DIR / "script.js").read_text(encoding="utf-8")

stylesheet_link = '<link rel="stylesheet" href="styles.css">'
script_link = '<script src="script.js" defer></script>'
site_url_assignment = "siteUrl.href = window.location.href.split('#')[0];"
if html.count(stylesheet_link) != 1 or html.count(script_link) != 1:
    raise RuntimeError("Could not find the portfolio stylesheet and script references in index.html.")
if script.count(site_url_assignment) != 1:
    raise RuntimeError("Could not find the portfolio URL assignment in script.js.")

html = html.replace(stylesheet_link, f"<style>{styles}</style>")
html = html.replace(script_link, "")
html = html.replace('<body class="has-portfolio-sidebar">', f'<body data-active-section="{sections[selected_section]}">')
html = html.replace(
    "</head>",
    """<style>
    body[data-active-section] #highschool-portfolio > .tab-panel { display: none !important; }
    body[data-active-section] #highschool-portfolio > #core-profile { display: none !important; }
    body[data-active-section="about"] #highschool-portfolio > #about,
    body[data-active-section="experience"] #highschool-portfolio > #experience,
    body[data-active-section="awards"] #highschool-portfolio > #awards { display: block !important; }
    body[data-active-section="club"] #highschool-portfolio > #activities,
    body[data-active-section="student-council"] #highschool-portfolio > #activities { display: block !important; }
    body[data-active-section="club"] #activities .activity-feature:not(#club),
    body[data-active-section="student-council"] #activities .activity-feature:not(#student-council) { display: none !important; }
    body[data-active-section="core-profile"] #highschool-portfolio > #core-profile { display: block !important; }
    </style></head>""",
)
script = script.replace(
    site_url_assignment,
    "siteUrl.href = window.parent.location.href.split('#')[0];",
)
html = html.replace("</body>", f"<script>{script}</script></body>")

st.markdown(
    """
    <style>
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none; }
    [data-testid="stMainBlockContainer"] { max-width: none; padding: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)
st.iframe(html, width="stretch", height="content", alt="김하은 취업 포트폴리오")
