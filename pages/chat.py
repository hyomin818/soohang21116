import streamlit as st
import random
import requests

st.set_page_config(page_title="2050 주민 대화", page_icon="💬", layout="wide")

# 선택된 건축 설계 정보는 메인 페이지의 session_state에서 읽습니다.
USAGE_PEOPLE = {
    "🏠 미래 주거시설": ["주민", "건물 관리인"],
    "🏫 미래 학교": ["학생", "교사", "건물 관리인"],
    "🏥 미래 병원": ["환자", "의사", "건물 관리인"],
    "🔬 미래 연구센터": ["연구원", "건물 관리인"],
}
SHAPE_TEXT = {
    "🏙️ 수직형 타워": "높은 층에 살면 전망은 좋지만 엘리베이터를 기다리는 시간이 길게 느껴질 때가 있어요.",
    "🌿 테라스형": "테라스가 있으면 바깥 공기를 쐬거나 식물을 돌보며 잠깐 쉴 수 있어요. 비 오거나 바람이 강한 날은 아쉬워요.",
    "🛸 돔형": "천장이 높고 공간이 탁 트인 느낌이에요. 다만 햇빛이 강한 날에는 눈부심이 생기는지 신경 쓰여요.",
    "🌍 저층 생태형": "바깥 공간과 가까워서 편안해요. 목적지에 따라 걸어 다니는 거리가 길어질 때는 있어요.",
    "🌍 반지하형": "바깥 날씨 영향을 덜 받는 느낌이지만, 햇빛이 잘 들어오는지와 습도 관리가 중요해요.",
}
MATERIAL_TEXT = {
    "🧱 저탄소 콘크리트": "실내는 차분하고 묵직한 느낌이에요. 저는 재료의 생산 방식보다는 실제로 지낼 때의 분위기가 먼저 느껴져요.",
    "🔩 저탄소 철강": "프레임이 보이는 곳은 도시적이고 단단한 인상을 줘요. 공간에 따라 조금 차갑게 느껴질 수도 있어요.",
    "🌲 목재·바이오 기반": "나무 느낌이 있는 공간은 따뜻하고 편안하게 느껴져요. 표면이나 관리 상태에 따라서 느낌이 달라질 것 같아요.",
    "♻️ 재사용·재활용 재료": "재료마다 색이나 표면이 조금씩 달라서 공간에 개성이 생길 수 있어요.",
}
TECH_TEXT = {
    "☀️ 태양광 발전": "공용 공간에서 쓰는 전기를 건물에서 만든다는 점이 마음에 들어요. 실제로 얼마나 절약되는지도 알 수 있으면 좋겠어요.",
    "🌬️ 자연환기": "날씨가 좋을 때는 공기가 답답하지 않아서 좋아요. 바깥 공기가 나쁜 날에는 다른 환기 방법도 필요하겠죠.",
    "🪟 외부 차양": "햇빛이 강한 시간에 눈부심이 줄어들면 실내에서 지내기가 훨씬 편해요.",
    "🌱 녹화 지붕": "초록이 보이면 건물이 덜 삭막하게 느껴져요. 옥상 주변의 더위를 줄이는 데도 도움이 될 수 있어요.",
    "💧 빗물 이용": "빗물을 조경에 활용한다면 물을 아낀다는 점에서 괜찮은 것 같아요.",
    "🔄 물 재이용": "물을 아껴 쓰는 건 좋은데, 어떤 용도로 다시 쓰는지 안내가 잘 되어 있으면 더 안심될 것 같아요.",
}
COST = {
    "🏠 미래 주거시설": 10, "🏫 미래 학교": 8, "🏥 미래 병원": 16, "🔬 미래 연구센터": 12,
    "🏙️ 수직형 타워": 18, "🌿 테라스형": 15, "🌿 테라스형 건축": 15, "🛸 돔형": 22, "🛸 돔형 건축": 22,
    "🌍 저층 생태형": 12, "🌍 반지하형": 12, "🌍 반지하형 건축": 12,
    "🧱 저탄소 콘크리트": 12, "🔩 저탄소 철강": 18, "🌲 목재·바이오 기반": 24, "♻️ 재사용·재활용 재료": 20,
    "☀️ 태양광 발전": 30, "🌬️ 자연환기": 15, "🪟 외부 차양": 10, "🌱 녹화 지붕": 18, "💧 빗물 이용": 7, "🔄 물 재이용": 15,
}
COLORS = {
    "#5D7F7A": "미래형 민트", "#A77D5C": "사막 모래", "#C9D4D0": "화이트",
    "#345C78": "딥 블루", "#46634E": "포레스트", "#A76543": "오렌지",
}

