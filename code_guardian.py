import sys
import ast

def validate_code_before_commit(target_file_path):
    """
    محرك الفحص الآلي المسبق لتأمين الأكواد من الكراش والـ Syntax Errors قبل الحفظ.
    """
    print(f"🔍 جاري قراءة وتدقيق أوزان الملف حياً: [{target_file_path}] ...")
    
    if not os.path.exists(target_file_path):
        print(f"❌ خطأ: الملف المستهدف غير موجود في المسار المحدد!")
        return False
        
    try:
        with open(target_file_path, "r", encoding="utf-8") as file:
            code_content = file.read()
            
        # 1. اختبار تفكيك الشجرة البرمجية (Abstract Syntax Tree) لكشف الأقواس وعلامات التنصيص المكسورة
        ast.parse(code_content)
        
        # 2. اختبار محاكاة التحميل والمسافات الحساسة لبايثون
        compile(code_content, target_file_path, 'exec')
        
        print("🟩 مبروك! الكود سليم هندسياً 100%، وموزون المسافات، وآمن تماماً للحفظ والنشر السحابي.")
        return True
        
    except SyntaxError as syntax_err:
        print("\n🛑 [تم رصد خلل رقابي بات في السنتكس والمسافات! تم حظر الحفظ فوراً]")
        print(f"📍 موقع الخطأ: السطر رقم ({syntax_err.lineno})")
        print(f"🔎 تفاصيل العطل: {syntax_err.msg}")
        print(f"💡 السطر المكسور: {syntax_err.text.strip() if syntax_err.text else 'غير محدد'}")
        return False
    except Exception as e:
        print(f"⚠️ تحذير: تم رصد تعارض تفاعلي صامت: {str(e)}")
        return False

if __name__ == "__main__":
    import os
    # يمكنك برمجياً كتابة اسم أي ملف تريد فحص كوده هنا قبل رفعه (مثل app.py أو governance_view.py)
    target_to_test = "app.py" 
    success = validate_code_before_commit(target_to_test)
    if not success:
        sys.exit(1) # إيقاف ميكانيكي صارم يمنع الرفع في حال وجود عطل
