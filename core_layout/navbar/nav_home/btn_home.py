import streamlit as st

def render_btn_home():
    """زر الانتقال المستقل للرئيسية وإعادة تصفير تبويبات العمل."""
    if st.button("الرئيسية", key="nav_btn_home", use_container_width=True):
        st.session_state["current_page"] = "home"
        st.rerun()
