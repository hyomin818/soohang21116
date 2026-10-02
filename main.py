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
        "budget": 100,
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
    total = MATERIALS[st.session_state.material]["cost"]
    for tech in st.session_state.technologies:
        total += TECHNOLOGIES[tech]["cost"]
    return total

def remaining_budget():
    return st.session_state.budget - design_cost()

def budget_text(value):
    sign = "-" if value < 0 else ""
    return f"{sign}{abs(value):,}억원"

def mission_success():
    return pollution_score() <= 40 and remaining_budget() >= 0
