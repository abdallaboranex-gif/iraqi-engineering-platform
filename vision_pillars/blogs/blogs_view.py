import streamlit as st

def render_blogs_view():
    """
    الواجهة التشغيلية المركزية (الموزع الفيدرالي لغرف المدونات).
    تجمع صندوق الاختيار الحاكم، وتستدعي الملف الفرعي المستقل لكل مدونة (صفر اعتمادية).
    """
    st.markdown(
        """
        <style>
        .premium-card-eval {
            background-color: rgba(7, 22, 21, 0.75) !important;
            border: 1px solid rgba(197, 160, 89, 0.3) !important;
            border-radius: 12px !important; 
            padding: 20px !important; 
            margin-top: 15px !important;
            box-shadow: 0 8px 25px rgba(0,0,0,0.5) !important;
        }
        .main-title-view {
            color: #c5a059 !important;
            font-size: 26px !important;
            font-weight: 800 !important;
            text-align: right !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important;
            margin-bottom: 5px !important;
        }
        .sub-title-view {
            color: #ffffff !important;
            font-size: 12px !important;
            text-align: right !important;
            margin-bottom: 25px !important;
            opacity: 0.85;
        }
        div[data-testid="stSelectbox"] > div {
            background-color: rgba(7, 22, 21, 0.85) !important;
            color: #ffffff !important;
            border: 1px solid rgba(197, 160, 89, 0.3) !important;
            border-radius: 4px !important;
        }
        div[data-testid="stNumberInput"] input { 
            background-color: rgba(7, 22, 21, 0.85) !important; 
            color: #ffffff !important; 
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 1. طباعة رأس وعنوان لوحة المنظومة الفيدرالية
    st.markdown('<h2 class="main-title-view">🏛️ منظومة التدقيق والمطابقة الهندسية الفيدرالية</h2>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title-view">بوابة فحص الامتثال الرقمي الموحد بين الواقع الميداني للمشاريع واللوائح القياسية لمدونات البناء العراقية.</p>', unsafe_allow_html=True)

    # 2. صندوق الاختيار المركزي والموحد للمدونات (المصنف الحاكم للبوابة)
    st.markdown("##### 🔍 اختر المصنف الهندسي المطلوب تدقيق مواصفاته:")
    selected_blog_tab = st.selectbox(
        "",
        options=[
            "🔬 لوائح وفحوصات التربة الهندسية (Soil Testing Rules)",
            "📐 المدونة المعمارية والسلامة من الحرائق (Architectural & Fire Safety)",
            "⚡ المدونة الكهربائية وكفاءة الطاقة (Electrical & Energy Efficiency)",
            "🧱 مدونة الأسس والجدران الساندة (Foundations & Retaining Walls)",
            "💧 مدونة الخدمات الصحية والبيئية (Sanitary & Environmental Services)"
        ],
        key="v700_premium_blog_selector",
        label_visibility="collapsed"
    )

    st.markdown("<br><hr style='border-color: rgba(197, 160, 89, 0.15);'><br>", unsafe_allow_html=True)

    # 3. خطة الاستدعاء الفيدرالي المباشر للغرف المعزولة والمفككة صراحة
    if "Soil Testing" in selected_blog_tab:
        # استدعاء ملف فحص التربة المستقل وتشغيل دالته الخالصة بأمان
        from vision_pillars.blogs.soil_module import show_soil_verification
        try:
            show_soil_verification()
        except Exception:
            st.error("⚠️ عطل في تحميل مصنف التربة المعزول.")

    elif "Architectural" in selected_blog_tab:
        # استدعاء ملف المعماري المستقل فور تأسيسه وحقنه بالمعادلات بالخطوات التالية
        try:
            from vision_pillars.blogs.architectural_module import show_arch_verification
            show_arch_verification()
        except Exception:
            st.info("📐 بوابة المدونة المعمارية والسلامة من الحرائق؛ معزولة وجاهزة لاستقبال ملف الغرفة البرمجية الخاص بها.")

    elif "Electrical" in selected_blog_tab:
        st.info("⚡ بوابة اللوائح الكهربائية وكفاءة الطاقة؛ معزولة تماماً في مجلدها الفرعي الخاص.")

    elif "Foundations" in selected_blog_tab:
        st.info("🧱 مدونة الأسس والجدران الساندة الفيدرالية؛ معزولة تماماً في مجلدها الفرعي الخاص.")

    elif "Sanitary" in selected_blog_tab:
        st.info("💧 مدونة الخدمات الصحية والبيئية؛ معزولة تماماً في مجلدها الفرعي الخاص.")
