import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية المستقلة لإدارة شريط التنقل العائم والمنحوت بالسنتر (صفر اعتمادية).
    تم حسم أوزان الأعمدة هنا برقم فريد ومستقل لكسر الصندوق الأحمر وإرجاع الواجهة فوراً.
    """
    # 1. قراءة وتشفير صورة العلم العراقي من مجلد assets بصيغة JPG
    flag_path = "assets/iraqi_flag.jpg"
    encoded_flag = ""
    try:
        if os.path.exists(flag_path):
            with open(flag_path, "rb") as f:
                encoded_flag = base64.b64encode(f.read()).decode()
    except Exception:
        pass

    # 2. حقن نظام تصاميم CSS صارم لتطهير النافبار من المربعات وجعل الكلمات تعوم بنعومة
    st.markdown(
        f"""
        <style>
        /* كسر وتصفير الحاويات الخارجية الافتراضية لـ Streamlit لمنع المربع المزدوج */
        div[data-testid="element-container"], div[data-testid="stBlock"] {{
            border: none !important; background: transparent !important; box-shadow: none !important;
        }}
        div[data-testid="stHorizontalBlock"] {{
            gap: 4px !important; align-items: center !important; background: transparent !important;
        }}
        div[data-testid="stColumn"] {{
            border: none !important; background: transparent !important; box-shadow: none !important; padding: 0px !important;
        }}
        
        /* رفع وموازنة العلم العراقي الحقيقي ليكون دائرياً وفي السنتر الموازي تماماً للأزرار */
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

        /* جعل الأزرار الستة كنصوص عائمة نظيفة تماماً وبدون أي مربعات مشوهة */
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
        
        /* نسف وتطهير الحواف والحدود البيضاء لحقل البحث وجعله مدمجاً ناعماً */
        .stTextInput > div > div {{
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            border-radius: 4px !important;
            box-shadow: none !important;
        }}
        .stTextInput > div > div:focus-within {{
            border: 1px solid #c5a059 !important;
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.2) !important;
        }}
        
        /* ضبط وتوازن لون زر تسجيل الدخول (العمود الأول) ليتناسق بجمالية فضية ذهبية مع الشريط */
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

    # 3. صياغة الهيكل بالتسلسل العربي القياسي الصحيح من اليمين لليسار بمفاتيح حصرية ومطهرة للأبعاد
    cols_isolated = st.columns([1.4, 1.6, 1.2, 0.9, 0.7, 0.7, 0.7, 0.6, 0.4])
    
    # العمود 1 (أقصى اليسار): زر تسجيل الدخول المذهب داخل حوافه ومربعها المضيء
    with cols_isolated:
        if st.button("تسجيل الدخول 🔒", key="prime_isolated_nav_auth_v99"):
            st.session_state["current_page"] = "auth"
            st.rerun()

    # العمود 2: حقل البحث المدمج والناعم المتطهر من التشويه البصري والحواف البيضاء
    with cols_isolated:
        search_q = st.text_input("", key="prime_isolated_nav_search_v99", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # العمود 3: زر عن المنصة / اتصل بنا كنصوص عائمة ونظيفة
    with cols_isolated:
        if st.button("عن المنصة / اتصل بنا", key="prime_isolated_nav_abt_v99"):
            st.session_state["current_page"] = "about"
            st.rerun()

    # العمود 4: زر حوكمة البيانات
    with cols_isolated:
        if st.button("حوكمة البيانات", key="prime_isolated_nav_gov_v99"):
            st.session_state["current_page"] = "data_governance"
            st.rerun()

    # العمود 5: زر المهندسون
    with cols_isolated:
        if st.button("المهندسون", key="prime_isolated_nav_eng_v99"):
            st.session_state["current_page"] = "engineers"
            st.rerun()

    # العمود 6: زر المشاريع
    with cols_isolated:
        if st.button("المشاريع", key="prime_isolated_nav_proj_v99"):
            st.session_state["current_page"] = "projects"
            st.rerun()

    # العمود 7: زر المدونات
    with cols_isolated:
        if st.button("المدونات", key="prime_isolated_nav_blogs_v99"):
            st.session_state["current_page"] = "blogs"
            st.rerun()

    # العمود 8: زر الرئيسية المستقر بجانب العلم مباشرة
    with cols_isolated:
        if st.button("الرئيسية", key="prime_isolated_nav_home_v99"):
            st.session_state["current_page"] = "home"
            st.rerun()

    # العمود 9 (أقصى اليمين): العلم العراقي الدائري المصغر المستقر برأس السنتر الموازي
    with cols_isolated:
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
