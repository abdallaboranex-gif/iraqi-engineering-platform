import streamlit as st

# استدعاء البرامج المصغرة المستقلة للتغذية السفلية من مجلداتها الفرعية المخصصة
from core_layout.footer.stats_newsletter_hub.research_hub import render_research_hub
from core_layout.footer.blog_feed_title.feed_title import render_blog_feed_title
from core_layout.footer.blog_smart_cities.card_smart_cities import render_blog_smart_cities
from core_layout.footer.blog_governance.card_governance import render_blog_governance
from core_layout.footer.blog_automation.card_automation import render_blog_automation
from core_layout.footer.blog_renewable.card_renewable import render_blog_renewable
from core_layout.footer.footer_bottom_bar.bottom_bar import render_footer_bottom_bar

def show_footer_section():
    """
    الدالة المركزية لتجميع برامج التغذية السفلية وبوابة الأبحاث والمدونات الأربعة.
    تطبق مبدأ صفر اعتمادية وحماية كاملة ضد انهيار قاع الشاشة.
    """
    
    # 1. تجميع وعزل بوابة الأبحاث والنشرة الموحدة للجامعات والنقابة
    try:
        render_research_hub()
    except Exception:
        st.error("⚠️ هنت: بوابة الأبحاث والتعليمات خاضعة للتحديث حالياً.")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 2. تجميع وعزل عنوان قسم أحدث المدونات
    try:
        render_blog_feed_title()
    except Exception:
        pass

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. إنشاء 4 أعمدة متساوية لصف خانات المقالات الأربعة جنباً إلى جنب كالصورة
    col1, col2, col3, col4 = st.columns(4)

    # تجميع وعزل خانة مقال المدن الذكية في العمود الأول
    with col1:
        try:
            render_blog_smart_cities()
        except Exception:
            st.caption("⚠️ المقال خاضع للصيانة")

    # تجميع وعزل خانة مقال حوكمة المشاريع في العمود الثاني
    with col2:
        try:
            render_blog_governance()
        except Exception:
            st.caption("⚠️ المقال خاضع للصيانة")

    # تجميع وعزل خانة مقال أتمتة المصانع في العمود الثالث
    with col3:
        try:
            render_blog_automation()
        except Exception:
            st.caption("⚠️ المقال خاضع للصيانة")

    # تجميع وعزل خانة مقال مستقبل الطاقة المتجددة في العمود الرابع
    with col4:
        try:
            render_blog_renewable()
        except Exception:
            st.caption("⚠️ المقال خاضع للصيانة")

    # 4. تجميع وعزل الشريط القانوني والختامي الأخير بأسفل الشاشة
    try:
        render_footer_bottom_bar()
    except Exception:
        pass
