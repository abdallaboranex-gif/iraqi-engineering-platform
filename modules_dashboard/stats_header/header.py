import streamlit as st

def render_stats_header():
    """
    برنامج مصغر لعرض ترويسة وعنوان لوحة المؤشرات الوطنية.
    """
    st.markdown(
        """
        <div style="border-bottom: 2px solid #c5a059; padding-bottom: 10px; margin-bottom: 20px;">
            <h3 style="color: #c5a059 !important; font-size: 22px; font-weight: 700; margin: 0;">
                📊 المؤشرات الوطنية الحية
            </h3>
        </div>
        """, 
        unsafe_allow_html=True
    )
