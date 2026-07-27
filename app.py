import streamlit as st

# 1. ضبط إعدادات الشاشة لتكون بعرض كامل وتستوعب لوحة المؤشرات الجانبية كالصورة
st.set_page_config(page_title="منصة المدونات الهندسية العراقية", page_icon="🇮🇶", layout="wide")

# 2. استدعاء ملف الإعدادات وأحزمة الأمان وطوابق الواجهة الرئيسية
from config.settings import apply_unified_background
from core_layout.navbar.navbar_linker import show_navbar_section
from core_layout.hero.hero_linker import show_hero_section
from core_layout.footer.footer_linker import show_footer_section
from modules_dashboard.dashboard_linker import show_dashboard_sidebar

# استدعاء واجهات كبائن الرؤى الأربعة الإعلامية الكبرى
from vision_pillars.smart_cities.smart_cities_view import render_smart_cities_view
from vision_pillars.governance.governance_view import render_governance_view
from vision_pillars.automation.automation_view import render_automation_view
from vision_pillars.sustainability.sustainability_view import render_sustainability_view

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

# 6. تقسيم الشاشة هندسياً إلى جزء رئيسي (اليسار) وجزء للمؤشرات الوطنية الجانبية (اليمين) كالصورة
main_content, sidebar_stats = st.columns([3, 1])

# --- الطابق الأيمن: لوحة المؤشرات الوطنية الجانبية الثابتة ---
with sidebar_stats:
    st.markdown("""
        <style>
        [data-testid="stColumn"] {
            background-color: rgba(13, 35, 33, 0.4);
            padding: 20px;
            border-radius: 12px;
            border: 1px solid rgba(197, 160, 89, 0.2);
        }
        </style>
    """, unsafe_allow_html=True)
    try:
        show_dashboard_sidebar()
    except Exception:
        st.caption("⚠️ لوحة المؤشرات الجانبية خاضعة للصيانة الكلية حالياً.")

# --- الطابق الأيسر: إدارة محتوى الشاشات والواجهات الجديدة ---
with main_content:
    current_view = st.session_state["current_page"]
    
    # السيناريو أ: إذا كان المهندس في الشاشة الرئيسية (تظهر الرؤى الأربعة والأهداف كالصورة)
    if current_view == "home":
        # عرض القسم الترحيبي والأهداف الخمسة
        try:
            show_hero_section()
        except Exception:
            pass
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # عرض كبائن الرؤى الأربعة الكبيرة كبطاقات تسويقية وإعلامية سريعة بالواجهة
        st.markdown("### 🏢 كبائن الرؤى الاستراتيجية الكبرى للمنصة")
        col_v1, col_v2 = st.columns(2)
        
        with col_v1:
            st.markdown("""
                <div style="background-color: rgba(7, 22, 21, 0.7); padding: 20px; border-radius: 10px; border-right: 5px solid #c5a059; margin-bottom: 15px;">
                    <h4 style="color: #c5a059 !important; margin: 0;">🏙️ كابينة المدن الذكية</h4>
                    <p style="font-size: 13px; color: #a0b0af !important; margin-top: 5px;">مشاريع التخطيط العمراني وفك الاختناقات المرورية لوزارة التخطيط ودعاية الشركات.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة المدن الذكية 🗺️", key="go_sc"):
                st.session_state["current_page"] = "smart_cities"
                st.rerun()

            st.markdown("""
                <div style="background-color: rgba(7, 22, 21, 0.7); padding: 20px; border-radius: 10px; border-right: 5px solid #c5a059; margin-bottom: 15px;">
                    <h4 style="color: #c5a059 !important; margin: 0;">🤖 كابينة الأتمتة والذكاء الاصطناعي</h4>
                    <p style="font-size: 13px; color: #a0b0af !important; margin-top: 5px;">محرك الفحص الذاتي وقصص نجاح المصانع المؤتمتة ومعامل الطابوق المحلية.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الأتمتة والتكنولوجيا 🧠", key="go_auto"):
                st.session_state["current_page"] = "automation"
                st.rerun()

        with col_v2:
            st.markdown("""
                <div style="background-color: rgba(7, 22, 21, 0.7); padding: 20px; border-radius: 10px; border-right: 5px solid #c5a059; margin-bottom: 15px;">
                    <h4 style="color: #c5a059 !important; margin: 0;">📊 كابينة حوكمة المشاريع الهندسية</h4>
                    <p style="font-size: 13px; color: #a0b0af !important; margin-top: 5px;">مراقبة الجودة والشفافية في المشاريع الفيدرالية الكبرى والحد من الهدر المالي.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الحوكمة والنزاهة 🔒", key="go_gov"):
                st.session_state["current_page"] = "governance"
                st.rerun()

            st.markdown("""
                <div style="background-color: rgba(7, 22, 21, 0.7); padding: 20px; border-radius: 10px; border-right: 5px solid #c5a059; margin-bottom: 15px;">
                    <h4 style="color: #c5a059 !important; margin: 0;">🌿 كابينة الاستدامة وكفاءة الطاقة</h4>
                    <p style="font-size: 13px; color: #a0b0af !important; margin-top: 5px;">مرصد الأبنية الخضراء، مشاريع الألواح الشمسية ودليل مواد البناء المعزولة.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الاستدامة البيئية ☀️", key="go_sustain"):
                st.session_state["current_page"] = "sustainability"
                st.rerun()
                
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # استدعاء وعرض شريط التغذية الموحد للجامعات والمقالات الأربعة بقاع الشاشة
        try:
            show_footer_section()
        except Exception:
            st.caption("⚠️ قاع الشاشة خاضع للتحديث.")

    # السيناريو ب: فتح الواجهات الجديدة والمستقلة بالكامل عند ضغط الأزرار
    elif current_view == "smart_cities":
        try: render_smart_cities_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_sc"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "governance":
        try: render_governance_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_gov"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "automation":
        try: render_automation_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_auto"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "sustainability":
        try: render_sustainability_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_sus"): st.session_state["current_page"] = "home"; st.rerun()
        
    # واجهات أزرار النافبار (محجوزة وتفتح كصفحات مستقلة مفرغة وجاهزة للخدمة)
    elif current_view in ["blogs", "projects", "engineers", "data_governance", "about", "auth"]:
        st.markdown(f"## 🚪 واجهة مركزية جديدة ومستقلة: `{current_view.upper()}`")
        st.info(f"🔒 هذه الخدمة معزولة تماماً في مجلدها الفرعي الخاص، وتعمل كبرنامج مستقل لمستندات {current_view}.")
        st.write("محرك الاستعلام الذكي في النافبار بالأعلى يعمل ويقرأ من جداول الإكسل شيت الخاصة بك في كل الأوقات بانتظام.")
        if st.button("↩️ العودة للشاشة الرئيسية", key="back_nav_pages"):
            st.session_state["current_page"] = "home"
            st.rerun()
