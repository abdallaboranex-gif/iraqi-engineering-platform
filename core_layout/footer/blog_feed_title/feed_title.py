import streamlit as st

def render_blog_feed_title():
    """
    برنامج مستقل لعرض ترويسة قسم أحدث المدونات والمقالات العملية.
    """
    col_t, col_b = st.columns([4, 1])
    with col_t:
        st.markdown("<h3 style='color: #c5a059 !important; font-size: 24px; font-weight: 700; margin:0;'>📰 أحدث المدونات والأدلة الميدانية</h3>", unsafe_allow_html=True)
    with col_b:
        if st.button("عرض الكل ➡️", key="btn_view_all_blogs"):
            st.info("هنت: جاري تحميل أرشيف المقالات الهندسية الكامل للمنصة.")
