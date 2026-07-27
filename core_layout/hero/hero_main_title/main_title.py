import streamlit as st

def render_main_title():
    """
    برنامج مصغر ومستقل لعرض العنوان الرئيسي للمنصة 
    مع إضاءة ذهبية خفيفة متناسقة مع الهوية العراقية.
    """
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <h1 style="
                font-size: 52px; 
                font-weight: 800; 
                color: #c5a059 !important; 
                text-shadow: 0 0 20px rgba(197, 160, 89, 0.6); 
                margin-bottom: 5px;
            ">
                المدونات الهندسية العراقية
            </h1>
        </div>
        """, 
        unsafe_allow_html=True
    )
