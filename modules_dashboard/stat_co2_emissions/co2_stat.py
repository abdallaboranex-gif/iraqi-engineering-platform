import streamlit as st

def render_co2_stat():
    """
    برنامج مستقل لعرض كمية انبعاثات ثاني أكسيد الكربون المخفضة في العراق.
    """
    st.metric(
        label="📉 انبعاثات CO₂ المخفضة سحابياً",
        value="2.4 مليون طن",
        delta="🪹 مستدام طبقاً للكود البيئي",
        delta_color="normal"
    )
