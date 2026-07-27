import streamlit as st
import pandas as pd
import os

def render_blogs_view():
    """
    الواجهة التشغيلية الكبرى لمرصد الكودات الهندسية الفيدرالية العراقية (مجلد المدونات).
    تقرأ ملفات الإكسل الخمسة حياً من مجلد database_rules وتتيح الفحص والاستعلام التفاعلي المحكم.
    """
    # 1. حقن تنسيقات زجاجية فخمة ومحاذة نصوص مخصصة للوحة البيانات لتعوم بنقاء فوق الخلفية
    st.markdown(
        """
        <style>
        .mono-card-stat {
            background-color: rgba(7, 22, 21, 0.65) !important;
            border: 1px solid rgba(197, 160, 89, 0.25) !important;
            border-radius: 10px !important;
            padding: 15px !important;
            margin-bottom: 20px !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
            backdrop-filter: blur(5px) !important;
        }
        .main-title-view {
            color: #c5a059 !important;
            font-size: 28px !important;
            font-weight: 800 !important;
            text-align: right !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.9) !important;
            margin-bottom: 5px !important;
        }
        .sub-title-view {
            color: #ffffff !important;
            font-size: 13px !important;
            text-align: right !important;
            margin-bottom: 25px !important;
            opacity: 0.85;
        }
        /* تجميل شكل جداول البيانات المرفوعة لتطابق فخامة المنصة */
        .dataframe {
            background-color: rgba(7, 22, 21, 0.8) !important;
            color: #ffffff !important;
            border: 1px solid rgba(197, 160, 89, 0.2) !important;
            font-size: 12px !important;
        }
        /* تجميل صناديق التحديد الافتراضية لـ Streamlit */
        div[data-testid="stSelectbox"] > div {
            background-color: rgba(7, 22, 21, 0.85) !important;
            color: #ffffff !important;
            border: 1px solid rgba(197, 160, 89, 0.3) !important;
            border-radius: 4px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 2. رأس وعنوان لوحة المرصد الفيدرالي
    st.markdown('<h2 class="main-title-view">🏛️ المدونات الهندسية واللوائح الفيدرالية العراقية</h2>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title-view">منظومة الفحص والاستعلام الرقمي الموحد لمدونات البناء القياسية الصادرة عن وزارة الإسكان ونقابة المهندسين</p>', unsafe_allow_html=True)

    # 3. جرد ومطابقة مسارات ملفات الإكسل الخمسة حقيقياً من مجلد database_rules
    base_db_dir = "database_rules"
    
    files_map = {
        "📐 المدونة المعمارية والسلامة من الحرائق (Architectural & Fire Safety)": "ibcp_Architectural_&_Fire_Safety.xlsx",
        "⚡ المدونة الكهربائية وكفاءة الطاقة (Electrical & Energy Efficiency)": "ibcp_Electrical_&_Energy_Efficiency.xlsx",
        "🧱 مدونة الأسس والجدران الساندة (Foundations & Retaining Walls)": "ibcp_Foundations_&_Retaining_Walls.xlsx",
        "💧 مدونة الخدمات الصحية والبيئية (Sanitary & Environmental Services)": "ibcp_Sanitary_&_Environmental_Services.xlsx",
        "🔬 لوائح وفحوصات التربة الهندسة (Soil Testing Rules)": "ibcp_soil_testing.xlsx"
    }

    # 4. بناء صندوق تحديد الكود الهندسي المراد فحص داتا ملفاته
    st.markdown("##### 🔍 اختر المصنف الهندسي المطلوب مراجعته:")
    selected_doc_name = st.selectbox(
        "", 
        options=list(files_map.keys()),
        key="v500_ultimate_blogs_selector",
        label_visibility="collapsed"
    )
    
    target_file_name = files_map[selected_doc_name]
    full_excel_path = os.path.join(base_db_dir, target_file_name)

    st.markdown("<br>", unsafe_allow_html=True)

    # 5. محرك قراءة ومعالجة البيانات الحي عبر مكتبة Pandas
    if os.path.exists(full_excel_path):
        try:
            # قراءة الإكسل شيت مع حزام أمان لمنع التجميد سحابياً
            df = pd.read_excel(full_excel_path)
            
            # تنظيف البيانات من الأسطر الفارغة تماماً
            df = df.dropna(how='all')
            
            # لوحة مؤشرات رقمية مصغرة خاصة بالملف المفتوح حالياً
            col_stat1, col_stat2 = st.columns([2, 2])
            with col_stat1:
                st.markdown(
                    f"""
                    <div class="mono-card-stat">
                        <span style="font-size: 11px; color: #a0b0af;">حالة قاعدة البيانات الحالية</span>
                        <h4 style="margin: 5px 0; color: #52c41a !important; font-size: 16px;">● متصلة ومحدثة حياً</h4>
                        <p style="font-size: 10px; color: #a0b0af; margin: 0;">الملف النشط: {target_file_name}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            with col_stat2:
                st.markdown(
                    f"""
                    <div class="mono-card-stat">
                        <span style="font-size: 11px; color: #a0b0af;">إجمالي البنود والحدود المسجلة</span>
                        <h4 style="margin: 5px 0; color: #c5a059 !important; font-size: 16px;">{len(df)} بنداً تدقيقياً</h4>
                        <p style="font-size: 10px; color: #a0b0af; margin: 0;">خاضع للتحقق القياسي الفيدرالي</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )

            # 6. شريط الفحص الداخلي الذكي داخل الجداول
            st.markdown("##### 🔎 فحص واستعلام سريع داخل البنود والجداول المرفوعة:")
            search_word = st.text_input("", placeholder="⌨️ اكتب كلمة للبحث (مثال: عزل، خرسانة، أحمال، كابلات)...", key="v500_ultimate_in_file_search", label_visibility="collapsed")
            
            # تطبيق تصفية واستعلام ديناميكي فوري بناء على كتابة المهندس
            if search_word:
                # البحث في كافة الأعمدة والنصوص دون حساسية لحجم الحروف
                mask = df.astype(str).apply(lambda x: x.str.contains(search_word, case=False, na=False)).any(axis=1)
                filtered_df = df[mask]
                st.markdown(f"📊 **نتائج الاستعلام المطابقة للكلمة ('{search_word}'):** وُجدت **{len(filtered_df)}** نتيجة.")
                if not filtered_df.empty:
                    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
                else:
                    st.warning("⚠️ لم يتم العثور على أي بنود مطابقة لهذه الكلمة داخل هذا المصنف. جرب كلمة أخرى أو مصنفاً آخر.")
            else:
                # في حالة عدم البحث، يتم عرض الجدول كاملاً بانتظام منسق وفخم
                st.markdown("📊 **استعراض كامل البيانات والمواصفات القياسية للجدول المرفوع:**")
                st.dataframe(df, use_container_width=True, hide_index=True)

        except Exception as e:
            st.error(f"⚠️ خطأ فني أثناء قراءة البيانات السحابية للإكسل شيت: {str(e)}")
            st.info("💡 تأكد من أن ملف الإكسل شيت غير تالف ومحفوظ بصيغة مصفوفة جداول قياسية.")
    else:
        st.error(f"❌ لم يتم العثور على ملف قاعدة البيانات المطلوب في مساره المعتمد: `{full_excel_path}`")
        st.info("💡 يرجى التأكد من رفع الملف بالاسم الدقيق والصحيح داخل مجلد database_rules على GitHub.")
