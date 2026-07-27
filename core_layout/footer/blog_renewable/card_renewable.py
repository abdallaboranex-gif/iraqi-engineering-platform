import streamlit as st

def render_blog_renewable():
    """
    برنامج مستقل يعرض خانة مقالات وأدلة هندسة الطاقة المتجددة والعزل.
    """
    st.markdown(
        """
        <div style="background-color: rgba(13, 35, 33, 0.5); padding: 15px; border-radius: 8px; border-bottom: 3px solid #c5a059; height: 180px;">
            <span style="font-size: 11px; color: #c5a059; font-weight: bold;">☀️ الطاقة المستدامة</span>
            <h4 style="margin: 5px 0; font-size: 15px; color: #ffffff !important;">مستقبل الطاقة المتجددة في العراق</h4>
            <p style="font-size: 12px; color: #a0b0af !important; margin: 0;">أدلة تخصصية لحساب السعات الإنتاجية للألواح الشمسية وشرح آليات العزل الحراري الذكي لتقليل الأحمال والضغوط على الشبكة الوطنية.</p>
        </div>
        """, unsafe_allow_html=True
    )
    if st.button("اقرأ المقال الكامل", key="btn_read_blog_renew"):
        st.info("هنت: سيتم فتح الدليل الحسابي المعتمد لكود كفاءة الطاقة العراقي.")
