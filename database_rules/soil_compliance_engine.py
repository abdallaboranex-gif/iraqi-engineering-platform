import os
import pandas as pd
import streamlit as st

def load_dynamic_excel_rules(file_name="ibcp_soil_testing.xlsx"):
    """
    دالة ذكية لقراءة ملف الإكسل الجذري ميكانيكياً وتحويل الصفوف الحاكمة 
    إلى مصفوفة برمجية ديناميكية (Dictionary) دون تثبيت النصوص يدوياً.
    """
    rules_dict = {}
    try:
        # تحديد مسار ملف الإكسل ميكانيكياً داخل مجلد database_rules
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, file_name)
        
        # إذا لم يجد الملف بالمسار المعزول يذهب للمسار الاحتياطي بالجذر
        if not os.path.exists(file_path):
            file_path = file_name
            
        if not os.path.exists(file_path):
            return rules_dict

        # قراءة الشيت ميكانيكياً (تخطي العناوين وتعيين الصفوف)
        df = pd.read_excel(file_path, header=None)
        
        # تفكيك الأعمدة (من العمود B فما فوق) حيث تمثل كل حالة هندسية عموداً مستقلاً
        for col_idx in range(1, df.shape[1]):
            col_data = df[col_idx]
            
            # جلب اسم العنصر الهندسي البرمجي المكتوب في الصف 11 (الفهرس 10 في بايثون)
            element_name = str(col_data.iloc[10]).strip() if pd.notna(col_data.iloc[10]) else ""
            
            if element_name and element_name != "اسم العنصر الهندسي البرمجي":
                # صهر وضغط الـ 26 فقرة المخزنة بالعمود داخل مصفوفة ديناميكية متكاملة
                rules_dict[element_name] = {
                    "req_type": str(col_data.iloc[1]).strip() if pd.notna(col_data.iloc[1]) else "",
                    "use_type": str(col_data.iloc[2]).strip() if pd.notna(col_data.iloc[2]) else "",
                    "sub_use": str(col_data.iloc[3]).strip() if pd.notna(col_data.iloc[3]) else "",
                    "geo_zone": str(col_data.iloc[4]).strip() if pd.notna(col_data.iloc[4]) else "",
                    "org_v": str(col_data.iloc[5]).strip() if pd.notna(col_data.iloc[5]) else "",
                    "area_limit": str(col_data.iloc[6]).strip() if pd.notna(col_data.iloc[6]) else "",
                    "dim_limit": str(col_data.iloc[7]).strip() if pd.notna(col_data.iloc[7]) else "",
                    "street_w": str(col_data.iloc[8]).strip() if pd.notna(col_data.iloc[8]) else "",
                    "height_limit": str(col_data.iloc[9]).strip() if pd.notna(col_data.iloc[9]) else "",
                    "operator": str(col_data.iloc[11]).strip() if pd.notna(col_data.iloc[11]) else "",
                    "target_value": str(col_data.iloc[12]).strip() if pd.notna(col_data.iloc[12]) else "",
                    "unit": str(col_data.iloc[13]).strip() if pd.notna(col_data.iloc[13]) else "",
                    "exceptions": str(col_data.iloc[14]).strip() if pd.notna(col_data.iloc[14]) else "",
                    "inputs_req": str(col_data.iloc[15]).strip() if pd.notna(col_data.iloc[15]) else "",
                    "code_name": str(col_data.iloc[16]).strip() if pd.notna(col_data.iloc[16]) else "",
                    "code_article": str(col_data.iloc[17]).strip() if pd.notna(col_data.iloc[17]) else "",
                    "law_name": str(col_data.iloc[18]).strip() if pd.notna(col_data.iloc[18]) else "",
                    "law_article": str(col_data.iloc[19]).strip() if pd.notna(col_data.iloc[19]) else "",
                    "severity": str(col_data.iloc[20]).strip() if pd.notna(col_data.iloc[20]) else "",
                    "violation_title": str(col_data.iloc[21]).strip() if pd.notna(col_data.iloc[21]) else "",
                    "citizen_explain": str(col_data.iloc[22]).strip() if pd.notna(col_data.iloc[22]) else "",
                    "engineer_explain": str(col_data.iloc[23]).strip() if pd.notna(col_data.iloc[23]) else "",
                    "fix_direction": str(col_data.iloc[24]).strip() if pd.notna(col_data.iloc[24]) else "",
                    "legal_penalty": str(col_data.iloc[25]).strip() if pd.notna(col_data.iloc[25]) else ""
                }
    except Exception:
        pass
    return rules_dict
def verify_soil_compliance(input_values, rules_dict):
    """
    دالة المعايرة الذكية الشاملة: تمسك القراءات الـ 13 وتطابقها رياضياً 
    مع شروط ملف الإكسل لإصدار شهادة الامتثال أو تقرير الرفض والعقوبة الجنائية الفاخر.
    """
    compliance_results = {"status": "PASS", "violations": []}
    
    # إذا كانت مصفوفة القوانين فارغة بسبب عدم العثور على الإكسل شيت
    if not rules_dict:
        compliance_results["status"] = "FAIL"
        compliance_results["violations"].append({
            "element": "System_Database",
            "title": "فشل الاتصال بقاعدة البيانات",
            "citizen": "لا يمكن إتمام عملية الفحص لعدم العثور على ملف الشروط الحاكمة في السيرفر.",
            "engineer": "Geotechnical Database Connection Failure (ibcp_soil_testing.xlsx missed).",
            "fix": "يرجى إبلاغ المستثمر أو الإدارة الفنية لمراجعة وجود ملف الإكسل في مجلد database_rules.",
            "penalty": "تجميد فوري لكافة الرخص لحماية السلامة الإنشائية والأرواح."
        })
        return compliance_results

    # معايرة ومطابقة كل عنصر مدخل مع شروطه المستخرجة ميكانيكياً
    for element_name, user_val in input_values.items():
        if element_name not in rules_dict:
            continue
            
        rule = rules_dict[element_name]
        op = rule["operator"]
        target_raw = rule["target_value"]
        
        is_compliant = True
        
        # 1. المعايرة والفرز الرياضي الذكي حسب نوع المعامل المكتوب بجدولك
        try:
            if op == "يساوي":
                is_compliant = (str(user_val).strip() == str(target_raw).strip())
            elif op == "أكبر من أو يساوي" or op == "اكبر من او يساوي":
                is_compliant = (float(user_val) >= float(target_raw))
            elif op == "أصغر من أو يساوي" or op == "اصغر من او يساوي":
                is_compliant = (float(user_val) <= float(target_raw))
        except ValueError:
            # في حال حدوث خطأ في تحويل النص إلى أرقام
            is_compliant = False

        # 2. في حال رصد مخالفة أو تحايل إنشائي: تسجيل الفقرات المرجعية والعقوبات فوراً من الإكسل
        if not is_compliant:
            compliance_results["status"] = "FAIL"
            compliance_results["violations"].append({
                "element": element_name,
                "title": rule["violation_title"],
                "citizen": rule["citizen_explain"],
                "engineer": rule["engineer_explain"],
                "fix": rule["fix_direction"],
                "penalty": rule["legal_penalty"],
                "code": f"{rule['code_name']} - {rule['code_article']}",
                "law": f"{rule['law_name']} - {rule['law_article']}"
            })

    return compliance_results
