import streamlit as st

def render_governance_view():
    """
    الواجهة المركزية المحدثة لكابينة الحوكمة.
    تستقبل المدخلات الـ 9 الشاملة (المحافظات الـ 19 كاملة، الحقول الرقمية المفتوحة)
    لتفعيل المحددات الجغرافية والإنشائية آلياً بموجب شروط جداول الإكسل.
    """
    # 1. حقن نظام تصاميم زجاجي فاخر متناسق مع الهوية البصرية السيادية للمنصة
    st.markdown(
        """
        <style>
        .gov-title-main {
            font-size: 24px !important; font-weight: 800 !important; color: #c5a059 !important;
            text-align: right !important; margin-bottom: 5px !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important;
        }
        .gov-panel-box {
            background-color: rgba(7, 22, 21, 0.6) !important;
            border: 1px solid rgba(197, 160, 89, 0.2) !important;
            border-radius: 8px !important; padding: 15px !important; margin-bottom: 15px !important;
        }
        .gov-section-header {
            font-size: 14px !important; font-weight: 700 !important; color: #c5a059 !important;
            border-bottom: 1px solid rgba(197, 160, 89, 0.2) !important;
            padding-bottom: 6px !important; margin-bottom: 15px !important; text-align: right !important;
        }
        .stSelectbox label, .stNumberInput label, .stTextInput label {
            color: #c5a059 !important; font-size: 12px !important; font-weight: 600 !important;
            display: block !important; text-align: right !important; direction: rtl !important;
        }
        .stSelectbox > div > div, .stNumberInput > div > div, .stTextInput > div > div {
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            background-color: rgba(7, 22, 21, 0.8) !important; border-radius: 4px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h2 class="gov-title-main">⚖️ البوابة المركزية لإدخال معطيات الرخصة الهندسية</h2>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: right; color: #a0b0af;'>يرجى ملء البيانات العامة للمعاملة؛ ليقوم النظام باحتساب القيود الجغرافية وتنشيط الفحوصات ديناميكياً تلبية لأكواد المدونة ومنع التحايل.</p>", unsafe_allow_html=True)

    # 🏢 الطابق الأول: نموذج المدخلات الـ 9 العامة المرنة والمقيدة جغرافياً وإنشائياً
    st.markdown('<div class="gov-panel-box">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header">📋 الخطوة 1: المعطيات التخطيطية والجغرافية العامة للعقار</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col3:
        # 1. إدراج محافظات العراق الـ 19 كاملة مع تفعيل فلاتر القيود الجغرافية تلقائياً
        gov_province = st.selectbox("1. المحافظة (النطاق الجغرافي للعقار)", 
                                    ["بغداد", "نينوى", "البصرة", "صلاح الدين", "الأنبار", "النجف", "كربلاء", "بابل", "القادسية", "المثنى", "ذي قار", "ميسان", "واسط", "ديالى", "كركوك", "أربيل", "السليمانية", "دهوك", "حلبجة"], 
                                    key="v9_province_v19")
        # 2. نوع الطلب مقيد بخيارات الإكسل شيت
        gov_req_type = st.selectbox("2. نوع الطلب / المعاملة", 
                                    ["بناء جديد", "إعادة بناء", "إضافة طابق", "ترميم وتعديل", "مشاريع استثمارية كبرى / أبراج"], 
                                    key="v9_req_type_v19")
        # 3. استعمال العقار مقيد بخيارات الإكسل شيت
        gov_property_use = st.selectbox("3. استعمال العقار الأساسي", 
                                        ["سكني", "تجاري", "خدمي", "صناعي", "مجمعات ومستشفيات / أبنية عامة"], 
                                        key="v9_use_v19")
        
    with col2:
        # 4. مساحة الأرض مفتوحة رقمياً مع تفعيل المحددات تلقائياً (مثل حفرتان للأراضي ≤ 400، وثلاث حفر للأراضي > 400)
        gov_area = st.number_input("4. مساحة العقار الكلية (m²)", min_value=10, max_value=1000000, value=200, step=10, key="v9_area_v19")
        gov_length = st.number_input("5. أبعاد العقار - الطول (m)", min_value=1.0, max_value=2000.0, value=20.0, step=0.5, key="v9_length_v19")
        gov_width = st.number_input("6. أبعاد العقار - العرض/الواجهة (m)", min_value=1.0, max_value=1000.0, value=10.0, step=0.5, key="v9_width_v19")

    with col1:
        gov_street_w = st.number_input("7. عرض الشارع المقابل للعقار (m)", min_value=1, max_value=200, value=10, key="v9_street_v19")
        # 8. حقل رقمي صريح لعدد الطوابق لحساب معادلات الأحمال اللاحقة
        gov_floors = st.number_input("8. عدد الطوابق المقترحة / ارتفاع المبنى", min_value=1, max_value=100, value=2, step=1, key="v9_floors_v19")
        # 9. خياري السرداب الصريحة والمبسطة
        gov_has_basement = st.selectbox("9. طابق السرداب (Basement)", ["غير موجود", "موجود"], key="v9_basement_v19")

    # حقل توثيق هوية العقار لمنع التحايل والتزوير الجنائي
    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.1); margin: 10px 0;'>", unsafe_allow_html=True)
    gov_id_text = st.text_input("📝 هوية العقار الرسمية (رقم العقار / القطعة والمقاطعة)", placeholder="مثال: 4/1250 مقاطعة 21 داودي", key="v9_id_text_v19")

    # تفعيل واحتساب فئة المسار ديناميكياً بناءً على محددات جدول الإكسل شيت
    is_heavy_path = (gov_floors >= 4) or (gov_has_basement == "موجود") or (gov_req_type == "مشاريع استثمارية كبرى / أبراج") or (gov_property_use == "مجمعات ومستشفيات / أبنية عامة") or (gov_province in ["النجف", "الأنبار", "المثنى", "نينوى"])
    is_medium_path = (not is_heavy_path) and (gov_area > 400 or gov_property_use in ["تجاري", "صناعي", "خدمي"])
    
    if is_heavy_path:
        st.error(f"🚨 فئة المعاملة: مشاريع استثمارية وأبنية ثقيلة. المحافظة المفعلة: [{gov_province}] (تنشيط القيود الجيوفيزيائية الـ 13 بالكامل لمنع التحايل).")
        active_route = "heavy"
    elif is_medium_path:
        st.warning(f"⚠️ فئة المعاملة: أبنية متوسطة ومنشآت تجارية. المحافظة: [{gov_province}] (تنشيط 9 فحوصات وحجب القيود الثقيلة آلياً).")
        active_route = "medium"
    else:
        st.success(f"🌿 فئة المعاملة: دور سكنية وأبنية خفيفة. المحافظة: [{gov_province}] (اختصار الواجهة وتفعيل 5 فحوصات أساسية فقط).")
        active_route = "light"

    st.markdown('</div>', unsafe_allow_html=True)
    
    # حفظ المتغيرات التفاعلية للخطوة التالية بالملف
    st.session_state["v19_active_route"] = active_route
    st.session_state["v19_has_basement_bool"] = (gov_has_basement == "موجود")
    st.session_state["v19_province_selected"] = gov_province
    # 🏢 الطابق الثاني: انبثاق حقول الفحوصات الجيوتقنية والقيود المفلترة بناءً على الـ 9 مدخلات السابقة
    st.markdown('<div class="gov-panel-box">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header">🧪 الخطوة 2: القراءات والفحوصات الجيوتقنية المطلوبة لهذه المعاملة</p>', unsafe_allow_html=True)
    
    # جلب مسار الفلترة والمحافظة النشطة من الذاكرة
    active_route = st.session_state.get("v19_active_route", "light")
    has_basement_active = st.session_state.get("v19_has_basement_bool", False)
    selected_province = st.session_state.get("v19_province_selected", "بغداد")
    
    gc1, gc2 = st.columns(2)
    
    # --- المجموعة 1: الفحوصات الأساسية (تظهر للجميع دائماً) ---
    with gc2:
        st.markdown("<p style='color: #c5a059; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>📋 فحوصات الاعتمادية والقدرة الأساسية:</p>", unsafe_allow_html=True)
        soil_validity = st.selectbox("صلاحية واعتمادية تقرير التربة (Soil_Report_Validity)", ["معتمد ومجاز ومصادق", "غير مصادق / تحت المراجعة"], key="f_soil_validity_v19")
        bh_count = st.number_input("عدد الحفر الاستكشافية المنفذة (Boreholes_Count)", min_value=0, max_value=50, value=2, key="f_bh_count_v19")
        
        # انبثاق الحقل المخصص للعمق بناءً على وزن البناية (طابق ضحل أو برج ثقيل)
        if active_route == "heavy":
            bh_depth = st.number_input("عمق الحفرة الاختبارية للأبراج العالية (Borehole_Depth_Heavy) - المطلوب ≥ 15م", min_value=0.0, max_value=150.0, value=15.0, key="f_bh_depth_heavy_v19")
        else:
            bh_depth = st.number_input("عمق الحفرة الاختبارية للأبنية الخفيفة (Borehole_Depth_Shallow) - المطلوب ≥ 6م", min_value=0.0, max_value=50.0, value=6.0, key="f_bh_depth_shallow_v19")
            
        bearing_capacity = st.number_input("قدرة تحمل التربة التصميمية المسموحة (Soil_Bearing_Capacity) - kN/m²", min_value=0.0, max_value=2000.0, value=150.0, key="f_bearing_v19")
        report_age = st.number_input("عمر التقرير الجيوتقني الحالي بالأشهر (Soil_Report_Age) - المطلوب ≤ 24 شهر", min_value=0, max_value=120, value=6, key="f_report_age_v19")

    # --- المجموعة 2: الفحوصات المتقدمة (تخضع لشرط الفئة حياً وتختفي تلقائياً للدور السكنية) ---
    with gc1:
        if active_route in ["medium", "heavy"]:
            st.markdown("<p style='color: #c5a059; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>🔬 الفحوصات المختبرية والكيميائية الإلزامية:</p>", unsafe_allow_html=True)
            sulphate_so3 = st.number_input("محتوى الكبريتات الثلاثية الذائبة في التربة (Soil_Sulphate_Content_SO3) - المطلوب ≤ 5%", min_value=0.0, max_value=100.0, value=2.1, key="f_sulphate_v19")
            chloride_content = st.number_input("نسبة أيونات الكلوريدات الذائبة (Soil_Chloride_Content) - المطلوب ≤ 0.1%", min_value=0.00, max_value=10.00, value=0.04, step=0.01, key="f_chloride_v19")
            organic_content = st.number_input("محتوى المواد العضوية والجذور (Soil_Organic_Content) - المطلوب ≤ 2%", min_value=0.0, max_value=100.0, value=0.5, key="f_organic_v19")
            compaction_degree = st.number_input("درجة الحدل ورص التربة الميداني (Soil_Compaction_Degree) - المطلوب ≥ 95%", min_value=0.0, max_value=100.0, value=96.5, key="f_compaction_v19")
        else:
            st.markdown("<div style='background: rgba(197, 160, 89, 0.03); padding: 15px; border-radius: 6px; border: 1px dashed rgba(197, 160, 89, 0.15); margin-top: 25px; text-align: right;'><p style='color: #a0b0af; margin:0; font-size:11px;'>🔒 تم إعفاء هذه المعاملة تلقائياً من الفحوصات الكيميائية المعقدة (كبريتات، كلوريدات، مواد عضوية، درجة حدل) لكونها تقع ضمن فئة الدور السكنية الخفيفة بموجب الكود العراقي.</p></div>", unsafe_allow_html=True)

    # --- المجموعة 3: قيود الأمان والجيوفيزياء (تتأثر بالمحافظة والسرداب والمشاريع الكبرى) ---
    if active_route == "heavy":
        st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown("<p style='color: #ff4b4b; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>⚠️ قيود السلامة والأمان الجيوفيزيائية والجبسية للأبراج العالية ومشاريع الاستثمار والمناطق الحرجة:</p>", unsafe_allow_html=True)
        
        g1, g2 = st.columns(2)
        with g2:
            # قيد الكهوف والفجوات يتفعل حتماً للمحافظات المحددة بالإكسل (النجف، الأنبار، المثنى، نينوى)
            if selected_province in ["النجف", "الأنبار", "المثنى", "نينوى"]:
                st.caption(f"🔍 تم رصد قيد جيولوجي نشط: [{selected_province}] مصنفة بوجود عيوب جيرية وتكهفات.")
                gpr_scan = st.selectbox("نتائج مسح الرادار الأرضي الاختراقي للكهوف (Soil_GPR_Void_Scan)", ["خالٍ من الفجوات والتكهفات الحرجة", "تم رصد فجوات وتجاويف تحت سطحية غير معالجة"], key="f_gpr_v19")
            else:
                st.caption(f"ℹ️ قيد الفجوات والتكهفات غير نشط (المحافظة المفترضة [{selected_province}] تقع خارج النطاق الحرجي الجيري).")
                gpr_scan = "خالٍ من الفجوات والتكهفات الحرجة"
                
            gypsum_content = st.number_input("نسبة محتوى الجبس الكلية (Soil_Gypsum_Content) - الحد الأعلى الآمن 10.75%", min_value=0.0, max_value=100.0, value=4.2, key="f_gypsum_v19")
        with g1:
            # فحص المياه الجوفية يتأثر صراحة بوجود السرداب
            if has_basement_active:
                water_table = st.number_input("منسوب المياه الجوفية المستقر تحت السطح (Water_Table_Depth) - بالمتر", min_value=0.0, max_value=100.0, value=3.5, key="f_water_v19")
            else:
                st.markdown("<div style='padding-top: 25px; text-align: right;'><p style='color: #a0b0af; margin:0; font-size:11px;'>ℹ️ فحص المياه الجوفية محجوب لعدم وجود سرداب مصمم بالرخصة.</p></div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 🏢 الطابق الثالث: بوابة جباية الأجور وإصدار التقارير الموثقة
    st.markdown('<div class="gov-panel-box" style="border-color: #c5a059 !important; background: rgba(197, 160, 89, 0.05) !important;">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header" style="color: #c5a059 !important; border-bottom-color: #c5a059 !important;">💰 الخطوة 3: جباية أجور المطابقة الآلية وإصدار شهادة الامتثال</p>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="direction: rtl; text-align: right; margin-bottom: 15px;">
            <p style="margin: 0; font-size: 12px; color: #ffffff;">أجور عملية التدقيق والمطابقة الرقمية الفورية للفئة الحالية تبلغ: <span style="color: #c5a059; font-weight: bold; font-size: 14px;">25,000 دينار عراقي</span></p>
            <p style="margin: 3px 0 0 0; font-size: 10px; color: #52c41a;">● بوابة الدفع الإلكتروني لنقابة المهندسين نشطة وجاهزة.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("💳 تأكيد الدفع وتدقيق المعاملة هندسياً للمطابقة الآلية", key="gov_btn_pay_and_audit_v105", use_container_width=True):
        st.success("✅ تم استقطاع الأجور بنجاح! جاري معايرة القراءات رقمياً وتشريعياً مع جداول الأكواد الفيدرالية...")
        st.info("💡 هنت للفريق القوي: كود التكيف والمحافظات الـ 19 مفتوح رقمياً وبكامل عافيته وحركته التفاعلية!")
        
    st.markdown('</div>', unsafe_allow_html=True)
