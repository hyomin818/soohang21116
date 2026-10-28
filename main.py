import random
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="2050 건축 프로젝트", page_icon="🏙️", layout="wide")

# --------------------------- 게임 데이터 ---------------------------
USAGES = {
    "🏠 미래 주거시설": {"cost": 8, "impact": 3, "desc": "사람들이 생활하는 공간입니다. 에너지 사용과 실내 쾌적성을 함께 고려합니다.", "advantages": ["생활에 필요한 공간을 제공", "환기와 채광 계획으로 쾌적성 향상"]},
    "🏫 미래 학교": {"cost": 10, "impact": 4, "desc": "학생과 교직원이 이용하는 교육 공간입니다. 채광과 공기 질이 중요합니다.", "advantages": ["학습 공간과 휴식 공간 제공", "자연채광과 환기를 고려한 교육 환경"]},
    "🏥 미래 병원": {"cost": 13, "impact": 5, "desc": "환자와 의료진이 이용하는 공간입니다. 안정적인 실내 환경이 중요합니다.", "advantages": ["환자와 의료진을 위한 공간", "쾌적한 실내 환경을 우선 고려"]},
    "🔬 미래 연구센터": {"cost": 12, "impact": 4, "desc": "연구와 실험을 수행하는 공간입니다. 안정적인 에너지 공급과 관리가 필요합니다.", "advantages": ["연구·실험을 위한 전문 공간", "에너지 관리 기술을 적용하기 좋음"]},
    "🌿 친환경 복합시설": {"cost": 11, "impact": 2, "desc": "여러 활동이 한 건물에서 이루어지는 복합 공간입니다.", "advantages": ["다양한 활동을 한곳에서 해결", "녹지와 공용 공간을 결합하기 좋음"]},
}
SHAPES = {
    "▰ 직육면체형": {"cost": 7, "impact": 3, "desc": "공간을 효율적으로 나누기 쉽고 구조 계획이 단순한 형태입니다."},
    "◠ 돔형": {"cost": 12, "impact": 1, "desc": "곡면 지붕을 활용하는 형태입니다. 내부 공간을 넓게 구성할 수 있습니다."},
    "▤ 테라스형": {"cost": 11, "impact": 0, "desc": "층마다 테라스를 두어 외부 공간과 녹지를 활용할 수 있습니다."},
    "▥ 타워형": {"cost": 10, "impact": 4, "desc": "수직으로 공간을 쌓아 제한된 땅을 효율적으로 활용하는 형태입니다."},
}
MATERIALS = {
    "일반 콘크리트": {"cost": 5, "impact": 2, "desc": "기본 구조에 사용하기 쉽지만 생산 과정의 환경 부담이 큰 편입니다."},
    "저탄소 콘크리트": {"cost": 9, "impact": -10, "desc": "시멘트 생산 등에서 발생하는 탄소 부담을 줄이는 방향의 자재입니다."},
    "저탄소 철강": {"cost": 12, "impact": -14, "desc": "철강 생산 단계의 환경 부담을 낮추는 선택입니다."},
    "목재·바이오 기반 자재": {"cost": 15, "impact": -20, "desc": "목재와 바이오 기반 재료를 활용해 재료 생산 단계의 부담을 줄입니다."},
    "재사용·재활용 자재": {"cost": 17, "impact": -24, "desc": "기존 자원을 다시 사용해 새 재료 생산과 폐기 부담을 줄입니다."},
}
TECHNOLOGIES = {
    "태양광 발전": {"cost": 17, "impact": -24, "desc": "건물에서 전기를 생산해 외부 전력 사용을 줄입니다."},
    "고효율 단열": {"cost": 12, "impact": -18, "desc": "열이 빠져나가거나 들어오는 것을 줄여 냉난방 에너지를 절약합니다."},
    "자연환기 설계": {"cost": 8, "impact": -13, "desc": "바람과 개구부를 활용해 기계식 환기·냉방 의존도를 낮춥니다."},
    "외부 차양": {"cost": 7, "impact": -10, "desc": "강한 햇빛의 실내 유입을 조절해 냉방 부담을 줄입니다."},
    "녹화 지붕·벽면": {"cost": 13, "impact": -17, "desc": "식생으로 열환경과 빗물 관리에 도움을 줍니다."},
    "빗물 저장·이용": {"cost": 6, "impact": -7, "desc": "빗물을 모아 조경 등에 활용해 수돗물 사용을 줄입니다."},
    "물 재이용 설비": {"cost": 9, "impact": -10, "desc": "사용한 물을 처리해 다시 활용합니다."},
}
COLORS = {"사막 모래색": "#d9b887", "청록색": "#38b7a4", "은회색": "#b9c4cf", "흰색": "#f1f3f5", "짙은 남색": "#344b68", "테라코타": "#bc6c4b"}