st.markdown("""
<style>
.stApp {background:linear-gradient(135deg,#071114,#102226 55%,#091417); color:#f5fbff;}
.block-container {max-width:1120px; padding-top:1.5rem; padding-bottom:3rem;}
h1,h2,h3,h4,p,li,label,small,.stMarkdown,[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p {color:#f5fbff !important;}
[data-testid="stCaptionContainer"],.stCaption {color:#c2d1d5 !important;}
section[data-testid="stSidebar"] {background:#142327; border-right:1px solid #3b555b;}
section[data-testid="stSidebar"] * {color:#f5fbff !important;}
div[data-testid="stChatMessage"] {background:#15282c; border:1px solid #355159; border-radius:16px; padding:1rem;}
div[data-testid="stChatMessage"] p {color:#f8fcff !important; line-height:1.75; font-size:16px;}
[data-testid="stChatInput"] textarea {background:#f7fafb !important; color:#142327 !important; caret-color:#142327 !important;}
[data-testid="stChatInput"] textarea::placeholder {color:#53656a !important;}
[data-testid="stSelectbox"] label {color:#f5fbff !important;}
/* 질문 버튼: 전역 흰색 글씨 규칙보다 우선하도록 버튼 내부까지 명시 */
div[data-testid="stButton"] > button,
div[data-testid="stButton"] > button *,
.stButton button,
.stButton button p,
.stButton button span,
.stButton button div {
    background-color: #f2f7f8 !important;
    color: #142327 !important;
    -webkit-text-fill-color: #142327 !important;
    border-color: #b8c9ce !important;
    border-radius: 10px !important;
    font-weight: 650 !important;
    text-shadow: none !important;
}
div[data-testid="stButton"] > button { min-height: 42px; }
div[data-testid="stButton"] > button:hover,
div[data-testid="stButton"] > button:hover * {
    background-color: #dceced !important;
    color: #071114 !important;
    -webkit-text-fill-color: #071114 !important;
}
div[data-testid="stAlert"] p {color:#f5fbff !important;}
hr {border-color:#3b555b !important;}
</style>
""", unsafe_allow_html=True)

# Read design values saved by the main app. Defaults keep the chat page usable on its own.
usage = st.session_state.get("usage", "🏠 미래 주거시설")
shape = st.session_state.get("shape", "🏙️ 수직형 타워")
material = st.session_state.get("material", "🧱 저탄소 콘크리트")
techs = st.session_state.get("technologies", [])
if not isinstance(techs, list):
    techs = list(techs) if techs else []
color = st.session_state.get("building_color", "#5D7F7A")
people = USAGE_PEOPLE.get(usage, USAGE_PEOPLE["🏠 미래 주거시설"])

def cost_of(value, fallback=0):
    return COST.get(value, fallback)

