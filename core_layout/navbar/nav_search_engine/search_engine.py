import streamlit as st
import pandas as pd
import os

def render_search_engine():
    """برنامج مستقل للبحث السريع والمباشر داخل مكتبات الإكسل شيت الخمسة للكود العراقي."""
    search_query = st.text_input("🔍 ابحث في الكودات الهندسية العراقية (أدخل كلمة مفتاحية):", key="nav_search_input", placeholder="مثال: أسس، جدران، عزل، أحمال...")
    
    if search_query:
        db_path = "database_rules/"
        found_results = False
        
        if os.path.exists(db_path):
            # مسح المجلد للبحث في كل ملفات الإكسل شيت المرفوعة
            for file in os.listdir(db_path):
                if file.endswith(".xlsx"):
                    try:
                        df = pd.read_excel(os.path.join(db_path, file))
                        # البحث في النصوص والأسطر بملف الإكسل
                        mask = df.astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
                        results = df[mask]
                        
                        if not results.empty:
                            st.markdown(f"##### 📋 نتائج من مكتبة: `{file.replace('ibcp_', '').replace('.xlsx', '')}`")
                            st.dataframe(results.head(5)) # عرض أول 5 أسطر مطابقة
                            found_results = True
                    except Exception:
                        continue
            
            if not found_results:
                st.info("ℹ️ لم يتم العثور على نتائج تطابق الكلمة المدخلة في المكتبات الخمسة الحالية.")
        else:
            st.warning("⚠️ مجلد قواعد البيانات database_rules غير متوفر حالياً.")
