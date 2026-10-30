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
    # 난이도를 아주 조금 높여 오염지수 85 이하 + 예산 이내일 때 성공합니다.
    return st.session_state.commissioned and pollution_score() <= 85 and remaining_budget() >= 0

def impact_sum():
    return (USAGES[st.session_state.usage]["impact"] + SHAPES[st.session_state.shape]["impact"] +
            MATERIALS[st.session_state.material]["impact"] +
            sum(TECHNOLOGIES[t]["impact"] for t in st.session_state.technologies))

# --------------------------- 3D 미리보기 ---------------------------


def building_figure():
    """큰 불투명 건물과 황폐하지만 지구다운 지형을 가진 회전형 3D 장면."""
    import math
    color = COLORS[st.session_state.color]
    shape = st.session_state.shape if st.session_state.commissioned else "▰ 직육면체형"
    techs = st.session_state.technologies or []
    is_tower = shape == "▥ 타워형"
    is_dome = shape == "◠ 돔형"
    height = 16.0 if is_tower else 12.5
    half = 4.8 if is_dome else 4.25
    fig = go.Figure()

    # 황폐한 지구의 자연 지형: 평평한 바닥 대신 완만한 구릉과 건조한 대지
    xs = [(-15 + i * .75) for i in range(41)]
    ys = [(-15 + j * .75) for j in range(41)]
    X, Y, Z = [], [], []
    for y in ys:
        row = []
        for x in xs:
            hill_a = 1.15 * math.exp(-(((x-10)/5.5)**2 + ((y-9)/5.0)**2))
            hill_b = .72 * math.exp(-(((x+11)/4.5)**2 + ((y-7)/6.0)**2))
            ridge = .32 * math.sin(x*.42) * math.cos(y*.31)
            crater = -.38 * math.exp(-(((x-8)/2.8)**2 + ((y+8)/3.0)**2))
            row.append(max(-.35, .05 + hill_a + hill_b + ridge + crater))
        X.append(xs)
        Y.append(y)
        Z.append(row)
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        surfacecolor=[[((x+15)/30)*.35 + ((y+15)/30)*.18 for x in xs] for y in ys],
        colorscale=[[0,"#66513e"],[.25,"#8a6d4d"],[.5,"#a58a62"],[.75,"#6f7955"],[1,"#9c8a69"]],
        cmin=0,cmax=1,showscale=False,opacity=1,
        lighting=dict(ambient=.72,diffuse=.72,specular=.08,roughness=.95),
        hoverinfo="skip",name="황폐한 지표"
    ))

    # 먼 산맥과 침식된 바위 능선
    for i in range(7):
        x0 = -15 + i*4.8
        ridge_x = [x0, x0+1.4, x0+3.0, x0+4.5]
        ridge_y = [13.2, 12.6, 13.4, 13.0]
        ridge_z = [.5, 2.4+(i%3)*.55, 1.5+(i%2)*.4, .45]
        fig.add_trace(go.Scatter3d(
            x=ridge_x,y=ridge_y,z=ridge_z,mode="lines",
            line=dict(color="#78644f",width=13),opacity=.85,
            showlegend=False,hoverinfo="skip"
        ))

    # 침식된 지면의 갈라진 자국과 마른 물길
    for k in range(5):
        cx = -12 + k*5.2
        fig.add_trace(go.Scatter3d(
            x=[cx,cx+1.1,cx+2.2,cx+3.4],
            y=[-12.5,-10.9,-11.8,-9.9],
            z=[.18,.22,.2,.24],mode="lines",
            line=dict(color="#c2a47a",width=4),opacity=.65,
            showlegend=False,hoverinfo="skip"
        ))

    # 멀리 보이는 낮은 폐허 건축물
    for rx, ry, rw, rh in [(-12,5,1.4,3.2),(12,7,1.7,4.1),(-10,-8,1.1,2.4),(11,-7,1.3,2.8)]:
        fig.add_trace(go.Mesh3d(
            x=[rx-rw,rx+rw,rx+rw,rx-rw,rx-rw,rx+rw,rx+rw,rx-rw],
            y=[ry-rw,ry-rw,ry+rw,ry+rw,ry-rw,ry-rw,ry+rw,ry+rw],
            z=[0,0,0,0,rh,rh*.92,rh,rh],
            i=[0,0,1,1,2,2,3,3],j=[1,2,2,6,3,7,0,4],k=[5,6,5,5,6,6,4,7],
            color="#756d60",opacity=1,flatshading=True,
            showlegend=False,hoverinfo="skip"
        ))

    # 건물 외벽: 완전 불투명한 면으로 구성
    verts = [(-half,-half,0),(half,-half,0),(half,half,0),(-half,half,0),
             (-half,-half,height),(half,-half,height),(half,half,height),(-half,half,height)]
    faces = [(0,1,5),(0,5,4),(1,2,6),(1,6,5),(2,3,7),(2,7,6),
             (3,0,4),(3,4,7),(4,5,6),(4,6,7)]
    ii,jj,kk = zip(*faces)
    fig.add_trace(go.Mesh3d(
        x=[p[0] for p in verts],y=[p[1] for p in verts],z=[p[2] for p in verts],
        i=ii,j=jj,k=kk,color=color,opacity=1,flatshading=False,
        lighting=dict(ambient=.68,diffuse=.78,specular=.18,roughness=.82,fresnel=.02),
        lightposition=dict(x=70,y=-100,z=180),
        showlegend=False,hoverinfo="skip",name="불투명한 건물 외벽"
    ))

    # 네 방향 모두 같은 층수·창문 리듬을 유지하도록 사면에 창문을 배치.
    # 창문은 내부가 보이지 않는 짙은 청회색 반사 패널.
    floors = 6 if is_tower else 5
    for n in range(1,floors):
        z = height*n/floors
        # 사면을 감싸는 두꺼운 층간 띠
        fig.add_trace(go.Scatter3d(
            x=[-half,half,half,-half,-half],
            y=[-half,-half,half,half,-half],z=[z]*5,
            mode="lines",line=dict(color="#d4c8b2",width=6),
            showlegend=False,hoverinfo="skip"
        ))
    window_color = "#263d4a"
    window_rows = [height*(n+.52)/floors for n in range(floors)]
    positions = [-2.8,-.95,.95,2.8]
    for z in window_rows:
        for p in positions:
            # 앞/뒤 면: 어두운 불투명 창 + 밝은 프레임
            for side in [-1,1]:
                y = side*(half+.025)
                fig.add_trace(go.Mesh3d(
                    x=[p-.57,p+.57,p+.57,p-.57],y=[y]*4,
                    z=[z-.62,z-.62,z+.62,z+.62],
                    i=[0,0],j=[1,2],k=[2,3],color=window_color,
                    opacity=1,flatshading=True,showlegend=False,hoverinfo="skip"
                ))
                fig.add_trace(go.Scatter3d(
                    x=[p-.62,p+.62,p+.62,p-.62,p-.62],
                    y=[y*1.002]*5,z=[z-.67,z-.67,z+.67,z+.67,z-.67],
                    mode="lines",line=dict(color="#b6b8ad",width=3),
                    showlegend=False,hoverinfo="skip"
                ))
            # 좌/우 면
            for side in [-1,1]:
                x = side*(half+.025)
                fig.add_trace(go.Mesh3d(
                    x=[x]*4,y=[p-.57,p+.57,p+.57,p-.57],
                    z=[z-.62,z-.62,z+.62,z+.62],
                    i=[0,0],j=[1,2],k=[2,3],color=window_color,
                    opacity=1,flatshading=True,showlegend=False,hoverinfo="skip"
                ))
                fig.add_trace(go.Scatter3d(
                    x=[x*1.002]*5,y=[p-.62,p+.62,p+.62,p-.62,p-.62],
                    z=[z-.67,z-.67,z+.67,z+.67,z-.67],
                    mode="lines",line=dict(color="#b6b8ad",width=3),
                    showlegend=False,hoverinfo="skip"
                ))

    # 테라스형: 층마다 실제 바닥판이 돌출되며 불투명한 난간 설치
    if shape == "▤ 테라스형":
        for level in range(1,5):
            z = height*level/5
            ext = half + (1.15 if level%2 else .72)
            fig.add_trace(go.Mesh3d(
                x=[-ext,ext,ext,-ext],y=[-ext,-ext,ext,ext],z=[z]*4,
                i=[0,0],j=[1,2],k=[2,3],color="#8c9b78",opacity=1,
                showlegend=False,hoverinfo="skip"
            ))
            fig.add_trace(go.Scatter3d(
                x=[-ext,ext,ext,-ext,-ext],y=[-ext,-ext,ext,ext,-ext],
                z=[z+.72]*5,mode="lines",
                line=dict(color="#d8d4c8",width=6),
                showlegend=False,hoverinfo="skip"
            ))

    # 돔형 지붕은 반투명 유리 대신 불투명한 금속 패널로 구성
    if is_dome:
        dome_x,dome_y,dome_z=[],[],[]
        for a in range(17):
            theta=math.pi*a/32
            for b in range(33):
                phi=2*math.pi*b/32
                dome_x.append(half*math.sin(theta)*math.cos(phi))
                dome_y.append(half*math.sin(theta)*math.sin(phi))
                dome_z.append(height+half*.72*math.cos(theta))
        di,dj,dk=[],[],[]
        for a in range(16):
            for b in range(32):
                q=a*33+b
                di.extend([q,q+1]);dj.extend([q+33,q+33]);dk.extend([q+34,q+34])
        fig.add_trace(go.Mesh3d(
            x=dome_x,y=dome_y,z=dome_z,i=di,j=dj,k=dk,
            color="#9b9b8e",opacity=1,flatshading=False,
            lighting=dict(ambient=.7,diffuse=.7,specular=.12,roughness=.85),
            showlegend=False,hoverinfo="skip"
        ))

    # 두꺼운 옥상 파라펫과 설비 구조물
    roof_z=height+.18
    fig.add_trace(go.Mesh3d(
        x=[-half-.25,half+.25,half+.25,-half-.25],
        y=[-half-.25,-half-.25,half+.25,half+.25],
        z=[roof_z]*4,i=[0,0],j=[1,2],k=[2,3],
        color="#c6bca8",opacity=1,showlegend=False,hoverinfo="skip"
    ))
    for x in [-2.5,0,2.5]:
        fig.add_trace(go.Mesh3d(
            x=[x-.42,x+.42,x+.42,x-.42],
            y=[-1.5,-1.5,1.5,1.5],
            z=[roof_z+.25]*4,i=[0,0],j=[1,2],k=[2,3],
            color="#344b60",opacity=1,showlegend=False,hoverinfo="skip"
        ))

    # 옥상 녹화와 태양광 설비
    if "녹화 지붕·벽면" in techs:
        for x in [-2.6,-1.3,0,1.3,2.6]:
            fig.add_trace(go.Scatter3d(
                x=[x,x+.22],y=[.2,.4],z=[roof_z+.3,roof_z+1.0],
                mode="lines",line=dict(color="#6e9862",width=8),
                showlegend=False,hoverinfo="skip"
            ))
    if "태양광 발전" in techs:
        for x in [-2.7,-1.0,.7,2.4]:
            fig.add_trace(go.Mesh3d(
                x=[x-.48,x+.48,x+.48,x-.48],
                y=[-1.6,-1.6,-.45,-.45],z=[roof_z+.32]*4,
                i=[0,0],j=[1,2],k=[2,3],color="#24445e",
                opacity=1,showlegend=False,hoverinfo="skip"
            ))

    # 정면의 묵직한 출입구와 넓은 캐노피
    front=-half-.08
    fig.add_trace(go.Mesh3d(
        x=[-1.05,1.05,1.05,-1.05],y=[front]*4,z=[0,0,3.0,3.0],
        i=[0,0],j=[1,2],k=[2,3],color="#253744",opacity=1,
        showlegend=False,hoverinfo="skip"
    ))
    fig.add_trace(go.Mesh3d(
        x=[-1.8,1.8,1.8,-1.8],
        y=[-half-1.05,-half-1.05,-half-.02,-half-.02],
        z=[3.15]*4,i=[0,0],j=[1,2],k=[2,3],
        color="#c2aa83",opacity=1,showlegend=False,hoverinfo="skip"
    ))

    # 황폐한 지구에도 남아 있는 드문 나무·관목
    for tx,ty,scale in [(-7,-3,.9),(7,-2,1.0),(-8,7,.75),(8,6,.8),(-3,-9,.55)]:
        fig.add_trace(go.Scatter3d(
            x=[tx,tx],y=[ty,ty],z=[.15,1.7*scale],
            mode="lines",line=dict(color="#66513b",width=8),
            showlegend=False,hoverinfo="skip"
        ))
        fig.add_trace(go.Scatter3d(
            x=[tx],y=[ty],z=[2.35*scale],
            mode="markers",marker=dict(size=17*scale,color="#71835a",opacity=1),
            showlegend=False,hoverinfo="skip"
        ))

    # 화면 내 건물 크기를 키우고, 어떤 방향에서도 왜곡되지 않도록 고정 비율 사용.
    fig.update_layout(
        height=720,margin=dict(l=0,r=0,t=0,b=0),
        paper_bgcolor="#17232a",plot_bgcolor="#17232a",
        scene=dict(
            xaxis=dict(visible=False,range=[-13,13]),
            yaxis=dict(visible=False,range=[-13,14]),
            zaxis=dict(visible=False,range=[0,19]),
            bgcolor="#17232a",
            aspectmode="manual",aspectratio=dict(x=1.0,y=1.0,z=1.0),
            camera=dict(eye=dict(x=1.55,y=1.55,z=1.05),projection=dict(type="orthographic")),
            dragmode="orbit"
        ),
        showlegend=False
    )
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
        st.plotly_chart(building_figure(),use_container_width=True,config={"displayModeBar":False,"scrollZoom":False,"doubleClick":False,"responsive":True})
    if st.session_state.commissioned:
        a,b,c=st.columns(3)
        a.metric("남은 예산",f"{remaining_budget()}억")
        b.metric("오염지수",f"{pollution_score()}/100",delta=f"{pollution_score()-100:+d} 지수",delta_color="inverse")
        c.metric("성공 목표","85 이하")
        st.info("게임 성공 조건: 의뢰받은 건물을 그대로 유지하고, 예산을 초과하지 않으며, 오염지수 85 이하를 달성하세요. 선택 조합에 따라 성공할 수 있습니다.")

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
        st.plotly_chart(building_figure(),use_container_width=True,config={"displayModeBar":False,"scrollZoom":False,"doubleClick":False,"responsive":True})

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
        st.plotly_chart(building_figure(),use_container_width=True,config={"displayModeBar":False,"scrollZoom":False,"doubleClick":False,"responsive":True})

elif st.session_state.page == "완성 및 결과":
    st.title("🏁 건축 프로젝트 완성")
    if not st.session_state.commissioned:
        st.warning("먼저 메인 화면에서 건축 의뢰를 받아 주세요.")
    else:
        st.plotly_chart(building_figure(),use_container_width=True,config={"displayModeBar":False,"scrollZoom":False,"doubleClick":False,"responsive":True})
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
            st.error("아직 성공 조건을 충족하지 못했습니다. 예산을 초과하지 않았는지, 오염지수가 90 이하인지 확인하고 자재·기술을 조정해 보세요.")
            st.write("성공 조건: 예산 100억 원 이내 · 오염지수 90 이하 · 의뢰 용도와 형태 유지")

st.caption("※ 오염지수와 비용은 게임을 위한 가상 수치입니다. 실제 건축물의 환경 성능을 정밀하게 예측하는 계산값은 아닙니다.")

