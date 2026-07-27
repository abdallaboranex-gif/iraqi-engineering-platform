import streamlit as st

def render_automation_pillar():
    """
    برنامج مصغر ومستقل لعرض ركيزة الأتمتة والذكاء الاصطناعي.
    """
    st.markdown(
        """
        <div style="text-align: center; padding: 10px; border-radius: 5px;">
            <div style="font-size: 32px; margin-bottom: 5px;">🤖</div>
            <p style="font-size: 16px; font-weight: 600; color: #c5a059 !important; margin: 0;">أتمتة</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
