import streamlit as st

st.set_page_config(page_title="2050 주민 대화", page_icon="💬", layout="wide")

# 이 페이지는 main.py에서 선택한 설계 정보를 st.session_state로 공유합니다.
USAGES = {
    "🏠 미래 주거시설": {"cost": 10, "role": "resident", "people": ["주민", "건물 관리인"], "place": "주거시설"},
    "🏫 미래 학교": {"cost": 8, "role": "student", "people": ["학생", "교사"], "place": "학교"},
    "🏥 미래 병원": {"cost": 16, "role": "patient", "people": ["환자", "의사"], "place": "병원"},
    "🔬 미래 연구센터": {"cost": 12, "role": "researcher", "people": ["연구원", "시설 관리자"], "place": "연구센터"},
}
SHAPES = {
    "🏙️ 수직형 타워": {"cost": 18, "impact": 7},
    "🌿 테라스형 건축": {"cost": 15, "impact": 3},
    "🛸 돔형 건축": {"cost": 22, "impact": 2},
    "🌍 저층 생태형": {"cost": 12, "impact": 1},
}
MATERIALS = {
    "🧱 저탄소 콘크리트": {"cost": 12, "impact": 6},
    "🔩 저탄소 철강": {"cost": 18, "impact": 5},
    "🌲 목재·바이오 기반": {"cost": 24, "impact": 2},
    "♻️ 재사용·재활용 재료": {"cost": 20, "impact": 0},
}
TECHNOLOGIES = {
    "☀️ 태양광 발전": {"cost": 30, "impact": -10},
    "🌬️ 자연환기": {"cost": 15, "impact": -7},
    "🪟 외부 차양": {"cost": 10, "impact": -6},
    "🌱 녹화 지붕": {"cost": 18, "impact": -7},
    "💧 빗물 이용": {"cost": 7, "impact": -5},
    "🔄 물 재이용": {"cost": 15, "impact": -5},
}
COLOR_NAMES = {
    "#5D7F7A": "미래형 민트", "#A77D5C": "사막 모래", "#C9D4D0": "화이트",
    "#345C78": "딥 블루", "#46634E": "포레스트", "#A76543": "오렌지",
}

st.markdown("""
<style>
.stApp {background: radial-gradient(circle at 80% 0%, #193033 0, #081113 42%, #05090a 100%); color:#f4fffc;}
.block-container {max-width:1100px; padding-top:2rem;}
h1,h2,h3,p,label {color:#f4fffc !important;}
[data-testid="stChatMessage"] {background:rgba(17,31,33,.88); border:1px solid rgba(160,220,208,.15); border-radius:16px;}
div[data-testid="stMetric"] {background:#0d1b1d; border:1px solid rgba(155,220,208,.18); border-radius:14px; padding:12px;}
</style>
""", unsafe_allow_html=True)

# Defaults allow this page to open safely even if the main designer has not been visited.
st.session_state.setdefault("budget", 100)
st.session_state.setdefault("usage", "🏠 미래 주거시설")
st.session_state.setdefault("shape", "🏙️ 수직형 타워")
st.session_state.setdefault("material", "🧱 저탄소 콘크리트")
st.session_state.setdefault("technologies", [])
st.session_state.setdefault("building_color", "#5D7F7A")
st.session_state.setdefault("completed", False)

usage = st.session_state.get("usage", "🏠 미래 주거시설")
shape = st.session_state.get("shape", "🏙️ 수직형 타워")
material = st.session_state.get("material", "🧱 저탄소 콘크리트")
techs = list(st.session_state.get("technologies", []))
color = st.session_state.get("building_color", "#5D7F7A")
usage_data = USAGES.get(usage, USAGES["🏠 미래 주거시설"])
shape_data = SHAPES.get(shape, SHAPES["🏙️ 수직형 타워"])
material_data = MATERIALS.get(material, MATERIALS["🧱 저탄소 콘크리트"])
tech_cost = sum(TECHNOLOGIES.get(t, {"cost": 0})["cost"] for t in techs)
total_cost = usage_data["cost"] + shape_data["cost"] + material_data["cost"] + tech_cost
remaining = st.session_state.get("budget", 100) - total_cost
pollution = max(0, 100 - abs(4 if usage == "🏠 미래 주거시설" else 2 if usage == "🏫 미래 학교" else 6 if usage == "🏥 미래 병원" else 3)
               - abs(shape_data["impact"]) - abs(material_data["impact"])
               - 2 * sum(abs(TECHNOLOGIES.get(t, {"impact": 0})["impact"]) for t in techs))
