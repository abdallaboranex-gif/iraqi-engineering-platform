import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية لشريط التنقل بعد حذف كلمة INCP 
    ليبقى العلم العراقي الدائري بمفرده وبشكل سيادي ونظيف في اليمين.
    """
    # 1. قراءة وتشفير صورة العلم العراقي من مجلد assets
    flag_path = "assets/iraqi_flag.jpg"
    encoded_flag = ""
    if os.path.exists(flag_path):
        with open(flag_path, "rb") as f:
            encoded_flag = base64.b64encode(f.read()).decode()

    # 2. حقن نظام تصاميم محكم لتقييد حجم العلم وتجميل الأزرار النحيفة
    st.markdown(
        f"""
        <style>
        /* تثبيت أبعاد العلم العراقي الحقيقي ليكون دائرياً ناعماً وصغيراً */
        .nav-flag-img {{
            width: 32px !important;
            height: 32px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            border: 1px solid #c5a059 !important;
            box-shadow: 0 0 8px rgba(197, 160, 89, 0.4) !important;
            display: inline-block !important;
            vertical-align: middle !important;
        }}

        /* تصفير وإغلاق الفراغات الحشوية الافتراضية لـ Streamlit بالكامل لتقريب الأزرار */
        div[data-testid="stHorizontalBlock"] {{
            gap: 2px !important;
            align-items: center !important;
        }}
        div[data-testid="stColumn"] {{
            background-color: transparent !important;
            border: none !important;
            padding: 0px !important;
            box-shadow: none !important;
            backdrop-filter: none !important;
        }}
        
        /* إعادة تصميم أزرار النافبار لتكون نحيفة جداً وشفافة وبخط صغير */
        .stButton > button {{
            border: none !important;
            background: rgba(7, 22, 21, 0.6) !important;
            color: #a0b0af !important;
            font-size: 11px !important;
            font-weight: 600 !important;
            padding: 4px 6px !important;
            white-space: nowrap !important;
            border-radius: 4px !important;
            width: 100% !important;
            transition: all 0.2s ease !important;
        }}
        .stButton > button:hover {{
            color: #c5a059 !important;
            background: rgba(197, 160, 89, 0.1) !important;
            border: none !important;
            box-shadow: none !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 3. صياغة الهيكل الموزع أفقياً بأبعاد مقربة ومحاذاة ممتازة بعد حذف العبارة
    cols = st.columns([0.4, 0.6, 0.6, 0.6, 0.7, 0.8, 1.2, 1.5, 0.9])
    
    # العمود 1 (أقصى اليمين): العلم الدائري المصغر بمفرده ونظيف تماماً
    with cols:
        st.markdown(
            f"""
            <div style="text-align: right; white-space: nowrap; padding-top: 5px;">
                <img class="nav-flag-img" src="data:image/jpeg;base64,{encoded_flag}">
            </div>
            """, 
            unsafe_allow_html=True
        )

    # العمود 2: زر الرئيسية
    with cols:
        if st.button("الرئيسية", key="nav_home_v5"):
            st.session_state["current_page"] = "home"; st.rerun()

    # العمود 3: زر المدونات
    with cols:
        if st.button("المدونات", key="nav_blogs_v5"):
            st.session_state["current_page"] = "blogs"; st.rerun()

    # العمود 4: زر المشاريع
    with cols:
        if st.button("المشاريع", key="nav_proj_v5"):
            st.session_state["current_page"] = "projects"; st.rerun()

    # العمود 5: زر المهندسون
    with cols:
        if st.button("المهندسون", key="nav_eng_v5"):
            st.session_state["current_page"] = "engineers"; st.rerun()

    # العمود 6: زر حوكمة البيانات
    with cols:
        if st.button("حوكمة البيانات", key="nav_gov_v5"):
            st.session_state["current_page"] = "data_governance"; st.rerun()

    # العمود 7: زر عن المنصة / اتصل بنا
    with cols:
        if st.button("عن المنصة / اتصل بنا", key="nav_abt_v5"):
            st.session_state["current_page"] = "about"; st.rerun()

    # العمود 8: خانة البحث المدمجة المجاورة للأزرار
    with cols:
        search_q = st.text_input("", key="nav_search_v5", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # العمود 9 (أقصى اليسار): بوابة تسجيل الدخول المذهبة النحيفة
    with cols:
        if st.button("🔒 دخول", key="nav_auth_v5"):
            st.session_state["current_page"] = "auth"; st.rerun()

    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)
