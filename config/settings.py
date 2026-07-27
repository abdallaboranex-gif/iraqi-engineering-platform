import streamlit as st
import base64
import os

def apply_unified_background():
    """
    برنامج الهوية البصرية المتقدم لإزالة كافة طبقات التعتيم والحدود المزعجة،
    وجعل الكلمات والكبائن تعوم مباشرة وبفخامة فائقة فوق تفاصيل الصورة الموحدة.
    """
    image_path = "assets/main_background.jpeg"
    bg_style = ""
    
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            bg_style = f'background-image: url("data:image/jpeg;base64,{encoded_string}") !important;'
        else:
            bg_style = 'background-color: #071615 !important;'
    except Exception:
        bg_style = 'background-color: #071615 !important;'
    
    st.markdown(
        f"""
        <style>
        /* 1. فرش وتثبيت الخلفية الموحدة على كامل المتصفح */
        body, .main, .stApp, [data-testid="stAppViewContainer"] {{
            {bg_style}
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        
        /* 2. جعل الحاوية الكبرى شفافة ومخفية بالكامل (100%) لتعوم الكلمات فوق الصورة */
        .block-container {{
            max-width: 1250px !important;
            padding-top: 25px !important;
            padding-bottom: 25px !important;
            padding-left: 20px !important;
            padding-right: 20px !important;
            margin: 20px auto !important;
            background-color: transparent !important; /* إلغاء التعتيم الداكن بالكامل */
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            backdrop-filter: none !important;
        }}
        
        /* 3. إخفاء وتصفير الخطوط والعناصر الافتراضية المزعجة */
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

        /* 4. توحيد مقاسات الخطوط وحقن تظليلي أسود ناعم خلفها لتبرز وتطير بوضوح فوق الصورة */
        h1 {{ 
            font-size: 42px !important; 
            font-weight: 800 !important; 
            color: #c5a059 !important; 
            text-align: center !important;
            text-shadow: 0 0 25px rgba(197, 160, 89, 0.6), 2px 2px 4px rgba(0,0,0,0.9) !important;
            margin-top: 15px !important;
            margin-bottom: 2px !important;
        }}
        h2 {{ font-size: 18px !important; font-weight: 700 !important; color: #ffffff !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important; }} 
        h3 {{ font-size: 15px !important; font-weight: 700 !important; color: #c5a059 !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important; }} 
        h4, h5, h6 {{ font-size: 13px !important; font-weight: 600 !important; color: #ffffff !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important; }} 
        
        p, span, label, li {{ 
            font-size: 12px !important; 
            color: #ffffff !important; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            text-align: right !important;
            line-height: 1.4 !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.9) !important; /* تظليف يحمي قراءة الكلمات العائمة */
        }}

        div[data-testid="stMetricValue"] {{ font-size: 18px !important; color: #ffffff !important; font-weight: bold !important; }}

        /* 5. تنحيف الأزرار وحقول الإدخال لتكون مدمجة وراقية بالشريط */
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

        /* 6. كسر وتصفير التعتيم والحدود عن الصناديق الداخلية واللوحة الجانبية لتصبح شفافة عائمة 100% */
        div[data-testid="stColumn"] {{
            background-color: transparent !important;
            background: transparent !important;
            padding: 10px !important;
            border-radius: 0px !important;
            border: none !important;
            box-shadow: none !important;
        }}
        
        /* تجميل خاص لكروت الكبائن الأربعة لتبرز صورها الدائرية المضاءة فقط وتطير نصوصها */
        div[data-testid="stColumn"] > div[style*="background-color"] {{
            background-color: rgba(7, 22, 21, 0.4) !important; /* تعتيم خفيف جداً مقتصر على الكرت فقط */
            border: 1px solid rgba(197, 160, 89, 0.2) !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
