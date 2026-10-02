import streamlit as st

st.set_page_config(
    page_title="2050 FUTURE ARCHITECT",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# 기본 스타일
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700;800&family=Noto+Sans+KR:wght@500;600;700;800&display=swap');

html, body, [class*="css"] { font-family:'Noto Sans KR',sans-serif; }
.stApp {
    background: radial-gradient(circle at 50% -10%, rgba(119,157,146,.13), transparent 35%), #060d0f;
    color:#f5fffc;
}
.block-container { max-width:1450px; padding-top:2rem; padding-bottom:5rem; }
h1,h2,h3 { color:#fff !important; }
.hero-title { font:800 clamp(40px,5vw,68px) 'Orbitron',sans-serif; letter-spacing:2px; color:#fff; line-height:1.05; }
.hero-sub { margin:12px 0 26px; color:#d3e5e1; font-size:17px; font-weight:800; letter-spacing:1.5px; }
.section-title { margin:30px 0 14px; color:#fff; font:800 28px 'Orbitron',sans-serif; }
.card { background:rgba(13,23,25,.96); border:1px solid rgba(177,230,217,.2); border-radius:20px; padding:23px; box-shadow:0 18px 50px rgba(0,0,0,.28); }
.small-note { color:#c5d7d3; line-height:1.8; font-size:14px; }
.effect-card { background:linear-gradient(145deg,#132426,#091214); border:1px solid rgba(176,228,216,.18); border-radius:18px; padding:18px; min-height:175px; margin:8px 0; }
.effect-title { color:#fff; font-size:18px; font-weight:800; margin-bottom:8px; }
.cost-line { color:#ffd98f; font-size:13px; font-weight:700; margin:-2px 0 9px; }
.cost-line b { color:#fff0bd; }
.effect-label { color:#7fe0ca; font-size:12px; font-weight:800; letter-spacing:1px; }
.effect-text { color:#d5e3e0; font-size:14px; line-height:1.75; }
.good { color:#8ef0c5; font-weight:800; }
.bad { color:#ffbd91; font-weight:800; }
.neutral { color:#dfe9e6; font-weight:800; }
.source-box { background:#0b1517; border:1px solid rgba(177,230,217,.16); border-radius:18px; padding:19px; color:#c8d8d5; font-size:14px; line-height:1.8; }

section[data-testid="stSidebar"] { background:#071012; border-right:1px solid rgba(160,220,208,.14); }
section[data-testid="stSidebar"] * { color:#f4fffc; }
section[data-testid="stSidebar"] button { background:#101a1c !important; color:#ffffff !important; border:1px solid rgba(180,225,215,.20) !important; }
section[data-testid="stSidebar"] button:hover { background:#18282a !important; border-color:rgba(180,225,215,.42) !important; }
section[data-testid="stSidebar"] button[kind="primary"] { background:#ff4b50 !important; color:#ffffff !important; border-color:#ff4b50 !important; }
section[data-testid="stSidebar"] button[kind="primary"]:hover { background:#ff6267 !important; }
section[data-testid="stSidebar"] button p, section[data-testid="stSidebar"] button span, section[data-testid="stSidebar"] button div { color:#ffffff !important; }
.expert-box { background:linear-gradient(145deg,#101e20,#0a1315); border:1px solid rgba(160,220,208,.20); border-radius:18px; padding:20px 22px; margin:16px 0; }
.expert-box .expert-kicker { color:#76d9c5; font-size:12px; font-weight:800; letter-spacing:1.5px; margin-bottom:7px; }
.expert-box h3 { margin:0 0 8px; color:#ffffff !important; font-size:20px; }
.expert-box p { margin:6px 0; color:#d8e6e3; line-height:1.85; font-size:14px; }
.expert-box b { color:#ffffff; }

[data-baseweb="select"] > div { min-height:52px; font-size:16px !important; font-weight:700 !important; }
button { font-size:16px !important; font-weight:800 !important; }
button[kind="primary"] { min-height:54px !important; border-radius:13px !important; }
.stRadio label, .stMultiSelect label, .stSelectbox label, [data-testid="stColorPicker"] label { color:#fff !important; font-size:16px !important; font-weight:800 !important; }
div[data-testid="stMetric"] { background:#0d1b1d; border:1px solid rgba(155,220,208,.18); border-radius:16px; padding:15px; }
div[data-testid="stMetricLabel"] { color:#bdd0cc !important; }
div[data-testid="stMetricValue"] { color:#fff !important; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# 세션 상태
# =========================================================
# 세션 상태를 항목별로 초기화합니다.
# 반복문 변수에 의존하지 않으므로 일부 줄이 누락될 때 발생하던 NameError를 방지합니다.
st.session_state.setdefault("page", "HOME")
st.session_state.setdefault("completed", False)
st.session_state.setdefault("usage", "🏠 미래 주거시설")
st.session_state.setdefault("shape", "🏙️ 수직형 타워")
st.session_state.setdefault("material", "🧱 저탄소 콘크리트")
st.session_state.setdefault("technologies", [])
st.session_state.setdefault("building_color", "#5D7F7A")
st.session_state.setdefault("budget", 100)

# =========================================================
# 설계 데이터
# impact는 '실제 배출량'이 아니라 게임용 가상 점수
# =========================================================
USAGES = {
    "🏠 미래 주거시설": {
        "impact": 4,
        "effect": "생활공간이므로 냉난방, 조명, 온수, 물 사용 등이 발생할 수 있습니다.",
        "limit": "실제 환경 영향은 건물 규모와 에너지 사용 방식에 따라 달라집니다.",
        "class": "housing",
        "badge": "LIVING",
    },
    "🏫 미래 학교": {
        "impact": 2,
        "effect": "자연채광과 자연환기를 활용하기 쉬운 공간으로 설정해 오염지수 영향을 낮게 반영했습니다.",
        "limit": "실제 학교의 에너지 사용량은 지역, 운영시간, 냉난방 설비 등에 따라 달라집니다.",
        "class": "school",
        "badge": "EDU",
    },
    "🏥 미래 병원": {
