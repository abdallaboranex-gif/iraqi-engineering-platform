import streamlit as st
import base64
import os

def show_navbar_section():
    """
    الدالة المركزية المطورة لبناء شريط تنقل متراص ومدمج أفقياً يحاكي الصورة القياسية تماماً.
    تم تحديث مسار العلم هنا ليقرأ الامتداد الحقيقي iraq_flag.jpg بنجاح وصفر اعتمادية.
    """
    # 1. قراءة وتشفير صورة العلم العراقي الحقيقية المرفوعة بصيغة JPG
    flag_path = "assets/iraqi_flag.jpg"
    encoded_flag = ""
    if os.path.exists(flag_path):
        with open(flag_path, "rb") as f:
            encoded_flag = base64.b64encode(f.read()).decode()

    # 2. حقن هندسة التصميم المتقدمة للتحكم الدقيق بالمسافات والأبعاد وتصغير الأزرار
    st.markdown(
        f"""
        <link rel="stylesheet" href="https://cloudflare.com">
        <style>
        /* إنشاء حاوية مرنة ومدمجة تجمع كل العناصر متراصة في سطر واحد */
        .custom-navbar {{
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            background-color: rgba(7, 22, 21, 0.85) !important;
            padding: 6px 16px !important;
            border-radius: 8px !important;
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            direction: rtl !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4) !important;
            margin-bottom: 15px !important;
        }}
        
        /* تجميع أزرار القائمة والعلم والشعار متراصين ومقربين جداً باليمين */
        .nav-right-block {{
            display: flex !important;
            align-items: center !important;
            gap: 10px !important; /* مسافات صغيرة ومحكومة بكسلياً بين العناصر */
        }}
        
        /* العلم العراقي الدائري الحقيقي والمضاء */
        .nav-flag {{
            width: 24px !important;
            height: 24px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            border: 1px solid #c5a059 !important;
            box-shadow: 0 0 6px rgba(197, 160, 89, 0.4) !important;
        }}
        
        /* الشعار والبحث المدمج */
        .nav-logo {{
            font-size: 14px !important;
            font-weight: 700 !important;
            color: #c5a059 !important;
            letter-spacing: 0.5px !important;
        }}
        
        /* تجميع الأزرار الستة الوسطية متراصة ومقربة بدون أي فراغات عمودية */
        .nav-center-menu {{
            display: flex !important;
            align-items: center !important;
            gap: 15px !important;
        }}
        
        /* تصفير وإعادة تشكيل تصميم أزرار Streamlit داخل حاوية النافبار لتبدو نبيلة ونحيفة */
        div[data-testid="stHorizontalBlock"] {{
            gap: 0px !important; /* إغلاق فراغات الأعمدة الافتراضية لـ Streamlit واكتناز الأبعاد */
        }}
        .stButton > button {{
            border: none !important;
            background: transparent !important;
            color: #a0b0af !important;
            font-size: 12px !important;
            font-weight: 600 !important;
            padding: 2px 4px !important;
            white-space: nowrap !important;
            transition: color 0.2s ease !important;
        }}
        .stButton > button:hover {{
            color: #c5a059 !important;
            background: transparent !important;
            box-shadow: none !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 3. صياغة الهيكل البصري المدمج بنظام توزيع الأعمدة المقربة (الأبعاد المكتنزة)
    col_nav = st.columns([1.2, 5.0, 1.0])
    
    # العمود الأيمن المتراص (العلم الحقيقي المرفوع، الشعار، والبرجر)
    with col_nav[0]:
        st.markdown(
            f"""
            <div class="nav-right-block">
                <i class="fa-solid fa-bars" style="color: #a0b0af; cursor: pointer; font-size: 14px;"></i>
                <img class="nav-flag" src="data:image/jpeg;base64,{encoded_flag}">
                <span class="nav-logo">INCP</span>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # العمود الأوسط المدمج (تقريب مسافات أزرار التنقل وحقل الاستعلام)
    with col_nav[1]:
        sub_cols = st.columns([0.6, 0.7, 0.7, 0.7, 1.0, 1.3, 1.8])
        with sub_cols[0]:
            if st.button("الرئيسية", key="nav_home_new"):
                st.session_state["current_page"] = "home"; st.rerun()
        with sub_cols[1]:
            if st.button("المدونات", key="nav_blogs_new"):
                st.session_state["current_page"] = "blogs"; st.rerun()
        with sub_cols[2]:
            if st.button("المشاريع", key="nav_proj_new"):
                st.session_state["current_page"] = "projects"; st.rerun()
        with sub_cols[3]:
            if st.button("المهندسون", key="nav_eng_new"):
                st.session_state["current_page"] = "engineers"; st.rerun()
        with sub_cols[4]:
            if st.button("حوكمة البيانات", key="nav_gov_new"):
                st.session_state["current_page"] = "data_governance"; st.rerun()
        with sub_cols[5]:
            if st.button("عن المنصة / اتصل بنا", key="nav_abt_new"):
                st.session_state["current_page"] = "about"; st.rerun()
        with sub_cols[6]:
            # حقل البحث المدمج والناعم المتواجد بجانب الأزرار مباشرة كالصورة المرجعية
            search_q = st.text_input("", key="nav_search_compact", placeholder="🔍 ابحث في الكودات الهندسية...", label_visibility="collapsed")
            if search_q:
                st.session_state["search_trigger"] = search_q

    # العمود الأيسر (حجز زر تسجيل الدخول المذهب بأقصى اليسار)
    with col_nav[2]:
        if st.button("🔒 تسجيل الدخول", key="nav_auth_new"):
            st.session_state["current_page"] = "auth"; st.rerun()

    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin-top: 2px; margin-bottom: 15px;'>", unsafe_allow_html=True)
