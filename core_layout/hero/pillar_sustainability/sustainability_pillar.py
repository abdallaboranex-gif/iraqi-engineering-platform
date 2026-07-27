import streamlit as st

def render_sustainability_pillar():
    """
    برنامج مصغر ومستقل لعرض ركيزة الاستدامة وأيقونتها البيئية.
    """
    st.markdown(
        """
        <div style="text-align: center; padding: 10px; border-radius: 5px;">
            <div style="font-size: 32px; margin-bottom: 5px;">🌿</div>
            <p style="font-size: 16px; font-weight: 600; color: #c5a059 !important; margin: 0;">استدامة</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
