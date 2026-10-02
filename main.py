    cost = design_cost()
    remain = remaining_budget()
    st.markdown("### 💰 설계 예산")
    st.progress(max(0, min(1, remain / st.session_state.budget)) if st.session_state.budget else 0)
    budget_color = "#8ef0c5" if remain >= 0 else "#ff7d7d"
    st.markdown(f"<div style='font:800 26px Orbitron;color:{budget_color};'>{budget_text(remain)}<span style='font-size:12px;color:#aebfbc;'> / {st.session_state.budget:,}억원</span></div>", unsafe_allow_html=True)
    st.caption(f"사용 금액 {cost:,}억 · 자재와 미래 기술에 따라 비용이 달라집니다.")
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
    st.markdown(effect_card(choice,data["impact"],data["effect"],data["limit"], data.get("cost")), unsafe_allow_html=True)
    st.markdown("""<div class='expert-box'><div class='expert-kicker'>ARCHITECTURE NOTE</div><h3>건축물의 용도는 필요한 환경을 결정해요.</h3><p>같은 크기의 건물이라도 주거시설, 학교, 병원처럼 <b>무엇을 하는 공간인지</b>에 따라 필요한 빛, 온도, 공기, 물, 전력의 조건이 달라집니다.</p><p><b>쉽게 말하면</b> 건축가는 먼저 건물에서 어떤 활동이 일어나는지 정한 뒤, 그 활동에 맞춰 공간과 설비를 계획합니다. 이 게임의 점수는 이런 차이를 이해하기 위한 가상 값입니다.</p></div>""", unsafe_allow_html=True)
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
    st.markdown(effect_card(choice,data["impact"],data["effect"],data["limit"], data.get("cost")), unsafe_allow_html=True)
    if st.button("다음 → 건축 자재", type="primary", use_container_width=True): st.session_state.page="MATERIAL"; st.rerun()

# =========================================================
# MATERIAL
# =========================================================
elif st.session_state.page == "MATERIAL":
    st.markdown("<div class='hero-title' style='font-size:42px;'>03 / MATERIAL</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>THE MATERIAL CHANGES THE BUILDING.</div>", unsafe_allow_html=True)
    current_material = st.session_state.material
    choice=st.radio("건축 자재를 선택하세요.", list(MATERIALS), index=list(MATERIALS).index(current_material), format_func=lambda x: f"{x}  ·  {MATERIALS[x]['cost']}억원")
    candidate_total = MATERIALS[choice]["cost"] + sum(TECHNOLOGIES[t]["cost"] for t in st.session_state.technologies)
    if candidate_total <= st.session_state.budget:
        st.session_state.material=choice
    else:
        st.warning(f"💸 {choice}는 현재 선택한 미래 기술과 함께 사용하면 {candidate_total - st.session_state.budget}억원이 부족합니다. 예산 안의 조합을 위해 기존 자재를 유지합니다.")
        st.session_state.material=current_material
        choice=current_material
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
    st.markdown("<div class='card'><b>💰 초기 설계 예산 100억원</b><br><span class='small-note'>오염지수 감축 효과가 큰 미래 기술은 더 비싸게 설정되어 있습니다. 예산이 부족하면 해당 기술을 추가할 수 없습니다.</span></div>", unsafe_allow_html=True)
    material_cost = MATERIALS[st.session_state.material]["cost"]
    selected=[]
    running_cost = material_cost
    for tech, data in TECHNOLOGIES.items():
        was_selected = tech in st.session_state.technologies
        can_afford = was_selected or (running_cost + data["cost"] <= st.session_state.budget)
        checked = st.checkbox(
            f"{tech}  ·  {data['cost']}억원  ·  오염지수 {data['impact']:+d}",
            value=was_selected,
            disabled=not can_afford,
            key=f"tech_{tech}"
        )
        if checked:
            selected.append(tech)
            running_cost += data["cost"]
    st.session_state.technologies=selected
    tech_cost = sum(TECHNOLOGIES[t]["cost"] for t in selected)
    total_cost = material_cost + tech_cost
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
