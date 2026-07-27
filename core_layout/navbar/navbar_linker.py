import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية المستقلة لإدارة شريط التنقل وحفظه في غرفته السحابية المعزولة (صفر اعتمادية).
    تؤمن المظهر المكتنز، التظليل الناعم، وإلغاء المربعات المزدوجة والحواف البيضاء للبحث.
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

    # 2. حقن نظام تصاميم صارم لتنظيف وتطهير الشريط بالمتصفح 100% منعاً للتداخل
    st.markdown(
        f"""
        <style>
        /* كسر وتصفير الحاويات الخارجية الافتراضية لـ Streamlit لمنع المربع المزدوج */
        div[data-testid="element-container"], div[data-testid="stBlock"] {{
            border: none !important; background: transparent !important; box-shadow: none !important;
        }}
        
        /* تقليص الفراغات الافتراضية بين الأعمدة لتقريب الأزرار أفقياً وعامودياً */
        div[data-testid="stHorizontalBlock"] {{
            gap: 4px !important;
            align-items: center !important;
            background: transparent !important;
        }}
        
        /* تصفير حواف عمود العلم لمنع تظليله الخارجي */
        div[data-testid="stColumn"] {{
            border: none !important; background: transparent !important; box-shadow: none !important; padding: 0px !important;
        }}
        
        /* رفع وموازنة العلم العراقي الحقيقي ليكون دائرياً ناعماً وفي السنتر الموازي للأزرار */
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
            border: none !important; /* حذف المربع تماماً */
            background: transparent !important; /* خلفية شفافة 100% */
            color: #ffffff !important; /* لون أبيض فخم وموحد */
            font-size: 11px !important;
            font-weight: 600 !important;
            padding: 4px 6px !important;
            white-space: nowrap !important;
            border-radius: 4px !important;
            width: 100% !important;
            box-shadow: none !important;
            transition: all 0.25s ease-in-out !important;
        }}
        
        /* تأثير التمرير (Hover): تظليل بمربع مذهب زجاجي خفيف ونحيف جداً فقط عند الملامسة */
        .stButton > button:hover {{
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.1) !important;
            border: none !important;
            box-shadow: none !important;
        }}
        
        /* نسف وتطهير الحواف البيضاء المشوهة لحقل البحث ومنحه الانكماش الناعم */
        .stTextInput > div > div {{
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            border-radius: 4px !important;
            box-shadow: none !important;
        }}
        .stTextInput > div > div:focus-within {{
            border: 1px solid #c5a059 !important; /* توهج ذهبي ناعم عند التركيز والكتابة بدل البياض */
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.2) !important;
        }}
        
        /* ضبط وتوازن لون زر تسجيل الدخول (العمود الأول) ليتناسق بصرياً مع الشريط */
        div[data-testid="stColumn"]:first-child .stButton > button {{
            border: 1px solid rgba(197, 160, 89, 0.4) !important; /* إطار مفرد ناعم ومذهب */
            color: #c5a059 !important; /* لون ذهبي هادئ */
            background: rgba(13, 35, 33, 0.4) !important;
            font-weight: 700 !important;
        }}
        div[data-testid="stColumn"]:first-child .stButton > button:hover {{
            background: #c5a059 !important;
            color: #071615 !important;
            border: 1px solid #c5a059 !important;
            box-shadow: 0 0 8px rgba(197, 160, 89, 0.4) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 3. صياغة الهيكل بالتسلسل العربي القياسي المقلوب من اليمين لليسار عبر موازنة الـ app.py
    cols = st.columns([1.4, 1.6, 1.2, 0.9, 0.7, 0.7, 0.7, 0.6, 0.4])
    
    # العمود 1 (أقصى اليسار): زر تسجيل الدخول المذهب الموزون بنسخته النهائية المعزولة
    with cols:
        if st.button("تسجيل الدخول 🔒", key="final_isolated_nav_auth"):
            st.session_state["current_page"] = "auth"; st.rerun()

    # العمود 2: حقل البحث المدمج والناعم المتطهر من الحواف البيضاء
    with cols:
        search_q = st.text_input("", key="final_isolated_nav_search", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # العمود 3: زر عن المنصة / اتصل بنا
    with cols:
        if st.button("عن المنصة / اتصل بنا", key="final_isolated_nav_abt"):
            st.session_state["current_page"] = "about"; st.rerun()

    # العمود 4: زر حوكمة البيانات
    with cols:
        if st.button("حوكمة البيانات", key="final_isolated_nav_gov"):
            st.session_state["current_page"] = "data_governance"; st.rerun()

    # العمود 5: زر المهندسون
    with cols:
        if st.button("المهندسون", key="final_isolated_nav_eng"):
            st.session_state["current_page"] = "engineers"; st.rerun()

    # العمود 6: زر المشاريع
    with cols:
        if st.button("المشاريع", key="final_isolated_nav_proj"):
            st.session_state["current_page"] = "projects"; st.rerun()

    # العمود 7: زر المدونات
    with cols:
        if st.button("المدونات", key="final_isolated_nav_blogs"):
            st.session_state["current_page"] = "blogs"; st.rerun()

    # العمود 8: زر الرئيسية
    with cols:
        if st.button("الرئيسية", key="final_isolated_nav_home"):
            st.session_state["current_page"] = "home"; st.rerun()

    # العمود 9 (أقصى اليمين): العلم العراقي الدائري المصغر المستقر برأس السنتر الموازي
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
