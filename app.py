import streamlit as st
import base64
import os
import sys

# 1. تهيئة الشاشة بالعرض الكامل فوراً كأول أمر برمي صارم
st.set_page_config(page_title="منصة المدونات الهندسية العراقية", page_icon="🇮🇶", layout="wide")

# 2. الحل القطعي لحل أزمة السيرفر: حقن المسار الجذري الفعلي للمشروع في نظام بايثون
# هذا السطر يجبر السيرفر سحابياً على قراءة كل المجلدات الفرعية كحزم نظام شرعية 100%
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 3. فرش الخلفية الموحدة وتأمين الهوية البصرية من ملف الإعدادات المحدث
from config.settings import apply_unified_background
apply_unified_background()

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

# 5. استدعاء شريط النافبار المعزول والمستقل مع حقن حزام أمان مطهر ومسار صريح
try:
    from core_layout.navbar.navbar_linker import show_navbar_section
    show_navbar_section()
except Exception:
    st.error("⚠️ هنت سيادي: عطل طارئ في منظومة شريط التحكم المركزي.")
import streamlit as st
import base64
import os
import sys

# 1. تهيئة الشاشة بالعرض الكامل فوراً كأول أمر برمي صارم
st.set_page_config(page_title="منصة المدونات الهندسية العراقية", page_icon="🇮🇶", layout="wide")

# 2. الحل القطعي لحل أزمة السيرفر: حقن المسار الجذري الفعلي للمشروع في نظام بايثون
# هذا السطر يجبر السيرفر سحابياً على قراءة كل المجلدات الفرعية كحزم نظام شرعية 100%
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 3. فرش الخلفية الموحدة وتأمين الهوية البصرية من ملف الإعدادات المحدث
from config.settings import apply_unified_background
apply_unified_background()

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

# 5. استدعاء شريط النافبار المعزول والمستقل مع حقن حزام أمان مطهر ومسار صريح
try:
    from core_layout.navbar.navbar_linker import show_navbar_section
    show_navbar_section()
except Exception:
    st.error("⚠️ هنت سيادي: عطل طارئ في منظومة شريط التحكم المركزي.")
