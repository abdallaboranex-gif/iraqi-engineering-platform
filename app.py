import streamlit as st
import base64
import os
import sys

# 1. تهيئة الشاشة بالعرض الكامل فوراً كأول أمر برمي صارم
st.set_page_config(page_title="منصة المدونات الهندسية العراقية", page_icon="iq", layout="wide")

# 2. حقن المسار الجذري الفعلي للمشروع لتأمين اتصال الغرف المعزولة سحابياً
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
img_governance = get_base64_image("assets/governance.png")
img_automation = get_base64_image("assets/automation.png")
img_sustainability = get_base64_image("assets/sustainability.png")

# 5. استدعاء شريط النافبار الموحد والمستقل بطريقة الاستدعاء المباشر الصافي
try:
    import core_layout.navbar.navbar_linker as nv_module
    nv_module.show_navbar_section()
except Exception:
    st.error("🚨 عطل طارئ في منظومة شريط التحكم المركزي.")

# 6. إدارة الذاكرة السحابية للتنقل الذكي المباشر بين الواجهات والتبويبات
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# تهيئة حالة ذاكرة تثبيت قائمة الفلترة الـ 9 العامة (تعني القفل وعدم المرور في حال False)
if "gate_filter_approved" not in st.session_state:
    st.session_state["gate_filter_approved"] = False
# 7. استدعاء الملقم الجانبي وتأمين الأزرار والرموز في قاع الملف
from modules_dashboard.dashboard_linker import show_dashboard_sidebar
from core_layout.footer.footer_linker import show_footer_section

# تقسيم الشاشة حسب الأوزان القياسية (اليمين محتوى واليسار مؤشرات نحيفة)
main_content, sidebar_stats = st.columns([4.5, 1.0])

# --- الطابق الأيسر: لوحة المؤشرات الوطنية الجانبية ---
with sidebar_stats:
    try:
        show_dashboard_sidebar()
    except Exception:
        st.caption("ℹ️ لوحة المؤشرات الجانبية خاضعة للصيانة حالياً.")

# --- الطابق الأيمن الرئيسي: تطبيق حلقة التوجيه وعزل غرف الفحص ---
with main_content:
    current_view = st.session_state["current_page"]
    # تطبيق فكرتك الجوهرية الشاملة: قفل وحجز الشاشة كلياً إلا بعد اجتياز بوابة الفلترة الـ 9 العامة
    if not st.session_state["gate_filter_approved"] and current_view in ["home", "data_governance", "blogs", "projects", "smart_cities", "automation", "sustainability"]:
        try:
            import vision_pillars.governance.governance_view as gov_package_v10
            gov_package_v10.render_governance_view()
        except Exception as e:
            st.error(f"⚠️ عطل في تحميل البوابة التمهيدية الموحدة: {str(e)}")
    else:
        if current_view == "data_governance":
            st.info("🧪 تم فك حظر كابينة الحوكمة! هنا ستفرد شاشة تدقيق شيت التربة.")
        elif current_view == "blogs":
            st.success("📚 تم فك حظر تبويب المدونات الوطني! هنا تعرض المقارنات المعتمدة.")
            
        if st.button("↩️ إعادة تعيين وتعديل قائمة المعطيات العامة الـ 9", key="app_reset_gate_v109"):
            st.session_state["gate_filter_approved"] = False; st.rerun()

if st.session_state["current_page"] in ["about", "auth"]:
    with main_content:
        st.markdown(f"## 🔒 واجهة مستقلة منفصلة: {st.session_state['current_page'].upper()}")
        if st.button("🏠 العودة للشاشة الرئيسية", key="app_back_nav_p109"):
            st.session_state["current_page"] = "home"; st.rerun()

try:
    show_footer_section()
except Exception:
    pass
