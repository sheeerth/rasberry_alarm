from alarm import Alarm
from emailer import Emailer
from userInterface import UserInterface
import time


def main():
    notifier = Emailer()
    alarm = Alarm()
    user_interface = UserInterface()

    sendTo = 'bartada@interia.pl'
    emailSubject = 'Alarm zazbrojony'
    emailContent = 'To jest testowy mail ' + time.ctime()

    while True:
        if alarm.is_alarm_on() & user_interface.motion_detected():
            image = '/home/lechu/Desktop/image.jpg'
            user_interface.camera.capture(image)
            notifier.sendmail(sendTo, emailSubject, emailContent, image)
            user_interface.buzzer_alarm_on()
            user_interface.led_alarm_on()
            user_interface.display_message('Intruz!')

        if alarm.is_alarm_on() & user_interface.pressed_deactivate_button():
            user_interface.display_message('Alarm wyłączony')
            user_interface.buzzer_alarm_off()
            user_interface.led_alarm_disarmed()
            alarm.deactivate_alarm()

        if alarm.is_alarm_off() & user_interface.pressed_activate_button():
            user_interface.display_message('Alarm zazbrojony')
            user_interface.led_alarm_armed()
            alarm.activate_alarm()


main()