design_cost = cost_of(usage, 10) + cost_of(shape, 18) + cost_of(material, 12)
tech_cost = sum(cost_of(item, 0) for item in techs)
total_cost = design_cost + tech_cost
budget = st.session_state.get("budget", 100)
remaining = budget - total_cost
pollution = st.session_state.get("pollution_index", st.session_state.get("pollution", None))
if pollution is None:
    usage_add = 4 if "주거" in usage else 2 if "학교" in usage else 6 if "병원" in usage else 3
    shape_add = 7 if "타워" in shape else 3 if "테라스" in shape else 2 if "돔" in shape else 1
    material_add = 6 if "콘크리트" in material else 5 if "철강" in material else 2 if "목재" in material else 0
    reductions = {"☀️ 태양광 발전": 10, "🌬️ 자연환기": 7, "🪟 외부 차양": 6, "🌱 녹화 지붕": 7, "💧 빗물 이용": 5, "🔄 물 재이용": 5}
    pollution = max(0, min(100, 42 + usage_add + shape_add + material_add - sum(reductions.get(t, 0) for t in techs)))

# Reset old messages if the building design has changed.
signature = (usage, shape, material, tuple(techs), color, total_cost, pollution)
if st.session_state.get("resident_chat_signature") != signature:
    st.session_state["resident_chat_signature"] = signature
    st.session_state["resident_chat_history"] = []
    st.session_state["resident_chat_character"] = None

def first_message(person):
    if person == "건물 관리인":
        tech_names = ", ".join(techs) if techs else "선택된 미래 기술 없음"
        return "안녕하세요. 건물 관리인입니다. 현재 설계 비용은 {}억원이고 남은 예산은 {}억원입니다. 선택된 기술은 {}입니다. 설비 유지관리나 운영비 관련 질문에 답변드리겠습니다.".format(total_cost, remaining, tech_names)
    if person == "학생":
        return random.choice([
            "나 여기 다니는 학생이야! 쉬는 시간에 편하게 앉아 있을 데가 있는지가 은근 중요해. 학교에서 지내는 느낌 궁금한 거 있어?",
            "안녕! 학교 건물은 수업 시간 말고 쉬는 시간에도 오래 있잖아. 햇빛이나 소리, 친구들이랑 머물 공간 같은 얘기 해줄게."
        ])
    if person == "교사":
        return "안녕하세요. 이 학교에서 학생들을 가르치고 있어요. 수업할 때나 쉬는 시간에 실제로 느끼는 점을 솔직하게 말씀드릴게요."
    if person == "환자":
        return "안녕하세요. 진료를 받으러 왔다가 대기하는 시간이 길어졌어요. 아플 때는 눈부심이나 소음도 신경 쓰이더라고요. 환자 입장에서 느낀 점을 이야기해 볼게요."
    if person == "의사":
        return "안녕하세요. 이 병원에서 일하는 의사입니다. 환자들이 기다릴 때 편안한지, 직원들이 이동하기에 괜찮은지 실제 사용 경험을 말씀드릴게요."
    if person == "연구원":
        return "안녕하세요! 여기서 연구하는 사람입니다. 하루 종일 집중하다 보면 빛이나 온도, 잠깐 쉴 공간이 중요하더라고요. 직접 지내며 느낀 점을 알려드릴게요."
    return random.choice([
        "안녕하세요! 여기 사는 주민이에요. 도면으로 볼 때랑 직접 살아볼 때는 또 다르더라고요. 좋은 점도 아쉬운 점도 편하게 물어봐요.",
        "안녕! 여기 살면서 느낀 점을 솔직하게 얘기해 줄게요. 멋진 외관도 좋지만, 매일 지내기 편한지가 제일 중요하더라고요."
    ])

