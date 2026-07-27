import streamlit as st

def render_auth_gate():
    """بوابة تسجيل الدخول وتأمين صلاحيات المكاتب الهندسية."""
    if st.button("تسجيل الدخول 🔒", key="nav_btn_auth_gate", use_container_width=True):
        st.session_state["current_page"] = "auth"
        st.rerun()
