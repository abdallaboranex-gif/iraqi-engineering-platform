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
    تطبق مبدأ صفر اعتمادية وحماية كاملة ضد انهيار قمة الشاشة.
    """
    
    # إنشاء صف علوي لتوزيع (العلم، الشعار، قائمة البرجر، والأزرار الستة، وتسجيل الدخول)
    # تم اختيار الأوزان البرمجية للأعمدة لضمان التراص الأفقي الأنيق كالصورة
    cols = st.columns([0.5, 0.6, 0.4, 1, 1, 1, 1, 1.2, 1.5, 1.2])
    
    # 1. العلم العراقي
    with cols[0]:
        try:
            render_iraqi_flag()
        except Exception:
            pass

    # 2. شعار المنصة INCP
    with cols[1]:
        try:
            render_nav_logo()
        except Exception:
            pass

    # 3. أيقونة البرجر للقائمة الجانبية المساعدة
    with cols[2]:
        try:
            render_menu_drawer()
        except Exception:
            pass

    # 4. زر الرئيسية
    with cols[3]:
        try:
            render_btn_home()
        except Exception:
            st.caption("⚠️ عطل")

    # 5. زر المدونات
    with cols[4]:
        try:
            render_btn_blogs()
        except Exception:
            st.caption("⚠️ عطل")

    # 6. زر المشاريع
    with cols[5]:
        try:
            render_btn_projects()
        except Exception:
            st.caption("⚠️ عطل")

    # 7. زر المهندسون
    with cols[6]:
        try:
            render_btn_engineers()
        except Exception:
            st.caption("⚠️ عطل")

    # 8. زر حوكمة البيانات
    with cols[7]:
        with st.container():
            try:
                render_btn_governance()
            except Exception:
                st.caption("⚠️ عطل")

    # 9. زر عن المنصة / اتصل بنا
    with cols[8]:
        try:
            render_btn_about_contact()
        except Exception:
            st.caption("⚠️ عطل")

    # 10. بوابة تسجيل الدخول الموحدة
    with cols[9]:
        try:
            render_auth_gate()
        except Exception:
            st.caption("⚠️ قفل")

    st.markdown("<br>", unsafe_allow_html=True)

    # 11. حقن وعزل محرك البحث الذكي المباشر داخل ملفات الإكسل شيت أسفل صف الأزرار لراحة العين
    try:
        render_search_engine()
    except Exception:
        st.sidebar.warning("⚠️ هنت: محرك الاستعلام الذكي في الإكسل خاضع للصيانة.")
        
    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.4); margin-top: 10px; margin-bottom: 25px;'>", unsafe_allow_html=True)
