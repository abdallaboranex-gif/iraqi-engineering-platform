import streamlit as st

def render_smart_cities_view():
    """
    برنامج مستقل لعرض رؤية المدن الذكية في العراق ودعاية الشركات الاستثمارية.
    """
    st.markdown("## 🏙️ مظلة المدن الذكية المستدامة")
    st.write("استعراض الخطط الاستراتيجية والمشاريع العمرانية الحديثة الملتزمة بمعايير المدن الذكية في العراق.")
    
    # قسم رؤية الحكومة والدولة
    st.markdown("### 🏛️ الرؤية الوطنية والخطط الرسمية")
    st.info("🎯 رؤية وزارة التخطيط 2030: التحول الرقمي الشامل للبنى التحتية وفك الاختناقات المرورية في المحافظات عبر نظم المرور الذكية وتوسعة المدن الجديدة (مثل مدينة الجواهري ومدينة علي الوردي).")
    
    # قسم استعراض مشاريع الشركات (المساحة الدعائية)
    st.markdown("### 🏗️ معرض مشاريع الشركات الاستثمارية الداعمة")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div style="background-color: rgba(13, 35, 33, 0.7); padding: 15px; border-radius: 8px; border-top: 3px solid #c5a059;">
                <h4 style="margin: 0; color: #c5a059 !important;">🏢 مجمع بوابات بغداد السكني</h4>
                <p style="font-size: 13px; color: #a0b0af !important;">المطور: شركة الاستثمارات العمرانية المحدودة</p>
                <p style="font-size: 12px; margin: 0;">مشروع سكني يعتمد شبكة تصريف مياه ذكية ونظم عزل حراري متكاملة ومطابقة للكود العراقي.</p>
            </div>
            """, unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div style="background-color: rgba(13, 35, 33, 0.7); padding: 15px; border-radius: 8px; border-top: 3px solid #c5a059;">
                <h4 style="margin: 0; color: #c5a059 !important;">⚡ مدينة بسماية الجديدة (الطور الذكي)</h4>
                <p style="font-size: 13px; color: #a0b0af !important;">الجهة: الهيئة الوطنية للاستثمار</p>
                <p style="font-size: 12px; margin: 0;">إدخال منظومات العدادات الذكية للكهرباء والماء وأتمتة إدارة النفايات بالتعاون مع مراكز الأبحاث الجامعية.</p>
            </div>
            """, unsafe_allow_html=True
        )
