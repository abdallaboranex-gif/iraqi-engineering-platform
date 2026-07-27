import streamlit as st

def apply_unified_background():
    """
    برنامج الهوية البصرية المتقدم لحقن الصورة الموحدة سحابياً كخلفية ثابتة 
    ومنع ظهور اللون الأبيض الافتراضي لـ Streamlit نهائياً.
    """
    # الرابط المباشر (Raw URL) لصورتك الموحدة الحقيقية المرفوعة في مستودعك على GitHub
    image_url = "https://githubusercontent.com"
    
    st.markdown(
        f"""
        <style>
        /* 1. فرش وتثبيت الخلفية السحابية الموحدة على كامل الشاشة */
        .stApp {{
            background-image: url("{image_url}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        
        /* 2. إخفاء وتصفير العناصر البيضاء والرمادية الافتراضية لـ Streamlit */
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

        /* 3. توحيد مقاسات الخطوط والنصوص باللونين الأبيض والذهبي */
        h1 {{ 
            font-size: 46px !important; 
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
        
        div[data-testid="stMetricValue"] {{ font-size: 18px !important; color: #ffffff !important; font-weight: bold !important; }}

        /* 4. تنحيف الأزرار وحقول الإدخال لتكون مكتنزة ونحيفة */
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

        /* 5. تعتيم الصناديق لتظهر واضحة فوق تفاصيل الصورة الخلفية */
        div[data-testid="stColumn"] {{
            background-color: rgba(7, 22, 21, 0.65) !important;
            padding: 10px !important;
            border-radius: 6px !important;
            border: 1px solid rgba(197, 160, 89, 0.12) !important;
            backdrop-filter: blur(4px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