def generate_natural_reply(message, person):
    """Use Gemini for open-ended, context-aware resident conversation when an API key is configured."""
    api_key = None
    try:
        api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
    except Exception:
        api_key = None

    if not api_key:
        return None

    usage_label = usage
    pollution_level = "낮음" if pollution <= 35 else "보통" if pollution <= 65 else "높음"
    if pollution <= 35:
        air_context = "오염지수가 낮아 주민은 공기가 비교적 쾌적하고 바깥 활동이 편하다고 느낄 수 있다. 단, 과장된 의학적 주장은 하지 않는다."
    elif pollution <= 65:
        air_context = "오염지수가 중간 정도라 주민은 날이나 시간대에 따라 공기가 괜찮기도 하고 답답하기도 하다고 말할 수 있다."
    else:
        air_context = "오염지수가 높아 주민은 공기가 탁하고 목이 칼칼하거나 오래 바깥에 있기 불편하다고 느낄 수 있다. 극단적인 공포를 조장하지 말고, 건물 안에서도 환기와 공기 정화가 중요하다고 말한다."

    system_prompt = f"""
너는 2050년에 완성된 건물에서 실제로 생활하는 '{person}'이다. 사용자와 자연스럽게 한국어로 대화한다.
이 사용자는 건축가이며 건축 자재와 설계의 전문 설명을 이미 잘 알고 있다. 그러므로 자재 사전을 읽듯 설명하거나 건축가를 가르치려 들지 말고, 실제 거주자의 후기, 생활 속 감정, 불편함, 작은 에피소드를 중심으로 말한다.
사용자가 건물과 무관한 일상 이야기나 전혀 다른 주제를 꺼내도 그 말에 자연스럽게 반응하고 대화를 이어간다. 매번 건축 이야기로 억지로 되돌리지 않는다. 너무 형식적인 문장, 같은 문구 반복, 보고서 말투, 목록식 답변을 피한다. 보통 2~5문장 정도로 말하고, 대화체를 사용한다.
건물 용도: {usage_label}
건물 형태: {shape}
선택 자재: {material}
선택 미래 기술: {", ".join(techs) if techs else "선택한 미래 기술 없음"}
외관 색상: {COLORS.get(color, color)}
현재 설계 총비용: {total_cost}억원 / 초기 예산 {budget}억원
남은 예산: {remaining}억원
게임 오염지수: {pollution}/100 ({pollution_level})
환경 체감 지침: {air_context}
건물 형태의 생활 체감: {SHAPE_TEXT.get(shape, "")}
자재의 생활 체감: {MATERIAL_TEXT.get(material, "")}
선택 기술의 생활 체감: {" ".join(TECH_TEXT[t] for t in techs if t in TECH_TEXT) or "특별히 선택한 미래 기술이 없음"}
대화 상대가 건물 관리인이면 설비, 예산, 유지관리 질문에 정확하고 조금 더 체계적으로 답한다. 그 외 인물은 비용 산정이나 자재의 기술적 특성을 전문가처럼 강의하지 말고 자기 경험을 말한다.
예산이 부족하거나 남은 예산이 적다는 사실은 질문이 비용/설계/생활에 관련될 때 자연스럽게 반영한다. 주민은 예산을 정확히 알지 못할 수 있으므로, 사용자가 직접 묻지 않는 한 숫자를 줄줄 말하지 않는다.
오염지수가 낮으면 쾌적함, 산책하기 편함, 창문을 열기 편함 등을 경험으로 표현할 수 있다. 오염지수가 높으면 공기가 탁함, 먼지, 답답함, 목이 칼칼한 느낌, 창문을 열기 망설여짐 등을 자연스럽게 언급한다. 이는 게임 속 설정이며 실제 건강 진단처럼 말하지 않는다.
선택한 기술의 영향도 주민 경험에 반영한다. 자연환기면 날씨가 좋을 때 환기, 차양이면 눈부심/더위 감소, 태양광이면 공용 전기 사용에 대한 체감, 녹화 지붕이면 초록 풍경과 열감, 빗물/물 재이용이면 물 절약에 대한 경험을 말한다.
학생/교사/환자/의사/연구원/주민 등 역할에 맞는 말투를 유지한다. 이모지는 과하게 쓰지 않는다.
사용자 메시지에 답만 하고 끝내지 말고, 필요하면 실제 사람처럼 짧은 맞장구나 자연스러운 되물음을 하나 곁들인다. 모르는 사실을 아는 척하지 않는다.
"""
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": message}]}],
        "generationConfig": {"temperature": 0.9, "maxOutputTokens": 350}
    }
    try:
        response = requests.post(
            url,
            params={"key": api_key},
            json=payload,
            timeout=20
        )
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception:
        return None


