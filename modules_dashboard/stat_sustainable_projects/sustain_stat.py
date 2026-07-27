import streamlit as st

def render_sustain_stat():
    """
    برنامج مستقل لعرض النسبة المئوية للمشاريع المستدامة المسجلة بالعراق.
    """
    st.metric(
        label="🌿 نسبة مشاريع الاستدامة الوطنية",
        value="36%",
        delta="+4.2% مقارنة بالعام الماضي",
        delta_color="normal"
    )
