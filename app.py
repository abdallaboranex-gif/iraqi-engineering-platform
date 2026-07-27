import streamlit as st
import base64
import os

# 1. تهيئة الشاشة بالعرض الكامل فوراً كأول أمر برمي صارم
st.set_page_config(page_title="منصة المدونات الهندسية العراقية", page_icon="🇮🇶", layout="wide")

# 2. فرش الخلفية الموحدة وتأمين الهوية البصرية من ملف الإعدادات
from config.settings import apply_unified_background
apply_unified_background()

# 3. دالة محمية لتشفير صور الكبائن الأربعة لتعمل سحابياً بامتياز
def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode()
        return ""
    except Exception:
        return ""

# تشفير كافة الصور بالأسماء والصيغ المتطابقة مع مجلد assets
img_smart_cities = get_base64_image("assets/smart_cities.jpeg")
img_governance = get_base64_image("assets/governance.jpg")
img_automation = get_base64_image("assets/automation.png")
img_sustainability = get_base64_image("assets/sustainability.jpg")

# 4. حقن وعرض شريط النافبار المعزول والمستقل من مجلده الفرعي بحزام أمان مطهر
try:
    import core_layout.navbar.navbar_linker as nv_linker
    nv_linker.show_navbar_section()
except Exception:
    st.error("⚠️ هنت سيادي: جاري صيانة وتحديث قمة شريط التحكم المركزي.")

# 5. إدارة الذاكرة السحابية للتنقل الذكي المباشر بين الواجهات والتبويبات
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# 6. استدعاء طوابق المرصد الجانبي وقاع المقالات بأحزمة أمان معزولة
from modules_dashboard.dashboard_linker import show_dashboard_sidebar
from core_layout.footer.footer_linker import show_footer_section

# 7. تقسيم الشاشة حسب الأوزان القياسية (اليمين محتوى واليسار مؤشرات نحيفة)
main_content, sidebar_stats = st.columns([4.5, 1.0])

# --- الطابق الأيسر: لوحة المؤشرات الوطنية الجانبية النحيفة الملونة ---
with sidebar_stats:
    try:
        show_dashboard_sidebar()
    except Exception:
        st.caption("⚠️ لوحة المؤشرات الجانبية خاضعة للصيانة الكلية حالياً.")

