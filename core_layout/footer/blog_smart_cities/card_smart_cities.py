import streamlit as st

def render_blog_smart_cities():
    """
    برنامج مستقل يعرض خانة مقالات وأدلة تصميم المدن الذكية المستدامة.
    """
    st.markdown(
        """
        <div style="background-color: rgba(13, 35, 33, 0.5); padding: 15px; border-radius: 8px; border-bottom: 3px solid #c5a059; height: 180px;">
            <span style="font-size: 11px; color: #c5a059; font-weight: bold;">🏙️ المدن الذكية</span>
            <h4 style="margin: 5px 0; font-size: 15px; color: #ffffff !important;">تصميم المدن الذكية المستدامة</h4>
            <p style="font-size: 12px; color: #a0b0af !important; margin: 0;">دليل تفصيلي حول آليات دمج نظم الشبكات الذكية وتوزيع الفضاءات الخضراء في التخطيط الحضري للمدن العراقية الجديدة.</p>
        </div>
        """, unsafe_allow_html=True
    )
    if st.button("اقرأ المقال الكامل", key="btn_read_blog_sc"):
        st.info("هنت: سيتم فتح المقال الفني المكتوب بواسطة أساتذة الجامعة التكنولوجية.")