color_name = COLOR_NAMES.get(color, f"사용자 지정 색상 {color}")
tech_text = "、".join(techs) if techs else "선택한 미래 기술 없음"
if not techs:
    tech_text = "선택한 미래 기술 없음"

# The selected design signature resets the conversation only when the design itself changes.
signature = (usage, shape, material, tuple(techs), color, total_cost, pollution)
if st.session_state.get("resident_chat_signature") != signature:
    st.session_state["resident_chat_signature"] = signature
    st.session_state["resident_chat_history"] = []
    st.session_state["resident_chat_character"] = None

people = usage_data["people"]
st.title("💬 완성된 건물의 주민과 대화하기")
st.caption("네가 설계한 건물의 실제 이용자가 되어 이야기를 나눠 보세요. 건물 용도·형태·자재·기술·가격 선택이 대화에 반영됩니다.")

if not st.session_state.get("completed", False):
    st.info("아직 건축물이 완성되지 않았어도 대화는 미리 체험할 수 있어. 꾸미기 페이지에서 '건축물 완성하기'를 누르면 완성된 설계를 기준으로 대화할 수 있어.")

with st.sidebar:
    st.markdown("## 🏗️ 현재 설계")
    st.write(f"**용도:** {usage}")
    st.write(f"**형태:** {shape}")
    st.write(f"**자재:** {material}")
    st.write("**미래 기술:** " + (", ".join(techs) if techs else "없음"))
    st.write(f"**총비용:** {total_cost}억원 / 100억원")
    st.write(f"**남은 예산:** {remaining}억원")
    st.write(f"**게임 오염지수:** {pollution} / 100")
    st.caption(f"외관 색상: {color_name}")
    st.divider()
    character = st.selectbox("누구와 대화할까?", people, key="resident_character_select")
    if st.button("💬 대화 다시 시작", use_container_width=True):
        st.session_state["resident_chat_history"] = []
        st.rerun()

# Switching from student to teacher (or patient to doctor) starts a fresh role-specific conversation.
if st.session_state.get("resident_chat_character_current") != character:
    st.session_state["resident_chat_character_current"] = character
    st.session_state["resident_chat_history"] = []

ROLE_LINES = {
    "주민": ("안녕하세요! 이 건물에 사는 주민이에요.", "집에서 보내는 하루를 기준으로 이야기해 볼게요."),
    "건물 관리인": ("반갑습니다. 이 건물의 관리인이에요.", "유지관리와 에너지 비용 관점에서 말씀드릴게요."),
    "학생": ("안녕! 나는 이 학교에 다니는 학생이야.", "교실에서 공부하고 쉬는 입장에서 말해 볼게."),
    "교사": ("안녕하세요. 이 학교에서 학생들을 가르치는 교사입니다.", "수업 환경과 학생들의 생활을 중심으로 이야기하겠습니다."),
    "환자": ("안녕하세요. 이 병원에서 진료를 받고 있는 환자예요.", "편안함, 소음, 실내 공기와 물 사용에 관해 이야기할게요."),
    "의사": ("안녕하세요. 이 병원에서 근무하는 의사입니다.", "환자의 쾌적함과 의료 공간의 운영 조건을 중심으로 답할게요."),
    "연구원": ("안녕하세요. 이 연구센터에서 일하는 연구원입니다.", "연구 환경과 시설의 효율을 기준으로 말씀드릴게요."),
    "시설 관리자": ("반갑습니다. 연구센터 시설을 관리하고 있습니다.", "설비 유지관리와 예산을 중심으로 답하겠습니다."),
}

