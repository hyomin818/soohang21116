        experience += MATERIALS.get(material, "")
        return opening + "\n\n" + experience + tech_sentence + " 살면서 좋은 점도 있고 아쉬운 점도 있어요. 궁금한 거 편하게 물어봐요!"
    if person == "학생":
        return random.choice([
            "안녕! 나 여기 다니는 학생이야. 교실에서 오래 있어도 덜 답답한지가 은근 중요하거든. 쉬는 시간에 어디가 제일 편한지도 말해줄게!",
            "안녕하세요는 좀 어색하니까 그냥 편하게 말할게! 여기 학교 다니면서 느낀 점은 햇빛이랑 쉬는 공간이 진짜 중요하다는 거야."
        ])
    if person == "교사":
        return "안녕하세요. 이 학교에서 학생들을 가르치고 있어요. 수업할 때 학생들이 집중하기 좋은지, 쉬는 시간에 편히 머물 곳이 있는지 실제로 느낀 점을 이야기해 드릴게요."
    if person == "환자":
        return "안녕하세요. 여기 진료받으러 왔다가 머무는 시간이 길어졌어요. 아픈 날에는 작은 소음이나 눈부심도 크게 느껴지더라고요. 환자 입장에서 느낀 점을 편하게 물어보세요."
    if person == "의사":
        return "안녕하세요. 이 병원에서 일하는 의사입니다. 환자들이 기다리는 동안 얼마나 편안한지, 직원들이 이동하기에 괜찮은지 현장에서 느끼는 점을 말씀드릴게요."
    if person == "연구원":
        return "안녕하세요! 이 연구센터에서 일하고 있어요. 하루 종일 집중해야 해서 빛이나 온도, 쉬는 공간 같은 게 생각보다 중요해요. 실제로 써본 느낌을 이야기해 볼게요."
    if person == "건물 관리인":
        return f"안녕하세요. 이 건물의 관리인입니다. 현재 설계 비용은 {total_cost}억원이고 남은 예산은 {remaining}억원입니다. 선택된 기술은 {', '.join(techs) if techs else '없음'}입니다. 설비 점검, 유지관리, 운영비 측면에서 질문해 주시면 답변하겠습니다."
    return "안녕하세요! 여기서 지내며 느낀 점을 솔직하게 이야기해 볼게요."

