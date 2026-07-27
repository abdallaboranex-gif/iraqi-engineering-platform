import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية الحاسمة والمطابقة 100% للصورة القياسية.
    توازن شريط التحكم بالمنتصف، وتوسع صندوق زر تسجيل الدخول لإعادة النص داخل المربع المذهب.
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

    # 2. حقن نظام تصاميم صارم لتأمين موازنة الشريط في المنتصف وتنحيف الأزرار
    st.markdown(
        f"""
        <style>
        /* الحل الجذري لموازنة الشريط: تحديد حد أقصى للعرض وحصره في منتصف الشاشة تلقائياً */
        div[data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row-reverse !important; /* قلب الصف كاملاً لتبدأ الأزرار من اليمين */
            gap: 4px !important;
            align-items: center !important;
            max-width: 90% !important; /* تقليص امتداد الشريط ليصبح ملموماً وموزوناً بالمنتصف */
            margin: 0 auto !important; /* حصر الحاوية في السنتر المباشر للشاشة */
            background: rgba(7, 22, 21, 0.4) !important; /* إعطاء لمحة تظليل خلفية خفيفة للشريط */
            padding: 4px 10px !important;
            border-radius: 6px !important;
        }}
        
        /* تثبيت أبعاد العلم العراقي الدائري المصغر النظيف */
        .nav-flag-img {{
            width: 30px !important;
            height: 30px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            border: 1px solid #c5a059 !important;
            box-shadow: 0 0 8px rgba(197, 160, 89, 0.4) !important;
            display: inline-block !important;
            vertical-align: middle !important;
        }}

        div[data-testid="stColumn"] {{
            background-color: transparent !important;
            border: none !important;
            padding: 0px !important;
            box-shadow: none !important;
            backdrop-filter: none !important;
        }}
        
        /* إعادة صياغة مظهر الأزرار لتكون نحيفة ومدمجة ومستقرة تماماً */
        .stButton > button {{
            border: none !important;
            background: rgba(7, 22, 21, 0.6) !important;
            color: #a0b0af !important;
            font-size: 11px !important;
            font-weight: 600 !important;
            padding: 4px 6px !important;
            white-space: nowrap !important; /* منع كسر أو نزول النص لسطر جديد */
            border-radius: 4px !important;
            width: 100% !important;
            transition: all 0.2s ease !important;
        }}
        
        /* تصميم خاص لزر تسجيل الدخول لمنحه التوهج المذهب الفخم المربع المضاء كالأصل */
        div[data-testid="stColumn"]:last-child .stButton > button {{
            border: 1px solid #c5a059 !important;
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.08) !important;
            font-weight: 700 !important;
        }}
        
        .stButton > button:hover {{
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.1) !important;
            box-shadow: none !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 3. صياغة التوزيع الهندسي للأعمدة (تم تكبير وتوسيع وزن العمود الأخير لزر التسجيل من 0.9 إلى 1.4 ليستوعب الكلمة بالداخل)
    cols = st.columns([0.4, 0.6, 0.6, 0.6, 0.7, 0.8, 1.2, 1.5, 1.4])
    
    # العمود 1 (يمين الشاشة): العلم الدائري المصغر المستقر بفخامة
    with cols:
        if encoded_flag:
            st.markdown(
                f"""
                <div style="text-align: right; padding-top: 5px;">
                    <img class="nav-flag-img" src="data:image/jpeg;base64,{encoded_flag}">
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.markdown("<div style='font-size: 22px; text-align: right;'>🇮🇶</div>", unsafe_allow_html=True)

    # الأزرار الوسطية المتراصة بانتظام خلف العلم مباشرة ومتجهة يساراً
    with cols:
        if st.button("الرئيسية", key="nav_home_final_v7"):
            st.session_state["current_page"] = "home"; st.rerun()

    with cols:
        if st.button("المدونات", key="nav_blogs_final_v7"):
            st.session_state["current_page"] = "blogs"; st.rerun()

    with cols:
        if st.button("المشاريع", key="nav_proj_final_v7"):
            st.session_state["current_page"] = "projects"; st.rerun()

    with cols:
        if st.button("المهندسون", key="nav_eng_final_v7"):
            st.session_state["current_page"] = "engineers"; st.rerun()

    with cols:
        if st.button("حوكمة البيانات", key="nav_gov_final_v7"):
            st.session_state["current_page"] = "data_governance"; st.rerun()

    with cols:
        if st.button("عن المنصة / اتصل بنا", key="nav_abt_final_v7"):
            st.session_state["current_page"] = "about"; st.rerun()

    # حقل البحث المدمج والناعم
    with cols:
        search_q = st.text_input("", key="nav_search_final_v7", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # العمود 9 (أقصى اليسار): بوابة تسجيل الدخول (تم تعديل النص وتوسيع المربع ليستقر بالداخل 100%)
    with cols:
        if st.button("تسجيل الدخول 🔒", key="nav_auth_final_v7"):
            st.session_state["current_page"] = "auth"; st.rerun()

    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)
