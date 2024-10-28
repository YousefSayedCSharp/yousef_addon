import globalPluginHandler
import api
import speech
import controlTypes

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super().__init__()
        # سنقوم هنا بإعداد قائمة مبدئية للأزرار وأسمائها
        self.button_labels = {
            "btnNSend": "إرسال",
            # يمكنك إضافة أسماء أخرى هنا لاحقًا
        }

    def script_announce_button_names(self, gesture):
        # دالة للحصول على أسماء الأزرار الحالية على الشاشة
        focus = api.getFocusObject()
        if focus.role == controlTypes.Role.BUTTON:
            button_name = focus.name
            if button_name:
                speech.speak(f"الزر الحالي اسمه: {button_name}")
                # تحقق مما إذا كان الاسم متواجد في القاموس
                if button_name in self.button_labels:
                    label = self.button_labels[button_name]
                    speech.speak(f"النص المخصص هو: {label}")
                else:
                    speech.speak("هذا الزر ليس له نص مخصص.")
            else:
                speech.speak("لا يوجد اسم لهذا الزر.")
        else:
            speech.speak("العنصر المحدد ليس زرًا.")

    # تعيين اختصار لتنفيذ هذه الدالة، يمكنك تخصيصه وفقًا لاحتياجك
    __gestures = {
        "kb:NVDA+a": "announce_button_names"
    }
