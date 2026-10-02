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
        "cost": 10,
        "effect": "생활공간이므로 냉난방, 조명, 온수, 물 사용 등이 발생할 수 있습니다.",
        "limit": "실제 환경 영향은 건물 규모와 에너지 사용 방식에 따라 달라집니다.",
        "class": "housing",
        "badge": "LIVING",
    },
    "🏫 미래 학교": {
        "impact": 2,
        "cost": 8,
        "effect": "자연채광과 자연환기를 활용하기 쉬운 공간으로 설정해 오염지수 영향을 낮게 반영했습니다.",
        "limit": "실제 학교의 에너지 사용량은 지역, 운영시간, 냉난방 설비 등에 따라 달라집니다.",
        "class": "school",
        "badge": "EDU",
    },
    "🏥 미래 병원": {
        "impact": 6,
        "cost": 16,
        "effect": "의료장비와 환기, 냉난방 등 지속적인 에너지 사용이 필요할 수 있어 게임에서는 높은 값을 적용했습니다.",
        "limit": "실제 병원의 환경 성능을 단순히 용도 하나만으로 판단할 수는 없습니다.",
        "class": "hospital",
        "badge": "MED",
    },
    "🔬 미래 연구센터": {
        "impact": 3,
        "cost": 12,
        "effect": "연구장비가 필요하지만 효율적인 공간과 설비를 설계할 수 있는 것으로 설정했습니다.",
        "limit": "실험 종류와 장비에 따라 에너지 사용량은 크게 달라질 수 있습니다.",
        "class": "research",
        "badge": "LAB",
    },
}

SHAPES = {
    "🏙️ 수직형 타워": {
        "impact": 7,
        "cost": 18,
        "effect": "높이를 크게 확보해 같은 부지에 많은 공간을 넣는 형태입니다. 게임에서는 구조와 외피 사용량을 고려해 부담을 높게 반영했습니다.",
        "limit": "실제 환경 성능은 높이만으로 결정되지 않고 설계와 재료에 따라 달라집니다.",
        "class": "tower",
    },
    "🌿 테라스형 건축": {
        "impact": 3,
        "cost": 15,
        "effect": "층마다 외부공간을 만들어 차양이나 녹지를 적용하기 쉬운 형태로 설정했습니다.",
        "limit": "테라스가 많아지면 구조와 외피가 복잡해질 수도 있습니다.",
        "class": "terrace",
    },
    "🛸 돔형 건축": {
        "impact": 2,
        "cost": 22,
        "effect": "곡면 외피를 가진 미래형 형태로 표현해 외부 환경에 대응하는 건축물로 설정했습니다.",
        "limit": "곡면 구조는 제작과 시공 방식에 따라 재료와 비용이 달라질 수 있습니다.",
        "class": "dome",
    },
    "🌍 저층 생태형": {
        "impact": 1,
        "cost": 12,
        "effect": "낮은 건물과 넓은 외부공간을 활용해 녹지와 건축물을 연결하기 쉬운 형태로 설정했습니다.",
        "limit": "넓은 부지가 필요할 수 있어 모든 지역에 적합한 형태는 아닙니다.",
        "class": "eco",
    },
}

MATERIALS = {
    "🧱 저탄소 콘크리트": {
        "impact": 6,
        "effect": "콘크리트의 생산 단계에서 발생하는 탄소 영향을 줄이는 방향의 재료로 설정했습니다.",
        "limit": "저탄소라고 해서 환경 영향이 0이 되는 것은 아니며 실제 성능은 생산 방식과 배합 등에 따라 달라집니다.",
        "class": "concrete",
        "cost": 12,
    },
    "🔩 저탄소 철강": {
        "impact": 5,
        "effect": "철강 생산 과정의 탄소 영향을 낮추는 방향의 재료로 설정했습니다. 철골 구조의 장점을 유지하면서 환경 부담을 줄이는 선택입니다.",
        "limit": "실제 탄소 영향은 생산 전력과 제조 방식 등에 따라 달라집니다.",
        "class": "steel",
        "cost": 18,
    },
    "🌲 목재·바이오 기반": {
        "impact": 2,
        "effect": "목재와 바이오 기반 재료를 활용하는 선택으로, 재료 생산 단계의 환경 부담을 낮추는 방향으로 반영했습니다.",
        "limit": "산림 관리, 생산 과정, 운송과 수명까지 함께 살펴야 합니다.",
        "class": "wood",
        "cost": 24,
    },
    "♻️ 재사용·재활용 재료": {
        "impact": 0,
        "effect": "기존 자원을 다시 활용해 새로운 재료 생산을 줄이는 자원순환 방식으로 설정했습니다.",
        "limit": "재사용 가능 여부와 품질, 운송 과정 등에 따라 실제 효과가 달라집니다.",
        "class": "recycled",
        "cost": 20,
    },
}

TECHNOLOGIES = {
    "☀️ 태양광 발전": {
        "impact": -10,
        "effect": "건물에서 전기를 생산해 외부 전력 사용을 줄이는 방향의 효과를 게임에 반영합니다.",
        "limit": "발전량은 일사량, 설치면적, 방향과 효율 등에 따라 달라집니다.",
        "visual": "solar",
        "cost": 30,
    },
    "🌬️ 자연환기": {
        "impact": -7,
        "effect": "바람과 개구부를 이용해 실내 공기를 순환시키고 기계식 냉방·환기 의존을 줄이는 방향으로 반영합니다.",
        "limit": "외부 온도와 공기질, 바람 조건이 좋지 않은 때에는 다른 설비가 필요할 수 있습니다.",
        "visual": "vent",
        "cost": 15,
    },
    "🪟 외부 차양": {
        "impact": -6,
        "effect": "강한 햇빛의 실내 유입을 조절해 냉방 부담을 낮추는 방향으로 반영합니다.",
        "limit": "차양의 위치와 방향을 잘못 설계하면 자연채광을 줄일 수도 있습니다.",
        "visual": "shade",
        "cost": 10,
    },
    "🌱 녹화 지붕": {
        "impact": -7,
        "effect": "옥상에 식생을 적용해 열환경과 빗물 관리에 도움을 주는 요소로 반영합니다.",
        "limit": "구조 하중, 관리, 물 공급 등을 고려해야 합니다.",
        "visual": "greenroof",
        "cost": 18,
    },
    "💧 빗물 이용": {
        "impact": -5,
        "effect": "빗물을 모아 조경이나 일부 용도에 활용해 수돗물 사용을 줄이는 방향으로 반영합니다.",
        "limit": "강수량과 저장시설 크기에 따라 이용 가능한 양이 달라집니다.",
        "visual": "rain",
        "cost": 7,
    },
    "🔄 물 재이용": {
        "impact": -5,
        "effect": "사용한 물을 처리해 다시 이용함으로써 물 사용량을 줄이는 방향으로 반영합니다.",
        "limit": "처리시설과 유지관리가 필요하며 모든 용도의 물을 같은 방식으로 재사용할 수 있는 것은 아닙니다.",
        "visual": "reuse",
        "cost": 15,
    },
}

COLORS = {
    "미래형 민트": "#5D7F7A",
    "사막 모래": "#A77D5C",
    "화이트": "#C9D4D0",
    "딥 블루": "#345C78",
    "포레스트": "#46634E",
    "오렌지": "#A76543",
}

# =========================================================
# 점수
# =========================================================
def pollution_score():
    score = 42
    score += USAGES[st.session_state.usage]["impact"]
    score += SHAPES[st.session_state.shape]["impact"]
    score += MATERIALS[st.session_state.material]["impact"]
    for tech in st.session_state.technologies:
        score += TECHNOLOGIES[tech]["impact"]
    return max(0, min(100, score))

