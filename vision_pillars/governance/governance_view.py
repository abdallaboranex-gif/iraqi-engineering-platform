import streamlit as st
import sys
import os
import pandas as pd

# إجبار نظام بايثون على إدراج المسار الجذري للمشروع لربط الغرف المفككة سحابياً
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

try:
    from soil_rules.soil_compliance_engine import load_dynamic_excel_rules, verify_soil_compliance
except Exception:
    pass

def render_governance_view():
    """
    الواجهة المركزية الكاملة والمطهرة لكابينة الحوكمة.
    تضم نظام الفوترة المرن، والتعمية الأمنية، والباركود المحلي الحقيقي والتحذير الجنائي بصفر أخطاء سنتكس.
    """
    # حقن نظام التصاميم الزجاجي الفاخر المتناسق مع الهوية المذهبة للمنصة وقهر عتمة الخطوط
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
            border: 1px solid rgba(197, 160, 89, 0.3) !important;
            border-radius: 8px !important; padding: 15px !important; margin-bottom: 15px !important;
        }
        .gov-section-header {
            font-size: 14px !important; font-weight: 700 !important; color: #c5a059 !important;
            border-bottom: 1px solid rgba(197, 160, 89, 0.3) !important;
            padding-bottom: 6px !important; margin-bottom: 15px !important; text-align: right !important;
        }
        .stSelectbox label, .stNumberInput label, .stTextInput label {
            color: #c5a059 !important; font-size: 12px !important; font-weight: 600 !important;
            display: block !important; text-align: right !important; direction: rtl !important;
        }
        
        .stSelectbox > div > div, .stNumberInput > div > div, .stTextInput > div > div {
            border: 1px solid rgba(197, 160, 89, 0.5) !important;
            background-color: rgba(7, 22, 21, 0.95) !important; border-radius: 4px !important;
        }
        
        .stSelectbox div[data-baseweb="select"] div,
        .stSelectbox div[data-baseweb="select"] span,
        .stSelectbox div[data-testid="stMarkdownContainer"] p,
        .stSelectbox div[aria-selected="true"],
        .stSelectbox select,
        .stSelectbox div,
        .stSelectbox span,
        .stNumberInput input, 
        .stTextInput input,
        div[role="listbox"] li,
        div[role="listbox"] div,
        div[role="option"],
        div[role="option"] span,
        div[data-baseweb="menu"] div,
        div[data-baseweb="menu"] span,
        div[data-baseweb="menu"] li {
            color: #ffffff !important; font-weight: 700 !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.9) !important;
            -webkit-text-fill-color: #ffffff !important;
        }
        
        div[data-baseweb="menu"], div[role="listbox"], ul[role="listbox"] {
            background-color: #071615 !important; background: #071615 !important;
            border: 1px solid #c5a059 !important; box-shadow: 0 8px 25px rgba(0,0,0,0.9) !important; border-radius: 6px;
        }
        div[role="listbox"] li, div[role="option"], div[data-baseweb="menu"] div, div[data-baseweb="menu"] li {
            background-color: #071615 !important; background: #071615 !important; padding: 8px 12px !important; text-align: right !important; direction: rtl !important;
        }
        button[data-testid="stNumberInputStepUp"], button[data-testid="stNumberInputStepDown"] {
            background-color: rgba(197, 160, 89, 0.15) !important; color: #ffffff !important;
        }
        button[data-testid="stNumberInputStepUp"] svg, button[data-testid="stNumberInputStepDown"] svg, .stSelectbox svg {
            fill: #ffffff !important; color: #ffffff !important; stroke: #ffffff !important;
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

    # 🏢 الخطوة 1: نموذج المدخلات العامة المصفّرة والمقيدة بـ "اختر بنداً..." لمنع العبور العشوائي
    st.markdown('<div class="gov-panel-box">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header">📋 الخطوة 1: المعطيات التخطيطية والجغرافية العامة للعقار</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col3:
        gov_province = st.selectbox("1. المحافظة (النطاق الجغرافي للعقار)", ["اختر بنداً...", "بغداد", "نينوى", "البصرة", "صلاح الدين", "الأنبار", "النجف", "كربلاء", "بابل", "القادسية", "المثنى", "ذي قار", "ميسان", "واسط", "ديالى", "كركوك", "أربيل", "السليمانية", "دهوك", "حلبجة"], key="v9_prov_final_v10")
        gov_req_type = st.selectbox("2. نوع الطلب / المعاملة", ["اختر بنداً...", "بناء جديد", "إعادة بناء", "إضافة طابق", "ترميم وتعديل", "مشاريع استثمارية كبرى / أبراج"], key="v9_req_final_v10")
        gov_property_use = st.selectbox("3. استعمال العقار الأساسي", ["اختر بنداً...", "سكني", "تجاري", "خدمي", "صناعي", "مجمعات ومستشفيات / أبنية عامة"], key="v9_use_final_v10")
    with col2:
        gov_area = st.number_input("4. مساحة العقار الكلية (m²)", min_value=0, max_value=1000000, value=0, step=10, key="v9_area_final_v10")
        gov_length = st.number_input("5. أبعاد العقار - الطول (m)", min_value=0.0, max_value=2000.0, value=0.0, step=0.5, key="v9_length_final_v10")
        gov_width = st.number_input("6. أبعاد العقار - العرض/الواجهة (m)", min_value=0.0, max_value=1000.0, value=0.0, step=0.5, key="v9_width_final_v10")
    with col1:
        gov_street_w = st.number_input("7. عرض الشارع المقابل للعقار (m)", min_value=0, max_value=200, value=0, key="v9_street_final_v10")
        gov_floors = st.number_input("8. عدد الطوابق المقترحة / ارتفاع المبنى", min_value=0, max_value=100, value=0, step=1, key="v9_floors_final_v10")
        gov_has_basement = st.selectbox("9. طابق السرداب (Basement)", ["اختر بنداً...", "غير موجود", "موجود"], key="v9_basement_final_v10")

    st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.1); margin: 10px 0;'>", unsafe_allow_html=True)
    gov_id_text = st.text_input("📝 هوية العقار الرسمية (رقم العقار / القطعة والمقاطعة)", placeholder="مثال: 4/1250 مقاطعة 21 داودي", key="v9_id_text_final_v10")

    is_heavy_path = (gov_floors >= 4) or (gov_has_basement == "موجود") or (gov_req_type == "مشاريع استثمارية كبرى / أبراج") or (gov_property_use == "مجمعات ومستشفيات / أبنية عامة") or (gov_province in ["النجف", "الأنبار", "المثنى", "نينوى"])
    is_medium_path = (not is_heavy_path) and (gov_area > 400 or gov_property_use in ["تجاري", "صناعي", "خدمي"])
    
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
    # 🏢 الخطوة 2: فرد وحجب الفحوصات الجيوتقنية المطهرة والعمياء تماماً لمنع التزوير
    st.markdown('<div class="gov-panel-box">', unsafe_allow_html=True)
    st.markdown('<p class="gov-section-header">🧪 الخطوة 2: القراءات والفحوصات الجيوتقنية المطلوبة لهذه المعاملة</p>', unsafe_allow_html=True)
    
    if active_route == "locked":
        st.markdown("<div style='background: rgba(197, 160, 89, 0.02); padding: 20px; border-radius: 6px; border: 1px dashed rgba(197, 160, 89, 0.15); text-align: right;'><p style='color: #a0b0af; margin:0; font-size:12px;'>⚠️ الرجاء إكمال معطيات الرخصة والخطوة الأولى بالكامل بالأعلى لتنشيط وفرد الحقول الجيوتقنية المطابقة لحالتك.</p></div>", unsafe_allow_html=True)
    else:
        gc1, gc2 = st.columns(2)
        with gc2:
            st.markdown("<p style='color: #c5a059; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>📋 فحوصات الاعتمادية والقدرة الأساسية للعقار:</p>", unsafe_allow_html=True)
            soil_validity = st.selectbox("صلاحية واعتمادية تقرير التربة (Soil_Report_Validity)", ["معتمد ومجاز ومصادق", "غير مصادق / تحت المراجعة"], key="f_sv_final_v10")
            bh_count = st.number_input("عدد الحفر الاستكشافية المنفذة في الموقع (Boreholes_Count)", min_value=0, max_value=50, value=0, key="f_bc_final_v10")
            
            if active_route == "heavy":
                bh_depth = st.number_input("عمق الحفرة الاختبارية المنفذة للأبراج العالية (Borehole_Depth_Heavy) - متر", min_value=0.0, max_value=150.0, value=0.0, key="f_bdh_final_v10")
            else:
                bh_depth = st.number_input("عمق الحفرة الاختبارية المنفذة للأبنية الخفيفة (Borehole_Depth_Shallow) - متر", min_value=0.0, max_value=50.0, value=0.0, key="f_bds_final_v10")
                
            bearing_capacity = st.number_input("قدرة تحمل التربة التصميمية المسموحة المعتمدة (Soil_Bearing_Capacity) - kN/m²", min_value=0.0, max_value=2000.0, value=0.0, key="f_bc_cap_final_v10")
            report_age = st.number_input("عمر التقرير الجيوتقني الحالي من تاريخ الإصدار (Soil_Report_Age) - بالأشهر", min_value=0, max_value=120, value=0, key="f_ra_final_v10")

        with gc1:
            if active_route in ["medium", "heavy"]:
                st.markdown("<p style='color: #c5a059; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>🔬 الفحوصات المختبرية والكيميائية الإلزامية للتربة:</p>", unsafe_allow_html=True)
                sulphate_so3 = st.number_input("محتوى الكبريتات الثلاثية الذائبة في التربة (Soil_Sulphate_Content_SO3) - %", min_value=0.0, max_value=100.0, value=0.0, key="f_so3_final_v10")
                chloride_content = st.number_input("نسبة أيونات الكلوريدات الذائبة في موقع التأسيس (Soil_Chloride_Content) - %", min_value=0.00, max_value=10.00, value=0.00, step=0.01, key="f_cl_final_v10")
                organic_content = st.number_input("محتوى المواد العضوية والجذور الكلية (Soil_Organic_Content) - %", min_value=0.0, max_value=100.0, value=0.0, key="f_org_final_v10")
                compaction_degree = st.number_input("درجة الحدل ورص التربة الميداني لطبقات الأساس (Soil_Compaction_Degree) - %", min_value=0.0, max_value=100.0, value=0.0, key="f_cd_final_v10")
            else:
                st.markdown("<div style='background: rgba(197, 160, 89, 0.03); padding: 15px; border-radius: 6px; border: 1px dashed rgba(197, 160, 89, 0.15); margin-top: 25px; text-align: right;'><p style='color: #a0b0af; margin:0; font-size:11px;'>🔒 تم إعفاء هذه المعاملة تلقائياً من الفحوصات الكيميائية المعقدة بموجب محددات الكود القياسي العراقي.</p></div>", unsafe_allow_html=True)

        if active_route == "heavy":
            st.markdown("<hr style='border-color: rgba(197, 160, 89, 0.15); margin: 10px 0;'>", unsafe_allow_html=True)
            st.markdown("<p style='color: #ff4b4b; font-weight: bold; font-size: 12px; margin-bottom: 5px; text-align: right;'>⚠️ قيود السلامة والأمان الجيوفيزيائية والجبسية للأبراج العالية ومشاريع الاستثمار:</p>", unsafe_allow_html=True)
            g1, g2 = st.columns(2)
            with g2:
                if gov_province in ["النجف", "الأنبار", "المثنى", "نينوى"]:
                    st.caption(f"🔍 قيد جيولوجي نشط: [{gov_province}] مصنفة بوجود عيوب جيرية وتكهفات.")
                    gpr_scan = st.selectbox("نتائج مسح الرادار الأرضي الاختراقي للكهوف والكهوف الجيرية (Soil_GPR_Void_Scan)", ["خالٍ من الفجوات والتكهفات الحرجة", "تم رصد فجوات وتجاويف تحت سطحية غير معالجة"], key="f_gpr_final_v10")
                else:
                    gpr_scan = "خالٍ من الفجوات والتكهفات الحرجة"
                gypsum_content = st.number_input("نسبة محتوى الجبس الكلية لطبقات التربة السطحية (Soil_Gypsum_Content) - %", min_value=0.0, max_value=100.0, value=0.0, key="f_gyp_final_v10")
            with g1:
                if gov_has_basement == "موجود":
                    water_table = st.number_input("منسوب المياه الجوفية المستقر تحت السطح (Water_Table_Depth) - بالمتر", min_value=0.0, max_value=100.0, value=0.0, key="f_wt_final_v10")
                else:
                    st.markdown("<div style='padding-top: 25px; text-align: right;'><p style='color: #a0b0af; margin:0; font-size:11px;'>ℹ️ فحص المياه الجوفية محجوب لعدم وجود سرداب.</p></div>", unsafe_allow_html=True)
