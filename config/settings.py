import streamlit as st
import base64

def apply_unified_background(image_path="assets/main_background.jpeg"):
    """
    برنامج الهوية البصرية المتقدم لتصغير الكلمات، توحيد الألوان، 
    ومنع تداخل العناصر لضمان تراص هندسي احترافي.
    """
    try:
        # قراءة الخلفية الموحدة وتحويلها لصيغة سريعة
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        # حقن نظام تصاميم متكامل (Custom CSS) لإعادة صياغة حجوم كلمات عناصر Streamlit
        st.markdown(
            f"""
            <style>
            /* 1. فرش الخلفية وتأمين ثباتها */
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            
           /* تجميل الصناديق الزجاجية وضبط نصوص اللوحة الجانبية والمحتوى بشكل منفصل */
div[data-testid="stColumn"] {
    background-color: rgba(7, 22, 21, 0.65) !important;
    padding: 10px !important;
    border-radius: 6px !important;
    border: 1px solid rgba(197, 160, 89, 0.12) !important;
    backdrop-filter: blur(4px);
}
            /* 3. تصغير حجوم الكلمات والنصوص لمنع التداخل والتشتت */
            h1 {{ font-size: 38px !important; font-weight: 800 !important; color: #c5a059 !important; text-align: center !important; }} /* العنوان المضاء */
            h2 {{ font-size: 20px !important; font-weight: 700 !important; color: #ffffff !important; }} /* عناوين الأقسام */
            h3 {{ font-size: 16px !important; font-weight: 700 !important; color: #c5a059 !important; }} /* المؤشرات الجانبية */
            h4, h5, h6 {{ font-size: 14px !important; font-weight: 600 !important; color: #ffffff !important; }} /* عناوين الكبائن والمقالات */
            p, span, label, li {{ 
                font-size: 12px !important; 
                color: #ffffff !important; 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
                text-align: right !important; /* توجيه النصوص للغة العربية */
                line-height: 1.4 !important;
            }}
            
            /* تصغير حجم خط الأعداد الكبيرة في لوحة المؤشرات (Metrics) */
            div[data-testid="stMetricValue"] {{
                font-size: 20px !important;
                color: #ffffff !important;
                font-weight: bold !important;
            }}
            div[data-testid="stMetricDelta"] {{
                font-size: 11px !important;
            }}

            /* 4. تصميم الأزرار وحقول الإدخال لتكون ناعمة ومدمجة وبخط مصغر */
            .stButton>button {{
                background-color: rgba(13, 35, 33, 0.85) !important;
                color: #c5a059 !important;
                border: 1px solid rgba(197, 160, 89, 0.3) !important;
                border-radius: 5px !important;
                font-size: 11px !important; /* تصغير خط كلمات الأزرار */
                padding: 4px 6px !important;
                transition: all 0.3s ease;
            }}
            .stButton>button:hover {{
                background-color: #c5a059 !important;
                color: #071615 !important;
                box-shadow: 0 0 8px rgba(197, 160, 89, 0.4);
            }}
            
            /* تجميل حقول النص المدخلة للبحث والنشرة بخط مصغر مريح */
            .stTextInput>div>div>input {{
                background-color: rgba(7, 22, 21, 0.8) !important;
                color: #ffffff !important;
                border: 1px solid rgba(197, 160, 89, 0.25) !important;
                border-radius: 5px !important;
                font-size: 12px !important;
                padding: 6px !important;
            }}

            /* 5. تعتيم الصناديق الزجاجية (Cards) وضبط أبعادها لتقليل المساحات البيضاء */
            div[data-testid="stColumn"] {{
                background-color: rgba(7, 22, 21, 0.65) !important;
                padding: 12px !important;
                border-radius: 8px !important;
                border: 1px solid rgba(197, 160, 89, 0.12) !important;
                backdrop-filter: blur(4px); /* تأثير الضبابية الزجاجية */
            }}
            
            /* تجميل تبويبات البحوث المتقاربة */
            .stTabs button {{
                color: #ffffff !important;
                font-size: 12px !important;
            }}
            .stTabs button[aria-selected="true"] {{
                color: #c5a059 !important;
                border-bottom-color: #c5a059 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        pass
