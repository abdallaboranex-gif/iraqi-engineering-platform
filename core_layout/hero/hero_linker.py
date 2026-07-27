import streamlit as st
import base64
import os

def show_hero_section():
    """
    الدالة المركزية المستقلة تماماً لإدارة وتأمين قسم الهيرو (صفر اعتمادية).
    تم توحيد صيغ قراءة صور الركائز الثلاث لتصبح jpg بالكامل لمنع أخطاء التجميع.
    """
    # 1. دالة تأسيسية محمية لتشفير وسائط الركائز الثلاث بصيغة JPG لتخطي حظر السيرفر
    def encode_hero_media(media_path):
        try:
            if os.path.exists(media_path):
                with open(media_path, "rb") as media_file:
                    return base64.b64encode(media_file.read()).decode()
            return ""
        except Exception:
            return ""

    # استدعاء وصهر بايتات الصور الثلاث من مجلد assets بالأسماء والامتدادات الموحدة الصريحة (.jpg)
    img_sus = encode_hero_media("assets/hero_sustainability.jpg")
    img_aut = encode_hero_media("assets/hero_automation.jpg")
    img_gov = encode_hero_media("assets/hero_governance.jpg")

    # 2. حقن نظام تصاميم محكم وصارم لدمج الصور داخل كروت الركائز بجمالية هندسية راقية
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
            margin-bottom: 25px !important;
            opacity: 0.95;
        }
        
        /* كروت الركائز المحدثة لاحتواء الصور الخلفية المضاءة بالذهب */
        .pillar-card-box-premium {
            background-color: rgba(7, 22, 21, 0.65) !important;
            border: 1px solid rgba(197, 160, 89, 0.2) !important;
            border-radius: 12px !important;
            padding: 0px !important; /* تصفير الحشو لفرش الصورة كاملة */
            text-align: center !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5) !important;
            backdrop-filter: blur(6px) !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            margin: 6px !important;
            overflow: hidden !important;
        }
        .pillar-card-box-premium:hover {
            border-color: #c5a059 !important;
            box-shadow: 0 12px 30px rgba(197, 160, 89, 0.35) !important;
            transform: translateY(-3px);
        }
        
        /* هندسة وعاء الصورة العلوية المدمجة داخل الكارت */
        .pillar-image-top {
            width: 100% !important;
            height: 110px !important;
            object-fit: cover !important;
            border-bottom: 2px solid rgba(197, 160, 89, 0.3);
        }
        
        .pillar-title-bottom {
            font-size: 14px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin: 0 !important;
            padding: 12px 6px !important;
            text-align: center !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important;
            background: linear-gradient(to top, rgba(7,22,21,0.9), rgba(7,22,21,0.4)) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 3. طباعة العنوان الرئيسي والفرعي بالوسط بانتظام متوازن
    st.markdown('<h1 class="hero-title-main">المدونات الهندسية العراقية</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle-sub">منصة وطنية للمعرفة الهندسية المستدامة</p>', unsafe_allow_html=True)

    # 4. تقسيم الركائز الثلاث داخل سطر واحد بـ 3 أعمدة متساوية تماماً لضمان المحاذاة والسنتر المعياري
    col_p1, col_p2, col_p3 = st.columns(3)

    # الركيزة 1: استدامة (اليمين بصرياً بالتسلسل العربي القياسي الصحيح)
    with col_p1:
        img_src_sus = f"data:image/jpeg;base64,{img_sus}" if img_sus else ""
        st.markdown(
            f"""
            <div class="pillar-card-box-premium">
                <img class="pillar-image-top" src="{img_src_sus}" alt="🌿">
                <h4 class="pillar-title-bottom">🌿 استدامة</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    # الركيزة 2: أتمتة (الوسط)
    with col_p2:
        img_src_aut = f"data:image/jpeg;base64,{img_aut}" if img_aut else ""
        st.markdown(
            f"""
            <div class="pillar-card-box-premium">
                <img class="pillar-image-top" src="{img_src_aut}" alt="⚙️">
                <h4 class="pillar-title-bottom">⚙️ أتمتة</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    # الركيزة 3: حوكمة سيادية (اليسار)
    with col_p3:
        img_src_gov = f"data:image/jpeg;base64,{img_gov}" if img_gov else ""
        st.markdown(
            f"""
            <div class="pillar-card-box-premium">
                <img class="pillar-image-top" src="{img_src_gov}" alt="🏛️">
                <h4 class="pillar-title-bottom">🏛️ حوكمة سيادية</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
