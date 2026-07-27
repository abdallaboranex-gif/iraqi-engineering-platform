import streamlit as st

def render_btn_blogs():
    """زر الانتقال المباشر لأرشيف المدونات الهندسية والأبحاث."""
    if st.button("المدونات", key="nav_btn_blogs", use_container_width=True):
        st.session_state["current_page"] = "blogs"
        st.rerun()
