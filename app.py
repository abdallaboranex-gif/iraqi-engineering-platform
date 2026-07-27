import streamlit as st

# 1. ضبط إعدادات الشاشة لتكون بعرض كامل وتستوعب التوزيع الأصلي
st.set_page_config(page_title="منصة المدونات الهندسية العراقية", page_icon="🇮🇶", layout="wide")

# 2. استدعاء ملف الإعدادات وأحزمة الأمان وطوابق الواجهة الرئيسية
from config.settings import apply_unified_background
from core_layout.navbar.navbar_linker import show_navbar_section
from core_layout.hero.hero_linker import show_hero_section
from core_layout.footer.footer_linker import show_footer_section
from modules_dashboard.dashboard_linker import show_dashboard_sidebar

# 3. تأمين الهوية البصرية وفرش الصورة الموحدة كخلفية ثابتة لجميع الشاشات
apply_unified_background()

# 4. زرع وحقن شريط التحكم والتنقل العلوي الثابت في قمة الشاشة
try:
    show_navbar_section()
except Exception:
    st.error("⚠️ هنت سيادي: عطل طارئ في منظومة شريط التحكم المركزي.")

# 5. إدارة الذاكرة السحابية للتنقل الذكي المباشر بين الواجهات (Session State)
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# 6. المطابقة الكبرى مع الصورة الأصلية:
# تقسيم الشاشة إلى عمودين: الأيمن كبير جداً للمحتوى (وزن 3.2)، والأيسر نحيف جداً للمؤشرات الجانبية (وزن 1.0)
main_content, sidebar_stats = st.columns([3.2, 1.0])

# --- الطابق الأيسر: لوحة المؤشرات الوطنية الجانبية النحيفة (مطابقة للأصل) ---
with sidebar_stats:
    try:
        show_dashboard_sidebar()
    except Exception:
        st.caption("⚠️ لوحة المؤشرات الجانبية خاضعة للصيانة الكلية حالياً.")

# --- الطابق الأيمن الرئيسي: المحتوى والكبائن المتراصة ---
with main_content:
    current_view = st.session_state["current_page"]
    
    if current_view == "home":
        # عرض القسم الترحيبي والأهداف الخمسة بالوسط
        try:
            show_hero_section()
        except Exception:
            pass
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # المطابقة الكبرى الثانية: عرض كبائن الرؤى الأربعة متراصة في سطر واحد (4 أعمدة متساوية بجانب بعضها)
        st.markdown("### 🏢 كبائن الرؤى الاستراتيجية الكبرى للمنصة")
        col_v1, col_v2, col_v3, col_v4 = st.columns(4)
        
        # كابينة 1
        with col_v1:
            st.markdown("""
                <div style="background-color: rgba(7, 22, 21, 0.7); padding: 12px; border-radius: 8px; border-top: 3px solid #c5a059; height: 130px; margin-bottom: 8px;">
                    <h4 style="color: #c5a059 !important; margin: 0; font-size: 13px;">🏙️ كابينة المدن الذكية</h4>
                    <p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.3;">مشاريع التخطيط العمراني وفك الاختناقات المرورية لوزارة التخطيط ودعاية الشركات.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة المدن 🗺️", key="go_sc", use_container_width=True):
                st.session_state["current_page"] = "smart_cities"
                st.rerun()

        # كابينة 2
        with col_v2:
            st.markdown("""
                <div style="background-color: rgba(7, 22, 21, 0.7); padding: 12px; border-radius: 8px; border-top: 3px solid #c5a059; height: 130px; margin-bottom: 8px;">
                    <h4 style="color: #c5a059 !important; margin: 0; font-size: 13px;">📊 كابينة حوكمة المشاريع</h4>
                    <p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.3;">مراقبة الجودة والشفافية في المشاريع الفيدرالية الكبرى والحد من الهدر المالي.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الحوكمة 🔒", key="go_gov", use_container_width=True):
                st.session_state["current_page"] = "governance"
                st.rerun()

        # كابينة 3
        with col_v3:
            st.markdown("""
                <div style="background-color: rgba(7, 22, 21, 0.7); padding: 12px; border-radius: 8px; border-top: 3px solid #c5a059; height: 130px; margin-bottom: 8px;">
                    <h4 style="color: #c5a059 !important; margin: 0; font-size: 13px;">🤖 كابينة الأتمتة والذكاء</h4>
                    <p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.3;">محرك الفحص الذاتي وقصص نجاح المصانع المؤتمتة ومعامل الطابوق المحلية.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الأتمتة 🧠", key="go_auto", use_container_width=True):
                st.session_state["current_page"] = "automation"
                st.rerun()

        # كابينة 4
        with col_v4:
            st.markdown("""
                <div style="background-color: rgba(7, 22, 21, 0.7); padding: 12px; border-radius: 8px; border-top: 3px solid #c5a059; height: 130px; margin-bottom: 8px;">
                    <h4 style="color: #c5a059 !important; margin: 0; font-size: 13px;">🌿 كابينة الاستدامة والطاقة</h4>
                    <p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.3;">مرصد الأبنية الخضراء، مشاريع الألواح الشمسية ودليل مواد البناء المعزولة.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الاستدامة ☀️", key="go_sustain", use_container_width=True):
                st.session_state["current_page"] = "sustainability"
                st.rerun()
                
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # استدعاء وعرض شريط التغذية الموحد للجامعات والمقالات الأربعة بقاع الشاشة
        try:
            show_footer_section()
        except Exception:
            st.caption("⚠️ قاع الشاشة خاضع للتحديث.")

    # --- إدارة فتح الصفحات الفرعية الجديدة ---
    elif current_view == "smart_cities":
        from vision_pillars.smart_cities.smart_cities_view import render_smart_cities_view
        try: render_smart_cities_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_sc"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "governance":
        from vision_pillars.governance.governance_view import render_governance_view
        try: render_governance_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_gov"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "automation":
        from vision_pillars.automation.automation_view import render_automation_view
        try: render_automation_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_auto"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "sustainability":
        from vision_pillars.sustainability.sustainability_view import render_sustainability_view
        try: render_sustainability_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_sus"): st.session_state["current_page"] = "home"; st.rerun()
        
    elif current_view in ["blogs", "projects", "engineers", "data_governance", "about", "auth"]:
        st.markdown(f"## 🚪 واجهة مركزية جديدة ومستقلة: `{current_view.upper()}`")
        st.info(f"🔒 هذه الخدمة معزولة تماماً في مجلدها الفرعي الخاص.")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_nav_pages"): st.session_state["current_page"] = "home"; st.rerun()
