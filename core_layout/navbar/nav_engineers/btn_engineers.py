import streamlit as st

def render_btn_engineers():
    """زر الانتقال لبوابة التحقق من هويات المهندسين وصلاحيات المكاتب الاستشارية."""
    if st.button("المهندسون", key="nav_btn_engineers", use_container_width=True):
        st.session_state["current_page"] = "engineers"
        st.rerun()
