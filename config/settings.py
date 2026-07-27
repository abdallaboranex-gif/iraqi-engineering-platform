import streamlit as st
import base64
import os

def apply_unified_background():
    """
    برنامج الهوية البصرية النهائي المعتمد لقراءة ملف الصورة محلياً من مجلد assets
    وتحويله برمجياً بصيغة Base64 لتخطي حجب المتصفحات وفرش الخلفية الموحدة فوراً.
    """
    # تحديد مسار ملف صورتك الموحدة الحقيقية داخل المجلد التابع للمشروع
    image_path = "assets/main_background.jpeg"
    bg_style = ""
    
    try:
        if os.path.exists(image_path):
            # قراءة الصورة وتحويلها فوراً إلى صيغة مشفرة يتقبلها المتصفح بدون جدران حماية
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            bg_style = f'background-image: url("data:image/jpeg;base64,{encoded_string}") !important;'
        else:
            # حزام أمان داكن في حال عدم تطابق اسم الملف
            bg_style = 'background-color: #071615 !important;'
    except Exception:
        bg_style = 'background-color: #071615 !important;'
    
    st.markdown(
        f"""
        <style>
        /* 1. فرش وتثبيت الخلفية الموحدة المشفرة على كامل الجسد الخارجي والداخلي للمتصفح */
        body, .main, .stApp, [data-testid="stAppViewContainer"] {{
            {bg_style}
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        
        /* 2. حماية التوازن الهندسي الملموم بالمنتصف وجعل الحاوية زجاجية شفافة لتمرير تفاصيل الصورة */
        .block-container {{
            max-width: 1250px !important; /* قفل أبعاد العرض لمنع التمطيط والسحب */
            padding-top: 25px !important;
            padding-bottom: 25px !important;
            padding-left: 20px !important;
            padding-right: 20px !important;
            margin: 40px auto !important; /* موازنة الصندوق في السنتر المباشر للشاشة */
            background-color: rgba(7, 22, 21, 0.78) !important; /* تعتيم زجاجي داكن مريح جداً للقراءة */
            border-radius: 12px !important;
            box-shadow: 0 15px 50px rgba(0,0,0,0.8) !important;
            backdrop-filter: blur(8px) !important; /* تأثير الضبابية الزجاجية الفخم */
            border: 1px solid rgba(197, 160, 89, 0.18) !important;
        }}
        
        /* 3. إخفاء وتصفير العناصر والخطوط الافتراضية المزعجة لـ Streamlit */
        div[data-testid="stHeader"], div[data-testid="stDecoration"] {{
            background-color: transparent !important;
            background: transparent !important;
            display: none !important;
        }}
        hr {{
            border-color: rgba(197, 160, 89, 0.15) !important;
            margin-top: 5px !important;
            margin-bottom: 10px !important;
        }}

        /* 4. توحيد مقاسات وألوان الخطوط داخل الحاوية الزجاجية */
        h1 {{ 
            font-size: 42px !important; 
            font-weight: 800 !important; 
            color: #c5a059 !important; 
            text-align: center !important;
            text-shadow: 0 0 25px rgba(197, 160, 89, 0.6) !important;
            margin-top: 15px !important;
            margin-bottom: 2px !important;
        }}
        h2 {{ font-size: 18px !important; font-weight: 700 !important; color: #ffffff !important; }} 
        h3 {{ font-size: 15px !important; font-weight: 700 !important; color: #c5a059 !important; }} 
        h4, h5, h6 {{ font-size: 13px !important; font-weight: 600 !important; color: #ffffff !important; }} 
        
        p, span, label, li {{ 
            font-size: 12px !important; 
            color: #ffffff !important; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            text-align: right !important;
            line-height: 1.4 !important;
        }}

        /* 5. تنحيف الأزرار وحقول الإدخال لتكون مدمجة ومصطفة */
        .stButton>button {{
            background-color: rgba(13, 35, 33, 0.85) !important;
            color: #c5a059 !important;
            border: 1px solid rgba(197, 160, 89, 0.3) !important;
            border-radius: 4px !important;
            font-size: 11px !important; 
            padding: 2px 6px !important; 
            min-height: 26px !important; 
            line-height: 1.2 !important;
            transition: all 0.2s ease;
        }}
        .stButton>button:hover {{
            background-color: #c5a059 !important;
            color: #071615 !important;
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.4);
        }}
        
        .stTextInput>div>div>input {{
            background-color: rgba(7, 22, 21, 0.8) !important;
            color: #ffffff !important;
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            border-radius: 4px !important;
            font-size: 11px !important;
            padding: 4px 8px !important; 
            height: 28px !important; 
        }}

        /* 6. تعتيم الصناديق الداخلية (Cards) لتنفصل بوضوح */
        div[data-testid="stColumn"] {{
            background-color: rgba(7, 22, 21, 0.45) !important;
            padding: 10px !important;
            border-radius: 6px !important;
            border: 1px solid rgba(197, 160, 89, 0.12) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
