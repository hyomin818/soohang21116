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
.effect-label { color:#7fe0ca; font-size:12px; font-weight:800; letter-spacing:1px; }
.effect-text { color:#d5e3e0; font-size:14px; line-height:1.75; }
.good { color:#8ef0c5; font-weight:800; }
.bad { color:#ffbd91; font-weight:800; }
.neutral { color:#dfe9e6; font-weight:800; }
.source-box { background:#0b1517; border:1px solid rgba(177,230,217,.16); border-radius:18px; padding:19px; color:#c8d8d5; font-size:14px; line-height:1.8; }

section[data-testid="stSidebar"] { background:#071012; border-right:1px solid rgba(160,220,208,.14); }
section[data-testid="stSidebar"] * { color:#f4fffc; }
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
def init_state():
    defaults = {
        "page": "HOME",
        "completed": False,
        "usage": "🏠 미래 주거시설",
        "shape": "🏙️ 수직형 타워",
        "material": "🧱 저탄소 콘크리트",
        "technologies": [],
        "building_color": "#5D7F7A",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

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
        "impact": 6,
        "effect": "의료장비와 환기, 냉난방 등 지속적인 에너지 사용이 필요할 수 있어 게임에서는 높은 값을 적용했습니다.",
        "limit": "실제 병원의 환경 성능을 단순히 용도 하나만으로 판단할 수는 없습니다.",
        "class": "hospital",
        "badge": "MED",
    },
    "🔬 미래 연구센터": {
        "impact": 3,
        "effect": "연구장비가 필요하지만 효율적인 공간과 설비를 설계할 수 있는 것으로 설정했습니다.",
        "limit": "실험 종류와 장비에 따라 에너지 사용량은 크게 달라질 수 있습니다.",
        "class": "research",
        "badge": "LAB",
    },
}

SHAPES = {
    "🏙️ 수직형 타워": {
        "impact": 7,
        "effect": "높이를 크게 확보해 같은 부지에 많은 공간을 넣는 형태입니다. 게임에서는 구조와 외피 사용량을 고려해 부담을 높게 반영했습니다.",
        "limit": "실제 환경 성능은 높이만으로 결정되지 않고 설계와 재료에 따라 달라집니다.",
        "class": "tower",
    },
    "🌿 테라스형 건축": {
        "impact": 3,
        "effect": "층마다 외부공간을 만들어 차양이나 녹지를 적용하기 쉬운 형태로 설정했습니다.",
        "limit": "테라스가 많아지면 구조와 외피가 복잡해질 수도 있습니다.",
        "class": "terrace",
    },
    "🛸 돔형 건축": {
        "impact": 2,
        "effect": "곡면 외피를 가진 미래형 형태로 표현해 외부 환경에 대응하는 건축물로 설정했습니다.",
        "limit": "곡면 구조는 제작과 시공 방식에 따라 재료와 비용이 달라질 수 있습니다.",
        "class": "dome",
    },
    "🌍 저층 생태형": {
        "impact": 1,
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
    },
    "🔩 저탄소 철강": {
        "impact": 5,
        "effect": "철강 생산 과정의 탄소 영향을 낮추는 방향의 재료로 설정했습니다. 철골 구조의 장점을 유지하면서 환경 부담을 줄이는 선택입니다.",
        "limit": "실제 탄소 영향은 생산 전력과 제조 방식 등에 따라 달라집니다.",
        "class": "steel",
    },
    "🌲 목재·바이오 기반": {
        "impact": 2,
        "effect": "목재와 바이오 기반 재료를 활용하는 선택으로, 재료 생산 단계의 환경 부담을 낮추는 방향으로 반영했습니다.",
        "limit": "산림 관리, 생산 과정, 운송과 수명까지 함께 살펴야 합니다.",
        "class": "wood",
    },
    "♻️ 재사용·재활용 재료": {
        "impact": 0,
        "effect": "기존 자원을 다시 활용해 새로운 재료 생산을 줄이는 자원순환 방식으로 설정했습니다.",
        "limit": "재사용 가능 여부와 품질, 운송 과정 등에 따라 실제 효과가 달라집니다.",
        "class": "recycled",
    },
}

TECHNOLOGIES = {
    "☀️ 태양광 발전": {
        "impact": -10,
        "effect": "건물에서 전기를 생산해 외부 전력 사용을 줄이는 방향의 효과를 게임에 반영합니다.",
        "limit": "발전량은 일사량, 설치면적, 방향과 효율 등에 따라 달라집니다.",
        "visual": "solar",
    },
    "🌬️ 자연환기": {
        "impact": -7,
        "effect": "바람과 개구부를 이용해 실내 공기를 순환시키고 기계식 냉방·환기 의존을 줄이는 방향으로 반영합니다.",
        "limit": "외부 온도와 공기질, 바람 조건이 좋지 않은 때에는 다른 설비가 필요할 수 있습니다.",
        "visual": "vent",
    },
    "🪟 외부 차양": {
        "impact": -6,
        "effect": "강한 햇빛의 실내 유입을 조절해 냉방 부담을 낮추는 방향으로 반영합니다.",
        "limit": "차양의 위치와 방향을 잘못 설계하면 자연채광을 줄일 수도 있습니다.",
        "visual": "shade",
    },
    "🌱 녹화 지붕": {
        "impact": -7,
        "effect": "옥상에 식생을 적용해 열환경과 빗물 관리에 도움을 주는 요소로 반영합니다.",
        "limit": "구조 하중, 관리, 물 공급 등을 고려해야 합니다.",
        "visual": "greenroof",
    },
    "💧 빗물 이용": {
        "impact": -5,
        "effect": "빗물을 모아 조경이나 일부 용도에 활용해 수돗물 사용을 줄이는 방향으로 반영합니다.",
        "limit": "강수량과 저장시설 크기에 따라 이용 가능한 양이 달라집니다.",
        "visual": "rain",
    },
    "🔄 물 재이용": {
        "impact": -5,
        "effect": "사용한 물을 처리해 다시 이용함으로써 물 사용량을 줄이는 방향으로 반영합니다.",
        "limit": "처리시설과 유지관리가 필요하며 모든 용도의 물을 같은 방식으로 재사용할 수 있는 것은 아닙니다.",
        "visual": "reuse",
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
    techs = st.session_state.technologies
    if "☀️ 태양광 발전" in techs:
        feature_html += '<div class="solar-panel sp1"></div><div class="solar-panel sp2"></div>'
    if "🌬️ 자연환기" in techs:
        feature_html += '<div class="air-ring ar1">AIR</div><div class="air-ring ar2">AIR</div>'
    if "🪟 외부 차양" in techs:
        feature_html += '<div class="shade sh1"></div><div class="shade sh2"></div><div class="shade sh3"></div>'
    if "🌱 녹화 지붕" in techs:
        feature_html += '<div class="green-roof">GREEN ROOF</div>'
    if "💧 빗물 이용" in techs:
        feature_html += '<div class="water-tank">RAIN<br>WATER</div>'
    if "🔄 물 재이용" in techs:
        feature_html += '<div class="reuse-mark">↻</div>'

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
        <div id="building3d" class="building-3d __SHAPE__ __USAGE__ __MATERIAL__" style="--building-color:__COLOR__">
            <div class="face front">
                <div class="top-cap"></div>
                <div class="badge">__BADGE__</div>
                <div class="window-grid">
                    <span></span><span></span><span></span><span></span>
                    <span></span><span></span><span></span><span></span>
                    <span></span><span></span><span></span><span></span>
                </div>
                <div class="vertical-core"></div>
                __FEATURES__
            </div>
            <div class="face right"><div class="side-lines"></div><div class="side-window sw1"></div><div class="side-window sw2"></div><div class="side-window sw3"></div></div>
            <div class="face left"><div class="side-lines"></div></div>
            <div class="face back"><div class="back-panel"></div></div>
            <div class="face top"><div class="roof-grid"></div></div>
            <div class="face bottom"></div>
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
.concrete .front{background:repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 3px,transparent 3px 14px),linear-gradient(90deg,rgba(255,255,255,.09),transparent 20%,rgba(0,0,0,.16)),var(--building-color)}
.steel .front{background:linear-gradient(105deg,rgba(255,255,255,.26),transparent 22%,rgba(255,255,255,.08) 52%,rgba(0,0,0,.18)),var(--building-color)}
.wood .front{background:repeating-linear-gradient(90deg,rgba(72,39,22,.15) 0 3px,transparent 3px 15px),var(--building-color)}
.recycled .front{background:repeating-linear-gradient(45deg,rgba(255,255,255,.10) 0 8px,transparent 8px 18px),var(--building-color)}
.terrace .front{clip-path:polygon(0 0,100% 0,100% 100%,0 100%,0 74%,8% 74%,8% 57%,0 57%,0 40%,8% 40%,8% 23%,0 23%)}
.dome .front{border-radius:48% 48% 8px 8px;background:radial-gradient(ellipse at 50% 3%,rgba(240,255,249,.28),transparent 35%),var(--building-color)}
.eco .front{border-radius:18px 18px 5px 5px;background:linear-gradient(180deg,rgba(116,170,116,.30),transparent 30%),var(--building-color)}
.top-cap{position:absolute;left:4%;right:4%;top:0;height:9px;background:rgba(226,246,238,.34)}
.badge{position:absolute;top:14px;right:14px;z-index:9;padding:5px 8px;background:rgba(0,0,0,.30);border:1px solid rgba(255,255,255,.28);color:#eafff7;font:700 10px 'Orbitron',sans-serif;letter-spacing:1px}
.window-grid{position:absolute;inset:38px 23px;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:17px;gap:22px 15px}.window-grid span{background:linear-gradient(180deg,#e1fff3,#71b29f);border:1px solid rgba(255,255,255,.38);box-shadow:0 0 10px rgba(140,240,209,.20)}
.school .window-grid span:nth-child(3n){background:linear-gradient(180deg,#dcecff,#7395be)}.hospital .window-grid span{background:linear-gradient(180deg,#f2ffff,#8fc5c6)}.research .window-grid span:nth-child(even){background:linear-gradient(180deg,#ddfff8,#5db8a7)}
.housing .front:after{content:'';position:absolute;left:10%;right:10%;bottom:13px;height:24px;border-top:2px solid rgba(231,255,247,.25);border-bottom:2px solid rgba(231,255,247,.16)}
.school .front:after{content:'CAMPUS';position:absolute;left:13px;bottom:12px;color:rgba(235,255,249,.65);font:700 8px 'Orbitron',sans-serif;letter-spacing:1px}.hospital .front:after{content:'+';position:absolute;left:50%;bottom:12px;transform:translateX(-50%);font:800 24px Arial;color:#d9ffff}.research .front:after{content:'R-2050';position:absolute;left:12px;bottom:12px;color:rgba(222,255,249,.7);font:700 8px 'Orbitron',sans-serif}
.vertical-core{position:absolute;left:48%;top:0;bottom:0;width:4px;background:rgba(218,255,246,.10)}
.side-lines{position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent 0 24px,rgba(220,245,237,.10) 24px 27px)}
.side-window{position:absolute;left:18px;width:48px;height:17px;background:#8fc6b6;box-shadow:0 0 9px rgba(145,230,206,.14)}.sw1{top:42px}.sw2{top:120px}.sw3{top:198px}
.back-panel{position:absolute;inset:18px;border:1px solid rgba(220,245,237,.13);background:repeating-linear-gradient(0deg,rgba(255,255,255,.04) 0 3px,transparent 3px 17px)}
.roof-grid{position:absolute;inset:12px;border:1px solid rgba(255,255,255,.15);background:repeating-linear-gradient(90deg,transparent 0 20px,rgba(255,255,255,.08) 20px 21px),repeating-linear-gradient(0deg,transparent 0 20px,rgba(255,255,255,.08) 20px 21px)}
.solar-panel{position:absolute;z-index:10;width:58px;height:37px;border:1px solid #8de2d1;background:repeating-linear-gradient(90deg,rgba(170,255,242,.24) 0 1px,transparent 1px 13px),repeating-linear-gradient(0deg,rgba(170,255,242,.24) 0 1px,transparent 1px 12px),#163944;transform:skewX(-15deg) rotate(-12deg)}.sp1{right:14px;top:9px}.sp2{left:13px;top:18px}
.air-ring{position:absolute;z-index:10;width:42px;height:42px;border:2px solid #99ddd0;border-radius:50%;color:#dffef7;font:700 8px 'Orbitron',sans-serif;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.18)}.ar1{left:11px;top:43%}.ar2{right:11px;top:54%}
.shade{position:absolute;z-index:10;left:8%;width:84%;height:8px;background:#bdc8c2;border-radius:3px;box-shadow:0 3px 0 rgba(0,0,0,.2)}.sh1{top:32%}.sh2{top:51%}.sh3{top:70%}
.green-roof{position:absolute;z-index:11;top:-7px;left:7%;width:86%;height:21px;border-radius:50%;background:linear-gradient(#7aa96f,#315c3d);box-shadow:0 0 18px rgba(105,189,121,.22);color:#eaffdf;text-align:center;font:700 7px 'Orbitron',sans-serif;padding-top:5px}
.water-tank{position:absolute;z-index:11;right:9px;bottom:12px;width:47px;height:47px;border-radius:50%;border:2px solid #78c9dc;background:rgba(27,105,126,.55);color:#dffaff;font:700 6px 'Orbitron',sans-serif;text-align:center;padding-top:14px}.reuse-mark{position:absolute;z-index:11;left:12px;bottom:15px;width:42px;height:42px;border:3px dashed #82e0ca;border-radius:50%;color:#dffff7;font-size:25px;text-align:center;line-height:36px}
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
    return (html.replace("__SHAPE__", shape)
                .replace("__USAGE__", usage)
                .replace("__MATERIAL__", material)
                .replace("__COLOR__", color)
                .replace("__BADGE__", badge)
                .replace("__FEATURES__", feature_html))


def show_building():
    st.html(building_html(), unsafe_allow_javascript=True)


def effect_card(title, impact, effect, limit):
    if impact < 0:
        impact_text = f"▼ {abs(impact)}"
        cls = "good"
    elif impact > 0:
        impact_text = f"▲ {impact}"
        cls = "bad"
    else:
        impact_text = "● 0"
        cls = "neutral"
    return f"""
<div class="effect-card">
    <div class="effect-title">{title}</div>
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
        if score<=40:
            st.success(f"🌍 설계 성공! 최종 오염지수 {score} — 2050 생존 조건을 통과했습니다.")
        else:
            st.error(f"⚠️ 설계 실패! 최종 오염지수 {score} — 미래 기술이나 자재를 바꿔보세요.")

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
        st.html("""
        <div style="height:520px;border-radius:26px;overflow:hidden;position:relative;border:1px solid rgba(255,235,205,.20);background:radial-gradient(circle at 75% 22%,rgba(255,221,159,.82) 0 55px,transparent 165px),linear-gradient(180deg,#151e20 0%,#55483e 47%,#a16d49 100%);box-shadow:0 30px 80px rgba(0,0,0,.45);">
            <div style="position:absolute;left:-10%;bottom:-220px;width:120%;height:450px;transform:rotateX(60deg);background:radial-gradient(ellipse at center,#a87550 0%,#714b37 46%,#2b211d 100%);"></div>
            <div style="position:absolute;right:18%;top:16%;width:84px;height:84px;border-radius:50%;background:#efb46e;box-shadow:0 0 80px rgba(255,183,101,.32);"></div>
            <div style="position:absolute;left:28px;top:28px;padding:14px 17px;background:rgba(5,10,11,.68);border-left:3px solid #d9b57d;color:#fff;font:700 12px Orbitron,sans-serif;letter-spacing:1px;">EARTH // 2050<br><span style="color:#d8c0b1;font-family:'Noto Sans KR';font-size:12px;">DESERTIFICATION / CRITICAL</span></div>
            <div style="position:absolute;left:50%;top:57%;transform:translate(-50%,-50%);color:rgba(255,255,255,.9);font:800 35px Orbitron,sans-serif;text-align:center;text-shadow:0 3px 25px rgba(0,0,0,.65);">THE LAST<br>BUILDING</div>
        </div>
        """)
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
    choice=st.radio("건축물의 용도를 선택하세요.", list(USAGES), index=list(USAGES).index(st.session_state.usage))
    st.session_state.usage=choice
    data=USAGES[choice]
    st.markdown(effect_card(choice,data["impact"],data["effect"],data["limit"]), unsafe_allow_html=True)
    st.markdown("<div class='source-box'><b>환경 영향은 어떻게 반영했나?</b><br>건축물은 용도에 따라 필요한 냉난방, 조명, 장비, 물 사용 등이 달라질 수 있습니다. 이 게임에서는 그 차이를 이해하기 쉽도록 간단한 가상 점수로 반영했습니다.</div>", unsafe_allow_html=True)
    if st.button("다음 → 건축 형태", type="primary", use_container_width=True): st.session_state.page="SHAPE"; st.rerun()

# =========================================================
# SHAPE
# =========================================================
elif st.session_state.page == "SHAPE":
    st.markdown("<div class='hero-title' style='font-size:42px;'>02 / FORM</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>CHANGE THE ARCHITECTURE ITSELF.</div>", unsafe_allow_html=True)
    choice=st.radio("건축 형태를 선택하세요.", list(SHAPES), index=list(SHAPES).index(st.session_state.shape))
    st.session_state.shape=choice
    show_building()
    data=SHAPES[choice]
    st.markdown(effect_card(choice,data["impact"],data["effect"],data["limit"]), unsafe_allow_html=True)
    if st.button("다음 → 건축 자재", type="primary", use_container_width=True): st.session_state.page="MATERIAL"; st.rerun()

# =========================================================
# MATERIAL
# =========================================================
elif st.session_state.page == "MATERIAL":
    st.markdown("<div class='hero-title' style='font-size:42px;'>03 / MATERIAL</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>THE MATERIAL CHANGES THE BUILDING.</div>", unsafe_allow_html=True)
    choice=st.radio("건축 자재를 선택하세요.", list(MATERIALS), index=list(MATERIALS).index(st.session_state.material))
    st.session_state.material=choice
    show_building()
    data=MATERIALS[choice]
    st.markdown(effect_card(choice,data["impact"],data["effect"],data["limit"]), unsafe_allow_html=True)
    st.markdown("<div class='source-box'><b>자료 근거</b><br>UNEP는 건축 자재의 생산과 사용에서 발생하는 탄소 영향을 줄이기 위해 자재 효율, 재사용·재활용, 저탄소 재료 등의 접근을 제시합니다. 이 프로그램은 이를 고등학교 수준의 게임 점수로 단순화했습니다.</div>", unsafe_allow_html=True)
    if st.button("다음 → 미래 기술", type="primary", use_container_width=True): st.session_state.page="TECH"; st.rerun()

# =========================================================
# TECH
# =========================================================
elif st.session_state.page == "TECH":
    st.markdown("<div class='hero-title' style='font-size:42px;'>04 / FUTURE TECH</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>EVERY TECHNOLOGY HAS AN ENVIRONMENTAL EFFECT.</div>", unsafe_allow_html=True)
    selected=st.multiselect("미래 기술을 선택하세요.", list(TECHNOLOGIES), default=st.session_state.technologies)
    st.session_state.technologies=selected
    show_building()
    st.markdown("### 기술별 효과 · 영향 · 한계")
    items=list(TECHNOLOGIES.items())
    for i in range(0,len(items),2):
        cols=st.columns(2)
        for j,col in enumerate(cols):
            if i+j>=len(items): continue
            title,data=items[i+j]
            with col: st.markdown(effect_card(title,data["impact"],data["effect"],data["limit"]), unsafe_allow_html=True)
    st.markdown("<div class='source-box'><b>자료 근거</b><br>IPCC는 건축물의 기후 적응과 관련해 자연환기, 태양 차양, 녹화 지붕·벽, 식생, 물 관리 등의 방법을 다룹니다. IEA도 건물의 에너지 효율과 냉난방 수요를 중요한 요소로 설명합니다. 실제 효과는 지역과 설계 조건에 따라 달라지므로 여기서는 게임용 점수로 표현했습니다.</div>", unsafe_allow_html=True)
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
    st.markdown("<div class='source-box'><b>COLOR RULE</b><br>색상은 환경 성능을 직접 결정하는 요소로 점수화하지 않았습니다. 대신 건축가가 같은 건축물의 분위기와 외관을 바꿀 수 있도록 했습니다.</div>", unsafe_allow_html=True)
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
    if score<=40: st.success(f"🌍 MISSION SUCCESS — 최종 오염지수 {score}")
    else: st.error(f"⚠️ MISSION FAILED — 최종 오염지수 {score}")
    a,b,c=st.columns(3)
    with a: st.metric("오염지수",score,"낮을수록 좋음")
    with b: st.metric("미래 기술",len(st.session_state.technologies))
    with c: st.metric("건물 색상",st.session_state.building_color)

    st.markdown("## 🧾 설계 분석")
    rows=[("건축물 용도",st.session_state.usage,USAGES[st.session_state.usage]),("건축 형태",st.session_state.shape,SHAPES[st.session_state.shape]),("건축 자재",st.session_state.material,MATERIALS[st.session_state.material])]
    for name,value,data in rows:
        st.markdown(effect_card(f"{name} · {value}",data["impact"],data["effect"],data["limit"]), unsafe_allow_html=True)
    for tech in st.session_state.technologies:
        data=TECHNOLOGIES[tech]
        st.markdown(effect_card(tech,data["impact"],data["effect"],data["limit"]), unsafe_allow_html=True)

    st.markdown("<div class='source-box'><b>참고 자료</b><br>UNEP · Building Materials and the Climate<br>IPCC · Climate Change 2022: Impacts, Adaptation and Vulnerability, Chapter 6<br>IEA · Energy Efficiency 2025 - Buildings<br><br>※ 오염지수는 실제 탄소배출량이나 실제 건물 성능을 계산한 값이 아니라, 환경 영향을 비교해 보는 게임용 가상 점수입니다.</div>", unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("🏠 메인으로",use_container_width=True): st.session_state.page="HOME"; st.rerun()
    with c2:
        if st.button("🔄 처음부터 다시 설계",use_container_width=True):
            st.session_state.completed=False; st.session_state.usage="🏠 미래 주거시설"; st.session_state.shape="🏙️ 수직형 타워"; st.session_state.material="🧱 저탄소 콘크리트"; st.session_state.technologies=[]; st.session_state.building_color="#5D7F7A"; st.session_state.page="USAGE"; st.rerun()
