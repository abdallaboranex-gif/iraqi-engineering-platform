import streamlit as st

def show_hero_section():
    """
    الدالة المركزية المستقلة لإدارة وتأمين قسم الهيرو الترحيبي (صفر اعتمادية).
    تنهي التشوه البصري وتجمع الركائز الثلاث في سطر واحد متناسق وموزون بالسنتر.
    """
    # 1. حقن نظام تصاميم صارم ومحدود لربط العناوين الترحيبية وتوسيطها بالملي
    st.markdown(
        """
        <style>
        .hero-title-main {
            font-size: 38px !important;
            font-weight: 800 !important;
            color: #c5a059 !important;
            text-align: center !important;
            text-shadow: 0 0 20px rgba(197, 160, 89, 0.5), 2px 2px 5px rgba(0,0,0,0.9) !important;
            margin-top: 10px !important;
            margin-bottom: 5px !important;
        }
        .hero-subtitle-sub {
            font-size: 16px !important;
            font-weight: 600 !important;
            color: #ffffff !important;
            text-align: center !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important;
            margin-bottom: 30px !important;
            opacity: 0.95;
        }
        /* تصميم الكروت الزجاجية العائمة للركائز الثلاث لضمان انتظام الأيقونات فوق النصوص */
        .pillar-card-box {
            background-color: rgba(7, 22, 21, 0.45) !important;
            border: 1px solid rgba(197, 160, 89, 0.15) !important;
            border-radius: 10px !important;
            padding: 15px 10px !important;
            text-align: center !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4) !important;
            backdrop-filter: blur(4px) !important;
            transition: all 0.3s ease !important;
            margin: 5px !important;
            min-height: 110px;
        }
        .pillar-card-box:hover {
            border-color: #c5a059 !important;
            box-shadow: 0 6px 20px rgba(197, 160, 89, 0.2) !important;
            transform: translateY(-2px);
        }
        .pillar-icon-style {
            font-size: 26px !important;
            color: #c5a059 !important;
            margin-bottom: 8px !important;
            text-shadow: 0 0 10px rgba(197, 160, 89, 0.4) !important;
        }
        .pillar-text-style {
            font-size: 13px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin: 0 !important;
            text-align: center !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 2. طباعة العنوان الرئيسي والفرعي بالوسط بانتظام متوازن
    st.markdown('<h1 class="hero-title-main">المدونات الهندسية العراقية</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle-sub">منصة وطنية للمعرفة الهندسية المستدامة</p>', unsafe_allow_html=True)

    # 3. الحل الهندسي الجذري: حصر الركائز الثلاث داخل سطر واحد بـ 3 أعمدة متساوية تماماً لإنهاء المتمطط
    col_p1, col_p2, col_p3 = st.columns(3)

    # الركيزة 1: استدامة (اليمين بصرياً بالتسلسل العربي)
    with col_p1:
        st.markdown(
            """
            <div class="pillar-card-box">
                <div class="pillar-icon-style">🌿</div>
                <h4 class="pillar-text-style">استدامة</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    # الركيزة 2: أتمتة (الوسط)
    with col_p2:
        st.markdown(
            """
            <div class="pillar-card-box">
                <div class="pillar-icon-style">⚙️</div>
                <h4 class="pillar-text-style">أتمتة</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    # الركيزة 3: حوكمة سيادية (اليسار)
    with col_p3:
        st.markdown(
            """
            <div class="pillar-card-box">
                <div class="pillar-icon-style">🏛️</div>
                <h4 class="pillar-text-style">حوكمة سيادية</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
