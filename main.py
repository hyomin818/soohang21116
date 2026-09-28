import streamlit as st

# =========================================================
# 2050 FUTURE ARCHITECT
# =========================================================

st.set_page_config(
    page_title="2050 FUTURE ARCHITECT",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 세션 상태
# =========================================================

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


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 15%, rgba(90, 110, 120, 0.15), transparent 25%),
        radial-gradient(circle at 80% 25%, rgba(20, 30, 35, 0.45), transparent 35%),
        linear-gradient(135deg, #071014 0%, #10191d 45%, #182326 100%);
    color: #edf4f2;
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #081114 0%, #0c171a 55%, #101c1f 100%);
    border-right: 1px solid rgba(150, 190, 180, 0.16);
}

section[data-testid="stSidebar"] * {
    color: #e8f1ef !important;
}

/* 제목 */
.main-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 48px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #dfffee;
    text-shadow: 0 0 22px rgba(100, 255, 190, 0.25);
    margin-bottom: 5px;
}

.subtitle {
    color: #9eafad;
    font-size: 16px;
    letter-spacing: 1px;
    margin-bottom: 30px;
}

/* 카드 */
.card {
    background: rgba(20, 31, 35, 0.82);
    border: 1px solid rgba(160, 210, 200, 0.14);
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    backdrop-filter: blur(8px);
}

.card h2 {
    margin-top: 0;
    color: #dfffee;
}

.card p {
    color: #aebdbb;
    line-height: 1.7;
}

/* 미래 도시 배경 */
.future-city {
    position: relative;
    height: 470px;
    overflow: hidden;
    border-radius: 25px;
    border: 1px solid rgba(160, 210, 200, 0.16);

    background:
        radial-gradient(circle at 72% 25%, rgba(220,230,220,0.18), transparent 8%),
        radial-gradient(circle at 72% 25%, rgba(90,100,100,0.18), transparent 19%),
        linear-gradient(
            180deg,
            #172226 0%,
            #263034 35%,
            #171e20 65%,
            #0a1012 100%
        );

    box-shadow:
        inset 0 0 100px rgba(0,0,0,0.55),
        0 20px 50px rgba(0,0,0,0.35);
}

/* 오염 안개 */
.future-city:before {
    content: "";
    position: absolute;
    left: -10%;
    right: -10%;
    bottom: 110px;
    height: 170px;
    background:
        radial-gradient(ellipse, rgba(130,145,140,0.18), transparent 65%);
    filter: blur(18px);
}

/* 지평선 */
.horizon {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 105px;
    height: 2px;
    background: rgba(180,200,190,0.08);
}

/* 도시 실루엣 */
.city-building {
    position: absolute;
    bottom: 105px;
    background: #0b1113;
    border: 1px solid rgba(120,150,145,0.10);
}

.city1 { left: 3%; width: 10%; height: 145px; }
.city2 { left: 15%; width: 7%; height: 210px; }
.city3 { left: 25%; width: 13%; height: 125px; }
.city4 { right: 20%; width: 12%; height: 190px; }
.city5 { right: 5%; width: 10%; height: 145px; }

