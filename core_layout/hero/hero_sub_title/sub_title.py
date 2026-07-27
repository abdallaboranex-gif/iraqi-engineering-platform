import streamlit as st

def render_sub_title():
    """
    برنامج مصغر ومستقل لعرض العنوان التوضيحي الفرعي 
    بخط واضح ناصع البياض ومريح للعين عند القراءة.
    """
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 30px;">
            <p style="
                font-size: 22px; 
                font-weight: 400; 
                color: #ffffff !important; 
                letter-spacing: 0.5px;
                opacity: 0.95;
            ">
                منصة وطنية للمعرفة الهندسية المستدامة
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
