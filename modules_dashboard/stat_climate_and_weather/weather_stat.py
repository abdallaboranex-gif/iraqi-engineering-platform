import streamlit as st

def render_weather_stat():
    """
    برنامج ذكي ومستقل لعرض الحالة المناخية الحية والجو العام في العراق (مرصد العزل).
    """
    # هنا تم تصميم محاكاة لمرصد جوي عراقي ذكي جاهز للربط الفوري بالـ API
    st.markdown(
        """
        <div style="background-color: rgba(13, 35, 33, 0.6); padding: 12px; border-radius: 8px; border-left: 4px solid #c5a059; margin-bottom: 15px;">
            <p style="font-size: 14px; margin: 0; color: #a0b0af !important;">🌤️ مرصد مناخ المحافظات (بغداد الآن)</p>
            <h4 style="margin: 5px 0; color: #ffffff !important; font-size: 24px;">38°C <span style="font-size: 14px; color: #c5a059;">صافي / جاف</span></h4>
            <p style="font-size: 12px; margin: 0; color: #809593 !important;">مؤشر الإشعاع الشمسي: مرتفع (يتطلب كود العزل الحراري الثالث)</p>
        </div>
        """,
        unsafe_allow_html=True
    )
