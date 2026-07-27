import os
import pandas as pd
import streamlit as st

def load_dynamic_excel_rules(file_name="ibcp_soil_testing.xlsx"):
    """
    دالة مطورة لقراءة ملف إكسل التربة ميكانيكياً من نفس الغرفة المعزولة soil_rules.
    """
    rules_dict = {}
    try:
        # قراءة الملف مباشرة من نفس المجلد الفرعي الحالي المتواجد فيه المحرك
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, file_name)
        
        if not os.path.exists(file_path):
            return rules_dict

        df = pd.read_excel(file_path, header=None)
        
        for col_idx in range(1, df.shape[1]):
            col_data = df[col_idx]
            element_name = str(col_data.iloc[10]).strip() if pd.notna(col_data.iloc[10]) else ""
            
            if element_name and element_name != "اسم العنصر الهندسي البرمجي":
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
    معايرة ومطابقة القراءات الـ 13 مع داتا الغرفة الفرعية المعزولة soil_rules.
    """
    compliance_results = {"status": "PASS", "violations": []}
    if not rules_dict:
        compliance_results["status"] = "FAIL"
        compliance_results["violations"].append({
            "element": "Soil_Database",
            "title": "فشل الاتصال بمدونة التربة",
            "citizen": "لا يمكن الفحص لعدم عثور المحرك الفرعي على ملف الشروط.",
            "engineer": "Soil Package Database Connection Failure.",
            "fix": "تأكد من وجود ibcp_soil_testing.xlsx داخل مجلد soil_rules.",
            "penalty": "حظر فوري للمعاملة لحماية الأرواح.",
            "code": "الكود العراقي", "law": "قانون النقابة"
        })
        return compliance_results

    for element_name, user_val in input_values.items():
        if element_name not in rules_dict:
            continue
        rule = rules_dict[element_name]
        op = rule["operator"]
        target_raw = rule["target_value"]
        is_compliant = True
        try:
            if op == "يساوي":
                is_compliant = (str(user_val).strip() == str(target_raw).strip())
            elif op in ["أكبر من أو يساوي", "اكبر من او يساوي"]:
                is_compliant = (float(user_val) >= float(target_raw))
            elif op in ["أصغر من أو يساوي", "اصغر من او يساوي"]:
                is_compliant = (float(user_val) <= float(target_raw))
        except ValueError:
            is_compliant = False

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
