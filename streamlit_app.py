from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).parent
html = (APP_DIR / "index.html").read_text(encoding="utf-8")
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
script = script.replace(
    site_url_assignment,
    "siteUrl.href = window.parent.location.href.split('#')[0];",
)
html = html.replace("</body>", f"<script>{script}</script></body>")

st.set_page_config(
    page_title="김하은 | 취업 포트폴리오",
    page_icon="💜",
    layout="wide",
)
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
