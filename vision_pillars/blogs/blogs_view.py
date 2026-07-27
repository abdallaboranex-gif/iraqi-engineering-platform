import streamlit as st

def render_blogs_view():
    """
    الواجهة التشغيلية المركزية الموحدة لتدقيق ومطابقة المواصفات الهندسية (مجلد المدونات).
    تتيح للمهندس اختيار المدونة الفيدرالية أولاً، لتنبثق حقول المطابقة الخاصة بها فوراً.
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
        /* تجميل صناديق التحديد والأرقام */
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

    # 1. رأس وعنوان لوحة المنظومة الفيدرالية
    st.markdown('<h2 class="main-title-view">🏛️ منظومة التدقيق والمطابقة الهندسية الفيدرالية</h2>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title-view">بوابة فحص الامتثال الرقمي الموحد بين الواقع الميداني للمشاريع واللوائح القياسية لمدونات البناء العراقية.</p>', unsafe_allow_html=True)

    # 2. حقل الاختيار الموحد للمدونات الهندسية (المصنف الحاكم للبوابة)
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
        key="v600_premium_blog_selector",
        label_visibility="collapsed"
    )

    st.markdown("<br><hr style='border-color: rgba(197, 160, 89, 0.15);'><br>", unsafe_allow_html=True)

    # 3. الفرع الأول الحركي: تشغيل واجهة فحص التربة عند اختيارها
    if "Soil Testing" in selected_blog_tab:
        st.markdown("### 📋 أدخل نتائج فحص التربة المختبري والميداني الفعلي من واقع الموقع:")
        
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            actual_bearing = st.number_input("قدرة تحمل التربة الفعلية من التقرير (Soil Bearing Capacity - kN/m²)", min_value=0.0, value=0.0, step=10.0, key="in_v600_bearing")
            actual_gypsum = st.number_input("نسبة محتوى الجبس الكلية بالتربة (Soil Gypsum Content - %)", min_value=0.0, max_value=100.0, value=0.0, step=0.5, key="in_v600_gypsum")
        with col_in2:
            actual_boreholes = st.number_input("عدد الحفر الاستكشافية المنفذة موقعياً (Boreholes Count)", min_value=0, value=0, step=1, key="in_v600_boreholes")
            actual_age = st.number_input("عمر التقرير الجيوتقني الحالي (Soil Report Age - بالأشهر)", min_value=0, value=0, step=1, key="in_v600_age")

        design_stress = st.number_input("الإجهاد التصميمي الأقصى للمنشأ الخاضع للتدقيق (Design Stress - kN/m²)", min_value=0.0, value=120.0, step=10.0, key="in_v600_design_stress")

        if st.button("🚀 افحص مطابقة لوائح التربة وإصدار رخصة البناء", key="btn_execute_soil_v600", use_container_width=True):
            failures_list = []
            
            # معالجة القوانين والمحددات الرقمية المأخوذة بالملي من جدول الإكسل شيت
            if actual_bearing < design_stress:
                failures_list.append("فشل مطابقة القدرة التحملية للتربة الإنشائية (القدرة المقررة بالتقرير أقل من الإجهادات التصميمية للبناية).")
            if actual_boreholes < 2:
                failures_list.append("مخالفة معايير الكثافة الدنيا للاستكشاف والجس الجيوتقني (عدد الحفر أقل من حفرتين للأرض).")
            if actual_gypsum > 10.75:
                failures_list.append("مخالفة المحددات الكيميائية لسلامة الأسس؛ محتوى الجبس يتجاوز الحد الأعلى الحاكم كودياً (10.75%) مما يرفع خطر ذوبان التربة وفجوات أسفل القواعد.")
            if actual_age > 24:
                failures_list.append("عمر التقرير الجيوتقني المرفوع يتجاوز الحد الأقصى المسموح به قانونياً (24 شهراً من تاريخ الصدور).")

            # صياغة النتيجة وإصدار القرار السيادي النهائي للرخصة
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

    # 4. بقية الأقسام تم عزل وتأمين غرفها وجاهزة لاستقبال الحقول والمعادلات فور طلبك
    elif "Architectural" in selected_blog_tab:
        st.info("📐 بوابة المدونة المعمارية والسلامة من الحرائق؛ ارفع لي داتا حقولها لتفعيل محرك فحص المطابقة الخاص بها فوراً.")
        
    elif "Electrical" in selected_blog_tab:
        st.info("⚡ بوابة اللوائح الكهربائية وكفاءة الطاقة؛ ارفع لي داتا حقولها لتفعيل محرك فحص المطابقة الخاص بها فوراً.")
        
    elif "Foundations" in selected_blog_tab:
        st.info("🧱 مدونة الأسس والجدران الساندة الفيدرالية؛ ارفع لي داتا حقولها لتفعيل محرك فحص المطابقة الخاص بها فوراً.")
        
    elif "Sanitary" in selected_blog_tab:
        st.info("💧 مدونة الخدمات الصحية والبيئية؛ ارفع لي داتا حقولها لتفعيل محرك فحص المطابقة الخاص بها فوراً.")
