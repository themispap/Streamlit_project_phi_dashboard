import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":house:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# st.title("Φ Εργαστήριο Μαθηματικών")
st.image('static/images/logo_math_long_wb_nowww.png')
