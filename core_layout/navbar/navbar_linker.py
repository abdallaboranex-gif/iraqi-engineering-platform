import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية المصلحة والنهائية لبناء شريط تنقل متراص ومدمج.
    تستخدم ميزة row-reverse لإجبار المتصفح على قلب الترتيب من اليمين لليسار 100%.
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

    # 2. حقن نظام تصاميم صارم يجبر العناصر على الانقالب والتراص من اليمين لليسار
    st.markdown(
        f"""
        <style>
        /* الحل الجذري: قلب اتجاه صف الأعمدة بالكامل لتبدأ من اليمين 100% */
        div[data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row-reverse !important; /* قلب الصف كاملاً بصرياً بالمتصفح */
            gap: 2px !important;
            align-items: center !important;
        }}
        
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

        div[data-testid="stColumn"] {{
            background-color: transparent !important;
            border: none !important;
            padding: 0px !important;
            box-shadow: none !important;
            backdrop-filter: none !important;
        }}
        
        /* إعادة تصميم أزرار النافبار لتكون نحيفة جداً وشفافة وبخط صغير مدمج */
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

    # 3. صياغة الهيكل بالتسلسل البرمجي (المتصفح سيقوم بقلبه تلقائياً بفضل كود الـ CSS أعلاه)
    # نكتب الترتيب هنا طبيعياً، وحقنة الـ row-reverse ستجعل العمود الأول يطير لأقصى اليمين والتاسع لأقصى اليسار
    cols = st.columns([0.5, 0.6, 0.6, 0.6, 0.7, 0.8, 1.2, 1.5, 0.9])
    
    # هذا العمود سيطير برمشة عين ليستقر في أقصى اليمين (العلم النظيف)
    with cols[0]:
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

    # الأزرار الوسطية ستترتب بانتظام خلف العلم مباشرة وتتجه يساراً
    with cols[1]:
        if st.button("الرئيسية", key="nav_home_final_v6"):
            st.session_state["current_page"] = "home"; st.rerun()

    with cols[2]:
        if st.button("المدونات", key="nav_blogs_final_v6"):
            st.session_state["current_page"] = "blogs"; st.rerun()

    with cols[3]:
        if st.button("المشاريع", key="nav_proj_final_v6"):
            st.session_state["current_page"] = "projects"; st.rerun()

    with cols[4]:
        if st.button("المهندسون", key="nav_eng_final_v6"):
            st.session_state["current_page"] = "engineers"; st.rerun()

    with cols[5]:
        if st.button("حوكمة البيانات", key="nav_gov_final_v6"):
            st.session_state["current_page"] = "data_governance"; st.rerun()

    with cols[6]:
        if st.button("عن المنصة / اتصل بنا", key="nav_abt_final_v6"):
            st.session_state["current_page"] = "about"; st.rerun()

    # حقل البحث المدمج
    with cols[7]:
        search_q = st.text_input("", key="nav_search_final_v6", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
        if search_q:
            st.session_state["search_trigger"] = search_q

    # هذا العمود سيطير ليستقر في أقصى اليسار (بوابة الدخول)
    with cols[8]:
        if st.button("🔒 دخول", key="nav_auth_final_v6"):
            st.session_state["current_page"] = "auth"; st.rerun()

    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)
