import streamlit as st
import base64
import os
import sys

# 1. تهيئة الشاشة بالعرض الكامل فوراً كأول أمر برمي صارم
st.set_page_config(page_title="منصة المدونات الهندسية العراقية", page_icon="🇮🇶", layout="wide")

# 2. حقن المسار الجذري الفعلي للمشروع لتأمين غرف الـ __init__.py المرفوعة
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# 🎯 حاقن فيدرالي لتطهير المسارات المخبأة وإجبار السيرفر على الاعتراف بالحزم الجديدة
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database_rules"))

# 3. فرش الخلفية الموحدة وتأمين الهوية البصرية من ملف الإعدادات
import config.settings as custom_settings
custom_settings.apply_unified_background()

# 4. دالة محمية لتشفير صور الكبائن الأربعة لتعمل سحابياً بامتياز
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

# 5. استدعاء شريط النافبار المعزول والمستقل بطريقة الاستدعاء المباشر الصافي 100%
try:
    import core_layout.navbar.navbar_linker as nv_module
    nv_module.show_navbar_section()
except Exception:
    st.error("⚠️ هنت سيادي: عطل طارئ في منظومة شريط التحكم المركزي.")
# 6. إدارة الذاكرة السحابية للتنقل الذكي المباشر بين الواجهات والتبويبات
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# تهيئة حالة ذاكرة تثبيت قائمة الفلترة الـ 9 العامة (False تعني القفل وعدم المرور)
if "gate_filter_approved" not in st.session_state:
    st.session_state["gate_filter_approved"] = False

# 7. استدعاء طوابق المرصد الجانبي وقاع المقالات بأحزمة أمان معزولة ومحمية
from modules_dashboard.dashboard_linker import show_dashboard_sidebar
from core_layout.footer.footer_linker import show_footer_section

# 8. تقسيم الشاشة حسب الأوزان القياسية (اليمين محتوى واليسار مؤشرات نحيفة)
main_content, sidebar_stats = st.columns([4.5, 1.0])

# --- الطابق الأيسر: لوحة المؤشرات الوطنية الجانبية النحيفة ---
with sidebar_stats:
    try:
        show_dashboard_sidebar()
    except Exception:
        st.caption("⚠️ لوحة المؤشرات الجانبية خاضعة للصيانة الكلية حالياً.")