shape_observations = {
    "🏙️ 수직형 타워": "높게 올라가는 형태라 공간을 효율적으로 쓰지만, 엘리베이터와 수직 이동 동선도 잘 관리해야 해요.",
    "🌿 테라스형 건축": "층마다 테라스가 이어져 바깥 공기와 녹지를 가까이 느낄 수 있어요. 다만 테라스 배수와 관리도 중요해요.",
    "🛸 돔형 건축": "둥근 돔과 삼각형 패널이 여러 방향으로 이어져 공간이 탁 트인 느낌이에요. 곡면 유리의 눈부심과 여름철 열 유입은 잘 조절해야 해요.",
    "🌍 저층 생태형": "높이가 낮고 외부 녹지와 연결되기 쉬워 이동이 편안할 수 있어요. 대신 넓은 부지를 관리해야 해요.",
}
material_observations = {
    "🧱 저탄소 콘크리트": "저탄소 콘크리트를 사용했어요. 익숙하고 단단한 구조를 유지하면서 재료 생산 과정의 환경 부담을 줄이려는 선택이에요.",
    "🔩 저탄소 철강": "저탄소 철강을 선택했어요. 구조를 튼튼하게 만들 수 있지만 생산 방식에 따라 실제 환경 효과가 달라질 수 있어요.",
    "🌲 목재·바이오 기반": "목재·바이오 기반 재료를 사용했어요. 실내에서 따뜻한 느낌을 줄 수 있고 재료 생산의 부담을 낮출 가능성이 있어요. 습기와 화재 안전, 산림 관리도 중요해요.",
    "♻️ 재사용·재활용 재료": "재사용·재활용 재료를 활용했어요. 새 자재 생산을 줄이는 장점이 있지만, 품질 확인과 부품 교체 계획이 중요해요.",
}
tech_observations = {
    "☀️ 태양광 발전": "태양광 설비가 전기를 생산해 외부 전력 사용을 줄여 줘요. 설치 면적과 햇빛 조건에 따라 발전량이 달라져요.",
    "🌬️ 자연환기": "자연환기로 바람이 실내를 지나가게 해요. 바깥 공기가 나쁘거나 날씨가 맞지 않을 때는 보조 설비가 필요해요.",
    "🪟 외부 차양": "외부 차양이 강한 햇빛을 막아 실내가 과열되는 것을 줄여 줘요. 창문 방향에 맞게 설계해야 해요.",
    "🌱 녹화 지붕": "옥상 녹지가 햇빛을 받고 빗물을 머금어 열환경에 도움을 줄 수 있어요. 방수와 하중, 식물 관리가 필요해요.",
    "💧 빗물 이용": "빗물을 모아 조경 등에 활용할 수 있어요. 비가 적게 오는 기간을 대비해 저장 공간을 계획해야 해요.",
    "🔄 물 재이용": "사용한 물을 처리해 다시 활용하는 시스템이에요. 물 사용을 줄이는 대신 처리 장치와 정기적인 관리가 필요해요.",
}