def reply_to(message, person):
    q = message.lower()
    if person == "건물 관리인":
        if any(word in q for word in ["예산", "비용", "가격", "돈", "얼마"]):
            return "현재 총비용은 {}억원이며 남은 예산은 {}억원입니다. 용도 {}억원, 형태 {}억원, 자재 {}억원, 미래 기술 {}억원으로 계산했습니다.".format(total_cost, remaining, cost_of(usage, 10), cost_of(shape, 18), cost_of(material, 12), tech_cost)
        if any(word in q for word in ["기술", "설비", "유지", "관리", "고장", "운영"]):
            details = " ".join(TECH_TEXT[t] for t in techs if t in TECH_TEXT)
            if not details:
                details = "현재 선택된 미래 기술은 없습니다."
            return "관리 측면에서는 정기 점검과 부품 교체가 중요합니다. " + details
        if any(word in q for word in ["오염", "탄소", "환경", "지수"]):
            return "게임상 오염지수는 {}/100입니다. 시뮬레이션용 점수이며 실제 건물 인증값은 아닙니다. 실제 성능은 자재 자료, 설비 효율, 사용량과 유지관리 상태를 함께 확인해야 합니다.".format(pollution)
        return "현재 형태는 {}, 자재는 {}입니다. 운영 중에는 점검 공간과 부품 교체 접근성을 확인해야 합니다. 총비용은 {}억원이고 남은 예산은 {}억원입니다.".format(shape, material, total_cost, remaining)

    if any(word in q for word in ["불편", "아쉬", "단점", "문제", "고쳐", "개선"]):
        if "타워" in shape:
            return "솔직히 높은 층에서 엘리베이터 기다릴 때는 좀 답답해. 출근이나 등교 시간이 겹치면 더 그렇고."
        if "테라스" in shape:
            return "테라스는 진짜 좋은데 비 오고 나면 바닥이 미끄럽거나 바람이 세서 오래 못 있을 때가 있어. 배수랑 그늘도 잘 되어 있으면 좋겠어."
        if "돔" in shape:
            return "공간이 멋있긴 한데 햇빛이 강한 날엔 눈부실 것 같아. 벽 쪽이 둥글어서 가구 놓는 게 애매한 자리도 있을 수 있겠더라."
        return "큰 불편은 없어도 사람마다 필요한 게 다르더라. 조용히 쉴 자리나 이동 동선은 더 신경 써주면 좋겠어."
    if any(word in q for word in ["좋은 점", "장점", "만족", "후기", "마음에", "좋아", "어때", "평가"]):
        if person == "학생":
            return "친구들이랑 잠깐 얘기하거나 앉아 있을 공간이 있으면 좋아. 교실만 왔다 갔다 하는 것보다 쉬는 시간이 덜 지루하거든."
        if person == "교사":
            return "학생들이 수업 외 시간에도 편하게 머물 수 있다는 점이 좋아요. 잠깐 쉬거나 이야기할 공간이 있으면 학교생활이 한결 여유로워져요."
        if person == "환자":
            return "기다리는 동안 눈이 부시거나 주변이 시끄럽지 않은 게 제일 좋아요. 아플 때는 작은 불편도 크게 느껴지거든요."
        if person == "의사":
            return "환자들이 덜 불안하게 기다릴 수 있고 직원들도 이동하기 편하면 좋습니다. 실제로 이용하기 편한 공간인지가 중요해요."
        if person == "연구원":
            return "집중할 수 있는 조용한 자리랑 잠깐 머리를 식힐 공간이 있는 게 좋아요. 하루 종일 일하면 그런 차이가 크게 느껴져요."
        return "제일 마음에 드는 건 공간이 주는 느낌이에요. {} 직접 지내보면 외관보다 빛이나 소리, 쉴 곳이 더 크게 느껴질 때도 있어요.".format(SHAPE_TEXT.get(shape, "공간이 편안해요."))
    if any(word in q for word in ["덥", "더위", "시원", "햇빛", "눈부", "온도", "추워"]):
        if "🪟 외부 차양" in techs:
            return "햇빛이 강한 시간에도 눈이 덜 부셔서 좋아. 계절이나 창문 방향에 따라 다르겠지만 낮에 머물기 한결 편해."
        return "한낮에는 햇빛이 강한 자리가 좀 덥거나 눈부실 수 있어. 그늘이 있거나 햇빛을 조절할 수 있으면 훨씬 편할 것 같아."
    if any(word in q for word in ["공기", "환기", "답답", "냄새", "바람"]):
        if "🌬️ 자연환기" in techs:
            return "날씨 괜찮을 때는 창문 열고 공기를 바꿀 수 있어서 좋아. 다만 바깥 공기가 안 좋은 날에는 다른 환기 방법도 필요해."
        return "사람이 많을 때는 조금 답답하게 느껴질 수 있어. 창문을 열기 어려운 날에도 공기가 잘 돌면 좋겠어."
    if any(word in q for word in ["소음", "시끄", "조용", "소리"]):
        return "사람이 몰리는 시간에는 복도나 공용 공간 소리가 들릴 때가 있어. 조용히 쉴 수 있는 자리가 따로 있으면 좋겠어."
    if any(word in q for word in ["물", "빗물", "수도"]):
        if any(t in techs for t in ["💧 빗물 이용", "🔄 물 재이용"]):
            return "물을 아껴 쓰는 설비가 있다는 게 좋아. 어떤 물을 어디에 다시 쓰는지 안내가 잘 되어 있으면 더 안심될 것 같아."
        return "물 쓰는 데 큰 불편은 없지만, 조경이나 청소에 빗물을 활용하면 물을 아낄 수 있을 것 같아."
    if any(word in q for word in ["전기", "전기료", "태양광"]):
        if "☀️ 태양광 발전" in techs:
            return "지붕에서 전기를 만든다는 점은 마음에 들어. 공용 전기료가 얼마나 줄었는지도 알 수 있으면 더 실감 날 것 같아."
        return "태양광이 있으면 공용 공간 전기 사용에 도움이 될 것 같아. 실제로 얼마나 절약되는지는 사용량을 봐야겠지."
    if any(word in q for word in ["자재", "재료", "콘크리트", "철강", "목재", "재활용"]):
        return "자재의 전문적인 장단점은 설계자인 네가 더 잘 알겠지만, 이용자 입장에서는 실내 분위기나 소리 울림, 만졌을 때 느낌이 먼저 와닿아. " + MATERIAL_TEXT.get(material, "")
    if any(word in q for word in ["기술", "태양광", "차양", "환기", "녹화"]):
        used = [TECH_TEXT[t] for t in techs if t in TECH_TEXT]
        if used:
            return "내가 느끼는 건 이런 부분이야. " + " ".join(used) + " 실제 생활에서 얼마나 체감되는지가 중요하더라."
        return "지금은 특별히 선택된 미래 기술이 없네. 그래도 일상에서는 햇빛, 공기, 소음처럼 매일 느끼는 부분이 중요해."
    if any(word in q for word in ["가격", "비용", "예산", "돈", "얼마"]):
        return "비용은 내가 자세히 알진 못하지만, 주민 입장에서는 돈을 들인 만큼 생활이 편해졌는지가 궁금해. 햇빛이 덜 눈부신지, 공기가 덜 답답한지 같은 거."
    if any(word in q for word in ["오염", "환경", "탄소", "친환경", "지수"]):
        return "환경 점수도 중요하지만, 우리가 실제로 변화를 느끼는지도 중요해. 여름에 덜 덥거나 물을 아껴 쓰는 것처럼 생활에서 느껴지면 더 와닿을 것 같아."
    return random.choice([
        "음, 직접 지내보면 도면에서는 잘 안 보이던 작은 부분이 크게 느껴지더라. 빛이나 소리, 쉬어 갈 자리 같은 거. 어떤 게 궁금해?",
        "내가 설계 설명을 해주긴 어렵지만, 여기서 하루를 보내는 느낌은 솔직하게 말해줄 수 있어. 좋은 점이 궁금해, 불편한 점이 궁금해?",
        "사람마다 다르겠지만 편안함이 제일 중요해. 생활하면서 어떤 상황이 궁금한지 더 구체적으로 물어봐!"
    ])

