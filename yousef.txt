import globalPluginHandler
import api
import speech
import controlTypes
import ui

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super().__init__()

    def script_focus_on_button(self, gesture):
        # تحديد اسم الزر المستهدف للبحث عنه
        target_button_name = "Number of Errors"  # اسم الزر المستهدف
        # البحث عن الزر ضمن عناصر واجهة المستخدم الحالية (النافذة النشطة)
        found_button = self.find_button_by_name(api.getForegroundObject(), target_button_name)
        
        if found_button:
            if found_button.isFocusable and found_button.location:
                #parent_names = self.get_parent_names(found_button)
                #parent_info = " > ".join(parent_names)
                #ui.message(parent_names[0])
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

    def script_announce_button_names(self, gesture):
        # دالة للتحقق من اسم الزر المحدد
        focus = api.getFocusObject()
        if focus.role == controlTypes.Role.BUTTON:
            button_name = focus.name # الحصول على اسم الزر الفعلي
            if button_name:
                ui.message(f"اسم الزر: {button_name}")
                ui.message(f"اسم الزر: {button_name}")

    def script_find_element_by_text(self, gesture):
        # النص المطلوب البحث عنه ضمن العناصر
        target_text = "No issues"
        found_element = self.find_element_containing_text(api.getForegroundObject(), target_text)
        
        if found_element:
            element_name = found_element.name or "غير مسمى"
            element_role = found_element.roleText or "نوع غير معروف"
            ui.message(f"تم العثور على العنصر: {element_name}, النوع: {element_role}")
        else:
            ui.message("لم يتم العثور على عنصر يحتوي على النص المطلوب.")

    def find_element_containing_text(self, obj, target_text):
        # التحقق مما إذا كان النص المطلوب جزء من اسم العنصر الحالي
        if obj.name and target_text in obj.name:
            return obj
        # البحث داخل العناصر الفرعية
        for child in obj.children:
            result = self.find_element_containing_text(child, target_text)
            if result:
                return result
        return None
    # تعيين اختصار لوحة المفاتيح للانتقال إلى الزر المحدد
    __gestures = {
        "kb:NVDA+a": "focus_on_button", # اختصار لتنفيذ دالة التركيز على الزر
        "kb:NVDA+w": "announce_button_names",  # اختصار للتحقق من اسم الزر
        "kb:control+shift+downArrow": "find_element_by_text"  # اختصار للبحث عن عنصر يحتوي على النص المطلوب
    }