# --- الطابق الأيمن الرئيسي: تطبيق بوابة الفرز الـ 9 قبل دخول المدونات والفحوصات ---
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
        
        # عرض كبائن الرؤى الأربعة متراصة في سطر واحد باستخدام صورك الحقيقية
        st.markdown("### 🏢 كبائن الرؤى الاستراتيجية الكبرى للمنصة")
        col_v1, col_v2, col_v3, col_v4 = st.columns(4)
        
        # كابينة 1: المدن الذكية
        with col_v1:
            st.markdown(f'<div style="background-color: rgba(7, 22, 21, 0.7); border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.3); padding: 0px; text-align: center; overflow: hidden; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.25); margin-bottom: 8px;"><img src="data:image/jpeg;base64,{img_smart_cities}" style="width: 100%; height: 140px; object-fit: cover; border-bottom: 2px solid #c5a059;"><div style="padding: 12px;"><h4 style="color: #c5a059 !important; margin: 0; font-size: 14px; font-weight: 700;">المدن الذكية</h4><p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.4;">تصميم وإدارة المدن الذكية لمستقبل العراق</p></div></div>', unsafe_allow_html=True)
            if st.button("استكشف واجهة المدن 🗺️", key="app_go_sc", use_container_width=True):
                st.session_state["current_page"] = "smart_cities"; st.rerun()

        # كابينة 2: حوكمة المشاريع (حساب الأحمال)
        with col_v2:
            st.markdown(f'<div style="background-color: rgba(7, 22, 21, 0.7); border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.3); padding: 0px; text-align: center; overflow: hidden; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.25); margin-bottom: 8px;"><img src="data:image/jpeg;base64,{img_governance}" style="width: 100%; height: 140px; object-fit: cover; border-bottom: 2px solid #c5a059;"><div style="padding: 12px;"><h4 style="color: #c5a059 !important; margin: 0; font-size: 14px; font-weight: 700;">حساب الأحمال</h4><p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.4;">حوكمة المشاريع الهندسية بأعلى معايير الشفافية</p></div></div>', unsafe_allow_html=True)
            if st.button("استكشف واجهة الحوكمة 🔒", key="app_go_gov", use_container_width=True):
                st.session_state["current_page"] = "data_governance"; st.rerun()

        # كابينة 3: الأتمتة والذكاء الاصطناعي
        with col_v3:
            st.markdown(f'<div style="background-color: rgba(7, 22, 21, 0.7); border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.3); padding: 0px; text-align: center; overflow: hidden; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.25); margin-bottom: 8px;"><img src="data:image/png;base64,{img_automation}" style="width: 100%; height: 140px; object-fit: cover; border-bottom: 2px solid #c5a059;"><div style="padding: 12px;"><h4 style="color: #c5a059 !important; margin: 0; font-size: 14px; font-weight: 700;">الأتمتة والذكاء الصناعي</h4><p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.4;">التحكم الذكي والأنظمة المؤتمتة لرفع الكفاءة</p></div></div>', unsafe_allow_html=True)
            if st.button("استكشف واجهة الأتمتة 🧠", key="app_go_auto", use_container_width=True):
                st.session_state["current_page"] = "automation"; st.rerun()

        # كابينة 4: الاستدامة وكفاءة الطاقة
        with col_v4:
            st.markdown(f'<div style="background-color: rgba(7, 22, 21, 0.7); border-radius: 12px; border: 1px solid rgba(197, 160, 89, 0.3); padding: 0px; text-align: center; overflow: hidden; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.25); margin-bottom: 8px;"><img src="data:image/jpeg;base64,{img_sustainability}" style="width: 100%; height: 140px; object-fit: cover; border-bottom: 2px solid #c5a059;"><div style="padding: 12px;"><h4 style="color: #c5a059 !important; margin: 0; font-size: 14px; font-weight: 700;">الاستدامة</h4><p style="font-size: 11px; color: #a0b0af !important; margin-top: 5px; line-height: 1.4;">مقالات وحلول مبتكرة لمستقبل أكثر استدامة</p></div></div>', unsafe_allow_html=True)
            if st.button("استكشف واجهة الاستدامة ☀️", key="app_go_sustain", use_container_width=True):
                st.session_state["current_page"] = "sustainability"; st.rerun()
                
        st.markdown("<br><br>", unsafe_allow_html=True)
        try:
            show_footer_section()
        except Exception:
            st.caption("⚠️ قاع الشاشة خاضع للتحديث.")

        # تطبيق فكرتك الجوهرية: قفل وحجز دخول المدونات والفحوصات إلا بعد اجتياز بوابة الفلترة الـ 9 العامة
        if not st.session_state["gate_filter_approved"]:
            try:
                # 🎯 استدعاء صريح وآمن ومحمي بالمسافات القياسية لنسخة كابينة الحوكمة العاشرة
                import vision_pillars.governance.governance_view as gov_package_v10
                gov_package_v10.render_governance_view()
            except Exception as e:
                st.error(f"⚠️ عطل في تحميل البوابة التمهيدية: {str(e)}")

            # إذا تم الضغط على زر تثبيت المعطيات الـ 9 بنجاح، تفتح الشرايين وتنبثق المدونة أو الفحص المختار
            st.success(f"🔓 البوابة مفتوحة ومؤمنة بالمعطيات الحالية. القسم النشط: `{current_view.upper()}`")
            
            # هنا سيتم توجيه المستخدم لملفات الفحص الصافية للمدونات الخمسة المعزولة لاحقاً
            if current_view == "data_governance":
                st.info("🧪 هنا ستنبثق شاشة فحص ومطابقة مدونة التربة (soil_rules) الحالية.")
            
            if st.button("↩️ إعادة تعيين وتعديل قائمة المعطيات العامة الـ 9", key="app_reset_gate"):
                st.session_state["gate_filter_approved"] = False; st.rerun()

    elif current_view in ["about", "auth"]:
        st.markdown(f"## 🚪 واجهة مستقلة: `{current_view.upper()}`")
        if st.button("↩️ العودة للشاشة الرئيسية", key="app_back_nav_p"): 
            st.session_state["current_page"] = "home"; st.rerun()
