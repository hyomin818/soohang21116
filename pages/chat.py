import streamlit as st
import random

st.set_page_config(page_title="2050 주민 대화", page_icon="💬", layout="wide")

# ---------------------------------------------------------
# 설계 정보는 메인 건축 앱의 st.session_state에서 가져옵니다.
# ---------------------------------------------------------
USAGES = {
    "🏠 미래 주거시설": {"people": ["주민", "건물 관리인"], "place": "아파트"},
    "🏫 미래 학교": {"people": ["학생", "교사", "건물 관리인"], "place": "학교"},
    "🏥 미래 병원": {"people": ["환자", "의사", "건물 관리인"], "place": "병원"},
    "🔬 미래 연구센터": {"people": ["연구원", "건물 관리인"], "place": "연구센터"},
}
SHAPES = {
    "🏙️ 수직형 타워": "높은 층까지 오르내려야 해서 엘리베이터와 이동 시간이 생활 만족도에 영향을 줘요.",
    "🌿 테라스형": "층마다 바깥으로 나갈 수 있는 테라스가 있어 날씨 좋은 날 잠깐 쉬거나 식물을 보는 재미가 있어요.",
    "🛸 돔형": "천장이 높고 둥글게 이어져 공간이 탁 트여 보여요. 가운데 공간은 멋지지만 가장자리 공간은 가구를 놓기 애매할 수도 있어요.",
    "🌍 저층 생태형": "층수가 낮아 이동하기 편하고 바깥 공간과 가까워요. 대신 목적지에 따라 걸어야 하는 거리가 길 수 있어요.",
    "🌍 반지하형": "바깥 날씨 영향을 덜 받는 느낌이지만, 자연광과 습도 관리가 잘되는지가 중요해요.",
}
MATERIALS = {
    "🧱 저탄소 콘크리트": "실내에서 크게 튀는 느낌은 없고 묵직하고 안정적인 분위기예요.",
    "🔩 저탄소 철강": "기둥이나 프레임이 드러나는 곳은 조금 더 도시적이고 단단한 인상을 줘요.",
    "🌲 목재·바이오 기반": "나무 느낌이 살아 있는 공간은 차갑지 않고 편안하게 느껴질 수 있어요.",
    "♻️ 재사용·재활용 재료": "재료마다 표면과 색이 조금씩 달라서 공간에 개성이 생길 수 있어요.",
}
TECHS = {
    "☀️ 태양광 발전": "낮에 공용 공간의 전기 사용에 보탬이 될 수 있어요. 주민 입장에서는 전기 요금이나 공용 시설 운영이 얼마나 달라지는지가 궁금해요.",
    "🌬️ 자연환기": "날씨가 좋을 때 창문을 열고 공기를 바꾸기 편할 수 있어요. 바깥 공기가 좋지 않은 날에는 창문을 닫고 지낼 수 있어야 해요.",
    "🪟 외부 차양": "햇빛이 강한 시간에 실내가 덜 눈부시고 덜 후끈하게 느껴질 수 있어요.",
    "🌱 녹화 지붕": "창밖으로 녹지가 보이면 삭막한 느낌이 줄고, 더운 날 옥상 주변의 열기를 줄이는 데도 도움이 될 수 있어요.",
    "💧 빗물 이용": "비가 온 뒤 조경에 물을 주는 데 빗물을 활용할 수 있어요. 생활용수로 쓰이는지는 설비 방식에 따라 달라요.",
    "🔄 물 재이용": "조경이나 청소 등에 쓸 물을 아끼는 데 도움이 될 수 있어요. 설비가 잘 관리되는지도 중요해요.",
}
COSTS = {
    "🏠 미래 주거시설": 10, "🏫 미래 학교": 8, "🏥 미래 병원": 16, "🔬 미래 연구센터": 12,
    "🏙️ 수직형 타워": 18, "🌿 테라스형 건축": 15, "🛸 돔형 건축": 22, "🌍 저층 생태형": 12, "🌍 반지하형 건축": 12,
    "🧱 저탄소 콘크리트": 12, "🔩 저탄소 철강": 18, "🌲 목재·바이오 기반": 24, "♻️ 재사용·재활용 재료": 20,
    "☀️ 태양광 발전": 30, "🌬️ 자연환기": 15, "🪟 외부 차양": 10, "🌱 녹화 지붕": 18, "💧 빗물 이용": 7, "🔄 물 재이용": 15,
}
COLOR_NAMES = {
    "#5D7F7A": "미래형 민트", "#A77D5C": "사막 모래", "#C9D4D0": "화이트",
    "#345C78": "딥 블루", "#46634E": "포레스트", "#A76543": "오렌지",
}

# ---------------------------------------------------------
# 화면 스타일: 밝은 글씨가 밝은 배경에 묻히지 않도록 대비 강화
# ---------------------------------------------------------
st.markdown("""
<style>
.stApp {
  background: radial-gradient(circle at 82% 0%, #183033 0%, #0a1416 42%, #071012 100%);
  color: #f5fbff;
}
.block-container {max-width: 1180px; padding-top: 1.8rem; padding-bottom: 2.5rem;}
h1,h2,h3,h4,p,li,label,small,.stMarkdown,.stCaption,
[data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
  color: #f5fbff !important;
}
.stCaption,[data-testid="stCaptionContainer"] {color:#b9cbd0 !important;}
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg,#111e22 0%,#17262b 100%);
  border-right: 1px solid #385057;
}
section[data-testid="stSidebar"] * {color:#f4f8fa !important;}
div[data-testid="stChatMessage"] {
  background: #142326 !important;
  border: 1px solid #345056 !important;
  border-radius: 17px !important;
  padding: 1rem 1.15rem !important;
}
div[data-testid="stChatMessage"] p,
div[data-testid="stChatMessage"] li {color:#f7fbff !important; font-size:16px; line-height:1.75;}
div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {color:#f7fbff !important;}
[data-testid="stChatInput"] textarea {
  color:#102024 !important; background:#f5f8f9 !important; caret-color:#102024 !important;
}
[data-testid="stChatInput"] textarea::placeholder {color:#53656a !important;}
[data-testid="stTextInput"] input, [data-testid="stSelectbox"] div,
[data-baseweb="select"] * {color:#142326 !important;}
[data-testid="stSelectbox"] label {color:#f4f8fa !important;}
.stButton button {
  background:#f3f7f8 !important; color:#142326 !important;
  border:1px solid #c1d0d4 !important; border-radius:11px !important;
  font-weight:650 !important; min-height:42px;
}
.stButton button:hover {background:#d9ecec !important; border-color:#8db8b9 !important;}
div[data-testid="stAlert"] p {color:#f7fbff !important;}
hr {border-color:#3b5157 !important;}
.design-card {
  background:linear-gradient(135deg,rgba(24,43,47,.96),rgba(13,26,29,.96));
  border:1px solid #36535a; border-radius:18px; padding:18px 20px; margin:10px 0;
}
.kicker {color:#8dd8cc !important; font-size:12px; font-weight:800; letter-spacing:1.5px;}
.big-stat {font-size:25px; font-weight:800; color:#ffffff !important;}