/* 바닥 */
.ground {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 108px;
    background:
        linear-gradient(180deg, #101819, #070b0c);
    border-top: 1px solid rgba(160,190,180,0.08);
}

/* 건축물 */
.building-scene {
    position: absolute;
    left: 50%;
    bottom: 107px;
    transform: translateX(-50%);
    width: 270px;
    min-height: 260px;
    display: flex;
    justify-content: center;
    align-items: flex-end;
}

.building {
    position: relative;
    width: 170px;
    min-height: 240px;
    background: linear-gradient(90deg, #18282c, #263b3e, #142225);
    border: 2px solid rgba(150,220,200,0.32);
    border-radius: 5px 5px 2px 2px;
    box-shadow:
        0 0 35px rgba(80,255,190,0.13),
        12px 15px 30px rgba(0,0,0,0.45);
    padding: 12px;
}

/* 창문 */
.windows {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-top: 10px;
}

.window {
    height: 20px;
    border-radius: 2px;
    background: #92d9cc;
    box-shadow: 0 0 9px rgba(110,255,220,0.28);
}

/* 나무 */
.tree {
    position: absolute;
    bottom: 0;
    width: 25px;
    height: 60px;
}

.tree:before {
    content: "";
    position: absolute;
    left: 8px;
    bottom: 0;
    width: 8px;
    height: 27px;
    background: #493d31;
}

.tree:after {
    content: "";
    position: absolute;
    left: -4px;
    top: 0;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: #47725d;
    box-shadow: 0 0 14px rgba(90,180,130,0.16);
}

.tree1 { left: 25%; }
.tree2 { right: 25%; }

.complete-banner {
    padding: 22px;
    border-radius: 16px;
    background: linear-gradient(
        135deg,
        rgba(50,150,110,0.18),
        rgba(20,60,55,0.25)
    );
    border: 1px solid rgba(100,230,180,0.25);
}

.danger-banner {
    padding: 22px;
    border-radius: 16px;
    background: rgba(130,70,50,0.15);
    border: 1px solid rgba(220,130,100,0.25);
}

.source-box {
    padding: 18px;
    margin-top: 30px;
    border-radius: 15px;
    background: rgba(10,18,20,0.75);
    border: 1px solid rgba(150,180,175,0.12);
    color: #98aaa7;
    font-size: 13px;
    line-height: 1.8;
}

.metric-box {
    text-align: center;
    padding: 22px 10px;
    border-radius: 16px;
    background: rgba(20,35,38,0.85);
    border: 1px solid rgba(150,210,195,0.12);
}

.metric-number {
    font-family: 'Orbitron', sans-serif;
    font-size: 36px;
    font-weight: 800;
    color: #dfffee;
}

.metric-label {
    color: #92a7a4;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 데이터
# =========================================================

USAGE_DATA = {
    "🏠 미래 주거시설": {"pollution": 4, "height": 250},
    "🏫 미래 학교": {"pollution": 2, "height": 220},
    "🏥 미래 병원": {"pollution": 5, "height": 270},
    "🏢 미래 연구센터": {"pollution": 3, "height": 290},
}

SHAPE_DATA = {
    "🏙️ 수직형 타워": {"pollution": 7, "height": 340},
    "🏡 테라스형": {"pollution": 3, "height": 270},
    "🫧 돔형": {"pollution": 2, "height": 230},
    "⬇️ 지하·반지하형": {"pollution": 1, "height": 210},
}

MATERIAL_DATA = {
    "🧱 저탄소 콘크리트": {
        "pollution": 8,
        "description": "기존 콘크리트보다 탄소 영향을 줄이는 방향의 재료를 가정"
    },
    "🔩 저탄소 철강": {
        "pollution": 7,
        "description": "철강 생산 과정의 탄소 영향을 줄이는 방향을 가정"
    },
    "🌲 목재·바이오 기반 재료": {
        "pollution": 3,
        "description": "재생 가능한 바이오 기반 재료를 사용하는 선택"
    },
    "♻️ 재사용·재활용 재료": {
        "pollution": 2,
        "description": "기존 자원을 다시 활용하는 순환형 건축 재료"
    },
}

TECH_DATA = {
    "☀️ 태양광 발전": -9,
    "🌬️ 자연 환기": -7,
    "🪟 외부 차양": -6,
    "🌿 녹색 지붕": -7,
    "💧 빗물 활용": -5,
    "♻️ 물 재이용": -5,
}

DECOR_DATA = {
    "🌳 수직 정원": -5,
    "🌿 녹색 벽": -4,
    "🌱 건물 주변 녹지": -4,
    "🪴 옥상 정원": -5,
}

# =========================================================
# 오염지수 계산
# =========================================================

def calculate_pollution():

    # 90을 출발점으로 하는 게임용 지표
    score = 90

    score += USAGE_DATA[st.session_state.usage]["pollution"]
    score += SHAPE_DATA[st.session_state.shape]["pollution"]
    score += MATERIAL_DATA[st.session_state.material]["pollution"]

    for tech in st.session_state.technologies:
        score += TECH_DATA[tech]

    for decor in st.session_state.decorations:
        score += DECOR_DATA[decor]

    return max(0, min(100, score))


# =========================================================
# 건축물 HTML
# =========================================================

def building_html():

    usage = st.session_state.usage
    shape = st.session_state.shape

    if "돔형" in shape:
        border_radius = "85px 85px 8px 8px"
    elif "테라스" in shape:
        border_radius = "5px 5px 25px 25px"
    elif "지하" in shape:
        border_radius = "35px 35px 3px 3px"
    else:
        border_radius = "5px"

    height = SHAPE_DATA[shape]["height"]

    windows = ""
    for _ in range(9):
        windows += '<div class="window"></div>'

    trees = ""
    if st.session_state.decorations:
        trees = """
        <div class="tree tree1"></div>
        <div class="tree tree2"></div>
        """

    return f"""
    <div class="future-city">

        <div class="city-building city1"></div>
        <div class="city-building city2"></div>
        <div class="city-building city3"></div>
        <div class="city-building city4"></div>
        <div class="city-building city5"></div>

        <div class="horizon"></div>

        <div class="building-scene">
            <div class="building"
                 style="height:{height}px;
                        border-radius:{border_radius};">

                <div style="
                    font-size:11px;
                    color:#b8d8d0;
                    text-align:center;
                    letter-spacing:1px;
                    margin-bottom:8px;">
                    2050 FUTURE ARCHITECT
                </div>

                <div class="windows">
                    {windows}
                </div>

            </div>
        </div>

        {trees}

        <div class="ground"></div>

        <div style="
            position:absolute;
            left:25px;
            top:25px;
            color:#d8e4e1;
            font-family:'Orbitron';
            font-size:13px;
            letter-spacing:2px;">
            YEAR 2050
        </div>

        <div style="
            position:absolute;
            right:25px;
            top:25px;
            color:#8faaa5;
            font-size:12px;">
            AIR QUALITY : CRITICAL
        </div>

    </div>
    """


# =========================================================
# 사이드바
# =========================================================

with st.sidebar:

    st.markdown("## 🏙️ 2050 ARCHITECT")

    st.caption("오염된 미래의 지구에서 새로운 건축물을 설계하세요.")

    st.divider()

    pages = {
        "🌍 메인": "HOME",
        "🏠 건축물 용도": "USAGE",
        "🏗️ 건축 형태": "SHAPE",
        "🧱 건축 자재": "MATERIAL",
        "⚡ 미래 기술": "TECH",
        "🎨 건축물 꾸미기": "DECOR",
        "🏆 완성 결과": "RESULT",
    }

    for label, page_name in pages.items():

        if st.button(
            label,
            key=f"nav_{page_name}",
            use_container_width=True
        ):
            st.session_state.page = page_name
            st.rerun()

    st.divider()

    pollution = calculate_pollution()

    st.markdown("### 현재 오염지수")

    st.progress(pollution / 100)

    st.markdown(
        f"""
        <div style="text-align:center;
                    font-family:'Orbitron';
                    font-size:27px;
                    margin:8px;">
            {pollution}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption("낮을수록 미래 환경에 적합한 설계")


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "HOME":

    st.markdown(
        '<div class="main-title">2050 FUTURE ARCHITECT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">BUILD A FUTURE THAT CAN SURVIVE.</div>',
        unsafe_allow_html=True
    )

    st.markdown(building_html(), unsafe_allow_html=True)

    st.markdown("")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("""
        <div class="card">

        <h2>🌍 2050년, 지구는 변했습니다.</h2>

        <p>
        대기오염과 기후 변화가 심해진 가상의 2050년.
        기존의 건축 방식만으로는 새로운 환경에 대응하기 어렵습니다.
        </p>

        <p>
        당신은 이 도시의 미래 건축가입니다.
        건축물의 용도와 형태, 재료, 미래 기술을 선택하고
        새로운 시대에 맞는 건축물을 완성해야 합니다.
        </p>

        <p>
        <b>목표는 하나.</b><br>
        오염지수를 낮추어 미래 도시에서 살아남을 수 있는 건축물을 만드는 것.
        </p>

        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🚀 미래 건축 설계 시작",
            type="primary",
            use_container_width=True
        ):
            st.session_state.page = "USAGE"
            st.rerun()

    with col2:

        st.markdown("""
        <div class="card">

        <h3>MISSION</h3>

        <p>① 건축물 용도 선택</p>
        <p>② 건축 형태 선택</p>
        <p>③ 건축 자재 선택</p>
        <p>④ 미래 기술 선택</p>
        <p>⑤ 건축물 꾸미기</p>
        <p>⑥ 최종 오염지수 확인</p>

        <hr>

        <p>
        <b>🏆 SUCCESS</b><br>
        오염지수 40 이하
        </p>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# USAGE
# =========================================================

elif st.session_state.page == "USAGE":

    st.markdown("## 🏠 01. 건축물 용도")

    st.markdown("""
    <div class="card">
    <h2>어떤 건축물을 만들까요?</h2>
    <p>
    2050년의 환경에서 사람들이 어떤 목적으로 사용할 건축물인지 선택하세요.
    </p>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        "건축물 용도를 선택하세요.",
        list(USAGE_DATA.keys()),
        index=list(USAGE_DATA.keys()).index(st.session_state.usage)
    )

    st.session_state.usage = selected

    st.info(
        "건축물의 용도에 따라 필요한 공간과 에너지 사용 특성이 달라질 수 있습니다."
    )

    if st.button("다음 → 건축 형태", type="primary"):
        st.session_state.page = "SHAPE"
        st.rerun()


# =========================================================
# SHAPE
# =========================================================

elif st.session_state.page == "SHAPE":

    st.markdown("## 🏗️ 02. 건축 형태")

    st.markdown("""
    <div class="card">
    <h2>미래 건축물의 형태를 결정하세요.</h2>
    <p>
    같은 기능의 건축물이라도 형태와 공간 구성에 따라
    환경에 대응하는 방식이 달라질 수 있습니다.
    </p>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        "건축 형태",
        list(SHAPE_DATA.keys()),
        index=list(SHAPE_DATA.keys()).index(st.session_state.shape)
    )

    st.session_state.shape = selected

    st.markdown(building_html(), unsafe_allow_html=True)

    if st.button("다음 → 건축 자재", type="primary"):
        st.session_state.page = "MATERIAL"
        st.rerun()


# =========================================================
# MATERIAL
# =========================================================

elif st.session_state.page == "MATERIAL":

    st.markdown("## 🧱 03. 건축 자재")

    st.markdown("""
    <div class="card">
    <h2>건축물의 재료를 선택하세요.</h2>
    <p>
    건축 재료의 생산과 사용 과정에서도 환경에 영향을 줄 수 있습니다.
    어떤 재료를 선택할지 결정하세요.
    </p>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        "주요 건축 자재",
        list(MATERIAL_DATA.keys()),
        index=list(MATERIAL_DATA.keys()).index(st.session_state.material)
    )

    st.session_state.material = selected

    st.success(
        MATERIAL_DATA[selected]["description"]
    )

    st.markdown("""
    <div class="source-box">
    📚 자료 근거<br>
    UNEP, <i>Building Materials and the Climate: Constructing a New Future</i>
    는 건축 재료의 생산과 사용 과정에서 발생하는 환경 영향을 고려하고,
    재사용·순환형 재료와 저탄소 재료로 전환하는 방향을 제시합니다.
    </div>
    """, unsafe_allow_html=True)

    if st.button("다음 → 미래 기술", type="primary"):
        st.session_state.page = "TECH"
        st.rerun()


# =========================================================
# TECH
# =========================================================

elif st.session_state.page == "TECH":

    st.markdown("## ⚡ 04. 미래 기술 및 요소")

    st.markdown("""
    <div class="card">
    <h2>2050년의 건축 기술을 선택하세요.</h2>
    <p>
    여러 기술을 동시에 선택할 수 있습니다.
    어떤 기술을 적용할지는 당신의 설계 전략에 달려 있습니다.
    </p>
    </div>
    """, unsafe_allow_html=True)

    selected = st.multiselect(
        "적용할 미래 기술을 선택하세요.",
        list(TECH_DATA.keys()),
        default=st.session_state.technologies
    )

    st.session_state.technologies = selected

    if selected:
        st.write("현재 선택한 기술")

        for item in selected:
            st.write(f"• {item}")

    st.markdown("""
    <div class="source-box">
    📚 자료 근거<br>
    IPCC는 기후 적응형 건축과 관련해 외부 차양, 자연환기,
    단열, 태양 방향을 고려한 설계, 녹색 지붕·벽,
    물 관리 등의 방법을 설명합니다.
    </div>
    """, unsafe_allow_html=True)

    if st.button("다음 → 건축물 꾸미기", type="primary"):
        st.session_state.page = "DECOR"
        st.rerun()


# =========================================================
# DECOR
# =========================================================

elif st.session_state.page == "DECOR":

    st.markdown("## 🎨 05. 건축물 꾸미기")

    st.markdown("""
    <div class="card">
    <h2>마지막으로 건축물의 자연 요소를 추가하세요.</h2>
    <p>
    건물의 외관을 꾸미면서 동시에 녹지와 자연 요소를 설계에 넣을 수 있습니다.
    </p>
    </div>
    """, unsafe_allow_html=True)

    selected = st.multiselect(
        "추가할 요소를 선택하세요.",
        list(DECOR_DATA.keys()),
        default=st.session_state.decorations
    )

    st.session_state.decorations = selected

    st.markdown(building_html(), unsafe_allow_html=True)

    st.markdown("")

    if st.button(
        "🏗️ 건축물 완성하기",
        type="primary",
        use_container_width=True
    ):
        st.session_state.completed = True
        st.session_state.page = "RESULT"
        st.rerun()


# =========================================================
# RESULT
# =========================================================

elif st.session_state.page == "RESULT":

    pollution = calculate_pollution()

    st.markdown("## 🏆 06. 2050 건축물 완성")

    st.markdown(building_html(), unsafe_allow_html=True)

    st.markdown("")

    # 성공 여부
    if pollution <= 40:

        st.markdown("""
        <div class="complete-banner">

        <h1>🏆 MISSION SUCCESS</h1>

        <p>
        당신의 건축물은 2050년의 오염된 환경에서
        살아남을 수 있는 설계 조건을 달성했습니다.
        </p>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="danger-banner">

        <h1>⚠️ MISSION FAILED</h1>

        <p>
        현재 설계의 오염지수가 목표 기준을 넘었습니다.
        다른 재료나 미래 기술을 선택해 설계를 다시 시도해보세요.
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="metric-box">
            <div class="metric-number">{pollution}</div>
            <div class="metric-label">오염지수</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-box">
            <div class="metric-number">{len(st.session_state.technologies)}</div>
            <div class="metric-label">미래 기술</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-box">
            <div class="metric-number">{len(st.session_state.decorations)}</div>
            <div class="metric-label">자연 요소</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 📋 나의 설계")

    st.write(f"**건축물 용도:** {st.session_state.usage}")
    st.write(f"**건축 형태:** {st.session_state.shape}")
    st.write(f"**건축 자재:** {st.session_state.material}")

    if st.session_state.technologies:
        st.write(
            "**미래 기술:** "
            + ", ".join(st.session_state.technologies)
        )
    else:
        st.write("**미래 기술:** 선택하지 않음")

    if st.session_state.decorations:
        st.write(
            "**꾸미기 요소:** "
            + ", ".join(st.session_state.decorations)
        )
    else:
        st.write("**꾸미기 요소:** 선택하지 않음")

    st.markdown("""
    <div class="source-box">

    ### 📚 프로그램에 사용한 자료

    <b>UNEP · Global Alliance for Buildings and Construction</b><br>
    건물·건설 부문의 에너지 사용과 CO₂ 배출,
    건축 재료의 탄소 영향 및 저탄소·순환형 건축 방향을 참고했습니다.

    <br><br>

    <b>UNEP · Building Materials and the Climate</b><br>
    건축 재료의 전 생애 과정과 저탄소 재료,
    재사용·순환형 건축 재료에 대한 내용을 참고했습니다.

    <br><br>

    <b>IPCC · AR6 WGII Chapter 6</b><br>
    녹색 지붕·벽, 도시 녹지, 차양, 자연환기,
    단열, 물 관리 등 기후 적응형 건축 요소를 참고했습니다.

    <br><br>

    <b>중요:</b> 오염지수는 위 자료를 바탕으로 프로그램의 선택 요소에
    차이를 주기 위해 만든 <b>게임용 가상 지표</b>이며,
    실제 건물의 탄소배출량이나 환경성능을 계산한 값은 아닙니다.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "🌍 메인으로 돌아가기",
            use_container_width=True
        ):
            st.session_state.page = "HOME"
            st.rerun()

    with col2:
        if st.button(
            "🔄 새로운 건축물 만들기",
            use_container_width=True
        ):

            st.session_state.completed = False
            st.session_state.usage = "🏠 미래 주거시설"
            st.session_state.shape = "🏙️ 수직형 타워"
            st.session_state.material = "🧱 저탄소 콘크리트"
            st.session_state.technologies = []
            st.session_state.decorations = []

            st.session_state.page = "USAGE"
            st.rerun()
