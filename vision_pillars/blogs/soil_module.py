import streamlit as st

def show_soil_verification():
    """
    الواجهة التشغيلية المعزولة تماماً لمدونة فحص التربة العراقية (صفر اعتمادية).
    """
    st.markdown("### 📋 أدخل نتائج فحص التربة المختبري والميداني الفعلي من واقع الموقع:")
    
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        actual_bearing = st.number_input("قدرة تحمل التربة الفعلية من التقرير (Soil Bearing Capacity - kN/m²)", min_value=0.0, value=0.0, step=10.0, key="soil_file_bearing")
        actual_gypsum = st.number_input("نسبة محتوى الجبس الكلية بالتربة (Soil Gypsum Content - %)", min_value=0.0, max_value=100.0, value=0.0, step=0.5, key="soil_file_gypsum")
    with col_in2:
        actual_boreholes = st.number_input("عدد الحفر الاستكشافية المنفذة موقعياً (Boreholes Count)", min_value=0, value=0, step=1, key="soil_file_boreholes")
        actual_age = st.number_input("عمر التقرير الجيوتقني الحالي (Soil Report Age - بالأشهر)", min_value=0, value=0, step=1, key="soil_file_age")

    design_stress = st.number_input("الإجهاد التصميمي الأقصى للمنشأ الخاضع للتدقيق (Design Stress - kN/m²)", min_value=0.0, value=120.0, step=10.0, key="soil_file_design_stress")

    if st.button("🚀 افحص مطابقة لوائح التربة وإصدار رخصة البناء", key="btn_execute_soil_file", use_container_width=True):
        failures_list = []
        
        if actual_bearing < design_stress:
            failures_list.append("فشل مطابقة القدرة التحملية للتربة الإنشائية (القدرة المقررة بالتقرير أقل من الإجهادات التصميمية للبناية).")
        if actual_boreholes < 2:
            failures_list.append("مخالفة معايير الكثافة الدنيا للاستكشاف والجس الجيوتقني (عدد الحفر أقل من حفرتين للأرض).")
        if actual_gypsum > 10.75:
            failures_list.append("مخالفة المحددات الكيميائية لسلامة الأسس؛ محتوى الجبس يتجاوز الحد الأعلى الحاكم كودياً (10.75%) مما يرفع خطر ذوبان التربة وفجوات أسفل القواعد.")
        if actual_age > 24:
            failures_list.append("عمر التقرير الجيوتقني المرفوع يتجاوز الحد الأقصى المسموح به قانونياً (24 شهراً من تاريخ الصدور).")

        if not failures_list:
            st.markdown(
                """
                <div class="premium-card-eval" style="border-right: 5px solid #52c41a !important; direction: rtl;">
                    <h3 style="color: #52c41a !important; margin: 0 0 10px 0;">🟢 نتيجة التدقيق: مطابق للمواصفات</h3>
                    <p style="margin: 0; color: #ffffff;">مبارك! كافة مدخلات تقرير التربة الميدانية ممتثلة تماماً للوائح وقوانين مدونة الأسس العراقية. تم تخويل المعاملة والحصول على موافقة رخصة البناء بنجاح.</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div class="premium-card-eval" style="border-right: 5px solid #ff4d4f !important; direction: rtl;">
                    <h3 style="color: #ff4d4f !important; margin: 0 0 10px 0;">🔴 نتيجة التدقيق: مرفوض (المعاملة مجمدة)</h3>
                    <p style="margin: 0; color: #ffffff; font-weight: bold; padding-bottom: 5px;">تم إيقاف تداول المعاملة وحظر رخصة البناء لوجود مخالفات حرجة ومخاطر إنشائية تهدد سلامة المنشأ:</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            for fail in failures_list:
                st.error(f"🚫 {fail}")
