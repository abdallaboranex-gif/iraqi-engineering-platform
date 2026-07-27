import streamlit as st

# استدعاء البرامج المساعدة المستقلة للأبحاث والشريط السفلي
from core_layout.footer.stats_newsletter_hub.research_hub import render_research_hub
from core_layout.footer.blog_feed_title.feed_title import render_blog_feed_title
from core_layout.footer.footer_bottom_bar.bottom_bar import render_footer_bottom_bar

def show_footer_section():
    """
    الدالة المركزية المطورة لتجميع برامج التغذية السفلية والمدونات الأربعة.
    تم حقن صور الخلفيات والتعتيم الزجاجي (Glassmorphism) لتطابق الصورة القياسية 100%.
    """
    
    # 1. تجميع وعزل بوابة الأبحاث والنشرة الموحدة للجامعات والنقابة
    try:
        render_research_hub()
    except Exception:
        st.error("⚠️ هنت: بوابة الأبحاث والتعليمات خاضعة للتحديث حالياً.")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 2. تجميع وعزل عنوان قسم أحدث المدونات (العنوان وزر عرض الكل)
    try:
        render_blog_feed_title()
    except Exception:
        pass

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. روابط صور سحابية خفيفة وتخصصية عالية الدقة لفرشها داخل الكروت الأربعة
    url_smart_cities = "https://unsplash.com"
    url_governance = "https://unsplash.com"
    url_automation = "https://unsplash.com"
    url_renewable = "https://unsplash.com"

    # إنشاء 4 أعمدة متساوية لصف خانات المقالات الأربعة جنباً إلى جنب كالصورة تماماً
    col1, col2, col3, col4 = st.columns(4)

    # كرت 1: مقال المدن الذكية المستدامة
    with col1:
        st.markdown(f"""
            <div style="background-image: linear-gradient(to top, rgba(7,22,21,0.95), rgba(7,22,21,0.75)), url('{url_smart_cities}'); background-size: cover; background-position: center; padding: 12px; border-radius: 8px; border: 1px solid rgba(197, 160, 89, 0.2); height: 190px; position: relative; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <span style="font-size: 10px; color: #c5a059; font-weight: bold; background: rgba(197,160,89,0.1); padding: 2px 6px; border-radius: 4px;">🏙️ مدن ذكية</span>
                <h4 style="margin: 8px 0 4px 0; font-size: 13px; color: #ffffff !important; font-weight: 700; line-height: 1.3;">تصميم المدن الذكية المستدامة</h4>
                <p style="font-size: 11px; color: #a0b0af !important; margin: 0; line-height: 1.4;">مبادئ التصميم المستدام للمدن الذكية في العراق وحلول التخطيط العمراني.</p>
                <div style="position: absolute; bottom: 10px; left: 12px; right: 12px; display: flex; justify-content: space-between; font-size: 9px; color: #809593;">
                    <span>📅 13 مايو 2026</span>
                    <span style="color: #c5a059;">إستكشف ➔</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("فتح مقال المدن 📄", key="btn_open_b1", use_container_width=True):
            st.info("هنت: سيتم فتح الدليل التفصيلي المكتوب بواسطة أساتذة التخطيط الحضري.")

    # كرت 2: مقال حوكمة المشاريع الهندسية
    with col2:
        st.markdown(f"""
            <div style="background-image: linear-gradient(to top, rgba(7,22,21,0.95), rgba(7,22,21,0.75)), url('{url_governance}'); background-size: cover; background-position: center; padding: 12px; border-radius: 8px; border: 1px solid rgba(197, 160, 89, 0.2); height: 190px; position: relative; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <span style="font-size: 10px; color: #c5a059; font-weight: bold; background: rgba(197,160,89,0.1); padding: 2px 6px; border-radius: 4px;">📊 حوكمة</span>
                <h4 style="margin: 8px 0 4px 0; font-size: 13px; color: #ffffff !important; font-weight: 700; line-height: 1.3;">حوكمة المشاريع الهندسية</h4>
                <p style="font-size: 11px; color: #a0b0af !important; margin: 0; line-height: 1.4;">أفضل الممارسات في إدارة المشاريع الهندسية الكبرى بأعلى معايير الشفافية المالية.</p>
                <div style="position: absolute; bottom: 10px; left: 12px; right: 12px; display: flex; justify-content: space-between; font-size: 9px; color: #809593;">
                    <span>📅 15 مايو 2026</span>
                    <span style="color: #c5a059;">إستكشف ➔</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("فتح مقال الحوكمة 🔒", key="btn_open_b2", use_container_width=True):
            st.info("هنت: سيتم فتح ورقة العمل التخصصية لإدارة النزاهة الرقمية للمشاريع.")

    # كرت 3: مقال الأتمتة في المصانع الذكية
    with col3:
        st.markdown(f"""
            <div style="background-image: linear-gradient(to top, rgba(7,22,21,0.95), rgba(7,22,21,0.75)), url('{url_automation}'); background-size: cover; background-position: center; padding: 12px; border-radius: 8px; border: 1px solid rgba(197, 160, 89, 0.2); height: 190px; position: relative; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <span style="font-size: 10px; color: #c5a059; font-weight: bold; background: rgba(197,160,89,0.1); padding: 2px 6px; border-radius: 4px;">🤖 أتمتة</span>
                <h4 style="margin: 8px 0 4px 0; font-size: 13px; color: #ffffff !important; font-weight: 700; line-height: 1.3;">الأتمتة في المصانع الذكية</h4>
                <p style="font-size: 11px; color: #a0b0af !important; margin: 0; line-height: 1.4;">دور أنظمة التحكم والذكاء الاصطناعي في تحسين الإنتاجية ومعامل البناء المحلية.</p>
                <div style="position: absolute; bottom: 10px; left: 12px; right: 12px; display: flex; justify-content: space-between; font-size: 9px; color: #809593;">
                    <span>📅 17 مايو 2026</span>
                    <span style="color: #c5a059;">إستكشف ➔</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("فتح مقال الأتمتة 🧠", key="btn_open_b3", use_container_width=True):
            st.info("هنت: سيتم فتح التقرير الميداني لتجربة أتمتة مصانع الجص الفيدرالية.")

    # كرت 4: مقال مستقبل الطاقة المتجددة في العراق
    with col4:
        st.markdown(f"""
            <div style="background-image: linear-gradient(to top, rgba(7,22,21,0.95), rgba(7,22,21,0.75)), url('{url_renewable}'); background-size: cover; background-position: center; padding: 12px; border-radius: 8px; border: 1px solid rgba(197, 160, 89, 0.2); height: 190px; position: relative; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <span style="font-size: 10px; color: #c5a059; font-weight: bold; background: rgba(197,160,89,0.1); padding: 2px 6px; border-radius: 4px;">☀️ استدامة</span>
                <h4 style="margin: 8px 0 4px 0; font-size: 13px; color: #ffffff !important; font-weight: 700; line-height: 1.3;">مستقبل الطاقة المتجددة</h4>
                <p style="font-size: 11px; color: #a0b0af !important; margin: 0; line-height: 1.4;">تحليل واقع وآفاق الطاقة الشمسية والرياح في الأبنية العراقية الحديثة وكود العزل.</p>
                <div style="position: absolute; bottom: 10px; left: 12px; right: 12px; display: flex; justify-content: space-between; font-size: 9px; color: #809593;">
                    <span>📅 19 مايو 2026</span>
                    <span style="color: #c5a059;">إستكشف ➔</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("فتح مقال الطاقة 🔋", key="btn_open_b4", use_container_width=True):
            st.info("هنت: سيتم فتح الدليل الرياضي لحساب سعات خلايا الألواح الشمسية.")

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. تجميع وعزل الشريط القانوني والختامي الأخير بأسفل الشاشة (شريط الشركاء والحقوق)
    try:
        render_footer_bottom_bar()
    except Exception:
        pass
