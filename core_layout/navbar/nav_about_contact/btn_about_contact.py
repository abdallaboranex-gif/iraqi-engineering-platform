import streamlit as st

def render_btn_about_contact():
    """زر الانتقال المباشر لصفحة التعريف بالمنصة وتفاصيل الاتصال الفني."""
    if st.button("عن المنصة / اتصل بنا", key="nav_btn_about", use_container_width=True):
        st.session_state["current_page"] = "about"
        st.rerun()
