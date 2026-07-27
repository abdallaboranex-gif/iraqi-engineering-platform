import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية المستقلة لإدارة شريط التنقل وحفظه في غرفته المعزولة (صفر اعتمادية).
    تم تصحيح الأقواس المتعرجة، وتصحيح معرّف stColumn، وفرز أرقام الأعمدة هندسياً 100%.
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

    # 2. حقن نظام تصاميم محكم ومطهر لتصفير حواف Streamlit وإلغاء المربع المزدوج والتشوهات البصرية
    st.markdown(
        f"""
        <style>
        /* كسر وتصفير الحاويات الخارجية الافتراضية لـ Streamlit لمنع المربع المزدوج */
        div[data-testid="element-container"], div[data-testid="stBlock"] {{
            border: none !important; background: transparent !important; box-shadow: none !important;
        }}
        
        /* إصلاح الخلل الأول: مضاعفة الأقواس المتعرجة لحاوية الـ stHorizontalBlock ليفهمها المتصفح بأمان */
        div[data-testid="stHorizontalBlock"] {{
            gap: 4px !important;
            align-items: center !important;
            background: transparent !important;
        }}
        
        div[data-testid="stColumn"] {{
            border: none !important; background: transparent !important; box-shadow: none !important; padding: 0px !important;
        }}
        
        /* رفع وموازنة العلم العراقي الدائري الحقيقي ليصبح في السنتر المباشر الموازي للأزرار */
        .nav-flag-img {{
            width: 28px !important;
            height: 28px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            border: 1px solid rgba(197, 160, 89, 0.4) !important;
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.3) !important;
            display: inline-block !important;
            margin-top: -6px !important; /* رفعه بضعة بكسلات للسنتر */
        }}

        /* إعادة بناء الأزرار الستة لتبدو كنصوص عائمة نظيفة تماماً وبدون أي مربعات مشوهة */
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
        
        /* نسف وتطهير الحواف والحدود البيضاء المشوهة لحقل البحث */
        .stTextInput > div > div {{
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            border-radius: 4px !important;
            box-shadow: none !important;
        }}
        .stTextInput > div > div:focus-within {{
            border: 1px solid #c5a059 !important;
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.2) !important;
        }}
        
        /* إصلاح الخلل الثاني: تعديل حرف testId ليصبح testid بحرف صغير ليتنحّف زر تسجيل الدخول */
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
        div[data-testid="stColumn"]:first-child .stButton > button:active {{
            background: transparent !important;
            color: #c5a059 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    # 3. صياغة الهيكل بالتسلسل العربي الصحيح من اليمين لليسار مع فرز أرقام الأعمدة هندسياً 100%
    cols_isolated = st.columns([1.4, 1.6, 1.2, 0.9, 0.7, 0.7, 0.7, 0.6, 0.4])
    
    # العمود 1 (الفهرس 0 - أقصى اليسار): زر تسجيل الدخول المذهب والنحيف داخل غرفته المحددة
    with cols_isolated[0]:
        if st.button("تسجيل الدخول 🔒", key="prime_isolated_nav_auth_v100"):
            st.session_state["current_page"] = "auth"; st.rerun()

    # العمود 2 (الفهرس 1): حقل البحث المدمج والناعم المتطهر من الحواف البيضاء المشوهة
    with cols_isolated[1]:
        search_q = st.text_input("", key="prime_isolated_nav_search_v100", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # العمود 3 (الفهرس 2): زر عن المنصة / اتصل بنا
    with cols_isolated[2]:
        if st.button("عن المنصة / اتصل بنا", key="prime_isolated_nav_abt_v100"):
            st.session_state["current_page"] = "about"; st.rerun()

    # العمود 4 (الفهرس 3): زر حوكمة البيانات
    with cols_isolated[3]:
        if st.button("حوكمة البيانات", key="prime_isolated_nav_gov_v100"):
            st.session_state["current_page"] = "data_governance"; st.rerun()

    # العمود 5 (الفهرس 4): زر المهندسون
    with cols_isolated[4]:
        if st.button("المهندسون", key="prime_isolated_nav_eng_v100"):
            st.session_state["current_page"] = "engineers"; st.rerun()

    # العمود 6 (الفهرس 5): زر المشاريع
    with cols_isolated[5]:
        if st.button("المشاريع", key="prime_isolated_nav_proj_v100"):
            st.session_state["current_page"] = "projects"; st.rerun()

    # العمود 7 (الفهرس 6): زر المدونات
    with cols_isolated[6]:
        if st.button("المدونات", key="prime_isolated_nav_blogs_v100"):
            st.session_state["current_page"] = "blogs"; st.rerun()

    # العمود 8 (الفهرس 7): زر الرئيسية المضاء والنظيف
    with cols_isolated[7]:
        if st.button("الرئيسية", key="prime_isolated_nav_home_v100"):
            st.session_state["current_page"] = "home"; st.rerun()

    # العمود 9 (الفهرس 8 - أقصى اليمين): العلم العراقي الدائري المصغر المستقر برأس السنتر الموازي
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
