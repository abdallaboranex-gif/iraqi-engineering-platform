import streamlit as st

def show_footer_section():
    """
    الدالة المركزية المستقلة لعرض كروت قاع الشاشة والتغذية الإخبارية (صفر اعتمادية).
    تم تطهير الاستدعاءات داخلها تماماً لكسر حظر KeyError وتأمين استقرار المنصة.
    """
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("### 📰 مرصد البحوث والتعليمات الوطنية الموحد")
    
    # بناء كروت التغذية الأربعة متراصة أفقياً بنظام الأعمدة الصافية لـ Streamlit
    col_f1, col_v_uni, col_f3, col_f4 = st.columns(4)
    
    with col_f1:
        st.markdown(
            """
            <div style="background-color: rgba(7, 22, 21, 0.6); padding: 12px; border-radius: 8px; border: 1px solid rgba(197, 160, 89, 0.2); height: 110px;">
                <h5 style="color: #c5a059 !important; margin: 0 0 6px 0; font-size: 13px;">📋 إحصائيات النشر</h5>
                <p style="font-size: 11px; color: #a0b0af !important; margin: 0; line-height: 1.4;">متابعة فورية ومباشرة لمعدلات قراءة وتدقيق المدونات الهندسية الوطنية.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with col_v_uni:
        st.markdown(
            """
            <div style="background-color: rgba(7, 22, 21, 0.6); padding: 12px; border-radius: 8px; border: 1px solid rgba(197, 160, 89, 0.2); height: 110px;">
                <h5 style="color: #c5a059 !important; margin: 0 0 6px 0; font-size: 13px;">🏛️ بحوث الجامعات العراقية</h5>
                <p style="font-size: 11px; color: #a0b0af !important; margin: 0; line-height: 1.4;">تغذية مباشرة لربط نتاجات الأكاديميين مع المكاتب الاستشارية الميدانية.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with col_f3:
        st.markdown(
            """
            <div style="background-color: rgba(7, 22, 21, 0.6); padding: 12px; border-radius: 8px; border: 1px solid rgba(197, 160, 89, 0.2); height: 110px;">
                <h5 style="color: #c5a059 !important; margin: 0 0 6px 0; font-size: 13px;">🔥 مقالات هندسية شائعة</h5>
                <p style="font-size: 11px; color: #a0b0af !important; margin: 0; line-height: 1.4;">البنود والتحليلات الأكثر جردًا وتدقيقاً من قبل لجان الحوكمة البيئية.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with col_f4:
        st.markdown(
            """
            <div style="background-color: rgba(7, 22, 21, 0.6); padding: 12px; border-radius: 8px; border: 1px solid rgba(197, 160, 89, 0.2); height: 110px;">
                <h5 style="color: #c5a059 !important; margin: 0 0 6px 0; font-size: 13px;">✨ المعرفة الهندسية المستدامة</h5>
                <p style="font-size: 11px; color: #a0b0af !important; margin: 0; line-height: 1.4;">منصة فيدرالية موحدة لتعزيز مرجعية المواصفات الفنية العراقية.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