# --------------------------- 세션 상태 ---------------------------
def init_state():
    defaults = {
        "page": "메인 화면", "commissioned": False, "completed": False,
        "usage": None, "shape": None, "material": "일반 콘크리트", "technologies": [],
        "color": "사막 모래색", "base_budget": 100, "show_result": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

def accept_commission():
    st.session_state.usage = random.choice(list(USAGES.keys()))
    st.session_state.shape = random.choice(list(SHAPES.keys()))
    st.session_state.material = "일반 콘크리트"
    st.session_state.technologies = []
    st.session_state.color = "사막 모래색"
    st.session_state.commissioned = True
    st.session_state.completed = False
    st.session_state.page = "메인 화면"

def design_cost():
    if not st.session_state.commissioned:
        return 0
    return (USAGES[st.session_state.usage]["cost"] + SHAPES[st.session_state.shape]["cost"] +
            MATERIALS[st.session_state.material]["cost"] +
            sum(TECHNOLOGIES[t]["cost"] for t in st.session_state.technologies))

def remaining_budget():
    return st.session_state.base_budget - design_cost()

def pollution_score():
    if not st.session_state.commissioned:
        return 100
    impact = (USAGES[st.session_state.usage]["impact"] + SHAPES[st.session_state.shape]["impact"] +
              MATERIALS[st.session_state.material]["impact"] +
              sum(TECHNOLOGIES[t]["impact"] for t in st.session_state.technologies))
    return max(0, min(100, 100 + impact))

def pollution_label(impact):
    if impact < 0:
        return f"🟢 오염지수 {abs(impact)} 감축"
    if impact > 0:
        return f"🔴 오염지수 {impact} 증가"
    return "⚪ 오염지수 변화 없음"

def success_check():
    # 의뢰 용도·형태는 랜덤 지정 후 잠겨 있으므로 조건 일치 여부를 유지합니다.
    # 오염지수 88 이하 + 예산 이내면 성공. 강한 기술 없이도 다양한 조합을 허용합니다.
    return st.session_state.commissioned and pollution_score() <= 88 and remaining_budget() >= 0

def impact_sum():
    return (USAGES[st.session_state.usage]["impact"] + SHAPES[st.session_state.shape]["impact"] +
            MATERIALS[st.session_state.material]["impact"] +
            sum(TECHNOLOGIES[t]["impact"] for t in st.session_state.technologies))

# --------------------------- 3D 미리보기 ---------------------------
def building_figure():
    """큰 불투명 건물과 황폐해졌지만 지구의 흔적이 남아 있는 3D 풍경."""
    import math
    color = COLORS[st.session_state.color]
    fig = go.Figure()

    # 굴곡 있는 황토색 지면
    gx = [i * 1.25 - 20 for i in range(33)]
    gy = [i * 1.25 - 20 for i in range(33)]
    gz = []
    ground_colors = []
    for y in gy:
        row, crow = [], []
        for x in gx:
            h = 0.16 * math.sin(x * 0.25) + 0.13 * math.cos(y * 0.22) + 0.07 * math.sin((x+y) * 0.31)
            row.append(max(0, h))
            crow.append((math.sin(x*.18) + math.cos(y*.19)) * 0.5)
        gz.append(row)
        ground_colors.append(crow)
    fig.add_trace(go.Surface(x=gx, y=gy, z=gz, surfacecolor=ground_colors,
        colorscale=[[0, "#665b49"], [0.22, "#887354"], [0.48, "#b39a70"], [0.72, "#c8ad7d"], [1, "#8d8a67"]],
        cmin=-1, cmax=1, showscale=False, opacity=1, hoverinfo="skip",
        lighting=dict(ambient=0.88, diffuse=0.4, roughness=1)))

    # 먼 곳의 낮은 산맥: 빈 사막이 아니라 실제 지형처럼 보이도록 함
    for i in range(13):
        x = -23 + i * 3.9
        y = 15.5 + (i % 3) * 0.7
        w = 2.8 + (i % 4) * 0.45
        h = 2.0 + (i % 5) * 0.65
        fig.add_trace(go.Mesh3d(
            x=[x-w, x, x+w, x-w, x+w], y=[y, y+0.4, y, y, y],
            z=[0.1, h, 0.1, 0.1, 0.1], i=[0,0,1], j=[1,2,2], k=[3,4,4],
            color=["#8c8268", "#a59a7b", "#716d5b"], opacity=1,
            flatshading=True, showlegend=False, hoverinfo="skip"))

    # 먼 곳의 건물 잔해와 작은 미래 도시 실루엣
    for i in range(11):
        x = -19 + i * 3.8
        y = 11.7 + (i % 3) * 0.8
        w = 0.75 + (i % 3) * 0.25
        h = 1.7 + (i % 4) * 0.65
        ztop = h
        vx=[x-w,x+w,x+w,x-w,x-w,x+w,x+w,x-w]
        vy=[y-0.6,y-0.6,y+0.6,y+0.6,y-0.6,y-0.6,y+0.6,y+0.6]
        vz=[0,0,0,0,ztop,ztop,ztop,ztop]
        faces=[(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7),(4,5,6),(4,6,7)]
        ii,jj,kk=zip(*faces)
        fig.add_trace(go.Mesh3d(x=vx,y=vy,z=vz,i=ii,j=jj,k=kk,color="#777565" if i%2 else "#89816b",
            opacity=1,flatshading=True,showlegend=False,hoverinfo="skip"))
        # 잔해 창문은 어두운 홈처럼 표현
        if i % 2 == 0:
            fig.add_trace(go.Scatter3d(x=[x-0.25,x+0.25,x-0.25,x+0.25],y=[y-0.615]*4,
                z=[0.6,0.6,1.25,1.25],mode="markers",marker=dict(size=3,color="#414b4a"),
                showlegend=False,hoverinfo="skip"))

    # 길과 갈라진 지면 흔적
    fig.add_trace(go.Scatter3d(x=[-18,-12,-7,0,7,13,19], y=[-12,-9,-7,-6,-7,-9,-12], z=[0.16]*7,
        mode="lines", line=dict(color="#625e52", width=18), showlegend=False, hoverinfo="skip"))
    fig.add_trace(go.Scatter3d(x=[-18,-12,-7,0,7,13,19], y=[-12,-9,-7,-6,-7,-9,-12], z=[0.19]*7,
        mode="lines", line=dict(color="#c0a77b", width=2, dash="dash"), showlegend=False, hoverinfo="skip"))

    # 듬성듬성 남은 나무와 관목: 중심 건물 주변은 비워 둠
    for i in range(15):
        x = -17 + (i * 11 % 35)
        y = -13 + (i * 7 % 25)
        if abs(x) < 5.7 and abs(y) < 5.7:
            continue
        trunk_h = 0.65 + (i % 3) * 0.18
        crown_h = 1.0 + (i % 4) * 0.22
        r = 0.12 + (i % 2) * 0.06
        fig.add_trace(go.Scatter3d(x=[x,x], y=[y,y], z=[0.12,trunk_h], mode="lines",
            line=dict(color="#51463a",width=5),showlegend=False,hoverinfo="skip"))
        # 여러 층의 각진 수관으로 나무 형태 표현
        for layer in range(3):
            rr = (0.65 - layer*0.14) * (0.8 + (i%3)*0.1)
            z0 = trunk_h + layer*crown_h*0.27
            fig.add_trace(go.Mesh3d(x=[x-rr,x+rr,x,x], y=[y-rr,y-rr,y+rr,y],
                z=[z0,z0,z0,z0+crown_h*0.48], i=[0,0],j=[1,2],k=[2,3],
                color="#777a5b" if i%3 else "#68745a", opacity=1,showlegend=False,hoverinfo="skip"))

    # 건축물 크기: 카메라에 더 꽉 차도록 키우고 중심을 고정
    shape = st.session_state.shape if st.session_state.commissioned else "▰ 직육면체형"
    height = 13.8 if shape == "▥ 타워형" else 10.2
    half = 4.5 if shape == "◠ 돔형" else 4.25
    if shape == "▤ 테라스형":
        height = 10.5

    # 본체는 완전 불투명한 외벽. 돔형은 원형 평면, 나머지는 닫힌 다면체로 만듦
    if shape == "◠ 돔형":
        theta_body = [2*math.pi*i/48 for i in range(49)]
        bx = [half*math.cos(t) for t in theta_body]
        by = [half*math.sin(t) for t in theta_body]
        fig.add_trace(go.Surface(x=[bx,bx], y=[by,by], z=[[0]*49,[height]*49],
            colorscale=[[0,color],[1,color]], showscale=False, opacity=1, hoverinfo="skip",
            lighting=dict(ambient=0.78,diffuse=0.48,specular=0.08,roughness=0.95)))
        fig.add_trace(go.Mesh3d(x=bx+[0], y=by+[0], z=[0]*49+[0],
            i=list(range(1,48)), j=list(range(2,49)), k=[49]*47, color=color, opacity=1,
            flatshading=True,showlegend=False,hoverinfo="skip"))
    else:
        verts = [(-half,-half,0),(half,-half,0),(half,half,0),(-half,half,0),
                 (-half,-half,height),(half,-half,height),(half,half,height),(-half,half,height)]
        faces = [(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),(3,0,4),(3,4,7),(4,5,6),(4,6,7),(0,3,2),(0,2,1)]
        ii,jj,kk=zip(*faces)
        fig.add_trace(go.Mesh3d(x=[v[0] for v in verts],y=[v[1] for v in verts],z=[v[2] for v in verts],
            i=ii,j=jj,k=kk,color=color,opacity=1,flatshading=True,
            lighting=dict(ambient=0.78,diffuse=0.48,specular=0.08,roughness=0.95),
            name="불투명 외벽",showlegend=False,hoverinfo="skip"))

    # 돔형은 원형 벽체와 반구 지붕으로 구성해 어느 각도에서도 둥근 형태가 보임
    if shape == "◠ 돔형":
        # 네모 본체 대신 원통형 하부 외벽을 추가해 둥근 평면을 보강
        theta_vals=[2*math.pi*i/48 for i in range(49)]
        cx=[half*math.cos(t) for t in theta_vals]
        cy=[half*math.sin(t) for t in theta_vals]
        for j in range(18):
            z0=height*j/18
            z1=height*(j+1)/18
            fig.add_trace(go.Surface(x=[[half*math.cos(t) for t in theta_vals],[half*math.cos(t) for t in theta_vals]],
                y=[[half*math.sin(t) for t in theta_vals],[half*math.sin(t) for t in theta_vals]],z=[[z0]*49,[z1]*49],
                colorscale=[[0,color],[1,color]],showscale=False,opacity=1,hoverinfo="skip",lighting=dict(ambient=0.8,diffuse=0.4)))
        xs,ys,zs=[],[],[]
        for a in range(17):
            theta=math.pi/2*a/16
            for b in range(49):
                phi=2*math.pi*b/48
                xs.append(half*math.sin(theta)*math.cos(phi))
                ys.append(half*math.sin(theta)*math.sin(phi))
                zs.append(height+half*math.cos(theta))
        I=[];J=[];K=[]
        for a in range(16):
            for b in range(48):
                q=a*49+b
                I.extend([q,q+1]); J.extend([q+49,q+49]); K.extend([q+50,q+50])
        fig.add_trace(go.Mesh3d(x=xs,y=ys,z=zs,i=I,j=J,k=K,color=color,opacity=1,flatshading=False,
            lighting=dict(ambient=0.78,diffuse=0.5,roughness=0.9),showscale=False,showlegend=False,hoverinfo="skip"))

    # 테라스형은 층마다 둘레 전체에 테라스 바닥과 난간을 둠
    elif shape == "▤ 테라스형":
        for level in range(1,4):
            z=height*level/4
            ext=half + (0.85 if level%2 else 0.45)
            fig.add_trace(go.Mesh3d(x=[-ext,ext,ext,-ext],y=[-ext,-ext,ext,ext],z=[z,z,z,z],
                i=[0,0],j=[1,2],k=[2,3],color="#9aa58a",opacity=1,showlegend=False,hoverinfo="skip"))
            for yy in [-ext,ext]:
                fig.add_trace(go.Scatter3d(x=[-ext,ext],y=[yy,yy],z=[z+0.55,z+0.55],mode="lines",
                    line=dict(color="#aab5a0",width=5),showlegend=False,hoverinfo="skip"))
            for xx in [-ext,ext]:
                fig.add_trace(go.Scatter3d(x=[xx,xx],y=[-ext,ext],z=[z+0.55,z+0.55],mode="lines",
                    line=dict(color="#aab5a0",width=5),showlegend=False,hoverinfo="skip"))

    # 사방 창문: 어두운 불투명 유리 패널과 외곽 프레임. 창문은 외벽 표면에만 놓음
    window_color = "#1e3945"
    z_levels = [2.4, 5.0, 7.6, 10.2, 12.6] if height >= 13 else [2.5, 5.2, 7.9]
    for z in z_levels:
        if z >= height - 0.6:
            continue
        for pos in [-2.65, 0, 2.65]:
            # 앞/뒤 면
            for y in [-half-0.045, half+0.045]:
                fig.add_trace(go.Mesh3d(x=[pos-.55,pos+.55,pos+.55,pos-.55],y=[y,y,y,y],
                    z=[z-.72,z-.72,z+.72,z+.72],i=[0,0],j=[1,2],k=[2,3],color=window_color,opacity=1,
                    flatshading=True,showlegend=False,hoverinfo="skip"))
                for xx in [pos-.57,pos+.57]:
                    fig.add_trace(go.Scatter3d(x=[xx,xx],y=[y,y],z=[z-.74,z+.74],mode="lines",
                        line=dict(color="#c7c1b4",width=4),showlegend=False,hoverinfo="skip"))
                fig.add_trace(go.Scatter3d(x=[pos,pos],y=[y,y],z=[z-.72,z+.72],mode="lines",
                    line=dict(color="#82949a",width=2),showlegend=False,hoverinfo="skip"))
            # 좌/우 면
            for x in [-half-0.045, half+0.045]:
                fig.add_trace(go.Mesh3d(x=[x,x,x,x],y=[pos-.55,pos+.55,pos+.55,pos-.55],
                    z=[z-.72,z-.72,z+.72,z+.72],i=[0,0],j=[1,2],k=[2,3],color=window_color,opacity=1,
                    flatshading=True,showlegend=False,hoverinfo="skip"))
                for yy in [pos-.57,pos+.57]:
                    fig.add_trace(go.Scatter3d(x=[x,x],y=[yy,yy],z=[z-.74,z+.74],mode="lines",
                        line=dict(color="#c7c1b4",width=4),showlegend=False,hoverinfo="skip"))
                fig.add_trace(go.Scatter3d(x=[x,x],y=[pos,pos],z=[z-.72,z+.72],mode="lines",
                    line=dict(color="#82949a",width=2),showlegend=False,hoverinfo="skip"))

    # 기술 선택은 건물 외부 전체의 모습에 반영
    if "태양광 발전" in (st.session_state.technologies or []) and shape != "◠ 돔형":
        for x in [-2.5,0,2.5]:
            fig.add_trace(go.Mesh3d(x=[x-.8,x+.8,x+.8,x-.8],y=[-2.7,-2.7,-1.1,-1.1],
                z=[height+.08]*4,i=[0,0],j=[1,2],k=[2,3],color="#1e4263",opacity=1,
                showlegend=False,hoverinfo="skip"))
    if "녹화 지붕·벽면" in (st.session_state.technologies or []) and shape != "◠ 돔형":
        fig.add_trace(go.Mesh3d(x=[-3.7,3.7,3.7,-3.7],y=[-3.7,-3.7,3.7,3.7],z=[height+.1]*4,
            i=[0,0],j=[1,2],k=[2,3],color="#527b4c",opacity=1,showlegend=False,hoverinfo="skip"))

    fig.update_layout(height=700, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor="#b9b6a8", plot_bgcolor="#b9b6a8",
        scene=dict(xaxis=dict(visible=False,range=[-10.5,10.5]),
                   yaxis=dict(visible=False,range=[-11,14]),
                   zaxis=dict(visible=False,range=[0,17]),bgcolor="#b9b6a8",dragmode="orbit",
                   aspectmode="manual",aspectratio=dict(x=1,y=1,z=1.05),
                   camera=dict(eye=dict(x=1.55,y=1.65,z=0.95),projection=dict(type="orthographic"))))
    return fig

# --------------------------- 스타일 ---------------------------
st.markdown('''
<style>
.stApp {background: linear-gradient(145deg,#101a20 0%,#17282c 48%,#26352f 100%); color:#f4f7f6;}
[data-testid="stSidebar"] {background:#172329;}
h1,h2,h3,p,li,label,.stMarkdown {color:#f4f7f6 !important;}
div[data-testid="stMetricValue"] {color:#ffffff !important;}
.stButton>button {background:#e2bd82;color:#182329;border:0;border-radius:10px;font-weight:800;min-height:2.7rem;}
.stButton>button:hover {background:#f1d3a2;color:#101a20;}
div[data-baseweb="select"] * {color:#f4f7f6 !important;}
[data-testid="stCaptionContainer"] {color:#d0dcda !important;}
.card {background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.15);border-radius:15px;padding:16px;margin:8px 0;}
</style>
''', unsafe_allow_html=True)

# --------------------------- 사이드바 ---------------------------
with st.sidebar:
    st.markdown("# 🏗️ 2050 건축 프로젝트")
    st.caption("황폐해진 지구에서 예산 안에 친환경 건축물을 설계하세요.")
    pages = ["메인 화면", "건물 용도", "건축 형태", "미래 자재", "미래 기술", "꾸미기", "완성 및 결과"]
    st.session_state.page = st.radio("페이지 이동", pages, index=pages.index(st.session_state.page) if st.session_state.page in pages else 0)
    st.divider()
    st.metric("초기 예산", "100억 원")
    st.metric("현재 남은 예산", f"{remaining_budget()}억 원" if st.session_state.commissioned else "의뢰 전")
    st.metric("현재 오염지수", f"{pollution_score()} / 100")
    st.caption("🟢 감축  ·  🔴 증가  ·  ⚪ 변화 없음")

# --------------------------- 메인 화면 ---------------------------
if st.session_state.page == "메인 화면":
    st.title("🌍 2050년, 다시 짓는 지구")
    st.write("오염으로 황폐해진 미래. 건축 의뢰를 받고, 제한된 예산 안에서 지속 가능한 건물을 완성하세요.")
    left,right=st.columns([1.25,1])
    with left:
        st.markdown('<div class="card"><h3>📩 건축 의뢰</h3><p>의뢰인이 지정한 용도와 형태는 무작위로 결정됩니다. 두 조건의 설계 비용은 의뢰를 수락할 때 예산에서 먼저 차감됩니다.</p></div>',unsafe_allow_html=True)
        if not st.session_state.commissioned:
            if st.button("📩 무작위 건축 의뢰 받기",type="primary",use_container_width=True):
                accept_commission(); st.rerun()
        else:
            st.success("의뢰 수락 완료! 지정된 용도와 형태를 유지해 설계하세요.")
            st.markdown(f"**의뢰 용도:** {st.session_state.usage}  \n**의뢰 형태:** {st.session_state.shape}")
            st.write(f"용도 비용 {USAGES[st.session_state.usage]['cost']}억 + 형태 비용 {SHAPES[st.session_state.shape]['cost']}억이 예산에서 차감됐습니다.")
            if st.button("🔄 새 의뢰 받기",use_container_width=True):
                accept_commission(); st.rerun()
        st.markdown("#### 설계 현황")
        st.write(f"**자재:** {st.session_state.material if st.session_state.commissioned else '아직 선택하지 않음'}")
        st.write(f"**미래 기술:** {', '.join(st.session_state.technologies) if st.session_state.technologies else '선택 없음'}")
        st.write(f"**색상:** {st.session_state.color}")
        st.caption("오른쪽 3D 건물은 마우스로 드래그해 여러 방향에서 확인할 수 있습니다.")
    with right:
        st.plotly_chart(building_figure(),use_container_width=True,config={"displayModeBar":False,"displaylogo":False,"scrollZoom":False})
    if st.session_state.commissioned:
        a,b,c=st.columns(3)
        a.metric("남은 예산",f"{remaining_budget()}억")
        b.metric("오염지수",f"{pollution_score()}/100",delta=f"{pollution_score()-100:+d} 지수",delta_color="inverse")
        c.metric("성공 목표","88 이하")
        st.info("게임 성공 조건: 의뢰받은 건물을 그대로 유지하고, 예산을 초과하지 않으며, 오염지수 88 이하를 달성하세요. 선택 조합에 따라 성공할 수 있습니다.")

elif st.session_state.page == "건물 용도":
    st.title("🏢 건물 용도")
    if not st.session_state.commissioned:
        st.warning("먼저 메인 화면에서 건축 의뢰를 받아 주세요.")
    else:
        data=USAGES[st.session_state.usage]
        st.markdown(f"### 의뢰된 용도: {st.session_state.usage}")
        st.write(data["desc"])
        st.info(f"의뢰 용도 비용: {data['cost']}억 원 · {pollution_label(data['impact'])}")
        st.caption("의뢰인이 지정한 용도이므로 변경할 수 없습니다. 이 비용은 의뢰 수락 시 예산에서 이미 차감되었습니다.")

elif st.session_state.page == "건축 형태":
    st.title("🏛️ 건축 형태")
    if not st.session_state.commissioned:
        st.warning("먼저 메인 화면에서 건축 의뢰를 받아 주세요.")
    else:
        data=SHAPES[st.session_state.shape]
        st.markdown(f"### 의뢰된 형태: {st.session_state.shape}")
        st.write(data["desc"])
        st.info(f"의뢰 형태 비용: {data['cost']}억 원 · {pollution_label(data['impact'])}")
        st.caption("의뢰인이 지정한 형태이므로 변경할 수 없습니다. 이 비용은 의뢰 수락 시 예산에서 이미 차감되었습니다.")
        st.plotly_chart(building_figure(),use_container_width=True,config={"displayModeBar":False,"displaylogo":False,"scrollZoom":False})

elif st.session_state.page == "미래 자재":
    st.title("🧱 미래 자재 선택")
    if not st.session_state.commissioned:
        st.warning("먼저 메인 화면에서 건축 의뢰를 받아 주세요.")
    else:
        st.write("감축 효과가 큰 자재일수록 비용이 높습니다. 자재별 비용은 선택 즉시 예산에 반영됩니다.")
        for name,data in MATERIALS.items():
            with st.container(border=True):
                col1,col2=st.columns([3,1])
                with col1:
                    st.subheader(name)
                    st.write(data["desc"])
                    st.markdown(f"**{pollution_label(data['impact'])}** · 비용 **{data['cost']}억 원**")
                with col2:
                    disabled=(remaining_budget()+MATERIALS[st.session_state.material]["cost"]-data["cost"]<0)
                    if st.button("선택됨" if st.session_state.material==name else "이 자재 선택",key=f"mat_{name}",disabled=disabled):
                        st.session_state.material=name; st.rerun()
        st.caption(f"현재 남은 예산: {remaining_budget()}억 원")

elif st.session_state.page == "미래 기술":
    st.title("⚙️ 미래 기술 선택")
    if not st.session_state.commissioned:
        st.warning("먼저 메인 화면에서 건축 의뢰를 받아 주세요.")
    else:
        st.write("필요한 기술을 여러 개 조합할 수 있습니다. 예산을 초과하는 기술은 선택할 수 없습니다.")
        for name,data in TECHNOLOGIES.items():
            with st.container(border=True):
                col1,col2=st.columns([3,1])
                with col1:
                    st.subheader(name)
                    st.write(data["desc"])
                    st.markdown(f"**{pollution_label(data['impact'])}** · 비용 **{data['cost']}억 원**")
                with col2:
                    selected=name in st.session_state.technologies
                    if selected:
                        if st.button("선택 해제",key=f"tech_off_{name}"):
                            st.session_state.technologies.remove(name); st.rerun()
                    else:
                        if st.button("기술 추가",key=f"tech_on_{name}",disabled=remaining_budget()<data["cost"]):
                            st.session_state.technologies.append(name); st.rerun()
        st.caption(f"현재 남은 예산: {remaining_budget()}억 원")

elif st.session_state.page == "꾸미기":
    st.title("🎨 건축물 꾸미기")
    if not st.session_state.commissioned:
        st.warning("먼저 메인 화면에서 건축 의뢰를 받아 주세요.")
    else:
        st.write("꾸미기에서는 건물 색상만 바꿀 수 있습니다. 예산과 오염지수에는 영향을 주지 않습니다.")
        st.session_state.color=st.selectbox("건물 외장 색상",list(COLORS.keys()),index=list(COLORS.keys()).index(st.session_state.color))
        st.plotly_chart(building_figure(),use_container_width=True,config={"displayModeBar":False,"displaylogo":False,"scrollZoom":False})

elif st.session_state.page == "완성 및 결과":
    st.title("🏁 건축 프로젝트 완성")
    if not st.session_state.commissioned:
        st.warning("먼저 메인 화면에서 건축 의뢰를 받아 주세요.")
    else:
        st.plotly_chart(building_figure(),use_container_width=True,config={"displayModeBar":False,"displaylogo":False,"scrollZoom":False})
        st.subheader("최종 설계 요약")
        x,y,z=st.columns(3)
        x.metric("총 설계 비용",f"{design_cost()}억 원")
        y.metric("남은 예산",f"{remaining_budget()}억 원")
        z.metric("최종 오염지수",f"{pollution_score()}/100",delta=f"{pollution_score()-100:+d} 지수",delta_color="inverse")
        st.write(f"**용도:** {st.session_state.usage}  ·  **형태:** {st.session_state.shape}")
        st.write(f"**자재:** {st.session_state.material}")
        st.write(f"**미래 기술:** {', '.join(st.session_state.technologies) if st.session_state.technologies else '추가 기술 없음'}")
        if st.button("🏗️ 건축물 완성 판정하기",type="primary",use_container_width=True):
            st.session_state.completed=True
            st.rerun()
        if st.session_state.completed and success_check():
            st.success("🎉 프로젝트 성공! 의뢰 조건을 지키며 예산과 환경 목표를 달성했습니다.")
            st.markdown("## 🌟 완성된 건축물의 장점")
            advantages=list(USAGES[st.session_state.usage]["advantages"])
            advantages.append(SHAPES[st.session_state.shape]["desc"])
            advantages.append(MATERIALS[st.session_state.material]["desc"])
            advantages.extend(TECHNOLOGIES[t]["desc"] for t in st.session_state.technologies)
            for item in advantages:
                st.markdown(f"- {item}")
            st.markdown("### 🌱 환경 성과")
            st.write(f"초기 오염지수 100에서 최종 {pollution_score()}로 바뀌었습니다. 총 변화는 **{pollution_label(pollution_score()-100)}**입니다.")
            st.write(f"총 {design_cost()}억 원을 사용했고, **{remaining_budget()}억 원**의 예산이 남았습니다.")
            st.markdown("### 🏡 주민이 누릴 수 있는 점")
            if "자연환기 설계" in st.session_state.technologies:
                st.write("- 바람을 활용하는 환기 계획으로 실내 공기를 순환시키는 데 도움이 됩니다.")
            if "고효율 단열" in st.session_state.technologies:
                st.write("- 냉난방 에너지 사용을 줄여 계절에 따른 실내 온도 변화를 완화할 수 있습니다.")
            if "녹화 지붕·벽면" in st.session_state.technologies:
                st.write("- 식생 공간이 열환경 개선과 휴식 공간 확보에 도움을 줄 수 있습니다.")
            if "태양광 발전" in st.session_state.technologies:
                st.write("- 건물에서 전력을 생산해 외부 전력망에 대한 의존을 줄일 수 있습니다.")
        elif st.session_state.completed:
            st.error("아직 성공 조건을 충족하지 못했습니다. 예산을 초과하지 않았는지, 오염지수가 88 이하인지 확인하고 자재·기술을 조정해 보세요.")
            st.write("성공 조건: 예산 100억 원 이내 · 오염지수 88 이하 · 의뢰 용도와 형태 유지")

st.caption("※ 오염지수와 비용은 게임을 위한 가상 수치입니다. 실제 건축물의 환경 성능을 정밀하게 예측하는 계산값은 아닙니다.")

