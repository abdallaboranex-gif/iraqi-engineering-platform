import streamlit as st
import sys
import os

# حقن مسار المجلد الجذري لضمان استدعاء المحرك من غرفته المعزولة soil_rules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

try:
    from database_rules.soil_rules.soil_compliance_engine import load_dynamic_excel_rules, verify_soil_compliance
except Exception:
    pass

def render_governance_view():
    """
    الواجهة المركزية المحدثة لكابينة الحوكمة.
    تم تصفير كافة الحقول القياسية، وحقن خيار "اختر بنداً..."، وتفتيح ألوان النصوص المدخلة لتصبح بيضاء مقروءة 100%.
    """
    # 1. حقن نظام تصاميم زجاجي فاخر مطور لتفتيح خطوط الكتابة داخل المربعات ومنع الغامق
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
            background-color: rgba(7, 22, 21, 0.85) !important; border-radius: 4px !important;
        }
        
        /* 🎯 كود حقن تفتيح الخطوط: إجبار الكلمات والأرقام المدخلة داخل المربعات على التلون بالأبيض الناصع المقروء */
        .stSelectbox div[data-testid="stMarkdownContainer"] p, 
        .stNumberInput input, 
        .stTextInput input,
        div[role="listbox"] li,
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] div {
            color: #ffffff !important;
            font-weight: 600 !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8) !important;
            -webkit-text-fill-color: #ffffff !important; /* قهر المتصفحات الذكية التي تقفل اللون */
        }
        
        .premium-violation-card {
            background-color: rgba(139, 0, 0, 0.15) !important;
            border: 1px solid #ff4b4b !important; border-right: 5px solid #ff4b4b !important;
            border-radius: 6px !important; padding: 15px !important; margin-bottom: 15px !important;
            text-align: right !important; direction: rtl !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h2 class="gov-title-main">⚖️ البوابة المركزية لإدخال معطيات الرخصة الهندسية</h2>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: right; color: #a0b0af;'>يرجى ملء البيانات العامة للمعاملة؛ ليقوم النظام باحتساب القيود الجغرافية وتنشيط الفحوصات ديناميكياً تلبية لأكواد المدونة ومنع التحايل.</p>", unsafe_allow_html=True)

    # 🏢 الطابق الأول: نموذج المدخلات الـ 9 المصفّرة والمقيدة بـ "اختر بنداً..." لمنع العبور العشوائي
    st.markdown('<div class="gov-panel-box">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header">📋 الخطوة 1: المعطيات التخطيطية والجغرافية العامة للعقار</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col3:
        # حقن خيار "اختر بنداً..." لتقييد الاختيار المسبق للمحافظات الـ 19
        gov_province = st.selectbox("1. المحافظة (النطاق الجغرافي للعقار)", ["اختر بنداً...", "بغداد", "نينوى", "البصرة", "صلاح الدين", "الأنبار", "النجف", "كربلاء", "بابل", "القادسية", "المثنى", "ذي قار", "ميسان", "واسط", "ديالى", "كركوك", "أربيل", "السليمانية", "دهوك", "حلبجة"], key="v9_prov_v7")
        gov_req_type = st.selectbox("2. نوع الطلب / المعاملة", ["اختر بنداً...", "بناء جديد", "إعادة بناء", "إضافة طابق", "ترميم وتعديل", "مشاريع استثمارية كبرى / أبراج"], key="v9_req_v7")
        gov_property_use = st.selectbox("3. استعمال العقار الأساسي", ["اختر بنداً...", "سكني", "تجاري", "خدمي", "صناعي", "مجمعات ومستشفيات / أبنية عامة"], key="v9_use_v7")
    with col2:
        # تصفير العدادات الرقمية بالكامل بجعل القيمة المبدئية للـ value تساوي 0
        gov_area = st.number_input("4. مساحة العقار الكلية (m²)", min_value=0, max_value=1000000, value=0, step=10, key="v9_area_v7")
        gov_length = st.number_input("5. أبعاد العقار - الطول (m)", min_value=0.0, max_value=2000.0, value=0.0, step=0.5, key="v9_length_v7")
        gov_width = st.number_input("6. أبعاد العقار - العرض/الواجهة (m)", min_value=0.0, max_value=1000.0, value=0.0, step=0.5, key="v9_width_v7")
    with col1:
        gov_street_w = st.number_input("7. عرض الشارع المقابل للعقار (m)", min_value=0, max_value=200, value=0, key="v9_street_v7")
        gov_floors = st.number_input("8. عدد الطوابق المقترحة / ارتفاع المبنى", min_value=0, max_value=100, value=0, step=1, key="v9_floors_v7")
        gov_has_basement = st.selectbox("9. طابق السرداب (Basement)", ["اختر بنداً...", "غير موجود", "موجود"], key="v9_basement_v7")

    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.1); margin: 10px 0;'>", unsafe_allow_html=True)
    gov_id_text = st.text_input("📝 هوية العقار الرسمية (رقم العقار / القطعة والمقاطعة)", placeholder="مثال: 4/1250 مقاطعة 21 داودي", key="v9_id_text_v7")

    # احتساب الفئة والمسار آلياً بناءً على الشروط الصارمة لجدول الإكسل
    is_heavy_path = (gov_floors >= 4) or (gov_has_basement == "موجود") or (gov_req_type == "مشاريع استثمارية كبرى / أبراج") or (gov_property_use == "مجمعات ومستشفيات / أبنية عامة") or (gov_province in ["النجف", "الأنبار", "المثنى", "نينوى"])
    is_medium_path = (not is_heavy_path) and (gov_area > 400 or gov_property_use in ["تجاري", "صناعي", "خدمي"])
    
    # حزام أمان يعطل احتساب المسار أو تفعيل الفحوصات ما دامت البنود معلقة على خيار "اختر بنداً..." أو المساحة صفر
    if gov_province == "اختر بنداً..." or gov_req_type == "اختر بنداً..." or gov_property_use == "اختر بنداً..." or gov_has_basement == "اختر بنداً..." or gov_area == 0:
        st.info("💡 في انتظار تحديد بنود الرخصة ومعطيات العقار العامة لتنشيط مسار الفحص والمدونات...")
        active_route = "locked"
    else:
        if is_heavy_path:
            st.error(f"🚨 فئة المعاملة: مشاريع استثمارية وأبنية ثقيلة. المحافظة المفعلة: [{gov_province}] (تنشيط كافة الفحوصات الـ 13).")
            active_route = "heavy"
        elif is_medium_path:
            st.warning(f"⚠️ فئة المعاملة: أبنية متوسطة ومنشآت تجارية. المحافظة: [{gov_province}] (تنشيط 9 فحوصات).")
            active_route = "medium"
        else:
            st.success(f"🌿 فئة المعاملة: دور سكنية وأبنية خفيفة. المحافظة: [{gov_province}] (تنشيط 5 فحوصات أساسية فقط).")
            active_route = "light"
            
    st.markdown('</div>', unsafe_allow_html=True)
    # 🏢 الطابق الثاني: انبثاق حقول الفحوصات الجيوتقنية والقيود المفلترة بناءً على معطيات البوابة التمهيدية
    st.markdown('<div class="gov-panel-box">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header">🧪 الخطوة 2: القراءات والفحوصات الجيوتقنية المطلوبة لهذه المعاملة</p>', unsafe_allow_html=True)
    
    # حجب وعزل الفحوصات بالكامل طالما أن البوابة التمهيدية معلقة على خيار "اختر بنداً..."
    if active_route == "locked":
        st.markdown("<div style='background: rgba(197, 160, 89, 0.02); padding: 20px; border-radius: 6px; border: 1px dashed rgba(197, 160, 89, 0.15); text-align: right;'><p style='color: #a0b0af; margin:0; font-size:12px;'>⚠️ الرجاء إكمال معطيات الرخصة والخطوة الأولى بالكامل بالأعلى (تحديد المحافظة، نوع الطلب، الاستعمال، وتصفير المساحة) لكي يتم تنشيط وفرد الحقول الجيوتقنية المطابقة لحالتك.</p></div>", unsafe_allow_html=True)
    else:
        gc1, gc2 = st.columns(2)
        
        # --- المجموعة 1: الفحوصات الأساسية (تظهر للجميع دائماً) ---
        with gc2:
            st.markdown("<p style='color: #c5a059; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>📋 فحوصات الاعتمادية والقدرة الأساسية:</p>", unsafe_allow_html=True)
            soil_validity = st.selectbox("صلاحية واعتمادية تقرير التربة (Soil_Report_Validity)", ["معتمد ومجاز ومصادق", "غير مصادق / تحت المراجعة"], key="f_sv_final_v7")
            bh_count = st.number_input("عدد الحفر الاستكشافية المنفذة (Boreholes_Count)", min_value=0, max_value=50, value=0, key="f_bc_final_v7") # تصفير القيمة الابتدائية إلى 0
            
            if active_route == "heavy":
                bh_depth = st.number_input("عمق الحفرة الاختبارية للأبراج العالية (Borehole_Depth_Heavy) - المطلوب ≥ 15م", min_value=0.0, max_value=150.0, value=0.0, key="f_bdh_final_v7")
            else:
                bh_depth = st.number_input("عمق الحفرة الاختبارية للأبنية الخفيفة (Borehole_Depth_Shallow) - المطلوب ≥ 6م", min_value=0.0, max_value=50.0, value=0.0, key="f_bds_final_v7")
                
            bearing_capacity = st.number_input("قدرة تحمل التربة التصميمية المسموحة (Soil_Bearing_Capacity) - kN/m²", min_value=0.0, max_value=2000.0, value=0.0, key="f_bc_cap_final_v7")
            report_age = st.number_input("عمر التقرير الجيوتقني الحالي بالأشهر (Soil_Report_Age) - المطلوب ≤ 24 شهر", min_value=0, max_value=120, value=0, key="f_ra_final_v7")

        # --- المجموعة 2: الفحوصات المتقدمة (تظهر للمتوسط والثقيل وتختفي تلقائياً للدور السكنية) ---
        with gc1:
            if active_route in ["medium", "heavy"]:
                st.markdown("<p style='color: #c5a059; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>🔬 الفحوصات المختبرية والكيميائية الإلزامية:</p>", unsafe_allow_html=True)
                sulphate_so3 = st.number_input("محتوى الكبريتات الثلاثية الذائبة في التربة (Soil_Sulphate_Content_SO3) - المطلوب ≤ 5%", min_value=0.0, max_value=100.0, value=0.0, key="f_so3_final_v7")
                chloride_content = st.number_input("نسبة أيونات الكلوريدات الذائبة (Soil_Chloride_Content) - المطلوب ≤ 0.1%", min_value=0.00, max_value=10.00, value=0.00, step=0.01, key="f_cl_final_v7")
                organic_content = st.number_input("محتوى المواد العضوية والجذور (Soil_Organic_Content) - المطلوب ≤ 2%", min_value=0.0, max_value=100.0, value=0.0, key="f_org_final_v7")
                compaction_degree = st.number_input("درجة الحدل ورص التربة الميداني (Soil_Compaction_Degree) - المطلوب ≥ 95%", min_value=0.0, max_value=100.0, value=0.0, key="f_cd_final_v7")
            else:
                st.markdown("<div style='background: rgba(197, 160, 89, 0.03); padding: 15px; border-radius: 6px; border: 1px dashed rgba(197, 160, 89, 0.15); margin-top: 25px; text-align: right;'><p style='color: #a0b0af; margin:0; font-size:11px;'>🔒 تم إعفاء هذه المعاملة تلقائياً من الفحوصات الكيميائية المعقدة بموجب الكود العراقي.</p></div>", unsafe_allow_html=True)

        # --- المجموعة 3: قيود الأمان والجيوفيزياء (تتأثر صراحة بالمحافظة والسرداب والمشاريع الكبرى) ---
        if active_route == "heavy":
            st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin: 10px 0;'>", unsafe_allow_html=True)
            st.markdown("<p style='color: #ff4b4b; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>⚠️ قيود السلامة والأمان الجيوفيزيائية والجبسية للأبراج العالية ومشاريع الاستثمار:</p>", unsafe_allow_html=True)
            g1, g2 = st.columns(2)
            with g2:
                if gov_province in ["النجف", "الأنبار", "المثنى", "نينوى"]:
                    st.caption(f"🔍 قيد جيولوجي نشط: [{gov_province}] مصنفة بوجود عيوب جيرية وتكهفات.")
                    gpr_scan = st.selectbox("نتائج مسح الرادار الأرضي الاختراقي للكهوف (Soil_GPR_Void_Scan)", ["خالٍ من الفجوات والتكهفات الحرجة", "تم رصد فجوات وتجاويف تحت سطحية غير معالجة"], key="f_gpr_final_v7")
                else:
                    st.caption(f"ℹ️ قيد الفجوات غير نشط في محافظة [{gov_province}].")
                    gpr_scan = "خالٍ من الفجوات والتكهفات الحرجة"
                gypsum_content = st.number_input("نسبة محتوى الجبس الكلية (Soil_Gypsum_Content) - الحد الأعلى الآمن 10.75%", min_value=0.0, max_value=100.0, value=0.0, key="f_gyp_final_v7")
            with g1:
                if gov_has_basement == "موجود":
                    water_table = st.number_input("منسوب المياه الجوفية المستقر تحت السطح (Water_Table_Depth) - بالمتر", min_value=0.0, max_value=100.0, value=0.0, key="f_wt_final_v7")
                else:
                    st.markdown("<div style='padding-top: 25px; text-align: right;'><p style='color: #a0b0af; margin:0; font-size:11px;'>ℹ️ فحص المياه الجوفية محجوب لعدم وجود سرداب.</p></div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 🏢 الطابق الثالث: بوابة جباية أجور عملية المطابقة الإلكترونية الفورية
        st.markdown('<div class="gov-panel-box" style="border-color: #c5a059 !important; background: rgba(197, 160, 89, 0.05) !important;">', unsafe_allow_html=True)
        st.markdown('<p class="gov-section-header" style="color: #c5a059 !important; border-bottom-color: #c5a059 !important;">💰 الخطوة 3: جباية أجور المطابقة الآلية وإصدار شهادة الامتثال</p>', unsafe_allow_html=True)
        st.markdown('<div style="direction: rtl; text-align: right; margin-bottom: 15px;"><p style="margin: 0; font-size: 12px; color: #ffffff;">أجور عملية التدقيق والمطابقة الرقمية الفورية تبلغ: <span style="color: #c5a059; font-weight: bold; font-size: 14px;">25,000 دينار عراقي</span></p><p style="margin: 3px 0 0 0; font-size: 10px; color: #52c41a;">● بوابة الدفع الإلكتروني لنقابة المهندسين نشطة وجاهزة.</p></div>', unsafe_allow_html=True)
        
        if st.button("💳 تأكيد الدفع وتدقيق المعاملة هندسياً للمطابقة الآلية", key="gov_btn_pay_final_v7", use_container_width=True):
            st.success("✅ تم استقطاع الأجور بنجاح! جاري معايرة القراءات ميكانيكياً مع شيت الإكسل...")
            
            # 1. تجميع المدخلات المفتوحة والمصفرة أمام المستخدم لإرسالها للمحرك
            input_data = {
                "Soil_Report_Validity": soil_validity,
                "Boreholes_Count": bh_count,
                "Soil_Bearing_Capacity": bearing_capacity,
                "Soil_Report_Age": report_age
            }
            if active_route == "heavy":
                input_data["Borehole_Depth_Heavy"] = bh_depth
                input_data["Soil_Gypsum_Content"] = gypsum_content
                if gov_province in ["النجف", "الأنبار", "المثنى", "نينوى"]:
                    input_data["Soil_GPR_Void_Scan"] = gpr_scan
                if gov_has_basement == "موجود":
                    input_data["Water_Table_Depth"] = water_table
            else:
                input_data["Borehole_Depth_Shallow"] = bh_depth
                
            if active_route in ["medium", "heavy"]:
                input_data["Soil_Sulphate_Content_SO3"] = sulphate_so3
                input_data["Soil_Chloride_Content"] = chloride_content
                input_data["Soil_Organic_Content"] = organic_content
                input_data["Soil_Compaction_Degree"] = compaction_degree

            # 2. استدعاء المحرك المركزي وقراءة الإكسل شيت حياً من مجلد soil_rules الجديد
            try:
                excel_rules = load_dynamic_excel_rules()
                audit_report = verify_soil_compliance(input_data, excel_rules)
                
                # 3. بث النتيجة وتوليد كروت الرفض الجنائية بالأبيض المقروء الفخم في حال التحايل
                if audit_report["status"] == "PASS":
                    st.balloons()
                    st.success("🎉 ممتاز! المعاملة مطابقة تماماً للمواصفات والضوابط العراقية المعتمدة لعام 2026. تم إصدار شهادة الامتثال الإلكترونية بنجاح.")
                else:
                    st.error("🛑 تم رفض تصديق المعاملة! تم رصد تحايل أو قراءات هندسية مخالفة للحدود المسموحة قانوناً.")
                    
                    # طباعة كل مخالفة مسجلة بداخل كارت أحمر فاخر مستخرج مباشرة من الإكسل وبنصوص بيضاء ناصعة
                    for violation in audit_report["violations"]:
                        st.markdown(
                            f"""
                            <div class="premium-violation-card">
                                <h4 style="color: #ff4b4b !important; margin: 0 0 8px 0; font-size: 14px; font-weight: bold;">🚨 بند المخالفة الرقابي: {violation['title']}</h4>
                                <p style="margin: 4px 0; font-size: 12px; color: #ffffff; -webkit-text-fill-color: #ffffff !important;"><strong style="color: #ff4b4b;">⚠️ لغة المواطن:</strong> {violation['citizen']}</p>
                                <p style="margin: 4px 0; font-size: 11px; color: #ffffff; -webkit-text-fill-color: #ffffff !important;"><strong style="color: #c5a059;">⚙️ المعايرة الإنشائية (لغة هندسية):</strong> {violation['engineer']}</p>
                                <p style="margin: 4px 0; font-size: 12px; color: #ffffff; -webkit-text-fill-color: #ffffff !important;"><strong style="color: #52c41a;">🔧 رسالة الإصلاح والتوجيه الإلزامي:</strong> {violation['fix']}</p>
                                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 4px; margin-top: 8px; border-right: 3px solid #ff4b4b;">
                                    <p style="margin: 0; font-size: 11px; color: #ff4b4b; font-weight: bold;">⚖️ العقوبة القانونية والأثر الجزائي المرتبط:</p>
                                    <p style="margin: 4px 0 0 0; font-size: 11px; color: #ffffff; line-height: 1.4; -webkit-text-fill-color: #ffffff !important;">{violation['penalty']}</p>
                                    <p style="margin: 4px 0 0 0; font-size: 10px; color: #c5a059;">🔗 المرجع: {violation['code']} | الحاكم: {violation['law']}</p>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            except Exception as e:
                st.error(f"⚠️ فشل في سحب ومعايرة البيانات من محرك الفحص المعزول: {str(e)}")
                
        st.markdown('</div>', unsafe_allow_html=True)
