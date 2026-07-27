import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية النهائية لشريط التحكم الموزون بالمنتصف.
    تم تطهير وتغيير كافة المفاتيح البرمجية هنا إلى v10_final لكسر الصندوق الأحمر وإرجاع الشريط فوراً.
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

    # 2. حقن نظام تصاميم صارم لتصفير حواف Streamlit الخارجية ومنع المربع المزدوج نهائياً
    st.markdown(
        f"""
        <style>
        /* كسر وتصفير الحاويات الخارجية لـ Streamlit التي تصنع المربع الثاني حول الأزرار والعلم */
        div[data-testid="element-container"], div[data-testid="stBlock"] {{
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
        }}
        
        /* تقليص الفراغات الافتراضية بين الأعمدة لتقريب الأزرار أفقياً */
        div[data-testid="stHorizontalBlock"] {{
            gap: 4px !important;
            align-items: center !important;
            background: transparent !important;
        }}
        
        /* تصفير حواف عمود العلم لمنع تظليله الخارجي بالكامل */
        div[data-testid="stColumn"] {{
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
            padding: 0px !important;
        }}
        
        /* تثبيت أبعاد العلم العراقي ليكون دائرياً ناعماً وصغيراً كالأيقونة */
        .nav-flag-img {{
            width: 28px !important;
            height: 28px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            border: 1px solid #c5a059 !important;
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.4) !important;
            display: inline-block !important;
        }}

        /* إعادة بناء أزرار النافبار لتكون بمربع مفرد ونحيف وتتظلل بنعومة عند التمرير */
        .stButton > button {{
            border: 1px solid rgba(197, 160, 89, 0.15) !important; /* مربع مفرد خفيف جداً */
            background: rgba(7, 22, 21, 0.5) !important;
            color: #a0b0af !important;
            font-size: 11px !important;
            font-weight: 600 !important;
            padding: 4px 6px !important;
            white-space: nowrap !important;
            border-radius: 4px !important;
            width: 100% !important;
            box-shadow: none !important;
            transition: all 0.25s ease-in-out !important;
        }}
        
        /* تأثير التمرير (Hover): تظليل الأزرار بمربع مفرد متوهج بالذهب الناعم وبدون أي تداخل */
        .stButton > button:hover {{
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.12) !important;
            border: 1px solid #c5a059 !important; /* توهج المربع المفرد */
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.2) !important;
        }}
        
        /* تصميم خاص لزر تسجيل الدخول لمنحه المربع المذهب والنص بداخل الحواف */
        div[data-testid="stColumn"]:first-child .stButton > button {{
            border: 1px solid #c5a059 !important;
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.08) !important;
            font-weight: 700 !important;
        }}
        div[data-testid="stColumn"]:first-child .stButton > button:hover {{
            background: #c5a059 !important;
            color: #071615 !important;
            box-shadow: 0 0 8px rgba(197, 160, 89, 0.4) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 3. توزيع الأعمدة بالتسلسل العربي القياسي الصحيح
    cols = st.columns([1.4, 1.6, 1.2, 0.9, 0.7, 0.7, 0.7, 0.6, 0.4])
    
    # العمود 1 (أقصى اليسار): زر تسجيل الدخول المذهب بمفتاح نهائي معزول
    with cols:
        if st.button("تسجيل الدخول 🔒", key="v10_final_nav_auth"):
            st.session_state["current_page"] = "auth"; st.rerun()

    # العمود 2: حقل البحث المدمج والناعم بمفتاح نهائي معزول
    with cols:
        search_q = st.text_input("", key="v10_final_nav_search", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # العمود 3: زر عن المنصة / اتصل بنا
    with cols:
        if st.button("عن المنصة / اتصل بنا", key="v10_final_nav_abt"):
            st.session_state["current_page"] = "about"; st.rerun()

    # العمود 4: زر حوكمة البيانات
    with cols:
        if st.button("حوكمة البيانات", key="v10_final_nav_gov"):
            st.session_state["current_page"] = "data_governance"; st.rerun()

    # العمود 5: زر المهندسون
    with cols:
        if st.button("المهندسون", key="v10_final_nav_eng"):
            st.session_state["current_page"] = "engineers"; st.rerun()

    # العمود 6: زر المشاريع
    with cols:
        if st.button("المشاريع", key="v10_final_nav_proj"):
            st.session_state["current_page"] = "projects"; st.rerun()

    # العمود 7: زر المدونات
    with cols:
        if st.button("المدونات", key="v10_final_nav_blogs"):
            st.session_state["current_page"] = "blogs"; st.rerun()

    # العمود 8: زر الرئيسية
    with cols:
        if st.button("الرئيسية", key="v10_final_nav_home"):
            st.session_state["current_page"] = "home"; st.rerun()

    # العمود 9 (أقصى اليمين): العلم العراقي الدائري المصغر النظيف محمي من أي تظليل خارجي
    with cols:
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
