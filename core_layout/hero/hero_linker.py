import streamlit as st

# استدعاء البرامج المصغرة المستقلة من مجلداتها الفرعية
from core_layout.hero.hero_main_title.main_title import render_main_title
from core_layout.hero.hero_sub_title.sub_title import render_sub_title
from core_layout.hero.pillar_sustainability.sustainability_pillar import render_sustainability_pillar
from core_layout.hero.pillar_automation.automation_pillar import render_automation_pillar
from core_layout.hero.pillar_governance.governance_pillar import render_governance_pillar

def show_hero_section():
    """
    الدالة المركزية لربط وتجميع عناصر القسم الترحيبي الـ 5 
    مع عزل كامل للأخطاء وصفر اعتمادية بينها وحمايتها بأحزمة أمان.
    """
    
    # 1. تجميع وعزل العنوان الرئيسي
    try:
        render_main_title()
    except Exception:
        st.sidebar.error("⚠️ هنت: عطل مؤقت في برنامج العنوان الرئيسي للمنصة.")

    # 2. تجميع وعزل العنوان الفرعي
    try:
        render_sub_title()
    except Exception:
        pass  # يختفي بصمت دون التأثير على التصميم

    # 3. إنشاء 3 أعمدة متساوية على الشاشة لصف أيقونات الركائز الثلاث بجانب بعضها
    col1, col2, col3 = st.columns(3)

    # تجميع وعزل أيقونة استدامة داخل العمود الأول
    with col1:
        try:
            render_sustainability_pillar()
        except Exception:
            st.warning("⚠️ القسم خاضع للصيانة")

    # تجميع وعزل أيقونة أتمتة داخل العمود الثاني
    with col2:
        try:
            render_automation_pillar()
        except Exception:
            st.warning("⚠️ القسم خاضع للصيانة")

    # تجميع وعزل أيقونة حوكمة سيادية داخل العمود الثالث
    with col3:
        try:
            render_governance_pillar()
        except Exception:
            st.warning("⚠️ القسم خاضع للصيانة")
