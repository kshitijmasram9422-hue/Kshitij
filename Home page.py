import streamlit as st

st.set_page_config(
    page_title="Kshitij Masram",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#0f172a);
}

/* Hero Animation */
.hero{
    text-align:center;
    padding:40px;
    animation: fadeIn 2s ease-in-out;
}

.hero h1{
    color:white;
    font-size:60px;
}

.hero h3{
    color:#38bdf8;
}

/* Card Design */
.card{
    background-color:rgba(255,255,255,0.08);
    padding:25px;
    border-radius:15px;
    margin:10px;
    transition:0.4s;
    color:white;
}

.card:hover{
    transform:translateY(-10px);
}

/* Animation */
@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(30px);
    }
    to{
        opacity:1;
        transform:translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Kshitij Masram</h1>
    <h3>Biotechnology | Bioprocess Engineering</h3>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <h1>Kshitij Masram</h1>
    <h3>Biotechnology | Bioprocess Engineering</h3>
</div>
""", unsafe_allow_html=True)
col1,col2 = st.columns([1,2])



with col2:
    st.markdown("""
    <div class="card">
        <h2>About Me</h2>
        <p>
        Biotechnology graduate passionate about
        fermentation technology, industrial biotechnology,
        and bioprocess engineering.
        </p>
    </div>
    """, unsafe_allow_html=True)
st.header("Skills")

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h3>🧬 Biotechnology</h3>
    <p>Microbiology<br>Biochemistry<br>Molecular Biology</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>⚙️ Bioprocess</h3>
    <p>Fermentation<br>Bioreactors<br>DSP</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h3>📊 Research</h3>
    <p>Data Analysis<br>Scientific Writing<br>Problem Solving</p>
    </div>
    """, unsafe_allow_html=True)
    st.header("Skill Level")

    st.write("Biotechnology")
    st.progress(90)

    st.write("Fermentation")
    st.progress(85)

    st.write("Bioprocess Engineering")
    st.progress(80)

    st.write("German Language")
    st.progress(60)
    st.header("Projects")

    st.markdown("""
    <div class="card">
    <h3>Fermentation Research</h3>
    <p>Study of microbial growth and fermentation optimization.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Bioprocess Development</h3>
    <p>Scale-up and process design concepts for industrial biotechnology.</p>
    </div>
    """, unsafe_allow_html=True)
    st.header("Contact")

    st.markdown("""
    <div class="card">
    📧 your_email@example.com<br><br>
    🔗 LinkedIn Profile<br><br>
    📍 India
    </div>
    """, unsafe_allow_html=True)


