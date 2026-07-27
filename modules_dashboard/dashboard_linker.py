import streamlit as st

# استدعاء البرامج المصغرة المستقلة للمؤشرات من مجلداتها الفرعية المخصصة
from modules_dashboard.stats_header.header import render_stats_header
from modules_dashboard.stat_co2_emissions.co2_stat import render_co2_stat
from modules_dashboard.stat_sustainable_projects.sustain_stat import render_sustain_stat
from modules_dashboard.stat_climate_and_weather.weather_stat import render_weather_stat
from modules_dashboard.stat_registered_engineers.engineers_stat import render_engineers_stat

def show_dashboard_sidebar():
    """
    الدالة المركزية لتجميع برامج المرصد الوطني الـ 5 وعرضها ككتلة جانبية محصنة.
    تطبق مبدأ صفر اعتمادية وحماية كاملة ضد انهيار الواجهة.
    """
    
    # 1. تجميع وعزل ترويسة العنوان
    try:
        render_stats_header()
    except Exception:
        st.sidebar.error("⚠️ هنت: عطل مؤقت في ترويسة لوحة المؤشرات.")

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. تجميع وعزل مؤشر انبعاثات الكربون
    try:
        render_co2_stat()
    except Exception:
        st.caption("⚠️ مؤشر CO₂ خاضع للصيانة المؤقتة.")

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. تجميع وعزل مؤشر نسبة مشاريع الاستدامة
    try:
        render_sustain_stat()
    except Exception:
        st.caption("⚠️ مؤشر الاستدامة خاضع للصيانة المؤقتة.")

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. تجميع وعزل برنامج الطقس والمناخ الحي
    try:
        render_weather_stat()
    except Exception:
        st.caption("🌤️ جاري تحديث بيانات مرصد المناخ العراقي...")

    st.markdown("<br>", unsafe_allow_html=True)

    # 5. تجميع وعزل عداد المهندسين المسجلين
    try:
        render_engineers_stat()
    except Exception:
        st.caption("⚠️ عداد التسجيل النقابي خاضع للتحديث.")