def design_cost():
    # 예산은 용도, 형태, 자재, 미래 기술을 고를 때마다 차감됩니다.
    total = USAGES[st.session_state.usage]["cost"]
    total += SHAPES[st.session_state.shape]["cost"]
    total += MATERIALS[st.session_state.material]["cost"]
    total += sum(TECHNOLOGIES[tech]["cost"] for tech in st.session_state.technologies)
    return total

def remaining_budget():
    return st.session_state.budget - design_cost()

def budget_text(value):
    sign = "-" if value < 0 else ""
    return f"{sign}{abs(value):,}억원"

def mission_success():
    return pollution_score() <= 40 and remaining_budget() >= 0

# =========================================================
# 3D 건축물 HTML
# f-string을 쓰지 않고 placeholder replace를 사용해
# CSS의 { } 때문에 NameError가 발생하지 않도록 함.
# =========================================================
def building_html():
    shape = SHAPES[st.session_state.shape]["class"]
    usage = USAGES[st.session_state.usage]["class"]
    material = MATERIALS[st.session_state.material]["class"]
    color = st.session_state.building_color
    badge = USAGES[st.session_state.usage]["badge"]

    feature_html = ""
    side_feature_html = ""
    roof_feature_html = ""
    dome_feature_html = ""
    techs = st.session_state.technologies
    if "☀️ 태양광 발전" in techs:
        feature_html += '<div class="solar-panel sp1"></div><div class="solar-panel sp2"></div>'
        side_feature_html += '<div class="side-solar ss1"></div><div class="side-solar ss2"></div>'
        roof_feature_html += '<div class="roof-solar rs1"></div><div class="roof-solar rs2"></div>'
        dome_feature_html += '<div class="dome-tech solar-dome"></div>'
    if "🌬️ 자연환기" in techs:
        feature_html += '<div class="air-ring ar1">AIR</div><div class="air-ring ar2">AIR</div>'
        side_feature_html += '<div class="side-vent sv1">AIR</div><div class="side-vent sv2">AIR</div>'
        roof_feature_html += '<div class="roof-vent rv1">AIR</div>'
        dome_feature_html += '<div class="dome-tech vent-dome">AIR</div>'
    if "🪟 외부 차양" in techs:
        feature_html += '<div class="shade sh1"></div><div class="shade sh2"></div><div class="shade sh3"></div>'
        side_feature_html += '<div class="side-shade ssh1"></div><div class="side-shade ssh2"></div>'
        dome_feature_html += '<div class="dome-shade ds1"></div><div class="dome-shade ds2"></div>'
    if "🌱 녹화 지붕" in techs:
        feature_html += '<div class="green-roof">GREEN ROOF</div>'
        roof_feature_html += '<div class="roof-green rg1">GREEN</div><div class="roof-green rg2">GREEN</div>'
        dome_feature_html += '<div class="dome-green">GREEN</div>'
    if "💧 빗물 이용" in techs:
        feature_html += '<div class="water-tank">RAIN<br>WATER</div>'
        side_feature_html += '<div class="side-water swt1">RAIN</div><div class="side-water swt2">RAIN</div>'
        roof_feature_html += '<div class="roof-water rw1"></div>'
        dome_feature_html += '<div class="dome-water">RAIN</div>'
    if "🔄 물 재이용" in techs:
        feature_html += '<div class="reuse-mark">↻</div>'
        side_feature_html += '<div class="side-reuse sru1">↻</div><div class="side-reuse sru2">↻</div>'
        dome_feature_html += '<div class="dome-reuse">↻</div>'

    html = """
<div id="futureViewer" class="future-viewer">
    <div class="drag-guide">↔ DRAG TO ROTATE 360°</div>
    <div class="desert-sky"></div>
    <div class="sun"></div>
    <div class="dust dust1"></div><div class="dust dust2"></div><div class="dust dust3"></div>
    <div class="desert-floor">
        <div class="crack c1"></div><div class="crack c2"></div><div class="crack c3"></div>
        <div class="dune-line dl1"></div><div class="dune-line dl2"></div>
        <div class="rock r1"></div><div class="rock r2"></div><div class="rock r3"></div>
    </div>

    <div class="building-stage">
        <div id="building3d" class="building-3d __SHAPE__ __USAGE__ __MATERIAL__ __TECH__" style="--building-color:__COLOR__">
            <div class="face front">
                <div class="surface-tech"></div>
                <div class="top-cap"></div>
                <div class="badge">__BADGE__</div>
                <div class="window-grid">
                    <span></span><span></span><span></span><span></span>
                    <span></span><span></span><span></span><span></span>
                    <span></span><span></span><span></span><span></span>
                    <span></span><span></span><span></span><span></span>
                </div>
                <div class="vertical-core"></div>
                __FEATURES__
            </div>
            <div class="face right"><div class="surface-tech"></div><div class="side-lines"></div><div class="side-window-grid"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>__SIDE_FEATURES__</div>
            <div class="face left"><div class="surface-tech"></div><div class="side-lines"></div><div class="side-window-grid"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>__SIDE_FEATURES__</div>
            <div class="face back"><div class="surface-tech"></div><div class="back-panel"></div><div class="back-window-grid"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>__SIDE_FEATURES__</div>
            <div class="face top"><div class="surface-tech"></div><div class="roof-grid"></div><div class="skylight s1"></div><div class="skylight s2"></div><div class="skylight s3"></div>__ROOF_FEATURES__</div>
            <div class="face bottom"><div class="surface-tech"></div></div>
            <div class="dome-shell">
                <div class="dome-band band1"></div><div class="dome-band band2"></div><div class="dome-band band3"></div><div class="dome-band band4"></div><div class="dome-band band5"></div><div class="dome-meridian dm1"></div><div class="dome-meridian dm2"></div><div class="dome-meridian dm3"></div>
                <div class="dome-window dw1"></div><div class="dome-window dw2"></div><div class="dome-window dw3"></div><div class="dome-window dw4"></div><div class="dome-window dw5"></div><div class="dome-window dw6"></div><div class="dome-window dw7"></div><div class="dome-window dw8"></div>
                <div class="dome-ring dr1"></div><div class="dome-ring dr2"></div>
                __DOME_FEATURES__
            </div>
        </div>
    </div>

    <div class="viewer-caption">
        <b>2050 / ONE BUILDING</b>
        <span>EARTH CONDITION : DESERTIFIED</span>
    </div>
    <button id="reset3d" class="reset3d">RESET VIEW</button>
</div>

<style>
.future-viewer{position:relative;width:100%;height:610px;overflow:hidden;border-radius:26px;border:1px solid rgba(255,235,205,.22);background:#4a362c;perspective:1100px;cursor:grab;user-select:none;touch-action:none;box-shadow:0 30px 80px rgba(0,0,0,.5)}
.future-viewer:active{cursor:grabbing}
.desert-sky{position:absolute;inset:0 0 36% 0;background:radial-gradient(circle at 74% 24%,rgba(255,223,161,.85) 0 52px,rgba(255,177,91,.18) 53px,transparent 180px),linear-gradient(180deg,#121b1e 0%,#3e403c 44%,#936246 100%)}
.sun{position:absolute;right:19%;top:16%;width:78px;height:78px;border-radius:50%;background:radial-gradient(circle,#ffe5a8,#d99a61 58%,#9b5c45);box-shadow:0 0 75px rgba(255,189,111,.32)}
.dust{position:absolute;border-radius:50%;filter:blur(12px);background:rgba(231,188,140,.16)}
.dust1{width:500px;height:90px;left:0;top:43%}.dust2{width:350px;height:80px;right:3%;top:48%}.dust3{width:260px;height:70px;left:38%;top:34%}
.desert-floor{position:absolute;left:-10%;bottom:-230px;width:120%;height:460px;transform:rotateX(61deg);transform-origin:top center;background:radial-gradient(ellipse at 50% 5%,#a36d48 0%,#704935 43%,#30231e 78%,#171112 100%);box-shadow:inset 0 55px 75px rgba(255,190,120,.08)}
.crack{position:absolute;height:2px;background:rgba(51,30,23,.5);transform-origin:left center}.c1{width:190px;left:25%;top:24%;transform:rotate(18deg)}.c2{width:260px;left:53%;top:40%;transform:rotate(-12deg)}.c3{width:150px;left:40%;top:62%;transform:rotate(8deg)}
.dune-line{position:absolute;height:2px;border-radius:50%;background:rgba(245,203,145,.16)}.dl1{width:62%;left:17%;top:25%;transform:rotate(-4deg)}.dl2{width:45%;right:15%;top:51%;transform:rotate(6deg)}
.rock{position:absolute;background:linear-gradient(145deg,#6e4937,#281c19);clip-path:polygon(5% 100%,24% 36%,55% 8%,85% 40%,100% 100%)}.r1{width:100px;height:70px;left:9%;top:18%}.r2{width:150px;height:84px;right:10%;top:26%}.r3{width:78px;height:50px;right:29%;top:13%}
.building-stage{position:absolute;left:50%;top:48%;width:440px;height:430px;transform:translate(-50%,-50%);transform-style:preserve-3d}
.building-3d{--w:210px;--h:310px;--d:150px;--building-color:#5D7F7A;position:absolute;left:50%;bottom:18px;width:var(--w);height:var(--h);transform-style:preserve-3d;transform-origin:center center;transform:translateX(-50%) rotateX(-4deg) rotateY(0deg)}
.building-3d.tower{--w:180px;--h:350px;--d:130px}.building-3d.terrace{--w:240px;--h:285px;--d:165px}.building-3d.dome{--w:280px;--h:250px;--d:190px}.building-3d.eco{--w:300px;--h:215px;--d:210px}
.face{position:absolute;box-sizing:border-box;border:1px solid rgba(235,255,247,.27);overflow:hidden;backface-visibility:hidden}.front,.back{width:var(--w);height:var(--h)}.front{transform:translateZ(calc(var(--d)/2));background:linear-gradient(90deg,rgba(255,255,255,.09),transparent 18%,transparent 82%,rgba(0,0,0,.18)),var(--building-color)}.back{transform:rotateY(180deg) translateZ(calc(var(--d)/2));background:#263735}.right,.left{width:var(--d);height:var(--h);left:calc((var(--w) - var(--d))/2)}.right{transform:rotateY(90deg) translateZ(calc(var(--w)/2));background:linear-gradient(90deg,#172827,#4a625d)}.left{transform:rotateY(-90deg) translateZ(calc(var(--w)/2));background:linear-gradient(90deg,#4a625d,#162424)}.top,.bottom{width:var(--w);height:var(--d);top:calc((var(--h) - var(--d))/2)}.top{transform:rotateX(90deg) translateZ(calc(var(--h)/2));background:linear-gradient(135deg,#899a91,#354945)}.bottom{transform:rotateX(-90deg) translateZ(calc(var(--h)/2));background:#0c1617}
.concrete .face{background:repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 3px,transparent 3px 14px),linear-gradient(90deg,rgba(255,255,255,.08),transparent 20%,rgba(0,0,0,.16)),var(--building-color)}
.steel .face{background:linear-gradient(105deg,rgba(255,255,255,.26),transparent 22%,rgba(255,255,255,.08) 52%,rgba(0,0,0,.18)),var(--building-color)}
.wood .face{background:repeating-linear-gradient(90deg,rgba(72,39,22,.15) 0 3px,transparent 3px 15px),linear-gradient(90deg,rgba(255,255,255,.07),transparent 30%,rgba(0,0,0,.12)),var(--building-color)}
.recycled .face{background:repeating-linear-gradient(45deg,rgba(255,255,255,.10) 0 8px,transparent 8px 18px),linear-gradient(135deg,rgba(255,255,255,.08),transparent 45%,rgba(0,0,0,.14)),var(--building-color)}
.concrete .top,.concrete .bottom,.steel .top,.steel .bottom,.wood .top,.wood .bottom,.recycled .top,.recycled .bottom{background-image:inherit}
.terrace .front{clip-path:polygon(0 0,100% 0,100% 100%,0 100%,0 74%,8% 74%,8% 57%,0 57%,0 40%,8% 40%,8% 23%,0 23%)}
.dome .face.front,.dome .face.back,.dome .face.left,.dome .face.right{background:rgba(0,0,0,0)!important;border-color:transparent!important}
/* 360-degree building detailing */
.side-solar{position:absolute;z-index:9;width:42px;height:72px;border:1px solid rgba(151,235,220,.5);background:repeating-linear-gradient(90deg,rgba(170,255,242,.24) 0 1px,transparent 1px 8px),#173c43;box-shadow:0 0 10px rgba(120,230,204,.10)}
.ss1{right:10px;top:48px;transform:skewY(-10deg)}.ss2{right:10px;top:136px;transform:skewY(-10deg)}
.roof-solar{position:absolute;z-index:8;width:56px;height:28px;border:1px solid rgba(151,235,220,.5);background:repeating-linear-gradient(90deg,rgba(170,255,242,.25) 0 1px,transparent 1px 9px),#173c43;transform:skewX(-12deg)}.rs1{left:32px;top:30px}.rs2{right:32px;top:30px}
.side-vent{position:absolute;z-index:10;width:27px;height:27px;border:2px solid rgba(156,232,215,.65);border-radius:50%;color:#dffff8;text-align:center;font:700 5px Orbitron;line-height:23px;background:rgba(9,38,38,.75)}.sv1{right:18px;top:90px}.sv2{left:18px;top:165px}
.roof-vent{position:absolute;z-index:10;left:50%;top:50%;transform:translate(-50%,-50%);width:38px;height:38px;border:2px solid rgba(156,232,215,.65);border-radius:50%;color:#dffff8;text-align:center;font:700 6px Orbitron;line-height:34px;background:rgba(9,38,38,.8)}
.side-shade{position:absolute;z-index:9;width:72px;height:5px;border-radius:4px;background:rgba(215,224,219,.9);box-shadow:0 3px 5px rgba(0,0,0,.25)}.ssh1{right:2px;top:80px;transform:rotate(-4deg)}.ssh2{left:2px;top:150px;transform:rotate(4deg)}
.roof-green{position:absolute;z-index:10;width:72px;height:20px;border-radius:50%;background:linear-gradient(#87b97b,#355c3c);color:#efffe9;text-align:center;font:700 6px Orbitron;line-height:20px}.rg1{left:25px;bottom:20px}.rg2{right:25px;bottom:20px}
.side-water{position:absolute;z-index:10;width:28px;height:28px;border:2px solid #78c9dc;border-radius:50%;color:#e7fbff;font:700 5px Orbitron;text-align:center;line-height:24px;background:rgba(27,105,126,.6)}.swt1{right:16px;bottom:24px}.swt2{left:16px;bottom:54px}
.roof-water{position:absolute;z-index:10;right:24px;top:18px;width:26px;height:26px;border:2px solid #78c9dc;border-radius:50%;background:rgba(27,105,126,.6)}
.side-reuse{position:absolute;z-index:10;width:27px;height:27px;border:2px dashed #82e0ca;border-radius:50%;color:#dffff7;font-size:18px;text-align:center;line-height:23px;background:rgba(7,30,29,.65)}.sru1{left:15px;bottom:22px}.sru2{right:15px;top:24px}

.dome .face.top{opacity:.25}
.dome .dome-shell{position:absolute;left:50%;bottom:0;width:280px;height:225px;transform:translateX(-50%);transform-style:preserve-3d;z-index:7;pointer-events:none}
.dome-band{position:absolute;left:50%;bottom:0;width:250px;height:190px;transform:translateX(-50%);border:2px solid rgba(230,255,248,.32);border-bottom:0;border-radius:50% 50% 0 0;clip-path:polygon(9% 100%,91% 100%,72% 55%,62% 25%,50% 0,38% 25%,28% 55%);background:linear-gradient(90deg,rgba(255,255,255,.10),rgba(255,255,255,.03) 48%,rgba(0,0,0,.18)),var(--building-color);transform-origin:center bottom}
.band1{transform:translateX(-50%) translateZ(22px)}
.band2{transform:translateX(-50%) translateZ(0) scale(.92);opacity:.72}
.band3{transform:translateX(-50%) translateZ(-22px) scale(.84);opacity:.52}
.dome-shell:before,.dome-shell:after{content:"";position:absolute;left:50%;bottom:0;width:242px;height:175px;transform:translateX(-50%) rotateY(90deg);border:2px solid rgba(230,255,248,.24);border-bottom:0;border-radius:50% 50% 0 0;clip-path:polygon(9% 100%,91% 100%,72% 55%,62% 25%,50% 0,38% 25%,28% 55%);background:rgba(110,180,164,.10)}
.dome-shell:after{transform:translateX(-50%) rotateY(45deg);opacity:.6}
.dome-meridian{position:absolute;left:50%;bottom:0;width:238px;height:190px;transform:translateX(-50%);border:2px solid rgba(230,255,248,.20);border-bottom:0;border-radius:50% 50% 0 0;clip-path:polygon(9% 100%,91% 100%,72% 55%,62% 25%,50% 0,38% 25%,28% 55%);pointer-events:none;z-index:11}.dm1{transform:translateX(-50%) rotateY(35deg)}.dm2{transform:translateX(-50%) rotateY(-35deg);opacity:.7}.dm3{transform:translateX(-50%) rotateY(90deg);opacity:.55}
.dome-window{position:absolute;width:30px;height:24px;border:1px solid rgba(239,255,251,.55);background:linear-gradient(135deg,#e8fff8,#5aa596);border-radius:45% 45% 20% 20%;box-shadow:0 0 12px rgba(120,230,204,.18);z-index:12}
.dw1{left:28px;bottom:58px;transform:rotate(-15deg)}.dw2{left:83px;bottom:103px}.dw3{right:83px;bottom:103px}.dw4{right:28px;bottom:58px;transform:rotate(15deg)}
.dome-ring{position:absolute;left:50%;transform:translateX(-50%);border:1px solid rgba(225,255,247,.34);border-radius:50%;z-index:13;pointer-events:none}.dr1{bottom:48px;width:222px;height:40px}.dr2{bottom:103px;width:150px;height:30px;opacity:.65}
.dome-tech{position:absolute;z-index:14;pointer-events:none}.solar-dome{left:50%;top:18px;transform:translateX(-50%);width:88px;height:38px;border:1px solid #8de2d1;background:repeating-linear-gradient(90deg,rgba(170,255,242,.28) 0 1px,transparent 1px 14px),#163944;clip-path:polygon(18% 100%,82% 100%,65% 0,35% 0)}
.vent-dome{left:50%;top:68px;transform:translateX(-50%);width:40px;height:40px;border:2px solid #9bded0;border-radius:50%;color:#e5fff9;font:700 7px Orbitron,sans-serif;text-align:center;line-height:36px}
.dome-shade{position:absolute;left:50%;width:86px;height:7px;transform:translateX(-50%);background:#c5cfca;border-radius:4px;z-index:15}.ds1{top:92px}.ds2{top:122px}
.dome-green{left:50%;top:-2px;transform:translateX(-50%);width:120px;height:18px;border-radius:50%;background:linear-gradient(#86b877,#355e3c);color:#eaffdf;text-align:center;font:700 7px Orbitron,sans-serif;line-height:18px}
.dome-water{right:35px;bottom:35px;width:36px;height:36px;border:2px solid #78c9dc;border-radius:50%;color:#dffaff;font:700 6px Orbitron,sans-serif;text-align:center;line-height:36px;background:rgba(27,105,126,.55)}
.dome-reuse{left:35px;bottom:34px;width:34px;height:34px;border:2px dashed #82e0ca;border-radius:50%;color:#dffff7;font-size:22px;text-align:center;line-height:30px}
.eco .front{border-radius:18px 18px 5px 5px;background:linear-gradient(180deg,rgba(116,170,116,.30),transparent 30%),var(--building-color)}
.top-cap{position:absolute;left:4%;right:4%;top:0;height:9px;background:rgba(226,246,238,.34)}
.badge{position:absolute;top:14px;right:14px;z-index:9;padding:5px 8px;background:rgba(0,0,0,.30);border:1px solid rgba(255,255,255,.28);color:#eafff7;font:700 10px 'Orbitron',sans-serif;letter-spacing:1px}
.window-grid{position:absolute;inset:38px 23px;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:17px;gap:22px 15px}.window-grid span{background:linear-gradient(180deg,#e1fff3,#71b29f);border:1px solid rgba(255,255,255,.38);box-shadow:0 0 10px rgba(140,240,209,.20)}
.school .window-grid span:nth-child(3n){background:linear-gradient(180deg,#dcecff,#7395be)}.hospital .window-grid span{background:linear-gradient(180deg,#f2ffff,#8fc5c6)}.research .window-grid span:nth-child(even){background:linear-gradient(180deg,#ddfff8,#5db8a7)}
.housing .front:after{content:'';position:absolute;left:10%;right:10%;bottom:13px;height:24px;border-top:2px solid rgba(231,255,247,.25);border-bottom:2px solid rgba(231,255,247,.16)}
.school .front:after{content:'CAMPUS';position:absolute;left:13px;bottom:12px;color:rgba(235,255,249,.65);font:700 8px 'Orbitron',sans-serif;letter-spacing:1px}.hospital .front:after{content:'+';position:absolute;left:50%;bottom:12px;transform:translateX(-50%);font:800 24px Arial;color:#d9ffff}.research .front:after{content:'R-2050';position:absolute;left:12px;bottom:12px;color:rgba(222,255,249,.7);font:700 8px 'Orbitron',sans-serif}
.vertical-core{position:absolute;left:48%;top:0;bottom:0;width:4px;background:rgba(218,255,246,.10)}
.side-lines{position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent 0 24px,rgba(220,245,237,.10) 24px 27px)}
.side-window{position:absolute;z-index:6;left:18px;width:48px;height:17px;background:#8fc6b6;box-shadow:0 0 9px rgba(145,230,206,.14)}.sw1{top:42px}.sw2{top:120px}.sw3{top:198px}
.back-panel{position:absolute;inset:18px;border:1px solid rgba(220,245,237,.13);background:repeating-linear-gradient(0deg,rgba(255,255,255,.04) 0 3px,transparent 3px 17px)}
.roof-grid{position:absolute;inset:12px;border:1px solid rgba(255,255,255,.15);background:repeating-linear-gradient(90deg,transparent 0 20px,rgba(255,255,255,.08) 20px 21px),repeating-linear-gradient(0deg,transparent 0 20px,rgba(255,255,255,.08) 20px 21px)}
.surface-tech{position:absolute;inset:0;z-index:2;pointer-events:none;opacity:0}
/* 선택한 미래 기술의 흔적을 모든 면에 적용 */
.future-viewer .surface-tech{opacity:.18}
.solar .surface-tech{opacity:.48;background:repeating-linear-gradient(90deg,transparent 0 23px,rgba(130,232,218,.22) 23px 25px),repeating-linear-gradient(0deg,transparent 0 23px,rgba(130,232,218,.18) 23px 25px);mix-blend-mode:screen}
.vent .surface-tech{opacity:.42;background:radial-gradient(circle at 25% 35%,rgba(154,224,211,.42) 0 2px,transparent 3px),radial-gradient(circle at 72% 66%,rgba(154,224,211,.35) 0 2px,transparent 3px);background-size:44px 44px,52px 52px}
.shade .surface-tech{opacity:.72;background:repeating-linear-gradient(0deg,transparent 0 55px,rgba(220,231,223,.34) 55px 62px);}
.greenroof .surface-tech{opacity:.36;background:radial-gradient(circle at 20% 20%,rgba(117,184,104,.45) 0 10px,transparent 11px),radial-gradient(circle at 75% 70%,rgba(117,184,104,.40) 0 13px,transparent 14px);background-size:70px 65px,85px 75px}
.rain .surface-tech{opacity:.44;background:repeating-linear-gradient(90deg,transparent 0 28px,rgba(104,202,226,.30) 28px 30px)}
.reuse .surface-tech{opacity:.40;background:repeating-linear-gradient(45deg,transparent 0 18px,rgba(129,225,203,.25) 18px 22px)}
.solar-panel{position:absolute;z-index:10;width:58px;height:37px;border:1px solid #8de2d1;background:repeating-linear-gradient(90deg,rgba(170,255,242,.24) 0 1px,transparent 1px 13px),repeating-linear-gradient(0deg,rgba(170,255,242,.24) 0 1px,transparent 1px 12px),#163944;transform:skewX(-15deg) rotate(-12deg)}.sp1{right:14px;top:9px}.sp2{left:13px;top:18px}
.air-ring{position:absolute;z-index:10;width:42px;height:42px;border:2px solid #99ddd0;border-radius:50%;color:#dffef7;font:700 8px 'Orbitron',sans-serif;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.18)}.ar1{left:11px;top:43%}.ar2{right:11px;top:54%}
.shade{position:absolute;z-index:10;left:8%;width:84%;height:8px;background:#bdc8c2;border-radius:3px;box-shadow:0 3px 0 rgba(0,0,0,.2)}.sh1{top:32%}.sh2{top:51%}.sh3{top:70%}
.green-roof{position:absolute;z-index:11;top:-7px;left:7%;width:86%;height:21px;border-radius:50%;background:linear-gradient(#7aa96f,#315c3d);box-shadow:0 0 18px rgba(105,189,121,.22);color:#eaffdf;text-align:center;font:700 7px 'Orbitron',sans-serif;padding-top:5px}
.water-tank{position:absolute;z-index:11;right:9px;bottom:12px;width:47px;height:47px;border-radius:50%;border:2px solid #78c9dc;background:rgba(27,105,126,.55);color:#dffaff;font:700 6px 'Orbitron',sans-serif;text-align:center;padding-top:14px}.reuse-mark{position:absolute;z-index:11;left:12px;bottom:15px;width:42px;height:42px;border:3px dashed #82e0ca;border-radius:50%;color:#dffff7;font-size:25px;text-align:center;line-height:36px}
.building-3d:after{content:"";position:absolute;left:50%;bottom:-18px;width:calc(var(--w) + 38px);height:24px;transform:translateX(-50%) rotateX(70deg);background:radial-gradient(ellipse,rgba(0,0,0,.62),transparent 70%);filter:blur(5px);pointer-events:none}
.building-3d .top-cap{position:absolute;z-index:8;left:8%;right:8%;top:10px;height:13px;border:1px solid rgba(230,255,247,.25);border-radius:5px;background:linear-gradient(90deg,rgba(255,255,255,.20),rgba(255,255,255,.04),rgba(0,0,0,.20))}
.building-3d .badge{position:absolute;z-index:9;right:10px;bottom:10px;padding:5px 7px;border:1px solid rgba(220,255,247,.35);background:rgba(4,15,16,.48);color:#eafff9;font:800 8px 'Orbitron',sans-serif;letter-spacing:1px}
.building-3d .window-grid{position:absolute;z-index:5;inset:48px 18px 28px;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:17px;gap:13px 8px;opacity:.94}
.building-3d .window-grid span{border:1px solid rgba(225,255,249,.32);background:linear-gradient(135deg,rgba(210,250,240,.88),rgba(35,73,75,.70));box-shadow:inset 0 0 8px rgba(230,255,250,.12),0 0 8px rgba(122,225,203,.08);border-radius:2px}
.side-window-grid{position:absolute;inset:30px 10px;display:grid;grid-template-columns:repeat(2,1fr);grid-auto-rows:20px;gap:17px 9px;z-index:6;transform:rotate(0deg)}
.side-window-grid span{border:1px solid rgba(225,255,249,.30);background:linear-gradient(135deg,#d7f7ec,#527f76);box-shadow:0 0 7px rgba(122,225,203,.08);border-radius:2px}
.back-window-grid{position:absolute;inset:36px 20px 26px;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:16px;gap:15px 8px;z-index:6;opacity:.75}
.back-window-grid span{border:1px solid rgba(225,255,249,.24);background:linear-gradient(135deg,#c6eee3,#355c59);border-radius:2px}
.skylight{position:absolute;z-index:8;width:28px;height:18px;border:1px solid rgba(228,255,248,.38);background:linear-gradient(135deg,#d8fff4,#568d83);border-radius:4px;transform:rotate(-8deg)}
.s1{left:23%;top:28%}.s2{left:46%;top:50%}.s3{right:18%;top:28%}
.terrace .window-grid{inset:45px 30px 22px;grid-template-columns:repeat(3,1fr);gap:15px 9px}
.dome .window-grid{display:none}
.eco .window-grid{inset:45px 34px 24px;grid-template-columns:repeat(4,1fr);gap:10px 7px}
.tech-tag{position:absolute;z-index:14;left:12px;top:13px;padding:4px 6px;border-radius:5px;background:rgba(4,16,17,.68);border:1px solid rgba(161,236,221,.38);color:#eafff8;font:800 7px 'Orbitron',sans-serif;letter-spacing:1px}
.tech-tag.vent-tag{border-color:rgba(173,232,220,.38)}
.viewer-caption{position:absolute;left:24px;bottom:22px;z-index:30;padding:12px 15px;background:rgba(5,12,13,.74);border-left:3px solid #d8b47e;backdrop-filter:blur(7px)}.viewer-caption b{display:block;color:#fff;font:800 13px 'Orbitron',sans-serif;letter-spacing:1px}.viewer-caption span{display:block;color:#d4e1de;margin-top:5px;font-size:12px}
.drag-guide{position:absolute;z-index:30;top:18px;left:50%;transform:translateX(-50%);padding:9px 15px;border-radius:999px;background:rgba(5,12,13,.70);border:1px solid rgba(255,255,255,.22);color:#fff;font:700 11px 'Orbitron',sans-serif;letter-spacing:1px}.reset3d{position:absolute;right:18px;bottom:18px;z-index:40;padding:9px 12px;border:1px solid rgba(255,255,255,.22);border-radius:9px;background:rgba(5,12,13,.78);color:#fff;font:700 10px 'Orbitron',sans-serif;cursor:pointer}
</style>

<script>
(function(){
    const viewer=document.getElementById('futureViewer');
    const building=document.getElementById('building3d');
    const reset=document.getElementById('reset3d');
    if(!viewer || !building) return;
    let rotY=0, rotX=-4, dragging=false, lastX=0, lastY=0;
    function render(){ building.style.transform='translateX(-50%) rotateX('+rotX+'deg) rotateY('+rotY+'deg)'; }
    viewer.addEventListener('pointerdown',function(e){
        if(e.target===reset) return;
        dragging=true; lastX=e.clientX; lastY=e.clientY;
        try{viewer.setPointerCapture(e.pointerId);}catch(err){}
    });
    viewer.addEventListener('pointermove',function(e){
        if(!dragging) return;
        rotY += (e.clientX-lastX)*0.55;
        rotX -= (e.clientY-lastY)*0.25;
        rotX=Math.max(-28,Math.min(28,rotX));
        lastX=e.clientX; lastY=e.clientY; render();
    });
    viewer.addEventListener('pointerup',function(){dragging=false;});
    viewer.addEventListener('pointercancel',function(){dragging=false;});
    reset.addEventListener('click',function(e){e.stopPropagation();rotY=0;rotX=-4;render();});
    render();
})();
</script>
"""
    tech_classes = []
    if "☀️ 태양광 발전" in techs: tech_classes.append("solar")
    if "🌬️ 자연환기" in techs: tech_classes.append("vent")
    if "🪟 외부 차양" in techs: tech_classes.append("shade")
    if "🌱 녹화 지붕" in techs: tech_classes.append("greenroof")
    if "💧 빗물 이용" in techs: tech_classes.append("rain")
    if "🔄 물 재이용" in techs: tech_classes.append("reuse")
    tech_class = " ".join(tech_classes)

    return (html.replace("__SHAPE__", shape)
                .replace("__USAGE__", usage)
                .replace("__MATERIAL__", material)
                .replace("__COLOR__", color)
                .replace("__BADGE__", badge)
                .replace("__FEATURES__", feature_html)
                .replace("__SIDE_FEATURES__", side_feature_html)
                .replace("__ROOF_FEATURES__", roof_feature_html)
                .replace("__DOME_FEATURES__", dome_feature_html)
                .replace("__TECH__", tech_class))


