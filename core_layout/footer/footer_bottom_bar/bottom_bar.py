import streamlit as st

def render_footer_bottom_bar():
    """
    برنامج مستقل لإظهار الشريط الأخير بنهاية الواجهة (الحقوق والسياسات السيادية).
    """
    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.3); margin-top: 40px; margin-bottom: 20px;'>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("<p style='font-size: 12px; color: #809593 !important; margin:0;'>جميع الحقوق محفوظة © منصة المدونات الهندسية العراقية ٢٠٢٦</p>", unsafe_allow_html=True)
    with col_r:
        st.markdown(
            """
            <div style="text-align: left; font-size: 12px;">
                <span style="color: #c5a059; cursor: pointer; margin-left: 15px;">شروط الاستخدام للمكاتب</span>
                <span style="color: #c5a059; cursor: pointer;">سياسة حماية السيادة والبيانات الهندسية</span>
            </div>
            """, unsafe_allow_html=True
        )
