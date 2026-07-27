import streamlit as st
import base64

def apply_unified_background(image_path="assets/main_background.jpeg"):
    """
    برنامج مستقل ومحصن لفرش الصورة الموحدة كخلفية ثابتة 
    لكل واجهات المنصة بصيغة JPEG مع ضبط الألوان والنصوص (صفر اعتمادية).
    """
    try:
        # قراءة الصورة وتحويلها إلى صيغة base64 لتعمل داخل المتصفح فوراً وبأعلى سرعة
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        # حقن كود CSS مخصص لتثبيت الخلفية الموحدة وضبط هوية المنصة البصرية
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            /* توحيد ألوان النصوص الأساسية داخل المنصة */
            h1, h2, h3, p, span, label {{
                color: #ffffff !important;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            /* إعطاء تلميح خفيف للبطاقات لتناسب التباين والخطوط الذهبية */
            .stMarkdown div div {{
                color: #ffffff;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        # حزام الأمان: في حال عدم رفع ملف الصورة بعد أو فقدانه، لا ينهار البرنامج!
        # بل يتحول تلقائياً إلى الخلفية الداكنة الافتراضية مع إظهار هنت خفيف للصيانة
        st.markdown(
            """
            <style>
            .stApp {{
                background-color: #071615 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.sidebar.warning("⚠️ هنت: جاري تحديث ملفات الهوية البصرية والخلفية الموحدة حالياً.")
