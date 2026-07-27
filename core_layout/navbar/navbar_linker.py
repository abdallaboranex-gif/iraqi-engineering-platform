import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية المستقلة لإدارة شريط التنقل وحفظه في غرفته المعزولة (صفر اعتمادية).
    تم حل مشكلة الـ Empty Label لحقل البحث وتطهير البياض المحيط به تماماً.
    """
    # 1. قراءة وتشفير صورة العلم العراقي من مجلد assets
    flag_path = "assets/iraqi_flag.jpg"
    encoded_flag = ""
    try:
        if os.path.exists(flag_path):
            with open(flag_path, "rb") as f:
                encoded_flag = base64.b64encode(f.read()).decode()
    except Exception:
        pass

    # 2. حقن نظام تصاميم صارم لتصفير حواف Streamlit وإلغاء التشوهات البصرية وحواف البحث البيضاء
    st.markdown(
        f"""
        <style>
        /* كسر وتصفير الحاويات الخارجية الافتراضية لـ Streamlit لمنع المربع المزدوج */
        div[data-testid="element-container"], div[data-testid="stBlock"] {{
            border: none !important; background: transparent !important; box-shadow: none !important;
        }}
        
        div[data-testid="stHorizontalBlock"] {{
            gap: 4px !important;
            align-items: center !important;
            background: transparent !important;
        }}
        
        div[data-testid="stColumn"] {{
            border: none !important; background: transparent !important; box-shadow: none !important; padding: 0px !important;
        }}
        
        /* رفع وموازنة العلم العراقي الدائري الحقيقي ليصبح متناسقاً وفي السنتر المباشر */
        .nav-flag-img {{
            width: 28px !important;
            height: 28px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            border: 1px solid rgba(197, 160, 89, 0.4) !important;
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.3) !important;
            display: inline-block !important;
            margin-top: -6px !important;
        }}

        /* الأزرار الستة كنصوص عائمة نظيفة تماماً وبدون أي مربعات مشوهة */
        .stButton > button {{
            border: none !important;
            background: transparent !important;
            color: #ffffff !important;
            font-size: 11px !important;
            font-weight: 600 !important;
            padding: 4px 6px !important;
            white-space: nowrap !important;
            border-radius: 4px !important;
            width: 100% !important;
            box-shadow: none !important;
            transition: all 0.25s ease-in-out !important;
        }}
        .stButton > button:hover {{
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.1) !important;
            border: none !important;
        }}
        
        /* نسف وتطهير الحواف والحدود البيضاء المشوهة لحقل البحث وقفلها سحابياً */
        .stTextInput, .stTextInput > div, .stTextInput > div > div, .stTextInput > div > div > div {{
            border: none !important;
            background-color: transparent !important;
            background: transparent !important;
            box-shadow: none !important;
            outline: none !important;
        }}
        
        /* صياغة الصندوق الداخلي الحقيقي للبحث ليكون داكناً وبحواف مذهبة خفيفة وناعمة */
        .stTextInput input {{
            background-color: rgba(7, 22, 21, 0.85) !important;
            color: #ffffff !important;
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            border-radius: 4px !important;
            padding: 4px 10px !important;
            height: 28px !important;
            font-size: 11px !important;
            box-shadow: none !important;
            outline: none !important;
            transition: all 0.2s ease-in-out !important;
        }}
        
        /* تأثير التوهج الذهبي الناعم عند الضغط والكتابة داخل حقل البحث بدل البياض القديم */
        .stTextInput input:focus {{
            border: 1px solid #c5a059 !important;
            box-shadow: 0 0 8px rgba(197, 160, 89, 0.3) !important;
            outline: none !important;
        }}
        
        /* تصفير الحواف المحيطة بزر تسجيل الدخول ليتناسق مع الأزرار */
        div[data-testid="stColumn"]:first-child .stButton > button {{
            border: 1px solid rgba(197, 160, 89, 0.4) !important;
            color: #c5a059 !important;
            background: rgba(13, 35, 33, 0.4) !important;
            font-weight: 700 !important;
        }}
        div[data-testid="stColumn"]:first-child .stButton > button:hover {{
            background: #c5a059 !important;
            color: #071615 !important;
            border: 1px solid #c5a059 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
       # 3. صياغة الهيكل بالتسلسل العربي القياسي الصحيح من اليمين لليسار مع فرز أرقام الأعمدة هندسياً 100%
    cols_isolated = st.columns([1.4, 1.6, 1.2, 0.9, 0.7, 0.7, 0.7, 0.6, 0.4])
    
    # العمود 1 (أقصى اليسار): زر تسجيل الدخول المذهب والنحيف
    with cols_isolated[0]:
        if st.button("تسجيل الدخول 🔒", key="prime_isolated_nav_auth_v300"):
            st.session_state["current_page"] = "auth"; st.rerun()

    # العمود 2: حقل البحث المدمج والناعم المتطهر من الحواف البيضاء والـ Empty Label سحابياً
    with cols_isolated[1]:
        search_q = st.text_input("search", key="prime_isolated_nav_search_v300", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # العمود 3: زر عن المنصة / اتصل بنا
    with cols_isolated[2]:
        if st.button("عن المنصة / اتصل بنا", key="prime_isolated_nav_abt_v300"):
            st.session_state["current_page"] = "about"; st.rerun()

    # العمود 4: زر حوكمة البيانات
    with cols_isolated[3]:
        if st.button("حوكمة البيانات", key="prime_isolated_nav_gov_v300"):
            st.session_state["current_page"] = "data_governance"; st.rerun()

    # العمود 5: زر المهندسون
    with cols_isolated[4]:
        if st.button("المهندسون", key="prime_isolated_nav_eng_v300"):
            st.session_state["current_page"] = "engineers"; st.rerun()

    # العمود 6: زر المشاريع
    with cols_isolated[5]:
        if st.button("المشاريع", key="prime_isolated_nav_proj_v300"):
            st.session_state["current_page"] = "projects"; st.rerun()

    # العمود 7: زر المدونات
    with cols_isolated[6]:
        if st.button("المدونات", key="prime_isolated_nav_blogs_v300"):
            st.session_state["current_page"] = "blogs"; st.rerun()

    # العمود 8: زر الرئيسية المضاء والنظيف
    with cols_isolated[7]:
        if st.button("الرئيسية", key="prime_isolated_nav_home_v300"):
            st.session_state["current_page"] = "home"; st.rerun()

    # العمود 9 (أقصى اليمين): العلم العراقي الدائري المصغر المستقر برأس السنتر الموازي
    with cols_isolated[8]:
        if encoded_flag:
            st.markdown(
                f"""
                <div style="text-align: center; padding-top: 4px;">
                    <img class="nav-flag-img" src="data:image/jpeg;base64,{encoded_flag}">
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.markdown("<div style='font-size: 20px; text-align: center;'>🇮🇶</div>", unsafe_allow_html=True)

    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)