st.title("💬 완성된 건물, 실제로 살아보면?")
st.write("건축 설명보다 이 건물을 매일 이용하는 사람들의 생활 후기와 불편한 점을 들어보세요.")
try:
    has_gemini_key = bool(st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY"))
except Exception:
    has_gemini_key = False
if not has_gemini_key:
    st.info("자유로운 주제에도 자연스럽게 답하는 대화를 사용하려면 Streamlit Cloud의 Settings → Secrets에 GEMINI_API_KEY를 추가해 주세요. 키가 없으면 기본 대화 규칙으로 응답합니다.")

with st.sidebar:
    st.subheader("🏗️ 현재 설계")
    st.write("**용도:** " + usage)
    st.write("**형태:** " + shape)
    st.write("**자재:** " + material)
    st.write("**미래 기술:** " + (", ".join(techs) if techs else "선택 없음"))
    st.write("**총비용:** {}억원 / {}억원".format(total_cost, budget))
    st.write("**남은 예산:** {}억원".format(remaining))
    st.write("**게임 오염지수:** {}/100".format(pollution))
    st.caption("외관 색상: " + COLORS.get(color, color))
    st.divider()
    selected_person = st.selectbox("누구와 대화할까요?", people, key="resident_person_picker")
    if st.button("대화 처음부터 다시 하기", use_container_width=True):
        st.session_state["resident_history"] = []
        st.rerun()

if st.session_state.get("resident_person_current") != selected_person:
    st.session_state["resident_person_current"] = selected_person
    st.session_state["resident_history"] = []

history = st.session_state.setdefault("resident_history", [])
if not history:
    history.append({"role": "assistant", "content": first_message(selected_person)})

for message in history:
    avatar = "🧑" if message["role"] == "user" else ("🧰" if selected_person == "건물 관리인" else "🙂")
    with st.chat_message(message["role"], avatar=avatar):
        if message["role"] == "assistant":
            st.caption(selected_person)
        st.markdown(message["content"])

prompt = st.chat_input("{}에게 생활 후기를 물어보세요…".format(selected_person))
if prompt:
    history.append({"role": "user", "content": prompt})
    ai_reply = generate_natural_reply(prompt, selected_person)
    history.append({"role": "assistant", "content": ai_reply or reply_to(prompt, selected_person)})
    st.rerun()

st.markdown("### 💡 이렇게 물어봐도 좋아요")
sample_questions = [
    "여기서 살면서 제일 마음에 드는 점은 뭐야?",
    "실제로 불편한 점은 없어?",
    "여름에 덥거나 눈부시진 않아?",
    "공기가 답답하거나 시끄럽진 않아?",
    "내가 고른 기술이 생활에 도움이 돼?",
]
columns = st.columns(5)
for index, question in enumerate(sample_questions):
    with columns[index]:
        if st.button(question, key="sample_question_{}".format(index), use_container_width=True):
            history.append({"role": "user", "content": question})
            ai_reply = generate_natural_reply(question, selected_person)
            history.append({"role": "assistant", "content": ai_reply or reply_to(question, selected_person)})
            st.rerun()