def show_building():
    st.html(building_html(), unsafe_allow_javascript=True)


def effect_card(title, impact, effect, limit, cost=None):
    if impact < 0:
        impact_text = f"▼ {abs(impact)}"
        cls = "good"
    elif impact > 0:
        impact_text = f"▲ {impact}"
        cls = "bad"
    else:
        impact_text = "● 0"
        cls = "neutral"
    cost_html = f'<div class="cost-line">💰 설계 비용 <b>{cost:,}억원</b></div>' if cost is not None else ''
    return f"""
<div class="effect-card">
    <div class="effect-title">{title}</div>
    {cost_html}
    <div class="effect-label">오염지수 영향</div>
    <div class="{cls}" style="font-size:23px;margin:4px 0 10px;">{impact_text}</div>
    <div class="effect-text"><b>효과</b> · {effect}</div>
    <div class="effect-text" style="margin-top:8px;color:#aebfbc;"><b>주의/한계</b> · {limit}</div>
</div>
"""

# =========================================================
# 사이드바
# =========================================================
with st.sidebar:
    st.markdown("<div style='font:800 20px Orbitron;color:#fff;'>2050 // ARCHITECT</div>", unsafe_allow_html=True)
    st.markdown("<div style='color:#a9c0bc;font-size:13px;margin:6px 0 20px;'>ONE BUILDING / DESERT EARTH</div>", unsafe_allow_html=True)

    nav = {
        "🏠 HOME":"HOME",
        "① 건축물 용도":"USAGE",
        "② 건축 형태":"SHAPE",
        "③ 건축 자재":"MATERIAL",
        "④ 미래 기술":"TECH",
        "⑤ 꾸미기":"DECOR",
        "📋 최종 설계":"RESULT",
    }
    for label, page in nav.items():
        if st.button(label, key="nav_"+page, use_container_width=True, type="primary" if st.session_state.page==page else "secondary"):
            st.session_state.page=page
            st.rerun()

    st.divider()
    cost = design_cost()
    remain = remaining_budget()
    st.markdown("### 💰 설계 예산")
    st.progress(max(0, min(1, remain / st.session_state.budget)) if st.session_state.budget else 0)
    budget_color = "#8ef0c5" if remain >= 0 else "#ff7d7d"
    st.markdown(f"<div style='font:800 26px Orbitron;color:{budget_color};'>{budget_text(remain)}<span style='font-size:12px;color:#aebfbc;'> / {st.session_state.budget:,}억원</span></div>", unsafe_allow_html=True)
    st.caption(f"사용 금액 {cost:,}억원 · 용도, 형태, 자재, 미래 기술을 선택할 때마다 예산이 차감됩니다.")
    if remain < 0: st.error("예산 초과 · 선택을 조정해 주세요.")

    score=pollution_score()
    st.markdown("### 🌫️ 현재 오염지수")
    st.progress(score/100)
    st.markdown(f"<div style='font:800 30px Orbitron;color:#fff;'>{score}<span style='font-size:13px;color:#aebfbc;'> / 100</span></div>", unsafe_allow_html=True)
    st.caption("낮을수록 환경 부담이 낮은 설계")
    if score <= 40: st.success("MISSION READY")
    else: st.warning("환경 부담을 더 줄여보세요.")

