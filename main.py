import streamlit as st

# =========================================================
# 2050 FUTURE ARCHITECT
# Streamlit single-file version
# =========================================================

st.set_page_config(
    page_title="2050 FUTURE ARCHITECT",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Global CSS
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;800&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 50% -10%, rgba(80, 130, 140, 0.18), transparent 35%),
        linear-gradient(180deg, #071216 0%, #09171a 48%, #050b0d 100%);
    color: #ffffff;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.8rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: 'Orbitron', sans-serif !important;
    letter-spacing: 1px;
}

.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(42px, 5vw, 70px);
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: 2px;
    color: #effff8;
    text-shadow: 0 0 22px rgba(190, 255, 235, 0.22);
    margin-bottom: 12px;
}

.hero-sub {
    color: #d7e8e5;
    letter-spacing: 1.5px;
    font-size: 21px;
    margin-bottom: 24px;
}

.section-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 28px;
    font-weight: 700;
    margin: 18px 0 12px;
}

.glass-card {
    background: rgba(11, 26, 29, 0.78);
    border: 1px solid rgba(145, 220, 207, 0.18);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.28);
}

.info-card {
    background: linear-gradient(135deg, rgba(21, 43, 45, .9), rgba(7, 20, 22, .88));
    border: 1px solid rgba(126, 226, 204, .16);
    border-radius: 18px;
    padding: 20px;
    height: 100%;
}

.info-label {
    color: #7dd9ca;
    font-size: 14px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.info-value {
    font-size: 18px;
    font-weight: 700;
}

.small-text {
    color: #91a9aa;
    font-size: 15px;
    line-height: 1.7;
}

.source-box {
    background: rgba(7, 18, 20, .88);
    border: 1px solid rgba(120, 185, 180, .16);
    border-radius: 16px;
    padding: 18px;
    color: #9eb5b5;
    font-size: 15px;
    line-height: 1.7;
}

button[kind="primary"] {
    border-radius: 12px !important;
    font-weight: 700 !important;
}

div[data-testid="stMetric"] {
    background: rgba(12, 28, 30, .72);
    border: 1px solid rgba(135, 210, 200, .14);
    border-radius: 16px;
    padding: 14px;
}

/* high-contrast typography */
.stMarkdown, .stMarkdown p, .stMarkdown li, label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
    color: #ffffff !important;
    font-size: 16px !important;
    line-height: 1.65 !important;
}

[data-baseweb="radio"] label, [data-baseweb="checkbox"] label,
[data-baseweb="select"] *, [data-baseweb="input"] * {
    color: #ffffff !important;
}

.stCaption, [data-testid="stCaptionContainer"] {
    color: #c6d7d5 !important;
    font-size: 14px !important;
}

button {
    font-size: 16px !important;
    min-height: 48px !important;
}

/* sidebar */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #071113 0%, #0a181a 100%);
    border-right: 1px solid rgba(135, 210, 200, .12);
}

.sidebar-title {
    font-family: 'Orbitron', sans-serif;
    color: #dffff6;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 4px;
}

.sidebar-sub {
    color: #718889;
    font-size: 14px;
    margin-bottom: 22px;
}

.nav-current {
    background: rgba(120, 224, 204, .10);
    border: 1px solid rgba(120, 224, 204, .24);
    color: #bffbed;
    border-radius: 10px;
    padding: 10px 12px;
    margin-bottom: 8px;
}

