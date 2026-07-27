import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية المصلحة والنهائية لشريط التحكم الموزون بالمنتصف.
    تم تأمين الكود برمجياً لمنع التداخل والتعارض مع سيرفر الاستضافة وإعادة الشريط فوراً.
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

    # 2. حقن نظام تصاميم محكم لتصغير الأزرار وتقريبها ومنع تمددها المفرط
    st.markdown(
        f"""
        <style>
        /* تقليص الفراغات الافتراضية لـ Streamlit بين الأعمدة لتقريب الأزرار أفقياً */
        div[data-testid="stHorizontalBlock"] {{
            gap: 4px !important;
            align-items: center !important;
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

        /* تنحيف أزرار النافبار بالكامل وجعل خطوطها مدمجة */
        .stButton > button {{
            border: none !important;
            background: rgba(7, 22, 21, 0.6) !important;
            color: #a0b0af !important;
            font-size: 11px !important;
            font-weight: 600 !important;
            padding: 3px 5px !important;
            white-space: nowrap !important;
            border-radius: 4px !important;
            width: 100% !important;
            transition: all 0.2s ease !important;
        }}
        .stButton > button:hover {{
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.1) !important;
        }}
        
        /* تجميل خاص لزر تسجيل الدخول لمنحه المربع المذهب والنص بداخل الحواف */
        div[data-testid="stColumn"]:first-child .stButton > button {{
            border: 1px solid #c5a059 !important;
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.08) !important;
            font-weight: 700 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 3. توزيع الأعمدة بالتسلسل العربي الصحيح المتناسق والمحسوب بدقة هندسية للأبعاد:
    # بدأنا بتسجيل الدخول باليسار (العمود الأول بوزن 1.3 ليستقر النص بداخله)، يليه البحث، الأزرار، وينتهي بالعلم باليمين (الوزن 0.4)
    cols = st.columns([1.3, 1.6, 1.2, 0.9, 0.7, 0.7, 0.7, 0.6, 0.4])
    
    # العمود 1 (أقصى اليسار): زر تسجيل الدخول المذهب والنحيف (مستقر ومستوعب النص 100%)
    with cols[0]:
        if st.button("تسجيل الدخول 🔒", key="nav_auth_f1"):
            st.session_state["current_page"] = "auth"; st.rerun()

    # العمود 2: حقل البحث المدمج والناعم
    with cols[1]:
        search_q = st.text_input("", key="nav_search_f1", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # العمود 3: زر عن المنصة / اتصل بنا
    with cols[2]:
        if st.button("عن المنصة / اتصل بنا", key="nav_abt_f1"):
            st.session_state["current_page"] = "about"; st.rerun()

    # العمود 4: زر حوكمة البيانات
    with cols[3]:
        if st.button("حوكمة البيانات", key="nav_gov_f1"):
            st.session_state["current_page"] = "data_governance"; st.rerun()

    # العمود 5: زر المهندسون
    with cols[4]:
        if st.button("المهندسون", key="nav_eng_f1"):
            st.session_state["current_page"] = "engineers"; st.rerun()

    # العمود 6: زر المشاريع
    with cols[5]:
        if st.button("المشاريع", key="nav_proj_f1"):
            st.session_state["current_page"] = "projects"; st.rerun()

    # العمود 7: زر المدونات
    with cols[6]:
        if st.button("المدونات", key="nav_blogs_f1"):
            st.session_state["current_page"] = "blogs"; st.rerun()

    # العمود 8: زر الرئيسية
    with cols[7]:
        if st.button("الرئيسية", key="nav_home_f1"):
            st.session_state["current_page"] = "home"; st.rerun()

    # العمود 9 (أقصى اليمين): العلم العراقي الدائري المصغر النظيف والسيادي بمفرده
    with cols[8]:
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
            st.markdown("<div style='font-size: 20px; text-align: center;'> </div>", unsafe_allow_html=True)

    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)