# =========================================================
# HOME
# =========================================================
if st.session_state.page == "HOME":
    st.markdown("<div class='hero-title'>2050 FUTURE ARCHITECT</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>BUILD ONE BUILDING. SURVIVE ONE PLANET.</div>", unsafe_allow_html=True)

    if st.session_state.completed:
        st.markdown("<div class='section-title'>🏙️ YOUR 2050 BUILDING</div>", unsafe_allow_html=True)
        show_building()
        score=pollution_score()
        remain = remaining_budget()
        if mission_success():
            st.success(f"🌍 설계 성공! 오염지수 {score} · 남은 예산 {remain:,} — 여러 조합 중 하나로 조건을 만족했습니다.")
        elif remain < 0:
            st.error(f"⚠️ 예산 초과! 오염지수 {score} · {abs(remain):,}억원 초과 — 기술이나 자재 조합을 바꿔보세요.")
        else:
            st.error(f"⚠️ 아직 조건을 만족하지 못했어요. 오염지수 {score} · 남은 예산 {remain:,} — 정답 하나가 아니라 다른 조합을 시도해보세요.")

        c1,c2=st.columns(2)
        with c1:
            if st.button("📋 설계 결과 자세히 보기", use_container_width=True):
                st.session_state.page="RESULT"; st.rerun()
        with c2:
            if st.button("🔄 새로운 건축물 만들기", use_container_width=True):
                st.session_state.completed=False
                st.session_state.usage="🏠 미래 주거시설"
                st.session_state.shape="🏙️ 수직형 타워"
                st.session_state.material="🧱 저탄소 콘크리트"
                st.session_state.technologies=[]
                st.session_state.building_color="#5D7F7A"
                st.session_state.page="USAGE"; st.rerun()
    else:
        st.markdown("""
        <div style="height:520px;border-radius:26px;overflow:hidden;position:relative;border:1px solid rgba(255,235,205,.20);background:radial-gradient(circle at 75% 22%,rgba(255,221,159,.82) 0 55px,transparent 165px),linear-gradient(180deg,#151e20 0%,#55483e 47%,#a16d49 100%);box-shadow:0 30px 80px rgba(0,0,0,.45);">
            <div style="position:absolute;left:-10%;bottom:-220px;width:120%;height:450px;transform:rotateX(60deg);background:radial-gradient(ellipse at center,#a87550 0%,#714b37 46%,#2b211d 100%);"></div>
            <div style="position:absolute;right:18%;top:16%;width:84px;height:84px;border-radius:50%;background:#efb46e;box-shadow:0 0 80px rgba(255,183,101,.32);"></div>
            <div style="position:absolute;left:28px;top:28px;padding:14px 17px;background:rgba(5,10,11,.68);border-left:3px solid #d9b57d;color:#fff;font:700 12px Orbitron,sans-serif;letter-spacing:1px;">EARTH // 2050<br><span style="color:#d8c0b1;font-family:'Noto Sans KR';font-size:12px;">DESERTIFICATION / CRITICAL</span></div>
            <div style="position:absolute;left:50%;top:57%;transform:translate(-50%,-50%);color:rgba(255,255,255,.9);font:800 35px Orbitron,sans-serif;text-align:center;text-shadow:0 3px 25px rgba(0,0,0,.65);">THE LAST<br>BUILDING</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="margin-top:18px;">
            <div class="effect-label">MISSION 2050</div>
            <h2 style="margin:7px 0 10px;">황량해진 지구에 단 하나의 건축물을 설계하라.</h2>
            <div class="small-note">용도 → 형태 → 자재 → 미래 기술 → 색상 순서로 선택합니다. 선택할 때마다 건물 외관이 실제로 달라지고, 환경 요소에 따라 오염지수도 변합니다. 완성 후 메인 화면에서 건물을 마우스로 드래그해 360°로 돌려볼 수 있습니다.</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("")
        if st.button("🚀 설계 시작하기", type="primary", use_container_width=True):
            st.session_state.page="USAGE"; st.rerun()

# =========================================================
# USAGE
# =========================================================
elif st.session_state.page == "USAGE":
    st.markdown("<div class='hero-title' style='font-size:42px;'>01 / BUILDING USE</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>WHAT WILL YOUR BUILDING DO?</div>", unsafe_allow_html=True)
    current_usage = st.session_state.usage
    fixed_cost = SHAPES[st.session_state.shape]["cost"] + MATERIALS[st.session_state.material]["cost"] + sum(TECHNOLOGIES[t]["cost"] for t in st.session_state.technologies)
    available_usages = [name for name, data in USAGES.items() if fixed_cost + data["cost"] <= st.session_state.budget or name == current_usage]
    choice=st.radio("건축물의 용도를 선택하세요. (예산이 부족한 선택지는 목록에서 제외됩니다.)", available_usages, index=available_usages.index(current_usage), format_func=lambda x: f"{x} · {USAGES[x]['cost']}억원")
    st.session_state.usage=choice
    unavailable_usages = [name for name, data in USAGES.items() if fixed_cost + data["cost"] > st.session_state.budget and name != current_usage]
    if unavailable_usages:
        st.caption("예산 부족으로 선택 불가: " + " · ".join(f"{name} ({USAGES[name]['cost']}억원)" for name in unavailable_usages))
    data=USAGES[choice]
    st.markdown(effect_card(choice,data["impact"],data["effect"],data["limit"], data.get("cost")), unsafe_allow_html=True)
    st.markdown("""<div class='expert-box'><div class='expert-kicker'>ARCHITECTURE NOTE</div><h3>건축물의 용도는 필요한 환경을 결정해요.</h3><p>같은 크기의 건물이라도 주거시설, 학교, 병원처럼 <b>무엇을 하는 공간인지</b>에 따라 필요한 빛, 온도, 공기, 물, 전력의 조건이 달라집니다.</p><p><b>쉽게 말하면</b> 건축가는 먼저 건물에서 어떤 활동이 일어나는지 정한 뒤, 그 활동에 맞춰 공간과 설비를 계획합니다. 이 게임의 점수는 이런 차이를 이해하기 위한 가상 값입니다.</p></div>""", unsafe_allow_html=True)
    if st.button("다음 → 건축 형태", type="primary", use_container_width=True): st.session_state.page="SHAPE"; st.rerun()

# =========================================================
# SHAPE
# =========================================================
elif st.session_state.page == "SHAPE":
    st.markdown("<div class='hero-title' style='font-size:42px;'>02 / FORM</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>CHANGE THE ARCHITECTURE ITSELF.</div>", unsafe_allow_html=True)
    current_shape = st.session_state.shape
    fixed_cost = USAGES[st.session_state.usage]["cost"] + MATERIALS[st.session_state.material]["cost"] + sum(TECHNOLOGIES[t]["cost"] for t in st.session_state.technologies)
    available_shapes = [name for name, data in SHAPES.items() if fixed_cost + data["cost"] <= st.session_state.budget or name == current_shape]
    choice=st.radio("건축 형태를 선택하세요. (예산이 부족한 선택지는 목록에서 제외됩니다.)", available_shapes, index=available_shapes.index(current_shape), format_func=lambda x: f"{x} · {SHAPES[x]['cost']}억원")
    st.session_state.shape=choice
    unavailable_shapes = [name for name, data in SHAPES.items() if fixed_cost + data["cost"] > st.session_state.budget and name != current_shape]
    if unavailable_shapes:
        st.caption("예산 부족으로 선택 불가: " + " · ".join(f"{name} ({SHAPES[name]['cost']}억원)" for name in unavailable_shapes))
    show_building()
    data=SHAPES[choice]
    st.markdown(effect_card(choice,data["impact"],data["effect"],data["limit"], data.get("cost")), unsafe_allow_html=True)
    if st.button("다음 → 건축 자재", type="primary", use_container_width=True): st.session_state.page="MATERIAL"; st.rerun()

# =========================================================
# MATERIAL
# =========================================================
elif st.session_state.page == "MATERIAL":
    st.markdown("<div class='hero-title' style='font-size:42px;'>03 / MATERIAL</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>THE MATERIAL CHANGES THE BUILDING.</div>", unsafe_allow_html=True)
    current_material = st.session_state.material
    fixed_cost = USAGES[st.session_state.usage]["cost"] + SHAPES[st.session_state.shape]["cost"] + sum(TECHNOLOGIES[t]["cost"] for t in st.session_state.technologies)
    available_materials = [name for name, data in MATERIALS.items() if fixed_cost + data["cost"] <= st.session_state.budget or name == current_material]
    choice=st.radio("건축 자재를 선택하세요. (예산이 부족한 선택지는 목록에서 제외됩니다.)", available_materials, index=available_materials.index(current_material), format_func=lambda x: f"{x}  ·  {MATERIALS[x]['cost']}억원")
    st.session_state.material=choice
    unavailable_materials = [name for name, data in MATERIALS.items() if fixed_cost + data["cost"] > st.session_state.budget and name != current_material]
    if unavailable_materials:
        st.caption("예산 부족으로 선택 불가: " + " · ".join(f"{name} ({MATERIALS[name]['cost']}억원)" for name in unavailable_materials))
    show_building()
    data=MATERIALS[choice]
    st.markdown(effect_card(choice,data["impact"],data["effect"],data["limit"], data.get("cost")), unsafe_allow_html=True)
    st.markdown("""<div class='expert-box'><div class='expert-kicker'>MATERIAL SCIENCE</div><h3>건물의 겉모습뿐 아니라 재료가 만들어지는 과정도 중요해요.</h3><p>콘크리트와 철강 같은 재료는 건물을 튼튼하게 만드는 데 중요하지만, 재료를 생산하고 운반하는 과정에서도 환경 부담이 생길 수 있습니다.</p><p><b>그래서 건축에서는</b> 필요한 재료의 양을 줄이거나, 탄소 부담이 낮은 재료를 사용하거나, 기존 자재를 다시 활용하는 방법을 함께 생각합니다. 이 게임에서는 그 개념을 쉽게 비교할 수 있도록 표현했습니다.</p></div>""", unsafe_allow_html=True)
    if st.button("다음 → 미래 기술", type="primary", use_container_width=True): st.session_state.page="TECH"; st.rerun()

# =========================================================
# TECH
# =========================================================
elif st.session_state.page == "TECH":
    st.markdown("<div class='hero-title' style='font-size:42px;'>04 / FUTURE TECH</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>EVERY TECHNOLOGY HAS AN ENVIRONMENTAL EFFECT.</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><b>💰 초기 설계 예산 100억원</b><br><span class='small-note'>용도·형태·자재·미래 기술을 고를 때마다 비용이 차감됩니다. 오염지수 감축 효과가 큰 기술과 환경 부담이 낮은 자재는 대체로 비싸게 설정되어 있습니다. 예산이 부족하면 해당 선택을 할 수 없습니다.</span></div>", unsafe_allow_html=True)
    base_cost = USAGES[st.session_state.usage]["cost"] + SHAPES[st.session_state.shape]["cost"] + MATERIALS[st.session_state.material]["cost"]
    selected=[]
    old_technologies = list(st.session_state.technologies)
    for tech, data in TECHNOLOGIES.items():
        was_selected = tech in old_technologies
        other_selected_cost = sum(TECHNOLOGIES[t]["cost"] for t in old_technologies if t != tech)
        can_afford = was_selected or (base_cost + other_selected_cost + data["cost"] <= st.session_state.budget)
        checked = st.checkbox(
            f"{tech}  ·  {data['cost']}억원  ·  오염지수 {data['impact']:+d}",
            value=was_selected,
            disabled=not can_afford,
            key=f"tech_{tech}"
        )
        if checked:
            selected.append(tech)
    st.session_state.technologies=selected
    tech_cost = sum(TECHNOLOGIES[t]["cost"] for t in selected)
    total_cost = base_cost + tech_cost
    remain_after = st.session_state.budget - total_cost
    if remain_after >= 0:
        st.info(f"💰 현재 자재 + 미래 기술 비용: {total_cost:,}억원 · 남은 예산: {remain_after:,}억원")
    else:
        st.error(f"💸 예산을 {-remain_after:,}억원 초과했습니다. 기술을 조합해서 예산 안에서 설계하세요.")
    show_building()
    st.markdown("### 기술별 효과 · 영향 · 한계")
    items=list(TECHNOLOGIES.items())
    for i in range(0,len(items),2):
        cols=st.columns(2)
        for j,col in enumerate(cols):
            if i+j>=len(items): continue
            title,data=items[i+j]
            with col: st.markdown(effect_card(title,data["impact"],data["effect"],data["limit"], data.get("cost")), unsafe_allow_html=True)
    st.markdown("""<div class='expert-box'><div class='expert-kicker'>FUTURE BUILDING SYSTEM</div><h3>미래 건축은 건물이 환경과 어떻게 반응하는지도 생각해요.</h3><p>태양광은 전기를 만들고, 자연환기는 바람을 이용해 공기를 움직이며, 차양은 강한 햇빛의 유입을 조절합니다. 녹화 지붕과 물 관리 기술은 건물 주변의 열과 물을 다루는 데 활용할 수 있습니다.</p><p><b>중요한 점은</b> 비싼 기술을 많이 넣는 것이 정답이 아니라는 것입니다. 오염지수 감축 효과가 큰 기술일수록 비용도 높게 설정했기 때문에, 제한된 100억원 안에서 여러 기술과 자재를 조합해야 합니다. 예산 안에서 서로 다른 기술이 부족한 부분을 보완하도록 조합하면 여러 가지 방식으로 성공 조건에 도달할 수 있습니다.</p></div>""", unsafe_allow_html=True)
    if st.button("다음 → 꾸미기", type="primary", use_container_width=True): st.session_state.page="DECOR"; st.rerun()

# =========================================================
# DECOR: 색만
# =========================================================
elif st.session_state.page == "DECOR":
    st.markdown("<div class='hero-title' style='font-size:42px;'>05 / COLOR</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>DECORATE WITH COLOR ONLY.</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><div class='effect-label'>CUSTOM COLOR</div><h2 style='margin:6px 0 8px;'>건축물의 외관 색만 정하세요.</h2><div class='small-note'>이 단계에서는 나무, 벽, 지붕 같은 추가 장식물을 선택하지 않습니다. 색상만 바뀌며 오염지수에는 영향을 주지 않습니다.</div></div>", unsafe_allow_html=True)
    color_name=st.selectbox("추천 색상", list(COLORS))
    st.session_state.building_color=COLORS[color_name]
    st.session_state.building_color=st.color_picker("직접 색상 선택", st.session_state.building_color)
    show_building()
    st.markdown("""<div class='expert-box'><div class='expert-kicker'>ARCHITECTURAL EXPRESSION</div><h3>색은 건축물의 인상을 바꾸는 마지막 설계 요소예요.</h3><p>같은 형태와 재료라도 색에 따라 건물의 밝기, 무게감, 미래적인 느낌이 다르게 보일 수 있습니다.</p><p>이번 단계에서는 환경 성능보다 <b>건축가의 시각적 표현</b>에 집중해 색만 바꾸도록 했습니다.</p></div>""", unsafe_allow_html=True)
    if st.button("🏗️ 건축물 완성하기", type="primary", use_container_width=True):
        st.session_state.completed=True; st.session_state.page="HOME"; st.rerun()

# =========================================================
# RESULT
# =========================================================
elif st.session_state.page == "RESULT":
    st.markdown("<div class='hero-title' style='font-size:42px;'>FINAL DESIGN</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>ONE BUILDING. ONE PLANET.</div>", unsafe_allow_html=True)
    show_building()
    score=pollution_score()
    remain = remaining_budget()
    if mission_success(): st.success(f"🌍 MISSION SUCCESS — 오염지수 {score} · 남은 예산 {remain:,}억원")
    elif remain < 0: st.error(f"⚠️ MISSION FAILED — 예산을 {-remain:,}억원 초과했습니다.")
    else: st.error(f"⚠️ MISSION FAILED — 오염지수 {score}. 다른 자재·기술 조합을 시도해보세요.")
    a,b,c,d=st.columns(4)
    with a: st.metric("오염지수",score,"낮을수록 좋음")
    with b: st.metric("남은 예산",f"{remain:,}억원")
    with c: st.metric("미래 기술",len(st.session_state.technologies))
    material_cost_result = MATERIALS[st.session_state.material]["cost"]
    with d: st.metric("자재 비용", f"{material_cost_result:,}억원")

    st.markdown("## 🧾 설계 분석")
    rows=[("건축물 용도",st.session_state.usage,USAGES[st.session_state.usage]),("건축 형태",st.session_state.shape,SHAPES[st.session_state.shape]),("건축 자재",st.session_state.material,MATERIALS[st.session_state.material])]
    for name,value,data in rows:
        st.markdown(effect_card(f"{name} · {value}",data["impact"],data["effect"],data["limit"], data.get("cost")), unsafe_allow_html=True)
    for tech in st.session_state.technologies:
        data=TECHNOLOGIES[tech]
        st.markdown(effect_card(tech,data["impact"],data["effect"],data["limit"], data.get("cost")), unsafe_allow_html=True)

    st.markdown("""<div class='expert-box'><div class='expert-kicker'>FINAL DESIGN REVIEW</div><h3>이 점수는 실제 탄소배출량이 아니라 설계 비교용 가상 지표입니다.</h3><p>실제 건물의 환경 성능은 건물의 크기, 위치, 기후, 재료의 생산 과정, 설비 효율, 사용 방식 등 여러 조건을 함께 계산해야 합니다.</p><p>따라서 이 게임에서는 복잡한 실제 계산 대신 <b>환경 부담과 예산을 함께 생각하면서 여러 조합을 실험하는 것</b>에 초점을 맞췄습니다. 비싼 선택 하나가 자동으로 정답이 되는 구조가 아니라, 서로 다른 자재와 기술을 조합해 조건을 만족하도록 설계하는 방식입니다.</p></div>""", unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("🏠 메인으로",use_container_width=True): st.session_state.page="HOME"; st.rerun()
    with c2:
        if st.button("🔄 처음부터 다시 설계",use_container_width=True):
            st.session_state.completed=False; st.session_state.usage="🏠 미래 주거시설"; st.session_state.shape="🏙️ 수직형 타워"; st.session_state.material="🧱 저탄소 콘크리트"; st.session_state.technologies=[]; st.session_state.building_color="#5D7F7A"; st.session_state.budget=100; st.session_state.page="USAGE"; st.rerun()