# --- الطابق الأيمن الرئيسي: تجميع كبائن الرؤى المضيئة والمدونات بقاع الشاشة ---
with main_content:
    current_view = st.session_state["current_page"]
    
    if current_view == "home":
        # عرض القسم الترحيبي والعناوين المضاءة بالوسط من مجلد الهيرو
        try:
            from core_layout.hero.hero_linker import show_hero_section
            show_hero_section()
        except Exception:
            pass
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # عرض كبائن الرؤى الأربعة متراصة في سطر واحد (4 أعمدة متساوية) باستخدام صورك الحقيقية
        st.markdown("### 🏢 كبائن الرؤى الاستراتيجية الكبرى للمنصة")
        col_v1, col_v2, col_v3, col_v4 = st.columns(4)
        
        # كابينة 1: المدن الذكية
        with col_v1:
            st.markdown(f"""
                <div style="background-color: rgba(7, 22, 21, 0.7); border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.3); padding: 0px; text-align: center; overflow: hidden; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.25); margin-bottom: 8px;">
                    <img src="data:image/jpeg;base64,{img_smart_cities}" style="width: 100%; height: 140px; object-fit: cover; border-bottom: 2px solid #c5a059;">
                    <div style="padding: 12px;">
                        <h4 style="color: #c5a059 !important; margin: 0; font-size: 14px; font-weight: 700;">المدن الذكية</h4>
                        <p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.4;">تصميم وإدارة المدن الذكية لمستقبل العراق</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة المدن 🗺️", key="ultimate_f_go_sc", use_container_width=True):
                st.session_state["current_page"] = "smart_cities"
                st.rerun()

        # كابينة 2: حوكمة المشاريع
        with col_v2:
            st.markdown(f"""
                <div style="background-color: rgba(7, 22, 21, 0.7); border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.3); padding: 0px; text-align: center; overflow: hidden; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.25); margin-bottom: 8px;">
                    <img src="data:image/jpeg;base64,{img_governance}" style="width: 100%; height: 140px; object-fit: cover; border-bottom: 2px solid #c5a059;">
                    <div style="padding: 12px;">
                        <h4 style="color: #c5a059 !important; margin: 0; font-size: 14px; font-weight: 700;">حساب الأحمال</h4>
                        <p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.4;">حوكمة المشاريع الهندسية بأعلى معايير الشفافية</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الحوكمة 🔒", key="ultimate_f_go_gov", use_container_width=True):
                st.session_state["current_page"] = "governance"
                st.rerun()

        # كابينة 3: الأتمتة والذكاء الاصطناعي
        with col_v3:
            st.markdown(f"""
                <div style="background-color: rgba(7, 22, 21, 0.7); border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.3); padding: 0px; text-align: center; overflow: hidden; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.25); margin-bottom: 8px;">
                    <img src="data:image/png;base64,{img_automation}" style="width: 100%; height: 140px; object-fit: cover; border-bottom: 2px solid #c5a059;">
                    <div style="padding: 12px;">
                        <h4 style="color: #c5a059 !important; margin: 0; font-size: 14px; font-weight: 700;">الأتمتة والذكاء الصناعي</h4>
                        <p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.4;">التحكم الذكي والأنظمة المؤتمتة لرفع الكفاءة</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الأتمتة 🧠", key="ultimate_f_go_auto", use_container_width=True):
                st.session_state["current_page"] = "automation"
                st.rerun()

        # كابينة 4: الاستدامة وكفاءة الطاقة
        with col_v4:
            st.markdown(f"""
                <div style="background-color: rgba(7, 22, 21, 0.7); border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.3); padding: 0px; text-align: center; overflow: hidden; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.25); margin-bottom: 8px;">
                    <img src="data:image/jpeg;base64,{img_sustainability}" style="width: 100%; height: 140px; object-fit: cover; border-bottom: 2px solid #c5a059;">
                    <div style="padding: 12px;">
                        <h4 style="color: #c5a059 !important; margin: 0; font-size: 14px; font-weight: 700;">الاستدامة</h4>
                        <p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.4;">مقالات وحلول مبتكرة لمستقبل أكثر استدامة</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("استكشف واجهة الاستدامة ☀️", key="ultimate_f_go_sustain", use_container_width=True):
                st.session_state["current_page"] = "sustainability"
                st.rerun()
                
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # عرض شريط التغذية الموحد للجامعات والمقالات الأربعة بقاع الشاشة
        try:
            show_footer_section()
        except Exception:
            st.caption("⚠️ قاع الشاشة خاضع للتحديث.")

    # --- إدارة فتح الصفحات الفرعية الجديدة والمعزولة ---
    elif current_view == "smart_cities":
        from vision_pillars.smart_cities.smart_cities_view import render_smart_cities_view
        try: render_smart_cities_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="ultimate_f_back_sc"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "governance":
        from vision_pillars.governance.governance_view import render_governance_view
        try: render_governance_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="ultimate_f_back_gov"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "automation":
        from vision_pillars.automation.automation_view import render_automation_view
        try: render_automation_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="ultimate_f_back_auto"): st.session_state["current_page"] = "home"; st.rerun()

    elif current_view == "sustainability":
        from vision_pillars.sustainability.sustainability_view import render_sustainability_view
        try: render_sustainability_view()
        except Exception: st.error("⚠️ عطل في الكابينة")
        if st.button("↩️ العودة للشاشة الرئيسية", key="ultimate_f_back_sus"): st.session_state["current_page"] = "home"; st.rerun()
        
    elif current_view in ["blogs", "projects", "engineers", "data_governance", "about", "auth"]:
        st.markdown(f"## 🚪 واجهة مركزية جديدة ومستقلة: `{current_view.upper()}`")
        st.info(f"🔒 هذه الخدمة معزولة تماماً في مجلدها الفرعي الخاص.")
        if st.button("↩️ العودة للشاشة الرئيسية", key="ultimate_f_back_nav_pages"): st.session_state["current_page"] = "home"; st.rerun()