def make_greeting(person):
    intro, role_note = ROLE_LINES[person]
    chosen_tech = "、".join(techs) if techs else "아직 추가된 미래 기술이 없어요"
    if person == "학생":
        detail = "교실에서 햇빛과 환기가 어떤지 가장 궁금해."
    elif person == "교사":
        detail = "학생들이 집중하고 쉬기 좋은 공간인지 살펴보고 있어요."
    elif person == "환자":
        detail = "병원에서 오래 머물러도 편안한 환경인지가 중요해요."
    elif person == "의사":
        detail = "환자에게 쾌적하면서도 의료 장비 운영에 안정적인 공간이 필요합니다."
    elif person == "연구원":
        detail = "연구 장비가 안정적으로 작동하고 집중할 수 있는 환경인지 궁금해요."
    elif person == "시설 관리자":
        detail = "유지관리 비용과 설비의 안정성을 함께 살펴보고 있어요."
    elif person == "건물 관리인":
        detail = "건물 운영비와 고장 없이 관리할 수 있는지가 중요합니다."
    else:
        detail = "실제로 생활하기 편하고 유지비도 부담스럽지 않은지 궁금해요."
    return (f"{intro} {role_note}\n\n"
            f"우리 건물은 **{shape}** 형태이고, **{material}**를 사용했어요. "
            f"추가 기술은 **{chosen_tech}**예요. 총비용은 **{total_cost}억원**, 남은 예산은 **{remaining}억원**이고, "
            f"게임 오염지수는 **{pollution}점**이에요.\n\n{detail} 설계에 관해 궁금한 걸 물어봐!")

def reply_to(message, person):
    msg = message.lower()
    tech_names = ", ".join(techs) if techs else "미래 기술을 아직 선택하지 않았어요"
    base = f"현재 설계는 {usage} / {shape} / {material}이고, 기술은 {tech_names}예요."
    if any(k in msg for k in ["가격", "비용", "예산", "돈", "비싸", "얼마"]):
        if remaining < 0:
            return f"지금 설계 비용은 {total_cost}억원이라 예산을 {-remaining}억원 초과했어요. 가장 비싼 항목은 선택한 기술 중 비용이 큰 것일 수 있어요. 기술을 하나씩 바꾸거나 자재를 조정해 봐요. {base}"
        return f"현재 총비용은 {total_cost}억원이고 {remaining}억원이 남았어요. 용도 {usage_data['cost']}억원, 형태 {shape_data['cost']}억원, 자재 {material_data['cost']}억원, 기술 {tech_cost}억원으로 계산돼요. 비용이 큰 선택을 하나 줄이면 다른 기술을 넣을 여유가 생겨요."
    if any(k in msg for k in ["오염", "환경", "탄소", "친환경", "지수"]):
        return f"게임 오염지수는 {pollution}/100이에요. 용도와 형태, 자재의 영향에 더해 선택한 미래 기술의 감축 효과를 반영했어요. {material_observations[material]} 현재 선택한 기술은 {tech_names}예요. 실제 건물의 환경 성능은 운영 방식과 지역 조건에 따라 달라질 수 있어요."
    if any(k in msg for k in ["형태", "돔", "테라스", "타워", "모양", "건물 모양"]):
        return f"나는 지금 건물의 형태가 **{shape}**라는 점이 눈에 띄어요. {shape_observations.get(shape, '')} 모든 면에서 보이는 외관뿐 아니라 이동 동선과 관리 공간도 함께 생각하면 더 좋아요."
    if any(k in msg for k in ["자재", "재료", "콘크리트", "철강", "목재", "재활용", "나무"]):
        return f"우리 건물은 **{material}**를 사용했어요. {material_observations.get(material, '')} 자재 선택 비용은 {material_data['cost']}억원이고, 다른 설비와 함께 예산 안에서 균형을 맞춰야 해요."
    if any(k in msg for k in ["기술", "태양광", "환기", "차양", "녹화", "빗물", "물 재이용", "물"]):
        if techs:
            details = " ".join(tech_observations[t] for t in techs if t in tech_observations)
            return f"현재 적용된 기술은 {tech_names}예요. {details} 기술 비용은 총 {tech_cost}억원이에요."
        return "아직 추가된 미래 기술이 없어요. 자연환기나 외부 차양처럼 비교적 저렴한 기술부터 고려하거나, 태양광·녹화 지붕처럼 비용이 큰 기술의 효과와 가격을 비교해 봐요."
    if any(k in msg for k in ["시끄", "소음", "조용", "소리"]):
        return f"{person} 입장에서 소음은 중요한 문제예요. {shape}의 형태만으로 소음이 해결되지는 않으니, 창호 성능과 실내 배치, 조용한 휴식 공간을 함께 설계해야 해요. 현재 자재는 {material}예요."
    if any(k in msg for k in ["덥", "더위", "햇빛", "시원", "온도", "열"]):
        shade = "외부 차양이 햇빛을 줄이는 데 도움을 줘요." if "🪟 외부 차양" in techs else "외부 차양을 추가하면 강한 햇빛이 실내로 들어오는 것을 줄이는 데 도움이 될 수 있어요."
        green = " 녹화 지붕도 선택되어 옥상 열환경에 도움을 줄 수 있어요." if "🌱 녹화 지붕" in techs else ""
        return f"실내 온도를 편안하게 유지하는 게 중요하죠. {shade}{green} 현재 기술 조합은 {tech_names}예요."
    if any(k in msg for k in ["물", "빗물", "수도", "물값"]):
        water = [t for t in techs if t in ["💧 빗물 이용", "🔄 물 재이용"]]
        return f"물 관리 기술로 선택된 것은 {', '.join(water) if water else '없음'}이에요. 빗물 이용은 모아 둔 물을 조경 등에 쓰고, 물 재이용은 처리한 물을 다시 쓰는 방식이에요. 둘 다 선택하지 않았다면 다음 설계에서 고려할 수 있어요."
    if any(k in msg for k in ["좋아", "만족", "마음", "어때", "어떻게 생각", "평가"]):
        return f"내가 사는 입장에서 보면 {shape} 형태와 {material} 자재의 조합이 특징적이에요. {shape_observations.get(shape, '')} 기술은 {tech_names}이고 비용은 {total_cost}억원이에요. 남은 예산 {remaining}억원을 유지하면서 생활 편의도 챙기는 게 중요해요."
    if any(k in msg for k in ["안녕", "반가", "이름"]):
        return f"반가워요! 저는 이 {usage_data['place']}의 {person}입니다. 지금 건물은 {shape}, 자재는 {material}, 기술은 {tech_names}예요. 어떤 점이 궁금하세요?"
    return (f"그 질문도 건물에서 생활할 때 중요한 부분이에요. {base} "
            f"{shape_observations.get(shape, '')} {material_observations.get(material, '')} "
            f"비용은 {total_cost}억원이고 {remaining}억원이 남아 있어요. 어떤 선택을 더 자세히 알아보고 싶다면 형태, 자재, 기술, 비용 중 하나를 물어봐 줘!")

