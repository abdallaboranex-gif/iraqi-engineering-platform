import streamlit as st

def render_blog_governance():
    """
    برنامج مستقل يعرض خانة مقالات وأدلة حوكمة المشاريع الهندسية.
    """
    st.markdown(
        """
        <div style="background-color: rgba(13, 35, 33, 0.5); padding: 15px; border-radius: 8px; border-bottom: 3px solid #c5a059; height: 180px;">
            <span style="font-size: 11px; color: #c5a059; font-weight: bold;">📊 الحوكمة الرقمية</span>
            <h4 style="margin: 5px 0; font-size: 15px; color: #ffffff !important;">حوكمة المشاريع الهندسية</h4>
            <p style="font-size: 12px; color: #a0b0af !important; margin: 0;">طرق الإدارة الحديثة لحماية جودة المنشآت والحد من الهدر المالي عبر تطبيق المراجعة الإلكترونية المؤتمتة لجداول الكميات الفيدرالية.</p>
        </div>
        """, unsafe_allow_html=True
    )
    if st.button("اقرأ المقال الكامل", key="btn_read_blog_gov"):
        st.info("هنت: سيتم فتح المقال القانوني والفني حول آليات الأتمتة الإدارية للمشاريع.")
