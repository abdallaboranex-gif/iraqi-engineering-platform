import streamlit as st
import base64

def apply_unified_background(image_path="assets/main_background.jpeg"):
    """
    برنامج الهوية البصرية المتقدم لإصلاح واجهة المنصة، توحيد الألوان، 
    إزالة الخطوط البيضاء، وتأمين التراص الهندسي المريح للعين.
    """
    try:
        # قراءة الخلفية الموحدة وتحويلها لصيغة سريعة
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        # حقن نظام تصاميم متكامل (Custom CSS) لإعادة صياغة عناصر Streamlit الافتراضية
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
            
            /* 2. تنظيف وإخفاء الخطوط البيضاء والحواف الفاقعة المزعجة بالصورة */
            div[data-testid="stHeader"], div[data-testid="stDecoration"] {{
                background-color: transparent !important;
                background: transparent !important;
                display: none !important;
            }}
            hr {{
                border-color: rgba(197, 160, 89, 0.2) !important;
                margin-top: 5px !important;
                margin-bottom: 15px !important;
            }}

            /* 3. توحيد وتأمين النصوص باللون الأبيض والذهبي العراقي */
            h1, h2, h3, h4, h5, h6, p, span, label, li {{
                color: #ffffff !important;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
                text-align: right !important; /* توجيه النصوص للغة العربية */
            }}
            
            /* 4. تصميم الأزرار وحقول الإدخال لتندمج مع الخلفية الداكنة وتختفي خلفيتها البيضاء */
            .stButton>button {{
                background-color: rgba(13, 35, 33, 0.8) !important;
                color: #c5a059 !important;
                border: 1px solid rgba(197, 160, 89, 0.4) !important;
                border-radius: 6px !important;
                transition: all 0.3s ease;
            }}
            .stButton>button:hover {{
                background-color: #c5a059 !important;
                color: #071615 !important;
                box-shadow: 0 0 10px rgba(197, 160, 89, 0.5);
            }}
            
            /* تجميل حقول النص المدخلة للبحث والنشرة ومنع البياض */
            .stTextInput>div>div>input {{
                background-color: rgba(7, 22, 21, 0.8) !important;
                color: #ffffff !important;
                border: 1px solid rgba(197, 160, 89, 0.3) !important;
                border-radius: 6px !important;
            }}

            /* 5. تفتيح وتعتيم الصناديق البرمجة (Cards) لتفصل النصوص بوضوح عن تفاصيل الصورة الخلفية */
            div[data-testid="stColumn"] {{
                background-color: rgba(7, 22, 21, 0.6) !important;
                padding: 15px !important;
                border-radius: 10px !important;
                border: 1px solid rgba(197, 160, 89, 0.15) !important;
                backdrop-filter: blur(5px); /* تأثير الضبابية الزجاجية الفخم */
            }}
            
            /* منع تداخل التبويبات الداخلية في الجامعات والنشرة */
            .stTabs button {{
                color: #ffffff !important;
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
        # حزام الأمان للحماية من أي نقص
        st.markdown("<style>.stApp {background-color: #071615 !important;}</style>", unsafe_allow_html=True)
