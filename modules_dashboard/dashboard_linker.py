import streamlit as st

def show_dashboard_sidebar():
    """
    الدالة المركزية المطورة لتجميع برامج المرصد الوطني الـ 5 وعرضها ككتلة جانبية.
    تم حقن الأيقونات الملونة والخطوط المضاءة لتطابق الصورة القياسية تماماً.
    """
    
    # 1. ترويسة وعنوان لوحة المؤشرات الوطنية
    st.markdown(
        """
        <div style="text-align: right; border-bottom: 1px solid rgba(197, 160, 89, 0.3); padding-bottom: 8px; margin-bottom: 15px;">
            <h3 style="color: #ffffff !important; font-size: 16px; font-weight: 700; margin: 0; display: inline-block;">
                📊 المؤشرات الوطنية الحية
            </h3>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # 2. مؤشر المشاريع المستدامة (أيقونة خضراء دائرية مضاءة)
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(7, 22, 21, 0.5); padding: 10px; border-radius: 8px; margin-bottom: 10px; border: 1px solid rgba(197, 160, 89, 0.1);">
            <div style="text-align: left;">
                <span style="font-size: 10px; color: #a0b0af;">المشاريع المستدامة</span>
                <h4 style="margin: 0; color: #ffffff !important; font-size: 18px; font-weight: 700;">1,248</h4>
                <span style="font-size: 9px; color: #52c41a;">🟢 منجز</span>
            </div>
            <div style="width: 36px; height: 36px; background: rgba(82, 196, 26, 0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 10px rgba(82, 196, 26, 0.3);">
                <span style="font-size: 18px;">🌱</span>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # 3. مؤشر انبعاثات الكربون المخفضة
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(7, 22, 21, 0.5); padding: 10px; border-radius: 8px; margin-bottom: 10px; border: 1px solid rgba(197, 160, 89, 0.15);">
            <div style="text-align: left;">
                <span style="font-size: 10px; color: #a0b0af;">الانبعاثات المخفضة</span>
                <h4 style="margin: 0; color: #ffffff !important; font-size: 18px; font-weight: 700;">2.4 <span style="font-size: 11px; font-weight: normal;">مليون طن CO₂</span></h4>
                <span style="font-size: 9px; color: #c5a059;">✨ مستدام طبقاً للكود البيئي</span>
            </div>
            <div style="width: 36px; height: 36px; background: rgba(197, 160, 89, 0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 10px rgba(197, 160, 89, 0.3);">
                <span style="font-size: 18px;">📉</span>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # 4. مؤشر نسبة الطاقة المتجددة الوطنية
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(7, 22, 21, 0.5); padding: 10px; border-radius: 8px; margin-bottom: 10px; border: 1px solid rgba(197, 160, 89, 0.1);">
            <div style="text-align: left;">
                <span style="font-size: 10px; color: #a0b0af;">الطاقة المتجددة</span>
                <h4 style="margin: 0; color: #ffffff !important; font-size: 18px; font-weight: 700;">36%</h4>
                <span style="font-size: 9px; color: #52c41a;">▲ +4.2% العام الحالي</span>
            </div>
            <div style="width: 36px; height: 36px; background: rgba(82, 196, 26, 0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 10px rgba(82, 196, 26, 0.2);">
                <span style="font-size: 18px;">☀️</span>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # 5. مرصد مناخ المحافظات الحية
    st.markdown(
        """
        <div style="background-color: rgba(13, 35, 33, 0.5); padding: 10px; border-radius: 8px; border-right: 3px solid #c5a059; margin-bottom: 10px; border-left: 1px solid rgba(197, 160, 89, 0.1);">
            <p style="font-size: 11px; margin: 0; color: #a0b0af !important; text-align: right;">🌤️ مرصد مناخ المحافظات (بغداد الآن)</p>
            <h4 style="margin: 3px 0; color: #ffffff !important; font-size: 20px; text-align: right;">38°C <span style="font-size: 12px; color: #c5a059; font-weight: normal;">صافي / جاف</span></h4>
            <p style="font-size: 10px; margin: 0; color: #809593 !important; text-align: right;">مؤشر الإشعاع الشمسي مرتفع (يتطلب كود العزل الحراري الثالث)</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 6. عداد المهندسين المسجلين
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(7, 22, 21, 0.5); padding: 10px; border-radius: 8px; margin-bottom: 10px; border: 1px solid rgba(197, 160, 89, 0.15);">
            <div style="text-align: left;">
                <span style="font-size: 10px; color: #a0b0af;">المهندسون والمكاتب المسجلة</span>
                <h4 style="margin: 0; color: #ffffff !important; font-size: 18px; font-weight: 700;">18,532</h4>
                <span style="font-size: 9px; color: #a0b0af;">🔒 قاعدة بيانات وطنية موثقة</span>
            </div>
            <div style="width: 36px; height: 36px; background: rgba(197, 160, 89, 0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 10px rgba(197, 160, 89, 0.2);">
                <span style="font-size: 18px;">👷</span>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # زر عرض التفاصيل النحيف بأسفل اللوحة
    if st.button("عرض التفاصيل الجغرافية 🗺️", key="btn_sidebar_details", use_container_width=True):
        st.sidebar.info("هنت: جاري تجهيز لوحة التوزيع الرقمي للمحافظات العراقية بالتعاون مع النقابة.")
