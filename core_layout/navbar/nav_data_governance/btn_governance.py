import streamlit as st

def render_btn_governance():
    """زر الانتقال لواجهة سياسات أمن البيانات وحماية سرية المخططات الهندسية السيادية."""
    if st.button("حوكمة البيانات", key="nav_btn_gov_data", use_container_width=True):
        st.session_state["current_page"] = "data_governance"
        st.rerun()
