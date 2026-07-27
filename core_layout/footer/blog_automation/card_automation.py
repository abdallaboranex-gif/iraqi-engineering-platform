import streamlit as st

def render_blog_automation():
    """
    برنامج مستقل يعرض خانة مقالات تكنولوجيا الأتمتة في قطاع البناء والتصنيع.
    """
    st.markdown(
        """
        <div style="background-color: rgba(13, 35, 33, 0.5); padding: 15px; border-radius: 8px; border-bottom: 3px solid #c5a059; height: 180px;">
            <span style="font-size: 11px; color: #c5a059; font-weight: bold;">🤖 الأتمتة والذكاء الاصطناعي</span>
            <h4 style="margin: 5px 0; font-size: 15px; color: #ffffff !important;">الأتمتة في المصانع الذكية</h4>
            <p style="font-size: 12px; color: #a0b0af !important; margin: 0;">مراجعة ميدانية لكيفية إدخال الروبوتات ونظم التحكم الذكي في معامل الطابوق والجص المحلية لضمان أعلى مطابقة للكود الإنشائي العراقي.</p>
        </div>
        """, unsafe_allow_html=True
    )
    if st.button("اقرأ المقال الكامل", key="btn_read_blog_auto"):
        st.info("هنت: سيتم مراجعة قصة نجاح أحد المصانع المؤتمتة حديثاً في البصرة.")