def resident_reply(message, person):
    m = message.lower()
    # Management persona is deliberately more factual and technical.
    if person == "건물 관리인":
        if any(k in m for k in ["비용", "가격", "예산", "돈", "얼마"]):
            tech_detail = ", ".join(f"{t} {COSTS.get(t,0)}억원" for t in techs) if techs else "미래 기술 선택 없음"
            return f"현재 계산된 총비용은 {total_cost}억원이며 잔여 예산은 {remaining}억원입니다. 용도 {COSTS.get(usage,10)}억원, 형태 {COSTS.get(shape,18)}억원, 자재 {COSTS.get(material,12)}억원, 기술 {tech_cost}억원입니다. 기술별 비용은 {tech_detail}입니다."
        if any(k in m for k in ["기술", "설비", "관리", "유지", "고장", "운영"]):
            details = " ".join(TECHS[t] for t in techs if t in TECHS) or "현재 선택된 미래 기술은 없습니다. 설비가 적을수록 관리 항목은 단순해질 수 있지만, 에너지·물 절감 효과도 함께 검토해야 합니다."
            return f"관리 관점에서는 점검 접근성과 교체 주기가 중요합니다. {details} 기술 선택 비용은 총 {tech_cost}억원입니다."
        if any(k in m for k in ["오염", "탄소", "환경", "지수"]):
            return f"게임상 오염지수는 {pollution}/100입니다. 이는 시뮬레이션용 점수이며 실제 건물 성능 인증값은 아닙니다. 실제 성능은 자재 생산 자료, 설비 효율, 사용량과 유지관리 상태를 함께 확인해야 합니다."
        return f"관리 측면에서 현재 형태는 {shape}, 자재는 {material}입니다. 운영 중에는 점검 공간과 부품 교체 접근성이 중요합니다. 총비용은 {total_cost}억원, 남은 예산은 {remaining}억원입니다. 어떤 설비나 운영 항목이 궁금하신가요?"

    # Ordinary users talk about what they experience, not material specifications.
    if any(k in m for k in ["좋은 점", "장점", "만족", "후기", "마음에", "좋아", "어때", "평가"]):
        if person == "주민":
            return f"제일 마음에 드는 건 {('공간이 높고 시야가 트인 점' if '타워' in shape else '테라스에서 바깥 공기를 쐴 수 있는 점' if '테라스' in shape else '천장이 높고 독특한 분위기' if '돔' in shape else '바깥 공간과 가깝고 이동이 편한 점')}이에요. "
        if person == "학생":
            return "쉬는 시간에 잠깐 앉아 있을 곳이 있고 교실이 너무 답답하지 않으면 그게 제일 좋아. 친구들이랑 얘기할 공간이 있다는 것도 꽤 커!"
        if person == "교사":
            return "학생들이 수업 외 시간에도 편하게 머물 수 있다는 점이 좋아요. 교실 밖에 잠깐 쉬거나 이야기할 공간이 있으면 수업 분위기에도 도움이 되더라고요."
        if person == "환자":
            return "기다리는 동안 눈이 부시거나 주변이 시끄럽지 않은 게 가장 좋아요. 아플 때는 아주 사소한 불편도 크게 느껴지거든요."
        if person == "의사":
            return "환자들이 기다리는 동안 덜 불안하고, 직원들이 환자 곁으로 이동하기 편한 점이 중요해요. 실제 만족도는 공간이 편안한지에서 많이 갈려요."
        if person == "연구원":
            return "집중할 수 있는 조용한 자리와 잠깐 머리를 식힐 공간이 있는 게 제일 좋아요. 하루 종일 일하면 그런 차이가 꽤 크게 느껴져요."
    if any(k in m for k in ["불편", "아쉬", "단점", "문제", "싫", "고쳐", "개선"]):
        if "타워" in shape:
            return "솔직히 높은 층에서 엘리베이터를 기다릴 때는 좀 답답해요. 출근이나 등교 시간이 겹치면 더 그렇고요."
        if "테라스" in shape:
            return "테라스는 좋지만 비 온 뒤 바닥이 미끄럽거나, 바람이 세면 오래 있기 어려워요. 그늘과 배수도 잘 되어 있으면 좋겠어요."
        if "돔" in shape:
            return "돔은 멋있는데 햇빛이 들어오는 각도에 따라 눈부실 수 있을 것 같아요. 벽 쪽에 가구를 놓기 애매한 곳도 있고요."
        return "전반적으로 괜찮아도 사람마다 필요한 게 다르더라고요. 조용히 쉴 곳이 부족하거나 이동 동선이 길면 조금 아쉬울 것 같아요."
    if any(k in m for k in ["덥", "더위", "시원", "햇빛", "눈부", "온도", "추워"]):
        if "🪟 외부 차양" in techs:
            return "햇빛이 강한 시간에도 예전만큼 눈이 부시진 않아요. 물론 계절이나 창문 방향에 따라 차이는 있겠지만, 낮에 머물기는 한결 편해요."
        if "🌱 녹화 지붕" in techs:
            return "옥상 녹화가 있어서 그런지 주변이 덜 삭막하고, 더운 날에도 위쪽 공간이 조금 덜 뜨겁게 느껴져요. 그래도 실내 온도는 창문과 냉방 상태에 따라 달라요."
        return "한낮에는 햇빛이 강한 공간이 조금 더울 때가 있어요. 그늘이나 차양이 있는 자리로 옮길 수 있으면 훨씬 편할 것 같아요."
    if any(k in m for k in ["공기", "환기", "답답", "냄새", "바람"]):
        if "🌬️ 자연환기" in techs:
            return "날씨가 괜찮을 땐 공기가 잘 바뀌는 느낌이라 좋아요. 다만 바깥 공기가 안 좋은 날에는 무조건 창문을 열 수 없어서 다른 환기 방법도 필요해요."
        return "사람이 많을 때는 조금 답답하게 느껴질 때가 있어요. 창문을 열기 어려운 날에도 공기가 잘 순환되면 훨씬 좋을 것 같아요."
    if any(k in m for k in ["소음", "시끄", "조용", "소리"]):
        return "사람이 몰리는 시간에는 복도나 공용 공간 소리가 들릴 때가 있어요. 잠깐 조용히 쉴 수 있는 곳이 따로 있으면 좋겠어요."
    if any(k in m for k in ["물", "빗물", "수도"]):
        if "💧 빗물 이용" in techs or "🔄 물 재이용" in techs:
            return "물을 아껴 쓰는 설비가 있다는 게 좋아요. 다만 우리가 실제로 쓰는 물과 조경용 물이 어떻게 나뉘는지 안내가 잘 되어 있으면 더 안심될 것 같아요."
        return "물 쓰는 데 큰 불편은 없지만, 조경이나 청소에 빗물을 활용하면 물을 아낄 수 있을 것 같아요."
    if any(k in m for k in ["태양광", "전기", "전기료", "전기 요금"]):
        if "☀️ 태양광 발전" in techs:
            return "지붕에서 전기를 만든다는 점은 마음에 들어요. 실제로 공용 전기료가 얼마나 줄었는지도 주민들에게 알려주면 더 실감 날 것 같아요."
        return "태양광이 있으면 공용 공간 전기 사용에 도움이 될 것 같아요. 다만 설치했다고 요금이 바로 크게 줄었다고 단정하긴 어렵겠죠."
    if any(k in m for k in ["테라스", "돔", "타워", "형태", "모양"]):
        return f"{SHAPES.get(shape, '건물의 형태')} 개인적으로는 도면에서 보는 것보다 직접 걷고 머물 때 어떤 느낌인지가 더 중요하다고 생각해요."
    if any(k in m for k in ["자재", "재료", "콘크리트", "철강", "목재", "재활용"]):
        # Redirect to lived experience rather than lecture on building materials.
        return f"자재의 전문적인 장단점은 설계자인 네가 더 잘 알겠지만, 이용자 입장에선 실내 분위기나 촉감, 소리 울림 같은 게 먼저 느껴져요. {MATERIALS.get(material, '')} 나는 실제로 지냈을 때 편안한지가 제일 궁금해요."
    if any(k in m for k in ["가격", "비용", "예산", "돈", "얼마"]):
        return f"비용 자체는 내가 자세히 알진 못하지만, 건물 이용자로서는 돈을 들인 만큼 생활이 편해졌는지가 궁금해요. 예를 들면 햇빛이 덜 눈부신지, 공기가 덜 답답한지 같은 거요. 지금 남은 예산은 {remaining}억원이라고 들었어요."
    if any(k in m for k in ["오염", "환경", "탄소", "친환경", "지수"]):
        return "환경 점수도 중요하겠지만, 주민 입장에서는 그 변화가 일상에서 느껴지는지가 더 와닿아요. 더위가 덜한지, 물을 아껴 쓰는지, 공용 공간이 쾌적한지 같은 식으로요."
    if any(k in m for k in ["안녕", "반가", "이름"]):
        return random.choice(["안녕! 편하게 물어봐요. 여기 살아보면서 느낀 점을 솔직하게 얘기해 줄게요.", "반가워요! 설계도만 봐서는 알기 어려운 생활 후기를 들려드릴게요."])
    return random.choice([
        "음, 직접 살아보니까 생각보다 작은 부분이 크게 느껴지더라고요. 빛이나 소리, 쉬어 갈 자리 같은 거요. 어떤 상황이 궁금해요?",
        "그건 실제로 지내보면 느낄 수 있는 부분이겠네요. 나는 설계 설명보다는 여기서 하루를 보내는 느낌을 말해줄 수 있어요. 장점이 궁금해요, 불편한 점이 궁금해요?",
        "사람마다 다르겠지만, 이용자 입장에서는 편안함이 제일 중요해요. 구체적으로 어느 부분이 궁금한지 물어봐요!"
    ])

