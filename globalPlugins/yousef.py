import globalPluginHandler
import api
import ui
import controlTypes

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super().__init__()

    def script_find_no_issues_found_and_focus(self, gesture):
        target_text = "No issues found"
        found_element = self.find_element_containing_text(api.getForegroundObject(), target_text)

        if found_element:
            ui.message(target_text)  # إذا وُجد العنصر، تمرير النص إلى القارئ
        else:
            self.focus_on_number_of_errors()  # إذا لم يُوجد، الانتقال إلى زر "Number of Errors"

    def find_element_containing_text(self, obj, target_text):
        if obj.name and target_text in obj.name:
            return obj
        for child in obj.children:
            result = self.find_element_containing_text(child, target_text)
            if result:
                return result
        return None




    def focus_on_number_of_errors(self):
        # تحديد اسم الزر المستهدف للبحث عنه
        target_button_name = "Number of Errors"  # اسم الزر المستهدف
        # البحث عن الزر ضمن عناصر واجهة المستخدم الحالية (النافذة النشطة)
        found_button = self.find_button_by_name(api.getForegroundObject(), target_button_name)
        
        if found_button:
            # نقل التركيز إلى الزر وإعلان اسمه
            found_button.setFocus()
            #speech.speak(f"تم الانتقال إلى الزر: {target_button_name}")
        else:
            # في حالة عدم العثور على الزر
            ui.message("لم يتم العثور على الزر المحدد.")

    def find_button_by_name(self, obj, target_name):
        # التحقق مما إذا كان العنصر هو زر بالاسم المطلوب
        if obj.role == controlTypes.Role.BUTTON and obj.name == target_name:
            return obj
        # البحث داخل العناصر الفرعية (الأبناء) إذا لم يكن العنصر الحالي هو الزر المستهدف
        for child in obj.children:
            result = self.find_button_by_name(child, target_name)
            if result:
                return result
        # إرجاع None إذا لم يتم العثور على الزر
        return None

    # تعيين اختصار لوحة المفاتيح للانتقال إلى الزر المحدد
    __gestures = {
        "kb:control+shift+downArrow": "find_no_issues_found_and_focus"  # اختصار للبحث
    }