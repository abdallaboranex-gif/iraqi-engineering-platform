import streamlit as st

def render_nav_logo():
    """برنامج مستقل لعرض شعار المنصة بجانب العلم."""
    st.markdown("<div style='font-size: 18px; font-weight: 700; color: #c5a059 !important; padding-top: 10px; text-align: center;'>INCP</div>", unsafe_allow_html=True)
