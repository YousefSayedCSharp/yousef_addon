import globalPluginHandler
import api
import ui
import speech
import controlTypes

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super().__init__()
        # قائمة لتعيين النصوص المخصصة بناءً على أسماء الأزرار
        self.button_labels = {
            "btnSave": "حفظ",
            "btnNSend": "إرسال",
            # يمكنك إضافة أسماء أخرى هنا لاحقًا
        }

    def script_announce_button_names(self, gesture):
        # دالة للتحقق من اسم الزر المحدد
        focus = api.getFocusObject()
        if focus.role == controlTypes.Role.BUTTON:
            button_name = focus.name # الحصول على اسم الزر الفعلي
            if button_name:
                speech.speak(f"اسم الزر: {button_name}")
                ui.message(f"اسم الزر: {button_name}")
                
                # تحقق إذا كان الاسم متواجدًا في القاموس
                #if button_name in self.button_labels:
                    #label = self.button_labels[button_name]
                    #speech.speak(f"النص المخصص هو: {label}")
                #else:
                    #speech.speak("هذا الزر ليس له نص مخصص.")
            else:
                speech.speak("لم يتم العثور على اسم للزر.")
        else:
            speech.speak("العنصر المحدد ليس زرًا.")

    # تعيين اختصار لتنفيذ هذه الدالة
    __gestures = {
        "kb:NVDA+a": "announce_button_names"
    }
