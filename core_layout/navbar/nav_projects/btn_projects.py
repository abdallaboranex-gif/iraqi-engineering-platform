import streamlit as st

def render_btn_projects():
    """زر الانتقال لواجهة تتبع المخططات والمشاريع الخاصة بالمهندس."""
    if st.button("المشاريع", key="nav_btn_projects", use_container_width=True):
        st.session_state["current_page"] = "projects"
        st.rerun()