/* hide empty markdown gaps */
div[data-testid="stMarkdownContainer"] p {
    margin-bottom: .35rem;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------
defaults = {
    "page": "HOME",
    "completed": False,
    "usage": "🏠 미래 주거시설",
    "shape": "🏙️ 수직형 타워",
    "material": "🧱 저탄소 콘크리트",
    "technologies": [],
    "decorations": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ---------------------------------------------------------
# Game data
# ---------------------------------------------------------
USAGES = {
    "🏠 미래 주거시설": {
        "pollution": 4,
        "desc": "기후 변화에 대응하면서 사람들이 생활할 수 있는 미래형 주거공간",
    },
    "🏫 미래 학교": {
        "pollution": 2,
        "desc": "자연채광과 환기를 활용하는 미래 교육공간",
    },
    "🏥 미래 병원": {
        "pollution": 5,
        "desc": "에너지와 물 사용량을 줄이는 미래 의료시설",
    },
    "🔬 미래 연구센터": {
        "pollution": 3,
        "desc": "미래 기술과 환경 연구를 위한 고성능 연구공간",
    },
}

SHAPES = {
    "🏙️ 수직형 타워": {
        "pollution": 7,
        "height": 350,
        "radius": "8px",
        "desc": "좁은 부지에 많은 공간을 확보하는 고층형 건축",
    },
    "🌿 테라스형 건축": {
        "pollution": 3,
        "height": 260,
        "radius": "28px 28px 8px 8px",
        "desc": "층마다 외부공간을 두어 녹지와 건축물을 연결",
    },
    "🛸 돔형 건축": {
        "pollution": 2,
        "height": 245,
        "radius": "50% 50% 12px 12px",
        "desc": "곡면 지붕을 활용한 미래형 공간",
    },
    "🌍 반지하형 건축": {
        "pollution": 1,
        "height": 190,
        "radius": "35px 35px 8px 8px",
        "desc": "지형과 건축물을 결합해 외부 환경의 영향을 줄이는 형태",
    },
}

MATERIALS = {
    "🧱 저탄소 콘크리트": {
        "pollution": 8,
        "desc": "일반 콘크리트보다 탄소 배출을 줄이는 방향의 건축 재료",
    },
    "🔩 저탄소 철강": {
        "pollution": 7,
        "desc": "철강 생산 과정에서의 탄소 배출 저감을 고려한 재료",
    },
    "🌲 목재·바이오 기반 재료": {
        "pollution": 3,
        "desc": "목재 등 바이오 기반 재료를 건축에 활용하는 방식",
    },
    "♻️ 재사용·재활용 재료": {
        "pollution": 2,
        "desc": "기존 자원을 다시 사용해 새로운 재료 생산을 줄이는 방식",
    },
}

TECHNOLOGIES = {
    "☀️ 태양광 발전": -9,
    "🌬️ 자연환기": -7,
    "🪟 외부 차양": -6,
    "🌱 녹화 지붕": -7,
    "💧 빗물 이용": -5,
    "🔄 물 재이용": -5,
}

DECORATIONS = {
    "🌳 수직 정원": -5,
    "🌿 녹색 벽": -4,
    "🌲 주변 녹지": -4,
    "🌱 옥상 정원": -5,
}


# ---------------------------------------------------------
# Pollution score
# This is a fictional game score, NOT real carbon emissions.
# Lower = better.
# ---------------------------------------------------------
def calculate_pollution():
    score = 90
    score += USAGES[st.session_state.usage]["pollution"]
    score += SHAPES[st.session_state.shape]["pollution"]
    score += MATERIALS[st.session_state.material]["pollution"]

    for item in st.session_state.technologies:
        score += TECHNOLOGIES[item]

    for item in st.session_state.decorations:
        score += DECORATIONS[item]

    return max(0, min(100, score))


# ---------------------------------------------------------
# 3D polluted future city
# Pure HTML/CSS 3D. No external 3D library needed.
# ---------------------------------------------------------
def polluted_world_html():
    return """
<div class="world-3d">
    <div class="stars"></div>

    <div class="sun-3d">
        <div class="sun-core"></div>
        <div class="sun-ring"></div>
    </div>

    <div class="smog smog-a"></div>
    <div class="smog smog-b"></div>
    <div class="smog smog-c"></div>

    <div class="mountain mountain-back"></div>
    <div class="mountain mountain-mid"></div>

    <div class="city-3d">
        <div class="tower t1"><i></i><i></i><i></i><i></i></div>
        <div class="tower t2"><i></i><i></i><i></i><i></i><i></i></div>
        <div class="tower t3"><i></i><i></i><i></i></div>
        <div class="tower t4"><i></i><i></i><i></i><i></i><i></i><i></i></div>
        <div class="tower t5"><i></i><i></i><i></i><i></i></div>
        <div class="tower t6"><i></i><i></i><i></i></div>
    </div>

    <div class="ground-3d"></div>

    <div class="road road-1"></div>
    <div class="road road-2"></div>
    <div class="road-grid"></div>
    <div class="holo-ring ring-1"></div>
    <div class="holo-ring ring-2"></div>

    <div class="warning-panel">
        <span>EARTH STATUS</span>
        <strong>CRITICAL</strong>
        <small>ATMOSPHERE / 2050</small>
    </div>

    <div class="world-caption">
        <b>EARTH // 2050</b>
        <span>THE AIR IS NO LONGER FREE.</span>
    </div>
</div>

<style>
.world-3d {
    position: relative;
    height: 520px;
    overflow: hidden;
    border-radius: 26px;
    border: 1px solid rgba(174, 234, 220, .18);
    background:
        radial-gradient(circle at 50% 42%, rgba(90, 140, 125, .22), transparent 18%),
        linear-gradient(180deg, #102a2d 0%, #243f3c 45%, #1b2928 68%, #090e0e 100%);
    perspective: 900px;
    box-shadow: inset 0 0 120px rgba(0,0,0,.58), 0 30px 70px rgba(0,0,0,.35);
}

.world-3d::after {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse at center, transparent 28%, rgba(0,0,0,.28) 75%, rgba(0,0,0,.72) 100%),
        repeating-linear-gradient(115deg, rgba(255,255,255,.018) 0 1px, transparent 1px 7px);
    pointer-events: none;
}

.stars {
    position: absolute;
    inset: 0;
    opacity: .55;
    background-image:
        radial-gradient(circle at 12% 22%, #d5eee5 0 1px, transparent 2px),
        radial-gradient(circle at 29% 13%, #d5eee5 0 1px, transparent 2px),
        radial-gradient(circle at 70% 18%, #d5eee5 0 1px, transparent 2px),
        radial-gradient(circle at 88% 30%, #d5eee5 0 1px, transparent 2px),
        radial-gradient(circle at 55% 9%, #d5eee5 0 1px, transparent 2px);
}

.sun-3d {
    position: absolute;
    top: 62px;
    right: 14%;
    width: 145px;
    height: 145px;
    transform: translateZ(-60px);
}

.sun-core {
    position: absolute;
    inset: 28px;
    border-radius: 50%;
    background: radial-gradient(circle, #d9ffbd 0%, #a3c77c 45%, #68764d 100%);
    box-shadow: 0 0 55px rgba(177, 224, 130, .28);
}

.sun-ring {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    border: 1px solid rgba(191, 222, 156, .24);
    box-shadow: 0 0 35px rgba(155, 198, 130, .12);
}

.smog {
    position: absolute;
    border-radius: 50%;
    filter: blur(25px);
    opacity: .42;
}

.smog-a {
    width: 520px;
    height: 150px;
    left: -80px;
    top: 155px;
    background: rgba(74, 102, 83, .62);
    transform: rotate(-5deg);
}

.smog-b {
    width: 610px;
    height: 180px;
    right: -120px;
    top: 205px;
    background: rgba(91, 83, 63, .54);
    transform: rotate(8deg);
}

.smog-c {
    width: 760px;
    height: 130px;
    left: 18%;
    top: 280px;
    background: rgba(68, 81, 76, .52);
    transform: rotate(-3deg);
}

.mountain {
    position: absolute;
    left: 0;
    width: 100%;
    clip-path: polygon(0 100%, 0 67%, 13% 45%, 25% 68%, 38% 40%, 52% 71%, 66% 46%, 79% 67%, 91% 42%, 100% 65%, 100% 100%);
}

.mountain-back {
    bottom: 135px;
    height: 260px;
    background: #253b39;
    opacity: .75;
    transform: translateZ(-180px) scale(1.2);
}

.mountain-mid {
    bottom: 100px;
    height: 210px;
    background: #172725;
    opacity: .92;
    transform: translateZ(-80px) scale(1.1);
}

.city-3d {
    position: absolute;
    left: 4%;
    right: 4%;
    bottom: 110px;
    height: 270px;
    display: flex;
    align-items: end;
    justify-content: space-around;
    transform: rotateX(8deg) translateZ(10px);
    transform-style: preserve-3d;
}

.tower {
    position: relative;
    width: 11%;
    min-width: 52px;
    background: linear-gradient(90deg, #101d1d, #2b4542 45%, #101919);
    border: 1px solid rgba(143, 192, 183, .15);
    box-shadow: -12px 0 30px rgba(0,0,0,.25), 12px 0 30px rgba(0,0,0,.15);
    transform: skewY(0deg) rotateY(-5deg);
}

.tower::before {
    content: "";
    position: absolute;
    left: 100%;
    top: 8px;
    width: 24px;
    height: 100%;
    background: linear-gradient(90deg, #142221, #0a1111);
    transform: skewY(-38deg);
    transform-origin: left top;
    opacity: .9;
}

.tower::after {
    content: "";
    position: absolute;
    left: 5px;
    right: 5px;
    top: -12px;
    height: 13px;
    background: #344f4a;
    transform: skewX(-45deg);
    opacity: .85;
}

.t1 { height: 145px; }
.t2 { height: 210px; }
.t3 { height: 125px; }
.t4 { height: 245px; }
.t5 { height: 175px; }
.t6 { height: 135px; }

.tower i {
    display: block;
    height: 4px;
    margin: 18px 7px;
    background: rgba(151, 205, 187, .34);
    box-shadow: 0 0 8px rgba(130, 205, 182, .08);
}

.ground-3d {
    position: absolute;
    left: -10%;
    bottom: -220px;
    width: 120%;
    height: 330px;
    background:
        linear-gradient(180deg, rgba(28,42,40,.2), rgba(4,8,8,.98)),
        repeating-linear-gradient(90deg, rgba(120,145,137,.08) 0 2px, transparent 2px 80px);
    transform: rotateX(64deg) translateZ(-20px);
    transform-origin: top center;
}

.road {
    position: absolute;
    bottom: 78px;
    width: 75%;
    height: 7px;
    background: rgba(123, 147, 141, .16);
    box-shadow: 0 0 18px rgba(130, 190, 175, .06);
    transform: skewX(-42deg);
}

.road-1 { left: -8%; }
.road-2 { right: -12%; bottom: 55px; }

.road-grid {
    position: absolute;
    left: -12%;
    bottom: 0;
    width: 124%;
    height: 210px;
    transform: perspective(500px) rotateX(66deg);
    transform-origin: bottom center;
    background:
        linear-gradient(rgba(110, 176, 161, .08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(110, 176, 161, .08) 1px, transparent 1px);
    background-size: 46px 30px;
    opacity: .7;
}

.holo-ring {
    position: absolute;
    border: 1px solid rgba(120, 220, 197, .16);
    border-radius: 50%;
    transform-style: preserve-3d;
    filter: blur(.2px);
}

.ring-1 {
    width: 520px;
    height: 170px;
    left: calc(50% - 260px);
    bottom: 88px;
    transform: rotateX(67deg);
}

.ring-2 {
    width: 350px;
    height: 110px;
    left: calc(50% - 175px);
    bottom: 115px;
    transform: rotateX(67deg);
}

.warning-panel {
    position: absolute;
    top: 28px;
    left: 28px;
    width: 155px;
    padding: 13px 15px;
    border-left: 3px solid #d8a56b;
    background: rgba(8, 18, 19, .63);
    backdrop-filter: blur(8px);
    color: #9fb7b3;
    letter-spacing: 1px;
}

.warning-panel span,
.warning-panel small {
    display: block;
    font-size: 9px;
}

.warning-panel strong {
    display: block;
    margin: 4px 0;
    font-family: 'Orbitron', sans-serif;
    font-size: 22px;
    color: #d9b57f;
}

.world-caption {
    position: absolute;
    right: 28px;
    bottom: 28px;
    text-align: right;
    z-index: 4;
}

.world-caption b {
    display: block;
    font-family: 'Orbitron', sans-serif;
    font-size: 18px;
    color: #dcece6;
}

.world-caption span {
    display: block;
    margin-top: 4px;
    color: #718785;
    font-size: 10px;
    letter-spacing: 2px;
}
</style>
"""


# ---------------------------------------------------------
# Building result preview
# ---------------------------------------------------------
def building_html():
    shape = st.session_state.shape
    height = SHAPES[shape]["height"]
    radius = SHAPES[shape]["radius"]

    material = st.session_state.material

    material_css = {
        "🧱 저탄소 콘크리트": """
            background: linear-gradient(105deg, #536765, #253b3a 46%, #172625);
            border-color: rgba(177, 214, 205, .30);
        """,
        "🔩 저탄소 철강": """
            background: linear-gradient(105deg, #687b7c, #263a3c 48%, #111b1c);
            border-color: rgba(184, 218, 225, .34);
        """,
        "🌲 목재·바이오 기반 재료": """
            background: linear-gradient(105deg, #68705c, #344138 50%, #1c2824);
            border-color: rgba(184, 211, 163, .28);
        """,
        "♻️ 재사용·재활용 재료": """
            background: linear-gradient(105deg, #516d69, #244543 50%, #142b2a);
            border-color: rgba(116, 226, 196, .35);
        """,
    }[material]

    windows = ""
    for i in range(12):
        windows += f'<span class="window w{i}"></span>'

    solar = ""
    if "☀️ 태양광 발전" in st.session_state.technologies:
        solar = """
        <div class="solar-panel solar-1"></div>
        <div class="solar-panel solar-2"></div>
        """

    green_roof = ""
    if "🌱 녹화 지붕" in st.session_state.technologies:
        green_roof = '<div class="green-roof"></div>'

    trees = ""
    if "🌳 수직 정원" in st.session_state.decorations or "🌲 주변 녹지" in st.session_state.decorations:
        trees += '<div class="tree tree-1"></div><div class="tree tree-2"></div><div class="tree tree-3"></div>'

    green_wall = ""
    if "🌿 녹색 벽" in st.session_state.decorations:
        green_wall = '<div class="green-wall"></div>'

    return f"""
<div class="building-world">
    <div class="building-stars"></div>
    <div class="building-haze"></div>

    <div class="future-moon"></div>

    <div class="far-city">
        <span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span>
    </div>

    <div class="building-ground"></div>

    <div class="building-wrap">
        <div class="building-shadow"></div>
        {green_roof}

        <div class="main-building"
             style="height:{height}px; border-radius:{radius}; {material_css}">
            <div class="building-top"></div>
            <div class="building-side"></div>
            {windows}
            {green_wall}
            {solar}
        </div>

        {trees}
    </div>

    <div class="building-label">
        <span>2050 FUTURE ARCHITECT</span>
        <b>{st.session_state.usage}</b>
        <small>{st.session_state.shape} · {st.session_state.material}</small>
    </div>
</div>

<style>
.building-world {
    position: relative;
    height: 520px;
    overflow: hidden;
    border-radius: 24px;
    border: 1px solid rgba(155, 220, 208, .18);
    background:
        radial-gradient(circle at 70% 24%, rgba(120, 171, 153, .16), transparent 18%),
        linear-gradient(180deg, #0a1b1e 0%, #122a2c 45%, #0b1617 100%);
    perspective: 900px;
}

.building-world::after {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, transparent 30%, rgba(0,0,0,.55) 100%);
    pointer-events: none;
}

.building-stars {
    position: absolute;
    inset: 0;
    opacity: .45;
    background-image:
        radial-gradient(circle at 10% 18%, #cde8df 0 1px, transparent 2px),
        radial-gradient(circle at 24% 31%, #cde8df 0 1px, transparent 2px),
        radial-gradient(circle at 48% 13%, #cde8df 0 1px, transparent 2px),
        radial-gradient(circle at 78% 19%, #cde8df 0 1px, transparent 2px),
        radial-gradient(circle at 91% 34%, #cde8df 0 1px, transparent 2px);
}

.building-haze {
    position: absolute;
    width: 700px;
    height: 170px;
    left: 25%;
    top: 180px;
    border-radius: 50%;
    background: rgba(83, 118, 108, .18);
    filter: blur(30px);
}

.future-moon {
    position: absolute;
    top: 65px;
    right: 12%;
    width: 88px;
    height: 88px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 35%, #d7eee4, #7eaaa1 58%, #344c49);
    box-shadow: 0 0 50px rgba(180, 232, 214, .14);
}

.far-city {
    position: absolute;
    left: 4%;
    right: 4%;
    bottom: 110px;
    height: 145px;
    display: flex;
    align-items: end;
    justify-content: space-around;
    opacity: .48;
    transform: translateZ(-80px) scale(1.12);
}

.far-city span {
    display: block;
    width: 8%;
    background: linear-gradient(90deg, #0c1718, #203432, #0b1314);
    border: 1px solid rgba(150, 190, 180, .12);
}

.far-city span:nth-child(1) { height: 75px; }
.far-city span:nth-child(2) { height: 105px; }
.far-city span:nth-child(3) { height: 58px; }
.far-city span:nth-child(4) { height: 130px; }
.far-city span:nth-child(5) { height: 88px; }
.far-city span:nth-child(6) { height: 112px; }
.far-city span:nth-child(7) { height: 70px; }
.far-city span:nth-child(8) { height: 96px; }

.building-ground {
    position: absolute;
    left: -10%;
    bottom: -180px;
    width: 120%;
    height: 300px;
    background:
        linear-gradient(180deg, rgba(29,48,45,.15), #050b0c 72%),
        repeating-linear-gradient(90deg, rgba(140,180,168,.08) 0 2px, transparent 2px 75px);
    transform: rotateX(63deg);
    transform-origin: top center;
}

.building-wrap {
    position: absolute;
    left: 50%;
    bottom: 65px;
    width: 430px;
    height: 430px;
    transform: translateX(-50%) rotateY(-10deg);
    transform-style: preserve-3d;
    z-index: 3;
}

.main-building {
    position: absolute;
    bottom: 0;
    left: 105px;
    width: 220px;
    border: 1px solid;
    box-shadow:
        0 0 30px rgba(110, 230, 202, .10),
        -24px 30px 45px rgba(0,0,0,.35);
    overflow: hidden;
    transform: perspective(700px) rotateY(-5deg);
}

.building-top {
    position: absolute;
    top: -12px;
    left: 5px;
    right: -18px;
    height: 15px;
    background: rgba(115, 156, 148, .75);
    transform: skewX(-45deg);
}

.building-side {
    position: absolute;
    top: 5px;
    left: 100%;
    width: 34px;
    height: 100%;
    background: linear-gradient(90deg, #172927, #081011);
    transform: skewY(-38deg);
    transform-origin: left top;
}

.window {
    position: absolute;
    width: 24px;
    height: 13px;
    background: linear-gradient(180deg, #d6fff2, #6bb4a4);
    border: 1px solid rgba(230,255,249,.45);
    box-shadow: 0 0 12px rgba(142, 244, 211, .20);
}

.w0 { left: 24px; top: 28px; }
.w1 { left: 72px; top: 28px; }
.w2 { left: 120px; top: 28px; }
.w3 { left: 168px; top: 28px; }
.w4 { left: 24px; top: 82px; }
.w5 { left: 72px; top: 82px; }
.w6 { left: 120px; top: 82px; }
.w7 { left: 168px; top: 82px; }
.w8 { left: 24px; top: 136px; }
.w9 { left: 72px; top: 136px; }
.w10 { left: 120px; top: 136px; }
.w11 { left: 168px; top: 136px; }

.green-roof {
    position: absolute;
    left: 96px;
    bottom: 402px;
    width: 230px;
    height: 28px;
    border-radius: 50%;
    background: linear-gradient(180deg, #5d9d78, #274d3a);
    box-shadow: 0 0 20px rgba(90, 183, 122, .22);
    z-index: 4;
}

.green-wall {
    position: absolute;
    left: 4px;
    top: 0;
    width: 9px;
    height: 100%;
    background: repeating-linear-gradient(
        180deg,
        #73ad78 0 9px,
        #2e6547 9px 17px
    );
    opacity: .82;
}

.solar-panel {
    position: absolute;
    width: 46px;
    height: 30px;
    border: 1px solid rgba(154, 222, 216, .48);
    background:
        repeating-linear-gradient(90deg, rgba(180,240,232,.20) 0 1px, transparent 1px 11px),
        repeating-linear-gradient(0deg, rgba(180,240,232,.20) 0 1px, transparent 1px 10px),
        linear-gradient(135deg, #183b42, #071b20);
    transform: skewX(-12deg) rotate(-12deg);
    z-index: 5;
}

.solar-1 {
    top: -6px;
    right: 24px;
}

.solar-2 {
    top: 18px;
    right: 42px;
}

.building-shadow {
    position: absolute;
    left: 55px;
    bottom: -10px;
    width: 320px;
    height: 55px;
    border-radius: 50%;
    background: rgba(0,0,0,.62);
    filter: blur(14px);
}

.tree {
    position: absolute;
    bottom: 4px;
    width: 30px;
    height: 68px;
    background: linear-gradient(90deg, #183d31, #5d956f);
    clip-path: polygon(50% 0, 86% 34%, 68% 34%, 94% 66%, 66% 66%, 84% 100%, 16% 100%, 34% 66%, 6% 66%, 32% 34%, 14% 34%);
    filter: drop-shadow(0 0 10px rgba(76, 164, 116, .16));
}

.tree-1 { left: 45px; }
.tree-2 { right: 44px; height: 85px; }
.tree-3 { right: 8px; height: 52px; }

.building-label {
    position: absolute;
    left: 28px;
    bottom: 25px;
    z-index: 6;
}

.building-label span {
    display: block;
    color: #72cdbd;
    font-family: 'Orbitron', sans-serif;
    font-size: 10px;
    letter-spacing: 2px;
}

.building-label b {
    display: block;
    margin-top: 4px;
    font-size: 17px;
    color: #e4f5ef;
}

.building-label small {
    color: #738b88;
    font-size: 11px;
}
</style>
"""


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-title">2050 // ARCHITECT</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">FUTURE CITY DESIGN SIMULATION</div>', unsafe_allow_html=True)

    pages = {
        "🏠 HOME": "HOME",
        "① 건축물 용도": "USAGE",
        "② 건축 형태": "SHAPE",
        "③ 건축 자재": "MATERIAL",
        "④ 미래 기술": "TECH",
        "⑤ 꾸미기": "DECOR",
        "📋 설계 결과": "RESULT",
    }

    for label, page_name in pages.items():
        if st.button(
            label,
            key=f"nav_{page_name}",
            use_container_width=True,
            type="primary" if st.session_state.page == page_name else "secondary",
        ):
            st.session_state.page = page_name
            st.rerun()

    st.divider()

    score = calculate_pollution()
    st.markdown("### 🌫️ 오염지수")
    st.progress(score / 100)
    st.markdown(
        f'<div style="font-family:Orbitron;font-size:25px;color:#dff9f2;">{score}<span style="font-size:12px;color:#78908e;"> / 100</span></div>',
        unsafe_allow_html=True,
    )
    st.caption("낮을수록 친환경적인 설계")

    if score <= 40:
        st.success("MISSION READY")
    else:
        st.warning("환경 부담이 아직 높습니다.")


# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------
if st.session_state.page == "HOME":
    st.markdown('<div class="hero-title">2050 FUTURE ARCHITECT</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">BUILD A FUTURE THAT CAN SURVIVE.</div>', unsafe_allow_html=True)

    # IMPORTANT:
    # This uses st.html instead of st.markdown so the HTML is rendered,
    # not shown as literal <div> text.
    if st.session_state.completed:
        st.markdown("## 🏙️ YOUR 2050 BUILDING")
        st.html(building_html())

        score = calculate_pollution()

        if score <= 40:
            st.success(f"🌍 설계 성공! 최종 오염지수 {score} — 2050 도시 생존 조건을 통과했습니다.")
        else:
            st.error(f"⚠️ 설계 실패! 최종 오염지수 {score} — 환경 부담을 더 낮춰야 합니다.")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("📋 설계 결과 자세히 보기", use_container_width=True):
                st.session_state.page = "RESULT"
                st.rerun()
        with c2:
            if st.button("🔄 새로운 건축물 만들기", use_container_width=True):
                st.session_state.completed = False
                st.session_state.technologies = []
                st.session_state.decorations = []
                st.session_state.page = "USAGE"
                st.rerun()

    else:
        st.html(polluted_world_html())

        st.markdown("")
        st.markdown("""
<div class="glass-card">
    <div class="info-label">MISSION 2050</div>
    <h2 style="margin:4px 0 10px;">오염된 지구에 새로운 건축물을 설계하라.</h2>
    <div class="small-text">
        2050년, 지구의 대기와 도시 환경은 지금보다 더 큰 압박을 받고 있습니다.
        당신은 미래의 건축가가 되어 건축물의 용도, 형태, 자재, 미래 기술과 주변 환경을 직접 선택합니다.
        선택한 요소에 따라 게임 속 오염지수가 달라집니다.
    </div>
</div>
""", unsafe_allow_html=True)

        st.markdown("")
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("""
<div class="info-card">
    <div class="info-label">01 / DESIGN</div>
    <div class="info-value">건축물 설계</div>
    <div class="small-text">용도부터 형태와 자재까지 직접 선택합니다.</div>
</div>
""", unsafe_allow_html=True)

        with c2:
            st.markdown("""
<div class="info-card">
    <div class="info-label">02 / TECHNOLOGY</div>
    <div class="info-value">미래 기술 적용</div>
    <div class="small-text">태양광, 자연환기, 녹화 등 미래 요소를 추가합니다.</div>
</div>
""", unsafe_allow_html=True)

        with c3:
            st.markdown("""
<div class="info-card">
    <div class="info-label">03 / SURVIVAL</div>
    <div class="info-value">도시의 미래 결정</div>
    <div class="small-text">최종 오염지수가 40 이하이면 미션 성공입니다.</div>
</div>
""", unsafe_allow_html=True)

        st.markdown("")
        if st.button("🚀 미래 건축 설계 시작", type="primary", use_container_width=True):
            st.session_state.page = "USAGE"
            st.rerun()

        st.markdown("""
<div class="source-box" style="margin-top:20px;">
<b>RESEARCH NOTE</b><br>
이 게임의 건축·환경 요소는 건축물의 에너지 사용, 건축 재료의 탄소 영향,
녹화·차양·자연환기·물 관리 등의 실제 환경 대응 개념을 참고해 구성했습니다.
단, 게임 속 오염지수는 이해를 위한 가상의 지표이며 실제 탄소배출량을 의미하지 않습니다.
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# USAGE
# ---------------------------------------------------------
elif st.session_state.page == "USAGE":
    st.markdown('<div class="hero-title" style="font-size:40px;">01 / BUILDING USE</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">WHAT WILL YOUR BUILDING DO?</div>', unsafe_allow_html=True)

    choice = st.radio(
        "건축물의 용도를 선택하세요.",
        list(USAGES.keys()),
        index=list(USAGES.keys()).index(st.session_state.usage),
    )
    st.session_state.usage = choice

    st.markdown(f"""
<div class="glass-card">
    <div class="info-label">SELECTED USE</div>
    <h2>{choice}</h2>
    <div class="small-text">{USAGES[choice]["desc"]}</div>
</div>
""", unsafe_allow_html=True)

    if st.button("다음 → 건축 형태", type="primary", use_container_width=True):
        st.session_state.page = "SHAPE"
        st.rerun()


# ---------------------------------------------------------
# SHAPE
# ---------------------------------------------------------
elif st.session_state.page == "SHAPE":
    st.markdown('<div class="hero-title" style="font-size:40px;">02 / FORM</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">SHAPE THE FUTURE CITY.</div>', unsafe_allow_html=True)

    choice = st.radio(
        "건축 형태를 선택하세요.",
        list(SHAPES.keys()),
        index=list(SHAPES.keys()).index(st.session_state.shape),
    )
    st.session_state.shape = choice

    st.html(building_html())

    st.markdown(f"""
<div class="glass-card">
    <div class="info-label">FORM DESCRIPTION</div>
    <h3>{choice}</h3>
    <div class="small-text">{SHAPES[choice]["desc"]}</div>
</div>
""", unsafe_allow_html=True)

    if st.button("다음 → 건축 자재", type="primary", use_container_width=True):
        st.session_state.page = "MATERIAL"
        st.rerun()


# ---------------------------------------------------------
# MATERIAL
# ---------------------------------------------------------
elif st.session_state.page == "MATERIAL":
    st.markdown('<div class="hero-title" style="font-size:40px;">03 / MATERIAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">WHAT WILL YOUR BUILDING BE MADE OF?</div>', unsafe_allow_html=True)

    choice = st.radio(
        "건축 자재를 선택하세요.",
        list(MATERIALS.keys()),
        index=list(MATERIALS.keys()).index(st.session_state.material),
    )
    st.session_state.material = choice

    st.markdown(f"""
<div class="glass-card">
    <div class="info-label">MATERIAL</div>
    <h2>{choice}</h2>
    <div class="small-text">{MATERIALS[choice]["desc"]}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="source-box" style="margin-top:18px;">
<b>REFERENCE</b><br>
UNEP의 건축 자재 관련 자료에서는 시멘트·철강·알루미늄 등의 재료가
건축물의 내재탄소와 연결될 수 있으며, 재사용·재활용과 저탄소 재료 등의 접근이
건축 부문의 탄소 저감과 관련된 방법으로 다뤄집니다.
</div>
""", unsafe_allow_html=True)

    if st.button("다음 → 미래 기술", type="primary", use_container_width=True):
        st.session_state.page = "TECH"
        st.rerun()


# ---------------------------------------------------------
# TECH
# ---------------------------------------------------------
elif st.session_state.page == "TECH":
    st.markdown('<div class="hero-title" style="font-size:40px;">04 / FUTURE TECH</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">UPGRADE YOUR BUILDING.</div>', unsafe_allow_html=True)

    selected = st.multiselect(
        "건축물에 적용할 미래 기술을 선택하세요.",
        list(TECHNOLOGIES.keys()),
        default=st.session_state.technologies,
    )
    st.session_state.technologies = selected

    st.markdown("")
    cols = st.columns(3)

    descriptions = {
        "☀️ 태양광 발전": "건물에서 전기를 생산하는 재생에너지 요소",
        "🌬️ 자연환기": "기계 장치에만 의존하지 않고 자연적인 공기 흐름을 활용",
        "🪟 외부 차양": "강한 햇빛을 조절해 냉방 부담을 줄이는 요소",
        "🌱 녹화 지붕": "옥상에 식생을 적용하는 방식",
        "💧 빗물 이용": "빗물을 모아 건물의 물 사용에 활용",
        "🔄 물 재이용": "사용한 물을 처리해 다시 활용하는 방식",
    }

    for i, item in enumerate(TECHNOLOGIES):
        with cols[i % 3]:
            checked = "SELECTED" if item in selected else "AVAILABLE"
            st.markdown(f"""
<div class="info-card" style="margin-bottom:14px;">
    <div class="info-label">{checked}</div>
    <div class="info-value">{item}</div>
    <div class="small-text">{descriptions[item]}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="source-box">
<b>REFERENCE</b><br>
IPCC의 기후변화 대응 관련 자료에서는 녹화, 도시 식생, 차양,
자연환기, 단열, 물 관리 등 다양한 건축·도시 대응 방법을 다룹니다.
</div>
""", unsafe_allow_html=True)

    if st.button("다음 → 꾸미기", type="primary", use_container_width=True):
        st.session_state.page = "DECOR"
        st.rerun()


# ---------------------------------------------------------
# DECOR
# ---------------------------------------------------------
elif st.session_state.page == "DECOR":
    st.markdown('<div class="hero-title" style="font-size:40px;">05 / DECORATE</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">MAKE THE BUILDING PART OF NATURE.</div>', unsafe_allow_html=True)

    selected = st.multiselect(
        "건축물 주변과 외관을 꾸며보세요.",
        list(DECORATIONS.keys()),
        default=st.session_state.decorations,
    )
    st.session_state.decorations = selected

    st.html(building_html())

    st.markdown("")
    if st.button("🏗️ 건축물 완성하기", type="primary", use_container_width=True):
        st.session_state.completed = True
        # 핵심 수정:
        # 완성 버튼을 누르면 결과를 RESULT 페이지에만 보여주는 것이 아니라
        # 바로 HOME으로 돌아가 완성된 건축물이 보이게 함.
        st.session_state.page = "HOME"
        st.rerun()


# ---------------------------------------------------------
# RESULT
# ---------------------------------------------------------
elif st.session_state.page == "RESULT":
    st.markdown('<div class="hero-title" style="font-size:40px;">DESIGN REPORT</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">YOUR 2050 ARCHITECTURE PROFILE</div>', unsafe_allow_html=True)

    score = calculate_pollution()

    st.html(building_html())

    st.markdown("")
    if score <= 40:
        st.success(f"🌍 MISSION SUCCESS — 오염지수 {score}")
    else:
        st.error(f"⚠️ MISSION FAILED — 오염지수 {score}")

    a, b, c = st.columns(3)
    with a:
        st.metric("오염지수", score, "낮을수록 좋음")
    with b:
        st.metric("미래 기술", len(st.session_state.technologies))
    with c:
        st.metric("환경 요소", len(st.session_state.decorations))

    st.markdown("## 🧾 설계 선택")

    st.markdown(f"""
<div class="glass-card">
    <div class="info-label">BUILDING USE</div>
    <h3>{st.session_state.usage}</h3>
    <div class="small-text">{USAGES[st.session_state.usage]["desc"]}</div>
    <hr style="border-color:rgba(255,255,255,.08);">
    <div class="info-label">FORM</div>
    <h3>{st.session_state.shape}</h3>
    <div class="small-text">{SHAPES[st.session_state.shape]["desc"]}</div>
    <hr style="border-color:rgba(255,255,255,.08);">
    <div class="info-label">MATERIAL</div>
    <h3>{st.session_state.material}</h3>
    <div class="small-text">{MATERIALS[st.session_state.material]["desc"]}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("### ⚡ 적용한 미래 기술")
    if st.session_state.technologies:
        for item in st.session_state.technologies:
            st.write("•", item)
    else:
        st.caption("선택한 미래 기술이 없습니다.")

    st.markdown("### 🌿 적용한 꾸미기 요소")
    if st.session_state.decorations:
        for item in st.session_state.decorations:
            st.write("•", item)
    else:
        st.caption("선택한 환경 요소가 없습니다.")

    st.markdown("""
<div class="source-box" style="margin-top:20px;">
<b>SOURCES</b><br>
• UNEP Global Status Report for Buildings and Construction<br>
• UNEP Building Materials and the Climate<br>
• IPCC AR6 WGII Chapter 6<br><br>
※ 본 프로그램의 오염지수는 실제 건물의 탄소배출량을 계산하는 값이 아니라
건축 요소의 환경 영향을 게임 방식으로 표현한 가상의 지표입니다.
</div>
""", unsafe_allow_html=True)

    st.markdown("")
    c1, c2 = st.columns(2)

    with c1:
        if st.button("🏠 메인 화면으로", use_container_width=True):
            st.session_state.page = "HOME"
            st.rerun()

    with c2:
        if st.button("🔄 새로운 설계 시작", use_container_width=True):
            st.session_state.completed = False
            st.session_state.usage = "🏠 미래 주거시설"
            st.session_state.shape = "🏙️ 수직형 타워"
            st.session_state.material = "🧱 저탄소 콘크리트"
            st.session_state.technologies = []
            st.session_state.decorations = []
            st.session_state.page = "USAGE"
            st.rerun()