# Keep selected character valid for this building type.
if character not in people:
    character = people[0]
    st.session_state["resident_character_select"] = character

history = st.session_state.setdefault("resident_chat_history", [])
if not history:
    greeting = make_greeting(character)
    history.append({"role": "assistant", "content": greeting, "character": character})

for item in history:
    with st.chat_message(item["role"], avatar="💬" if item["role"] == "assistant" else "🧑"):
        if item["role"] == "assistant":
            st.caption(item.get("character", character))
        st.markdown(item["content"])

prompt = st.chat_input(f"{character}에게 물어보기…")
if prompt:
    history.append({"role": "user", "content": prompt})
    answer = reply_to(prompt, character)
    history.append({"role": "assistant", "content": answer, "character": character})
    st.rerun()

st.markdown("### 💡 대화 시작 예시")
examples = ["이 건물의 장점은 뭐야?", "왜 이 자재를 선택했어?", "예산을 얼마나 썼어?", "실내가 더워지지는 않을까?", "선택한 기술은 환경에 어떤 도움이 돼?"]
cols = st.columns(len(examples))
for i, example in enumerate(examples):
    with cols[i]:
        if st.button(example, key=f"example_{i}", use_container_width=True):
            st.session_state["resident_chat_history"].append({"role": "user", "content": example})
            st.session_state["resident_chat_history"].append({"role": "assistant", "content": reply_to(example, character), "character": character})
            st.rerun()
