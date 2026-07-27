import streamlit as st

def render_governance_view():
    """
    الواجهة التفاعلية الذكية لكابينة حوكمة البيانات (حساب الأحمال).
    تقوم بفلترة الفحوصات الـ 13 وعرض القراءات المطلوبة حياً بناءً على طبيعة العقار.
    """
    # 1. حقن نظام تصاميم زجاجي فاخر ومتكامل يتوافق مع الهوية السيادية للمنصة
    st.markdown(
        """
        <style>
        .gov-title-main {
            font-size: 24px !important; font-weight: 800 !important; color: #c5a059 !important;
            text-align: right !important; margin-bottom: 5px !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important;
        }
        .gov-desc-text {
            font-size: 13px !important; color: #a0b0af !important; text-align: right !important;
            line-height: 1.5 !important; margin-bottom: 20px !important;
        }
        .gov-panel-box {
            background-color: rgba(7, 22, 21, 0.6) !important;
            border: 1px solid rgba(197, 160, 89, 0.2) !important;
            border-radius: 8px !important; padding: 15px !important; margin-bottom: 15px !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
        }
        .gov-section-header {
            font-size: 14px !important; font-weight: 700 !important; color: #c5a059 !important;
            border-bottom: 1px solid rgba(197, 160, 89, 0.2) !important;
            padding-bottom: 6px !important; margin-bottom: 15px !important; text-align: right !important;
        }
        .stSelectbox label, .stNumberInput label, .stTextInput label {
            color: #c5a059 !important; font-size: 12px !important; font-weight: 600 !important;
        }
        .stSelectbox > div > div, .stNumberInput > div > div, .stTextInput > div > div {
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            background-color: rgba(7, 22, 21, 0.8) !important; border-radius: 4px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h2 class="gov-title-main">⚖️ منظومة حوكمة المشاريع والتدقيق الآلي للتربة</h2>', unsafe_allow_html=True)
    st.markdown('<p class="gov-desc-text">نموذج الفحص والفلترة الذكي للتخلص من المطابقة اليدوية، وحماية المنظومة من القراءات الوهمية والتحايل الإنشائي.</p>', unsafe_allow_html=True)

    # 🏢 الطابق الأول: فلاتر تحديد المعاملة وفئة المنشأ
    st.markdown('<div class="gov-panel-box">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header">🗺️ الخطوة 1: معطيات الرخصة وتحديد مسار التدقيق</p>', unsafe_allow_html=True)
    
    # صف مدخلات الفرز بالتسلسل العربي (من اليمين لليسار عبر تقسيم الأعمدة)
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    
    with col_f4:
        req_type = st.selectbox("نوع الطلب / المعاملة", ["بناء جديد", "إضافة طابق", "مشاريع استثمارية كبرى", "ترميم وتعديل"], key="gov_req_type_v3")
    with col_f3:
        total_area = st.number_input("مساحة الأرض الكلية (m²)", min_value=50, max_value=50000, value=200, step=10, key="gov_total_area_v3")
    with col_f2:
        total_floors = st.number_input("عدد الطوابق المقترحة", min_value=1, max_value=60, value=2, step=1, key="gov_total_floors_v3")
    with col_f1:
        has_basement_floor = st.selectbox("هل يتضمن المخطط طابق سرداب؟", ["لا", "نعم"], key="gov_has_basement_floor_v3")

    # تطبيق معادلات الفلترة الشرطية الحاكمة لجدول الإكسل آلياً حياً
    is_heavy = (total_floors >= 4) or (has_basement_floor == "نعم") or (req_type == "مشاريع استثمارية كبرى")
    is_medium = (not is_heavy) and (total_area > 400 or req_type in ["إضافة طابق", "ترميم وتعديل"])
    is_light = (not is_heavy) and (not is_medium)

    # بث النتيجة البصرية الفورية لتأكيد نجاح الفرز للمهندس أو الموظف الفاحص
    if is_heavy:
        st.error("🚨 فئة المنشأ الحالية: مشاريع استثمارية ثقيلة وأبراج عالية (تفعيل الـ 13 فحصاً بالكامل بكافة الصرامة).")
        gov_route = "heavy"
    elif is_medium:
        st.warning("⚠️ فئة المنشأ الحالية: أبنية متوسطة ومنشآت تجارية/خدمية (تفعيل 9 فحوصات رئيسية وحجب الفحوصات الثقيلة).")
        gov_route = "medium"
    else:
        st.success("🌿 فئة المنشأ الحالية: دور سكنية وأبنية خفيفة (اختصار الواجهة وتفعيل 5 فحوصات أساسية مبسطة فقط).")
        gov_route = "light"

    st.markdown('</div>', unsafe_allow_html=True)
    
    # تخزين المتغيرات للشق الثاني من الواجهة التفاعلية
    st.session_state["gov_route_active"] = gov_route
    st.session_state["has_basement_bool"] = (has_basement_floor == "نعم")
    # 🏢 الطابق الثاني: انبثاق الحقول التفاعلية بناءً على الفئة المفروزة آلياً
    st.markdown('<div class="gov-panel-box">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header">🧪 الخطوة 2: القراءات والفحوصات الجيوتقنية المطلوبة لهذه المعاملة</p>', unsafe_allow_html=True)
    
    # جلب مسار الفلترة النشط من الذاكرة
    active_route = st.session_state.get("gov_route_active", "light")
    has_basement_active = st.session_state.get("has_basement_bool", False)
    
    # شبكةColumns لتوزيع مدخلات الفحص بانتظام هندسي من اليمين لليسار
    gc1, gc2 = st.columns(2)
    
    # ------------------ المجموعه 1: الفحوصات المشتركة لجميع الفئات (حتمية الوجود) ------------------
    with gc2:
        st.markdown("<p style='color: #c5a059; font-weight: bold; font-size: 12px; margin-bottom: 5px;'>📋 فحوصات الاعتمادية والقدرة الأساسية:</p>", unsafe_allow_html=True)
        soil_validity = st.selectbox("صلاحية واعتمادية تقرير التربة (Soil_Report_Validity)", ["معتمد ومجاز ومصادق", "غير مصادق / تحت المراجعة"], key="f_soil_validity")
        bh_count = st.number_input("عدد الحفر الاستكشافية المنفذة (Boreholes_Count)", min_value=0, max_value=20, value=2, key="f_bh_count")
        
        # تحديد حقل عمق الحفر ديناميكياً حسب وزن البناية (طابق ضحل أو برج ثقيل)
        if active_route == "heavy":
            bh_depth = st.number_input("عمق الحفرة الاختبارية للأبراج العالية (Borehole_Depth_Heavy) - المطلوب ≥ 15م", min_value=0.0, max_value=100.0, value=15.0, key="f_bh_depth_heavy")
        else:
            bh_depth = st.number_input("عمق الحفرة الاختبارية للأبنية الخفيفة (Borehole_Depth_Shallow) - المطلوب ≥ 6م", min_value=0.0, max_value=50.0, value=6.0, key="f_bh_depth_shallow")
            
        bearing_capacity = st.number_input("قدرة تحمل التربة التصميمية المسموحة (Soil_Bearing_Capacity) - kN/m²", min_value=0.0, max_value=1000.0, value=150.0, key="f_bearing")
        report_age = st.number_input("عمر التقرير الجيوتقني الحالي بالأشهر (Soil_Report_Age) - المطلوب ≤ 24 شهر", min_value=0, max_value=120, value=6, key="f_report_age")

    # ------------------ المجموعه 2: الفحوصات الكيميائية والإنشائية المتقدمة (تظهر للمتوسط والثقيل وتختفي للبيوت) ------------------
    with gc1:
        if active_route in ["medium", "heavy"]:
            st.markdown("<p style='color: #c5a059; font-weight: bold; font-size: 12px; margin-bottom: 5px;'>🔬 الفحوصات المختبرية والكيميائية الإلزامية:</p>", unsafe_allow_html=True)
            sulphate_so3 = st.number_input("محتوى الكبريتات الثلاثية الذائبة في التربة (Soil_Sulphate_Content_SO3) - المطلوب ≤ 5%", min_value=0.0, max_value=100.0, value=2.1, key="f_sulphate")
            chloride_content = st.number_input("نسبة أيونات الكلوريدات الذائبة (Soil_Chloride_Content) - المطلوب ≤ 0.1%", min_value=0.00, max_value=10.00, value=0.04, step=0.01, key="f_chloride")
            organic_content = st.number_input("محتوى المواد العضوية والجذور (Soil_Organic_Content) - المطلوب ≤ 2%", min_value=0.0, max_value=100.0, value=0.5, key="f_organic")
            compaction_degree = st.number_input("درجة الحدل ورص التربة الميداني (Soil_Compaction_Degree) - المطلوب ≥ 95%", min_value=0.0, max_value=100.0, value=96.5, key="f_compaction")
        else:
            # حجب الفحوصات الإنشائية المعقدة تلقائياً للبيوت لتخفيف واجهة المواطن
            st.markdown("<div style='background: rgba(197, 160, 89, 0.05); padding: 15px; border-radius: 6px; border: 1px dashed rgba(197, 160, 89, 0.15); margin-top: 20px; text-align: right;'><p style='color: #a0b0af; margin:0;'>🔒 تم حجب وإعفاء هذه المعاملة من الفحوصات الكيميائية المعقدة (كبريتات، كلوريدات، مواد عضوية، درجة حدل) لكونها تقع ضمن فئة الدور السكنية الخفيفة بموجب الكود العراقي.</p></div>", unsafe_allow_html=True)

    # ------------------ المجموعه 3: الفحوصات الجيوفيزيائية والسيادية الكبرى (تظهر للأبراج والسرداب فقط وتختفي كلياً لغيرها) ------------------
    if active_route == "heavy":
        st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown("<p style='color: #ff4b4b; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>⚠️ قيود السلامة والأمان الجيوفيزيائية للأبراج العالية ومشاريع الاستثمار:</p>", unsafe_allow_html=True)
        
        g1, g2 = st.columns(2)
        with g2:
            gpr_scan = st.selectbox("نتائج مسح الرادار الأرضي الاختراقي للكهوف (Soil_GPR_Void_Scan)", ["خالٍ من الفجوات والتكهفات الحرجة", "تم رصد فجوات وتجاويف تحت سطحية غير معالجة"], key="f_gpr")
            gypsum_content = st.number_input("نسبة محتوى الجبس الكلية (Soil_Gypsum_Content) - الحد الأعلى الآمن 10.75%", min_value=0.0, max_value=100.0, value=4.2, key="f_gypsum")
        with g1:
            # تفعيل فحص المياه الجوفية حتماً إذا وجد سرداب بموجب جدول الإكسل شيت
            if has_basement_active:
                water_table = st.number_input("منسوب المياه الجوفية المستقر تحت السطح (Water_Table_Depth) - بالمتر", min_value=0.0, max_value=50.0, value=3.5, key="f_water")
            else:
                st.markdown("<div style='padding-top: 25px; text-align: right;'><p style='color: #a0b0af; margin:0;'>ℹ️ فحص المياه الجوفية محجوب لعدم وجود سرداب مصمم بالرخصة.</p></div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 🏢 الطابق الثالث: بوابة الدفع وجباية الأجور وإصدار التقارير ومنع التحايل
    st.markdown('<div class="gov-panel-box" style="border-color: #c5a059 !important; background: rgba(197, 160, 89, 0.05) !important;">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header" style="color: #c5a059 !important; border-bottom-color: #c5a059 !important;">💰 الخطوة 3: جباية أجور المطابقة الآلية وإصدار شهادة الامتثال</p>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="direction: rtl; text-align: right; margin-bottom: 15px;">
            <p style="margin: 0; font-size: 12px; color: #ffffff;">أجور عملية التدقيق والمطابقة الرقمية الفورية للفئة الحالية تبلغ: <span style="color: #c5a059; font-weight: bold; font-size: 14px;">25,000 دينار عراقي</span></p>
            <p style="margin: 3px 0 0 0; font-size: 10px; color: #52c41a;">● بوابة الدفع الإلكتروني لنقابة المهندسين (زين كاش / مصرف الرافدين) نشطة وجاهزة.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # زر تشغيل العداد الإلكتروني وجباية الأموال والتحقق
    if st.button("💳 تأكيد الدفع وتدقيق المعاملة هندسياً للمطابقة الآلية", key="gov_btn_pay_and_audit", use_container_width=True):
        st.success("✅ تم استقطاع الأجور بنجاح! جاري معايرة القراءات رقمياً وتشريعياً مع جداول الأكواد الفيدرالية...")
        st.info("💡 هنت للفريق القوي: في الخطوة القادمة، سيتم استدعاء محرك الفحص (soil_compliance_engine.py) ليقارن هذه الأرقام ديناميكياً مع ملف الإكسل المرفوع، ويطلق شهادة الامتثال الفورية أو الرفض القانوني الفاخر باللون الأحمر!")
        
    st.markdown('</div>', unsafe_allow_html=True)
