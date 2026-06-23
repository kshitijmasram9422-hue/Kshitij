import streamlit as st
import time
# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Kshitij Masram | Biotech Professional",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed",
)
# ─── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');
/* ── Root & Body ── */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
    background-color: #050b14;
    color: #f0f6ff;
}
.stApp {
    background: linear-gradient(135deg, #050b14 0%, #0a1628 50%, #080f1e 100%);
    background-attachment: fixed;
}
/* Hide Streamlit default header/footer/menu */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2rem 4rem 2rem !important; max-width: 1100px; }
/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a1628; }
::-webkit-scrollbar-thumb { background: #00d4ff55; border-radius: 3px; }
/* ─── HERO ─────────────────────────────────────────────────────────────────── */
.hero-section {
    min-height: 95vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 6rem 0 3rem 0;
    position: relative;
    overflow: hidden;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.35);
    color: #10b981;
    padding: 0.45rem 1.1rem;
    border-radius: 100px;
    font-size: 0.88rem;
    font-weight: 600;
    margin-bottom: 1.8rem;
    animation: fadeInDown 0.8s ease forwards;
    letter-spacing: 0.02em;
}
.badge-dot {
    width: 8px; height: 8px;
    background: #10b981;
    border-radius: 50%;
    display: inline-block;
    animation: blink 1.5s ease-in-out infinite;
}
.hero-title {
    font-size: clamp(3rem, 6vw, 5.5rem);
    font-weight: 900;
    line-height: 1.05;
    margin-bottom: 1rem;
    letter-spacing: -0.02em;
}
.gradient-text {
    background: linear-gradient(135deg, #00d4ff 0%, #7c3aed 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-subtitle {
    font-size: 1.1rem;
    color: #8899bb;
    margin-bottom: 1.5rem;
    font-weight: 400;
}
.hero-subtitle span {
    color: #00d4ff;
    font-weight: 600;
}
.hero-description {
    font-size: 1.08rem;
    color: #7a8ba8;
    max-width: 580px;
    line-height: 1.85;
    margin-bottom: 2.5rem;
}
/* Hero Stats */
.hero-stats {
    display: flex;
    align-items: center;
    gap: 2.5rem;
    padding: 1.5rem 2rem;
    background: rgba(15, 30, 53, 0.6);
    border: 1px solid rgba(0, 212, 255, 0.12);
    border-radius: 20px;
    backdrop-filter: blur(10px);
    width: fit-content;
    margin-top: 1rem;
}
.stat-item { text-align: center; }
.stat-num {
    display: block;
    font-size: 2.2rem;
    font-weight: 900;
    background: linear-gradient(135deg, #00d4ff, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
}
.stat-lbl {
    font-size: 0.75rem;
    color: #4a5a7a;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 4px;
}
.stat-div { width: 1px; height: 48px; background: rgba(0,212,255,0.15); }
/* ─── SECTIONS ─────────────────────────────────────────────────────────────── */
.section-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #00d4ff;
    letter-spacing: 0.12em;
    display: block;
    margin-bottom: 0.5rem;
}
.section-title {
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 800;
    background: linear-gradient(135deg, #00d4ff, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}
.section-divider {
    height: 3px;
    width: 60px;
    background: linear-gradient(90deg, #00d4ff, #7c3aed);
    border-radius: 2px;
    margin-bottom: 2.5rem;
}
/* ─── CARDS ─────────────────────────────────────────────────────────────────── */
.glass-card {
    background: rgba(15, 30, 53, 0.7);
    border: 1px solid rgba(0, 212, 255, 0.12);
    border-radius: 20px;
    padding: 1.75rem;
    backdrop-filter: blur(12px);
    transition: all 0.3s ease;
    height: 100%;
}
.glass-card:hover {
    border-color: rgba(0, 212, 255, 0.3);
    box-shadow: 0 8px 40px rgba(0, 212, 255, 0.12);
    transform: translateY(-4px);
}
.glass-card-purple {
    background: rgba(15, 30, 53, 0.7);
    border: 1px solid rgba(124, 58, 237, 0.2);
    border-radius: 20px;
    padding: 1.75rem;
    backdrop-filter: blur(12px);
    transition: all 0.3s ease;
}
.glass-card-purple:hover {
    border-color: rgba(124, 58, 237, 0.4);
    box-shadow: 0 8px 40px rgba(124, 58, 237, 0.15);
    transform: translateY(-4px);
}
/* ─── PROFILE CARD ───────────────────────────────────────────────────────── */
.profile-card {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    background: rgba(15, 30, 53, 0.8);
    border: 1px solid rgba(0, 212, 255, 0.15);
    border-radius: 20px;
    padding: 1.75rem;
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.3);
}
.avatar-container {
    position: relative;
    width: 80px; height: 80px;
    flex-shrink: 0;
}
.avatar-ring {
    position: absolute; inset: -3px;
    border-radius: 50%;
    background: linear-gradient(135deg, #00d4ff, #7c3aed);
    animation: rotate 4s linear infinite;
}
.avatar-inner {
    position: relative; z-index: 1;
    width: 80px; height: 80px;
    background: #0a1628;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    border: 3px solid #050b14;
    font-size: 1.6rem; font-weight: 900;
    background: linear-gradient(135deg, #00d4ff, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.profile-name {
    font-size: 1.3rem; font-weight: 800; margin-bottom: 0.2rem;
}
.profile-role { color: #00d4ff; font-size: 0.9rem; margin-bottom: 0.8rem; }
.profile-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.ptag {
    background: rgba(0, 212, 255, 0.1);
    border: 1px solid rgba(0, 212, 255, 0.2);
    color: #00d4ff;
    padding: 0.2rem 0.75rem;
    border-radius: 100px;
    font-size: 0.75rem;
    font-weight: 500;
}
/* ─── TIMELINE ───────────────────────────────────────────────────────────── */
.timeline-item {
    position: relative;
    padding-left: 2rem;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-left: 2px solid rgba(0, 212, 255, 0.2);
}
.timeline-item:last-child { border-left: 2px solid transparent; }
.timeline-dot {
    position: absolute;
    left: -9px; top: 2px;
    width: 16px; height: 16px;
    border-radius: 50%;
    background: #050b14;
    border: 3px solid #00d4ff;
    box-shadow: 0 0 12px rgba(0, 212, 255, 0.5);
    animation: dotGlow 2s ease-in-out infinite;
}
.edu-badge {
    display: inline-block;
    background: linear-gradient(135deg, #00d4ff, #7c3aed);
    color: #050b14;
    font-size: 0.7rem; font-weight: 700;
    padding: 0.18rem 0.7rem;
    border-radius: 100px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.6rem;
}
.edu-degree { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.15rem; }
.edu-inst { color: #00d4ff; font-size: 0.85rem; margin-bottom: 0.7rem; }
.edu-desc { color: #7a8ba8; font-size: 0.88rem; line-height: 1.7; margin-bottom: 0.9rem; }
.subject-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.stag {
    background: rgba(124, 58, 237, 0.12);
    border: 1px solid rgba(124, 58, 237, 0.25);
    color: #a78bfa;
    padding: 0.2rem 0.75rem;
    border-radius: 100px;
    font-size: 0.75rem;
}
/* ─── SKILL BARS ─────────────────────────────────────────────────────────── */
.skill-bar-wrap { margin-bottom: 1.1rem; }
.skill-bar-header {
    display: flex; justify-content: space-between;
    align-items: center; margin-bottom: 0.4rem;
    font-size: 0.88rem;
}
.skill-bar-name { color: #c8d8f0; font-weight: 500; }
.skill-bar-pct {
    color: #00d4ff; font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
}
.skill-bar-track {
    height: 7px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 100px;
    overflow: hidden;
}
.skill-bar-fill {
    height: 100%;
    border-radius: 100px;
    background: linear-gradient(90deg, #00d4ff, #7c3aed);
    transition: width 1.2s ease;
    position: relative;
}
.skill-bar-fill::after {
    content: '';
    position: absolute;
    right: 0; top: 50%;
    transform: translateY(-50%);
    width: 8px; height: 8px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 8px #00d4ff;
}
.fill-green { background: linear-gradient(90deg, #10b981, #00d4ff) !important; }
/* ─── FOCUS CARDS ────────────────────────────────────────────────────────── */
.focus-card {
    background: rgba(15, 30, 53, 0.7);
    border: 1px solid rgba(0, 212, 255, 0.1);
    border-radius: 16px;
    padding: 1.4rem;
    text-align: center;
    transition: all 0.3s ease;
    cursor: default;
    height: 100%;
}
.focus-card:hover {
    border-color: rgba(0, 212, 255, 0.3);
    transform: translateY(-6px);
    box-shadow: 0 12px 40px rgba(0, 212, 255, 0.12);
}
.focus-icon { font-size: 2.2rem; margin-bottom: 0.7rem; }
.focus-title { font-size: 0.95rem; font-weight: 700; margin-bottom: 0.4rem; }
.focus-desc { font-size: 0.8rem; color: #7a8ba8; line-height: 1.6; }
/* ─── LANGUAGE CARDS ─────────────────────────────────────────────────────── */
.lang-flag { font-size: 2.5rem; margin-bottom: 0.6rem; }
.lang-name { font-size: 1.2rem; font-weight: 700; margin-bottom: 0.2rem; }
.lang-level { color: #00d4ff; font-size: 0.85rem; margin-bottom: 1.2rem; }
.lang-tag {
    background: rgba(0, 212, 255, 0.08);
    border: 1px solid rgba(0, 212, 255, 0.15);
    color: #00d4ff;
    padding: 0.2rem 0.7rem;
    border-radius: 100px;
    font-size: 0.72rem;
    display: inline-block;
    margin: 0.2rem;
}
/* German progress ring */
.progress-ring-wrap {
    display: flex; flex-direction: column;
    align-items: center; padding: 1rem 0;
}
.ring-container { position: relative; width: 130px; height: 130px; }
.ring-svg { transform: rotate(-90deg); }
.ring-label {
    position: absolute; inset: 0;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
}
.ring-pct { font-size: 1.6rem; font-weight: 900; color: #00d4ff; line-height: 1; }
.ring-sub { font-size: 0.65rem; color: #4a5a7a; margin-top: 2px; }
/* Native badge */
.native-badge {
    background: rgba(245, 158, 11, 0.08);
    border: 1px solid rgba(245, 158, 11, 0.2);
    border-radius: 12px;
    padding: 0.8rem;
    text-align: center;
    margin-bottom: 1rem;
}
.native-stars { color: #f59e0b; font-size: 1.2rem; letter-spacing: 0.1em; }
/* ─── INTEREST NODES ─────────────────────────────────────────────────────── */
.interest-node {
    display: inline-block;
    background: rgba(15, 30, 53, 0.7);
    border: 1px solid rgba(0, 212, 255, 0.2);
    color: #c8d8f0;
    padding: 0.55rem 1.1rem;
    border-radius: 100px;
    font-size: 0.88rem;
    font-weight: 500;
    margin: 0.35rem;
    transition: all 0.3s ease;
    cursor: default;
}
.interest-node:hover {
    background: rgba(0, 212, 255, 0.1);
    border-color: #00d4ff;
    color: #00d4ff;
    transform: scale(1.06);
}
/* ─── STRENGTH CARDS ─────────────────────────────────────────────────────── */
.strength-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    background: rgba(15, 30, 53, 0.7);
    border: 1px solid rgba(0, 212, 255, 0.1);
    border-radius: 16px;
    padding: 1.25rem;
    transition: all 0.3s ease;
    margin-bottom: 1rem;
}
.strength-item:hover {
    border-color: rgba(0, 212, 255, 0.3);
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(0, 212, 255, 0.1);
}
.str-icon { font-size: 1.6rem; flex-shrink: 0; }
.str-title { font-size: 0.95rem; font-weight: 700; margin-bottom: 0.3rem; }
.str-desc { font-size: 0.82rem; color: #7a8ba8; line-height: 1.6; }
/* ─── CONTACT ────────────────────────────────────────────────────────────── */
.contact-info-item {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    padding: 0.85rem 1.1rem;
    background: rgba(15, 30, 53, 0.6);
    border: 1px solid rgba(0, 212, 255, 0.1);
    border-radius: 12px;
    margin-bottom: 0.8rem;
    font-size: 0.9rem;
    color: #8899bb;
    transition: all 0.3s ease;
}
.contact-info-item:hover {
    border-color: rgba(0, 212, 255, 0.3);
    color: #c8d8f0;
}
.contact-icon { font-size: 1.2rem; }
/* ─── FORM STYLING ───────────────────────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: rgba(15, 30, 53, 0.8) !important;
    border: 1px solid rgba(0, 212, 255, 0.2) !important;
    border-radius: 10px !important;
    color: #f0f6ff !important;
    font-family: 'Outfit', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #00d4ff !important;
    box-shadow: 0 0 0 3px rgba(0, 212, 255, 0.08) !important;
}
.stTextInput label, .stTextArea label {
    color: #8899bb !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
.stButton > button {
    background: linear-gradient(135deg, #00d4ff, #7c3aed) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.7rem 2rem !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    font-family: 'Outfit', sans-serif !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 20px rgba(0, 212, 255, 0.25) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(0, 212, 255, 0.4) !important;
}
/* ─── QUOTE CARD ─────────────────────────────────────────────────────────── */
.quote-card {
    background: rgba(15, 30, 53, 0.6);
    border-left: 4px solid #7c3aed;
    border-radius: 0 16px 16px 0;
    padding: 1.25rem 1.5rem;
    margin-top: 1.5rem;
}
.quote-mark { font-size: 2.5rem; color: #7c3aed; line-height: 1; opacity: 0.7; }
.quote-text { color: #8899bb; font-style: italic; line-height: 1.7; font-size: 0.95rem; }
/* ─── SECTION SEPARATOR ──────────────────────────────────────────────────── */
.section-sep {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,212,255,0.2), transparent);
    margin: 4rem 0;
}
/* ─── FOOTER ─────────────────────────────────────────────────────────────── */
.footer-wrap {
    text-align: center;
    padding: 2.5rem 0;
    border-top: 1px solid rgba(0,212,255,0.1);
    margin-top: 4rem;
}
.footer-logo {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.1rem;
    color: #c8d8f0;
    margin-bottom: 0.5rem;
}
.footer-logo span { color: #00d4ff; }
.footer-tagline { color: #4a5a7a; font-size: 0.85rem; margin-bottom: 0.3rem; }
.footer-copy { color: #2a3a5a; font-size: 0.78rem; }
/* ─── ANIMATIONS ─────────────────────────────────────────────────────────── */
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.2; }
}
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
@keyframes dotGlow {
    0%, 100% { box-shadow: 0 0 6px rgba(0,212,255,0.4); }
    50% { box-shadow: 0 0 18px rgba(0,212,255,0.8); }
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
/* ─── SIDEBAR ────────────────────────────────────────────────────────────── */
.css-1d391kg, [data-testid="stSidebar"] {
    background: rgba(10, 22, 40, 0.95) !important;
    border-right: 1px solid rgba(0,212,255,0.1) !important;
}
/* Nav pills in sidebar */
.nav-pill {
    display: block;
    padding: 0.7rem 1rem;
    border-radius: 10px;
    color: #8899bb;
    font-weight: 500;
    font-size: 0.92rem;
    text-decoration: none;
    transition: all 0.25s ease;
    margin-bottom: 0.3rem;
    cursor: pointer;
}
.nav-pill:hover, .nav-pill.active {
    background: rgba(0,212,255,0.1);
    color: #00d4ff;
    padding-left: 1.4rem;
}
/* Subject chips */
.subj-chip {
    display: inline-block;
    background: rgba(15, 30, 53, 0.8);
    border: 1px solid rgba(0,212,255,0.12);
    border-radius: 100px;
    padding: 0.5rem 1.1rem;
    font-size: 0.85rem;
    font-weight: 500;
    margin: 0.3rem;
    transition: all 0.25s ease;
    cursor: default;
}
.subj-chip:hover {
    background: rgba(0,212,255,0.08);
    border-color: #00d4ff;
    color: #00d4ff;
    transform: translateY(-2px);
}
/* ─── SUCCESS BOX ────────────────────────────────────────────────────────── */
.success-box {
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
}
.success-icon-wrap {
    width: 56px; height: 56px;
    background: linear-gradient(135deg, #10b981, #00d4ff);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    margin: 0 auto 1rem;
}
/* Streamlit selectbox customization */
.stSelectbox > div > div {
    background: rgba(15, 30, 53, 0.8) !important;
    border: 1px solid rgba(0, 212, 255, 0.2) !important;
    border-radius: 10px !important;
    color: #f0f6ff !important;
}
</style>
""", unsafe_allow_html=True)
# ─── DATA ─────────────────────────────────────────────────────────────────────
BIOTECH_SKILLS = {
    "Fermentation Technology": 90,
    "Bioprocess Engineering": 85,
    "Industrial Microbiology": 82,
    "Molecular Biology": 80,
    "Biochemical Engineering": 78,
    "Upstream Processing": 76,
    "Downstream Processing": 74,
    "Bioreactor Operations": 80,
}
TECH_SKILLS = {
    "Python Programming": 65,
    "Data Science Fundamentals": 55,
    "Process Engineering Concepts": 72,
    "Computational Biotechnology": 50,
}
INTERESTS = [
    "🧬 Industrial Biotechnology", "⚗️ Fermentation Science",
    "🫧 Bioreactor Operations", "⬆️ Upstream Processing",
    "⬇️ Downstream Processing", "📊 Process Optimisation",
    "💻 Python & Data Science", "🏭 Biotech Manufacturing",
    "🌐 IELTS Preparation", "🇩🇪 German Language",
    "🔬 Biochemical Engineering", "📐 Engineering Mathematics",
]
SUBJECTS_BSC = ["🧬 Biotechnology", "🦠 Microbiology", "⚗️ Biochemistry",
                 "🔬 Molecular Biology", "🧪 Genetics", "🔵 Cell Biology",
                 "🌡️ Thermodynamics", "💧 Chemistry"]
SUBJECTS_MSC = ["⚙️ Bioprocess Technology", "🍺 Fermentation Technology",
                 "🏭 Industrial Biotechnology", "🫧 Bioreactor Design",
                 "💊 Biochemical Engineering", "📊 Process Optimisation",
                 "🦠 Industrial Microbiology", "🔄 Downstream Processing"]
STRENGTHS = [
    ("🔍", "Scientific Curiosity",
     "Strong drive to explore industrial applications of biological sciences at scale."),
    ("🎯", "Independent Learning",
     "Self-motivated learner with consistent study habits across multiple disciplines."),
    ("⚙️", "Engineering Mindset",
     "Bridges life sciences with engineering concepts and process-oriented thinking."),
    ("🏗️", "Applied Science Focus",
     "Preference for practical, real-world industrial applications over pure theory."),
    ("📈", "Continuous Improvement",
     "Actively developing English, German, and Python alongside core biotech skills."),
]
FOCUS_AREAS = [
    ("⬆️", "Upstream Processing",
     "Media prep, inoculum development, bioreactor operations and scale-up strategies"),
    ("⬇️", "Downstream Processing",
     "Product recovery, purification methods and yield optimisation techniques"),
    ("🫧", "Bioreactor Design",
     "Stirred tank reactors, aeration, agitation systems and process control loops"),
    ("📊", "Process Optimisation",
     "Statistical tools, DOE methodology and data-driven production improvements"),
]
# ─── HELPER FUNCTIONS ─────────────────────────────────────────────────────────
def skill_bar(name: str, pct: int, green: bool = False) -> str:
    cls = "skill-bar-fill fill-green" if green else "skill-bar-fill"
    return f"""
    <div class="skill-bar-wrap">
        <div class="skill-bar-header">
            <span class="skill-bar-name">{name}</span>
            <span class="skill-bar-pct">{pct}%</span>
        </div>
        <div class="skill-bar-track">
            <div class="{cls}" style="width:{pct}%"></div>
        </div>
    </div>"""
def section_header(tag: str, title: str):
    st.markdown(f"""
    <p class="section-tag">{tag}</p>
    <h2 class="section-title">{title}</h2>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)
def section_sep():
    st.markdown('<div class="section-sep"></div>', unsafe_allow_html=True)
# ─── SIDEBAR NAVIGATION ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem 0 2rem; text-align:center;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:1.1rem;">
            <span style="color:#00d4ff;">&lt;</span>
            <span style="color:#f0f6ff;">KM</span>
            <span style="color:#00d4ff;">/&gt;</span>
        </div>
        <div style="color:#4a5a7a; font-size:0.75rem; margin-top:0.5rem;">Portfolio</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Navigate**")
    page = st.radio(
        "Navigation",
        ["🏠 Home", "👤 About", "📚 Education", "💡 Skills",
         "🌍 Languages", "🔬 Interests", "📬 Contact"],
        label_visibility="hidden",
    )
    st.markdown("---")
    st.markdown("""
    <div style="padding:1rem; background:rgba(0,212,255,0.05); border:1px solid rgba(0,212,255,0.1);
                border-radius:12px; font-size:0.82rem; color:#8899bb; line-height:1.6;">
        <div style="color:#10b981; font-weight:600; margin-bottom:0.5rem;">● Open to Opportunities</div>
        M.Sc. Biotechnology<br>
        Fermentation · Bioprocess<br>
        Python · IELTS · German
    </div>
    """, unsafe_allow_html=True)
# ─── PAGE: HOME / HERO ────────────────────────────────────────────────────────
if page == "🏠 Home":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge">
            <span class="badge-dot"></span>
            Open to Opportunities
        </div>
        <h1 class="hero-title">
            Hi, I'm <span class="gradient-text">Kshitij</span> 👋
        </h1>
        <p class="hero-subtitle">
            M.Sc. Biotechnology &nbsp;|&nbsp;
            <span>Fermentation Expert · Bioprocess Engineer · Python Learner</span>
        </p>
        <p class="hero-description">
            Passionate about harnessing biological systems at industrial scale —
            from fermentation vessels to bioprocess pipelines. Where science meets engineering.
        </p>
        <div class="hero-stats">
            <div class="stat-item">
                <span class="stat-num">2</span>
                <span class="stat-lbl">Degrees</span>
            </div>
            <div class="stat-div"></div>
            <div class="stat-item">
                <span class="stat-num">10+</span>
                <span class="stat-lbl">Core Subjects</span>
            </div>
            <div class="stat-div"></div>
            <div class="stat-item">
                <span class="stat-num">3</span>
                <span class="stat-lbl">Languages</span>
            </div>
            <div class="stat-div"></div>
            <div class="stat-item">
                <span class="stat-num">B2</span>
                <span class="stat-lbl">German Goal</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    # Quick-glance cards
    st.markdown('<p class="section-tag">// quick glance</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    cards = [
        ("🧬", "Biotechnology", "B.Sc. + M.Sc. from India", "#00d4ff"),
        ("⚗️", "Fermentation", "Industrial-scale bioprocess expertise", "#7c3aed"),
        ("🐍", "Python", "Programming & data science skills", "#10b981"),
        ("🌐", "Languages", "Hindi · English · German (A1→B2)", "#f59e0b"),
    ]
    for col, (icon, title, desc, color) in zip([c1, c2, c3, c4], cards):
        with col:
            st.markdown(f"""
            <div class="focus-card">
                <div class="focus-icon">{icon}</div>
                <div class="focus-title">{title}</div>
                <div class="focus-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
# ─── PAGE: ABOUT ──────────────────────────────────────────────────────────────
elif page == "👤 About":
    section_header("// about me", "Who Am I?")
    col_text, col_card = st.columns([1.2, 0.8], gap="large")
    with col_text:
        st.markdown("""
        <div class="glass-card">
            <p style="color:#8899bb; line-height:1.85; margin-bottom:1.1rem; font-size:0.97rem;">
                I'm <strong style="color:#00d4ff;">Kshitij Masram</strong>, a biotechnology postgraduate
                from India with a profound passion for industrial biological science. My academic journey
                spans both B.Sc. and M.Sc. in Biotechnology, building deep expertise at the crossroads
                of life sciences and engineering.
            </p>
            <p style="color:#8899bb; line-height:1.85; margin-bottom:1.1rem; font-size:0.97rem;">
                My primary focus lies in <em style="color:#10b981; font-style:normal; font-weight:600;">
                fermentation technology</em>,
                <em style="color:#10b981; font-style:normal; font-weight:600;">bioprocess engineering</em>,
                and <em style="color:#10b981; font-style:normal; font-weight:600;">industrial biotechnology</em>
                — the science of scaling biological processes to meet real-world industrial demands.
            </p>
            <p style="color:#8899bb; line-height:1.85; font-size:0.97rem;">
                Beyond bench science, I actively develop skills in
                <strong style="color:#00d4ff;">Python programming</strong>,
                <strong style="color:#00d4ff;">data science</strong>, and
                <strong style="color:#00d4ff;">computational biotechnology</strong> — believing
                that the future of bioprocessing is deeply data-driven.
            </p>
        </div>
        """, unsafe_allow_html=True)
        # Highlights
        st.markdown("<br>", unsafe_allow_html=True)
        highlights = [
            ("📍", "Based in India"),
            ("🏭", "Industrial Biotech Focus"),
            ("📈", "Continuous Learner"),
            ("🌍", "Multilingual Aspirant"),
        ]
        h1, h2 = st.columns(2)
        for i, (icon, label) in enumerate(highlights):
            col = h1 if i % 2 == 0 else h2
            with col:
                st.markdown(f"""
                <div class="contact-info-item">
                    <span class="contact-icon">{icon}</span>
                    <span>{label}</span>
                </div>
                """, unsafe_allow_html=True)
    with col_card:
        st.markdown("""
        <div class="profile-card">
            <div class="avatar-container">
                <div class="avatar-ring"></div>
                <div class="avatar-inner" style="background:#0a1628; border:3px solid #050b14;">
                    <span style="font-size:1.6rem; font-weight:900;
                          background: linear-gradient(135deg,#00d4ff,#7c3aed);
                          -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                          background-clip:text;">KM</span>
                </div>
            </div>
            <div>
                <div class="profile-name">Kshitij Masram</div>
                <div class="profile-role">M.Sc. Biotechnology</div>
                <div class="profile-tags">
                    <span class="ptag">Fermentation</span>
                    <span class="ptag">Bioprocess</span>
                    <span class="ptag">Python</span>
                    <span class="ptag">IELTS</span>
                </div>
            </div>
        </div>
        <div class="quote-card">
            <div class="quote-mark">"</div>
            <p class="quote-text">
                Science at industrial scale is where biology becomes truly powerful —
                turning microbes into machines of production.
            </p>
        </div>
        """, unsafe_allow_html=True)
# ─── PAGE: EDUCATION ──────────────────────────────────────────────────────────
elif page == "📚 Education":
    section_header("// education", "Academic Journey")
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="edu-badge">Latest</div>
        <div class="edu-degree">Master of Science (M.Sc.) — Biotechnology</div>
        <div class="edu-inst">University, India</div>
        <div class="edu-desc">
            Advanced specialization in bioprocess engineering, fermentation science, industrial
            microbiology, biochemical engineering, and upstream/downstream processing. Deep focus
            on industrial-scale biological production systems.
        </div>
        <div class="subject-tags">
            <span class="stag">Fermentation Technology</span>
            <span class="stag">Bioprocess Engineering</span>
            <span class="stag">Industrial Microbiology</span>
            <span class="stag">Biochemical Engineering</span>
            <span class="stag">Bioreactor Design</span>
            <span class="stag">Process Optimisation</span>
        </div>
    </div>
    <div class="timeline-item">
        <div class="timeline-dot" style="border-color:#7c3aed; box-shadow:0 0 12px rgba(124,58,237,0.5);"></div>
        <div class="edu-badge" style="background:linear-gradient(135deg,#7c3aed,#ec4899);">Foundation</div>
        <div class="edu-degree">Bachelor of Science (B.Sc.) — Biotechnology</div>
        <div class="edu-inst">University, India</div>
        <div class="edu-desc">
            Comprehensive foundation covering core biological and chemical sciences including
            Thermodynamics — bridging biology with engineering concepts for a strong interdisciplinary base.
        </div>
        <div class="subject-tags">
            <span class="stag">Biotechnology</span>
            <span class="stag">Microbiology</span>
            <span class="stag">Biochemistry</span>
            <span class="stag">Molecular Biology</span>
            <span class="stag">Genetics</span>
            <span class="stag">Cell Biology</span>
            <span class="stag">Thermodynamics</span>
            <span class="stag">Chemistry</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    section_sep()
    st.markdown('<p class="section-tag">// core subjects</p><h3 style="font-weight:700;margin-bottom:1.5rem;color:#c8d8f0;">Academic Subjects</h3>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🎓 M.Sc. Subjects", "📖 B.Sc. Subjects"])
    with tab1:
        chips = "".join(f'<span class="subj-chip">{s}</span>' for s in SUBJECTS_MSC)
        st.markdown(f'<div style="padding:1rem 0;">{chips}</div>', unsafe_allow_html=True)
    with tab2:
        chips = "".join(f'<span class="subj-chip">{s}</span>' for s in SUBJECTS_BSC)
        st.markdown(f'<div style="padding:1rem 0;">{chips}</div>', unsafe_allow_html=True)
# ─── PAGE: SKILLS ─────────────────────────────────────────────────────────────
elif page == "💡 Skills":
    section_header("// skills & expertise", "What I Bring")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""
        <div class="glass-card">
            <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.5rem;">
                <span style="font-size:1.5rem;">🧬</span>
                <span style="font-size:1rem;font-weight:700;">Biotechnology & Life Sciences</span>
            </div>
        """, unsafe_allow_html=True)
        bars = "".join(skill_bar(k, v) for k, v in BIOTECH_SKILLS.items())
        st.markdown(bars + "</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="glass-card">
            <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.5rem;">
                <span style="font-size:1.5rem;">💻</span>
                <span style="font-size:1rem;font-weight:700;">Technical & Programming</span>
            </div>
        """, unsafe_allow_html=True)
        bars = "".join(skill_bar(k, v, green=True) for k, v in TECH_SKILLS.items())
        st.markdown(bars + "</div>", unsafe_allow_html=True)
    section_sep()
    st.markdown('<p class="section-tag">// focus areas</p><h3 style="font-weight:700;margin-bottom:1.5rem;color:#c8d8f0;">🎯 Key Focus Areas</h3>', unsafe_allow_html=True)
    fc1, fc2, fc3, fc4 = st.columns(4, gap="medium")
    for col, (icon, title, desc) in zip([fc1, fc2, fc3, fc4], FOCUS_AREAS):
        with col:
            st.markdown(f"""
            <div class="focus-card">
                <div class="focus-icon">{icon}</div>
                <div class="focus-title">{title}</div>
                <div class="focus-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
# ─── PAGE: LANGUAGES ──────────────────────────────────────────────────────────
elif page == "🌍 Languages":
    section_header("// languages", "Language Journey")
    lc1, lc2, lc3 = st.columns(3, gap="large")
    # Hindi / Marathi
    with lc1:
        st.markdown("""
        <div class="glass-card">
            <div class="lang-flag">🇮🇳</div>
            <div class="lang-name">Hindi / Marathi</div>
            <div class="lang-level">Native Speaker</div>
            <div class="native-badge">
                <div class="native-stars">★★★★★</div>
                <div style="font-size:0.82rem;color:#8899bb;margin-top:0.3rem;">Native Proficiency</div>
            </div>
            <div>
                <span class="lang-tag">First Language</span>
                <span class="lang-tag">Fluent</span>
                <span class="lang-tag">Professional</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    # English
    with lc2:
        eng_bars = "".join(
            skill_bar(k, v)
            for k, v in {"Reading": 88, "Listening": 80, "Writing": 75, "Speaking": 65}.items()
        )
        st.markdown(f"""
        <div class="glass-card">
            <div class="lang-flag">🇬🇧</div>
            <div class="lang-name">English</div>
            <div class="lang-level">B1+ → C1 (IELTS Preparation)</div>
            {eng_bars}
            <div style="margin-top:1rem;">
                <span class="lang-tag">Grammar Accuracy</span>
                <span class="lang-tag">Fluency Building</span>
                <span class="lang-tag">IELTS Ready</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    # German
    with lc3:
        st.markdown("""
        <div class="glass-card">
            <div class="lang-flag">🇩🇪</div>
            <div class="lang-name">German</div>
            <div class="lang-level">A1–A2 → Target: B2</div>
            <div class="progress-ring-wrap">
                <div class="ring-container">
                    <svg class="ring-svg" viewBox="0 0 100 100" width="130" height="130">
                        <defs>
                            <linearGradient id="rg" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#00d4ff"/>
                                <stop offset="100%" stop-color="#7c3aed"/>
                            </linearGradient>
                        </defs>
                        <circle cx="50" cy="50" r="40" fill="none"
                                stroke="rgba(255,255,255,0.06)" stroke-width="8"/>
                        <circle cx="50" cy="50" r="40" fill="none"
                                stroke="url(#rg)" stroke-width="8"
                                stroke-linecap="round"
                                stroke-dasharray="251.2"
                                stroke-dashoffset="201"/>
                    </svg>
                    <div class="ring-label">
                        <span class="ring-pct">20%</span>
                        <span class="ring-sub">to B2 Goal</span>
                    </div>
                </div>
                <div style="color:#8899bb;font-size:0.82rem;text-align:center;">
                    A1–A2 → <strong style="color:#00d4ff;">B2</strong> Target
                </div>
            </div>
            <div>
                <span class="lang-tag">Vocabulary</span>
                <span class="lang-tag">Grammar</span>
                <span class="lang-tag">Conversations</span>
                <span class="lang-tag">Stories</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
# ─── PAGE: INTERESTS ──────────────────────────────────────────────────────────
elif page == "🔬 Interests":
    section_header("// interests", "Academic Focus")
    st.markdown("""
    <div class="glass-card" style="margin-bottom:2rem;">
        <div style="color:#8899bb;font-size:0.9rem;margin-bottom:1.2rem;font-weight:600;
                    text-transform:uppercase;letter-spacing:0.08em;">Areas of Interest</div>
    """, unsafe_allow_html=True)
    chips = "".join(f'<span class="interest-node">{i}</span>' for i in INTERESTS)
    st.markdown(f'{chips}</div>', unsafe_allow_html=True)
    section_sep()
    st.markdown('<p class="section-tag">// strengths</p><h3 style="font-weight:700;margin-bottom:1.5rem;color:#c8d8f0;">⭐ Academic Strengths</h3>', unsafe_allow_html=True)
    sc1, sc2 = st.columns(2, gap="large")
    for i, (icon, title, desc) in enumerate(STRENGTHS):
        col = sc1 if i % 2 == 0 else sc2
        with col:
            st.markdown(f"""
            <div class="strength-item">
                <div class="str-icon">{icon}</div>
                <div>
                    <div class="str-title">{title}</div>
                    <div class="str-desc">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
# ─── PAGE: CONTACT ────────────────────────────────────────────────────────────
elif page == "📬 Contact":
    section_header("// contact", "Let's Connect")
    cc1, cc2 = st.columns([1, 1.2], gap="large")
    with cc1:
        st.markdown("""
        <div class="glass-card">
            <p style="color:#8899bb;line-height:1.8;margin-bottom:1.5rem;font-size:0.97rem;">
                I'm always open to discussions about biotechnology, fermentation technology,
                bioprocess engineering, or collaborative academic and professional opportunities.
                Feel free to reach out!
            </p>
        """, unsafe_allow_html=True)
        info_items = [
            ("📍", "Based in India"),
            ("🎯", "Open to Industrial Biotech Roles"),
            ("🌐", "Hindi · Marathi · English · German"),
            ("📚", "IELTS Prep · Python · German (A1→B2)"),
            ("🧬", "Fermentation & Bioprocess Focus"),
        ]
        for icon, text in info_items:
            st.markdown(f"""
            <div class="contact-info-item">
                <span class="contact-icon">{icon}</span>
                <span>{text}</span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with cc2:
        with st.form("contact_form", clear_on_submit=True):
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            name = st.text_input("Your Name", placeholder="John Doe")
            email = st.text_input("Email Address", placeholder="john@example.com")
            subject = st.selectbox("Subject", [
                "Industrial Biotechnology Collaboration",
                "Bioprocess Engineering Discussion",
                "Job / Internship Opportunity",
                "Research Partnership",
                "General Inquiry",
            ])
            message = st.text_area("Message", placeholder="Your message here...", height=120)
            submitted = st.form_submit_button("🚀 Send Message")
            st.markdown("</div>", unsafe_allow_html=True)
        if submitted:
            if name and email and message:
                with st.spinner("Sending..."):
                    time.sleep(1)
                st.markdown("""
                <div class="success-box">
                    <div class="success-icon-wrap">✓</div>
                    <h4 style="margin-bottom:0.4rem;">Message Sent!</h4>
                    <p style="color:#8899bb;font-size:0.9rem;">
                        Thanks for reaching out. I'll get back to you soon! 🙏
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Please fill in all required fields.")
# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-wrap">
    <div class="footer-logo">
        <span>&lt;</span> Kshitij Masram <span>/&gt;</span>
    </div>
    <div class="footer-tagline">M.Sc. Biotechnology · Fermentation · Bioprocess · Python</div>
    <div class="footer-copy">© 2024 Kshitij Masram · Built with ♥ using Streamlit</div>
</div>
""", unsafe_allow_html=True)