history = st.session_state.setdefault("resident_chat_history", [])
if not history:
    if character == "건물 관리인":
        greeting = initial_message(character)
    else:
        greeting = initial_message(character)
    history.append({"role": "assistant", "content": greeting, "character": character})

# Display conversation
for item in history:
    role = item.get("role", "assistant")
    with st.chat_message(role, avatar=("🧑" if role == "user" else ("🧰" if item.get("character") == "건물 관리인" else "🙂"))):
        if role == "assistant":
            st.caption(item.get("character", character))
        st.markdown(item.get("content", ""))

prompt = st.chat_input(f"{character}에게 생활 후기를 물어보기…")
if prompt:
    history.append({"role": "user", "content": prompt})
    history.append({"role": "assistant", "content": resident_reply(prompt, character), "character": character})
    st.rerun()

st.markdown("### 💡 이런 걸 물어봐도 좋아요")
examples = [
    "여기 살면서 제일 마음에 드는 점은 뭐야?",
    "실제로 불편한 점은 없어?",
    "여름에 많이 덥거나 눈부시진 않아?",
    "공기가 답답하거나 시끄럽진 않아?",
    "하루를 보내면 어떤 느낌이야?",
]
cols = st.columns(len(examples))
for i, example in enumerate(examples):
    with cols[i]:
        if st.button(example, key=f"resident_example_{i}", use_container_width=True):
            st.session_state["resident_chat_history"].append({"role": "user", "content": example})
            st.session_state["resident_chat_history"].append({"role": "assistant", "content": resident_reply(example, character), "character": character})
