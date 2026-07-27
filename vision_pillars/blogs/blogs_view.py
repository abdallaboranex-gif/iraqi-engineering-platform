import streamlit as st

def render_blogs_view():
    """
    الواجهة التشغيلية الذكية لمدونة فحص التربة العراقية.
    تطلب مدخلات ميدانية وتقارنها مع اللوائح وتصدر موافقة رخصة البناء.
    """
    st.markdown(
        """
        <style>
        .premium-card-eval {
            background-color: rgba(7, 22, 21, 0.75) !important;
            border: 1px solid rgba(197, 160, 89, 0.3) !important;
            border-radius: 12px !important; padding: 20px !important; margin-top: 15px !important;
            box-shadow: 0 8px 25px rgba(0,0,0,0.5) !important;
        }
        .text-header-title { color: #c5a059 !important; font-size: 24px !important; text-align: right !important; }
        .text-desc-title { color: #ffffff !important; font-size: 12px !important; text-align: right !important; opacity: 0.85; }
        div[data-testid="stNumberInput"] input { background-color: rgba(7, 22, 21, 0.85) !important; color: #ffffff !important; }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h2 class="text-header-title">🔬 منظومة تدقيق رخص البناء والتربة السيادية</h2>', unsafe_allow_html=True)
    st.markdown('<p class="text-desc-title">بوابة الفحص الرقمي لمطابقة تقارير التربة مع مدونة الأسس العراقية.</p>', unsafe_allow_html=True)

    st.markdown("### 📋 أدخل بيانات تقرير فحص التربة والموقع الفعلي:")
    
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        actual_bearing = st.number_input("قدرة تحمل التربة (kN/m²)", min_value=0.0, value=0.0, step=10.0, key="in_soil_bearing")
        actual_gypsum = st.number_input("نسبة محتوى الجبس (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.5, key="in_soil_gypsum")
    with col_in2:
        actual_boreholes = st.number_input("عدد الحفر الاستكشافية", min_value=0, value=0, step=1, key="in_soil_boreholes")
        actual_age = st.number_input("عمر التقرير (بالأشهر)", min_value=0, value=0, step=1, key="in_soil_age")

    design_stress = st.number_input("الإجهاد التصميمي الفعلي (kN/m²)", min_value=0.0, value=120.0, step=10.0, key="in_design_stress")

    if st.button("🚀 افحص المطابقة الفيدرالية وإصدار رخصة البناء", key="btn_execute_soil_match_v500", use_container_width=True):
        failures_list = []
        
        # تطبيق قيود الكود المستخرجة من
        if actual_bearing < design_stress:
            failures_list.append("فشل تحمل التربة (القدرة التصميمية أقل من المطلوبة)")
        if actual_boreholes < 2:
            failures_list.append("عدد الحفر الاستكشافية غير كافٍ هندسياً (أقل من 2)")
        if actual_gypsum > 10.75:
            failures_list.append("ارتفاع نسبة الجبس (تتجاوز 10.75%)")
        if actual_age > 24:
            failures_list.append("تقرير التربة منتهي الصلاحية (أكثر من 24 شهر)")

        # عرض النتائج
        if not failures_list:
            st.markdown('<div class="premium-card-eval" style="border-right: 5px solid #52c41a !important;"><h3 style="color: #52c41a !important;">🟢 نتيجة الفحص: مطابق ومصادق</h3></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="premium-card-eval" style="border-right: 5px solid #ff4d4f !important;"><h3 style="color: #ff4d4f !important;">🔴 نتيجة الفحص: مرفوض (توجد مخالفات حرجة)</h3></div>', unsafe_allow_html=True)
            for fail in failures_list:
                st.error(f"🚫 {fail}")
