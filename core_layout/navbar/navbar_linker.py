import streamlit as st

# استدعاء البرامج المصغرة المستقلة للنافكيشن بار من مجلداتها الفرعية المخصصة
from core_layout.navbar.nav_iraqi_flag.flag import render_iraqi_flag
from core_layout.navbar.nav_logo.logo import render_nav_logo
from core_layout.navbar.nav_menu_drawer.menu_drawer import render_menu_drawer
from core_layout.navbar.nav_search_engine.search_engine import render_search_engine
from core_layout.navbar.nav_home.btn_home import render_btn_home
from core_layout.navbar.nav_blogs.btn_blogs import render_btn_blogs
from core_layout.navbar.nav_projects.btn_projects import render_btn_projects
from core_layout.navbar.nav_engineers.btn_engineers import render_btn_engineers
from core_layout.navbar.nav_data_governance.btn_governance import render_btn_governance
from core_layout.navbar.nav_about_contact.btn_about_contact import render_btn_about_contact
from core_layout.navbar.nav_auth_gate.auth_gate import render_auth_gate

def show_navbar_section():
    """
    الدالة المركزية لتجميع برامج شريط التنقل الـ 11 ومحرك بحث الإكسل.
    تم تعديل أوزان الأعمدة هنا لتقريب الأزرار وتراصها أفقياً بنسبة اعتماد صفرية.
    """
    
    # حقن كود CSS مصغر ومستقل لعزل وتجميل أزرار النافبار وجعلها متقاربة وبدون فراغات بيضاء
    st.markdown(
        """
        <style>
        /* تصغير الفراغات بين أعمدة النافبار وجعل الخطوط متناسقة */
        div[data-testid="stHorizontalBlock"] > div {{
            padding-left: 2px !important;
            padding-right: 2px !important;
        }}
        /* تجميل خطوط أزرار النافبار المتقاربة */
        .stButton > button {{
            font-size: 13px !important;
            padding: 4px 8px !important;
            white-space: nowrap !important; /* منع نزول النص لسطر جديد */
            width: 100% !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # إنشاء 10 أعمدة متراصة ومقربة جداً لصف الأزرار والعلم والشعار بجانب بعضها
    # الأرقام تمثل العرض النسبي لكل عمود (أوزان خفيفة ومتقاربة)
    cols = st.columns([0.2, 0.4, 0.2, 0.6, 0.6, 0.6, 0.6, 1.0, 1.3, 0.9])
    
    # 1. العلم العراقي
    with cols[0]:
        try: render_iraqi_flag()
        except Exception: pass

    # 2. شعار المنصة INCP
    with cols[1]:
        try: render_nav_logo()
        except Exception: pass

    # 3. أيقونة البرجر للقائمة الجانبية المساعدة
    with cols[2]:
        try: render_menu_drawer()
        except Exception: pass

    # 4. زر الرئيسية
    with cols[3]:
        try: render_btn_home()
        except Exception: pass

    # 5. زر المدونات
    with cols[4]:
        try: render_btn_blogs()
        except Exception: pass

    # 6. زر المشاريع
    with cols[5]:
        try: render_btn_projects()
        except Exception: pass

    # 7. زر المهندسون
    with cols[6]:
        try: render_btn_engineers()
        except Exception: pass

    # 8. زر حوكمة البيانات
    with cols[7]:
        try: render_btn_governance()
        except Exception: pass

    # 9. زر عن المنصة / اتصل بنا
    with cols[8]:
        try: render_btn_about_contact()
        except Exception: pass

    # 10. بوابة تسجيل الدخول الموحدة
    with cols[9]:
        try: render_auth_gate()
        except Exception: pass

    st.markdown("<br>", unsafe_allow_html=True)

    # 11. حقن وعزل محرك البحث الذكي المباشر داخل ملفات الإكسل شيت أسفل صف الأزرار لراحة العين
    try:
        render_search_engine()
    except Exception:
        st.sidebar.warning("⚠️ هنت: محرك الاستعلام الذكي في الإكسل خاضع للصيانة.")
        
    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.3); margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)
