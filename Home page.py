import streamlit as st

st.set_page_config(
    page_title="Kshitij Masram"
)
st.title("kshitij")
st.sidebar.subheader("Select the page above.")

import streamlit as st

st.set_page_config(
    page_title="Kshitij Masram",
    page_icon="🧬",
    layout="wide"
)

# HERO SECTION
st.title("Kshitij Masram")
st.subheader("Biotechnology | Bioprocess Engineering | Fermentation Technology")

st.markdown("---")

# ABOUT
st.header("About Me")

st.write("""
I am a Biotechnology graduate with a strong interest in Bioprocess Engineering,
Fermentation Technology, Industrial Biotechnology, and Process Development.

I enjoy learning new technologies, solving scientific problems, and exploring
innovative approaches in biotechnology and bioprocessing.
""")

st.markdown("---")

# SKILLS
st.header("Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
    ### Biotechnology
    - Microbiology
    - Molecular Biology
    - Biochemistry
    - Cell Culture
    """)

with col2:
    st.info("""
    ### Bioprocess Engineering
    - Fermentation
    - Bioreactors
    - Downstream Processing
    - Process Optimization
    """)

with col3:
    st.warning("""
    ### Additional Skills
    - Data Analysis
    - Research
    - Scientific Writing
    - Problem Solving
    """)

st.markdown("---")

# PROJECTS
st.header("Projects")

project1, project2 = st.columns(2)

with project1:
    st.subheader("Fermentation Studies")
    st.write("""
    Research involving fermentation processes,
    microbial growth and process optimization.
    """)

with project2:
    st.subheader("Bioprocess Development")
    st.write("""
    Studies focused on process design,
    scale-up concepts and industrial biotechnology.
    """)

st.markdown("---")

# EDUCATION
st.header("Education")

st.write("""
**Master of Science (Biotechnology)**

Advanced studies in biotechnology, microbiology,
biochemistry and bioprocess-related subjects.
""")

st.markdown("---")

# INTERESTS
st.header("Interests")

st.write("""
- Industrial Biotechnology
- Fermentation Technology
- Bioprocess Engineering
- Sustainable Technologies
- Scientific Research
- German Language Learning
""")

st.markdown("---")

# CONTACT
st.header("Contact")

st.write("📧 Email: your_email@example.com")
st.write("🔗 LinkedIn: Add your LinkedIn URL")
st.write("📍 Location: India")

st.image("profile.jpg", width=250)

