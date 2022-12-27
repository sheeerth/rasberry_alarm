import Adafruit_CharLCD as LCD
from gpiozero import MotionSensor, Buzzer, LED, Button
from picamera import PiCamera

class UserInterface:
    lcd_rs = 26
    lcd_en = 19
    lcd_d4 = 13
    lcd_d5 = 6
    lcd_d6 = 5
    lcd_d7 = 11
    lcd_backlight = 15
    lcd_columns = 16
    lcd_rows = 2


    def __init__(self):
        self.led_orange = None
        self.camera_init()
        self.pir_init()
        self.buzzer_init()
        self.led_init()
        self.button_init()
        self.lcd_init()

    def camera_init(self):
        self.camera = PiCamera()
        self.camera.resolution = (2592, 1944)
        self.camera.framerate = 15
        print("Camera initialized")

    def pir_init(self):
        self.motion_sensor = MotionSensor(22)
        print("PIR initialized")

    def buzzer_init(self):
        self.buzzer = Buzzer(27)
        print("Buzzer initialized")

    def led_init(self):
        self.led_orange = LED(17)
        self.led_green = LED(18)
        self.led_red = LED(23)
        print("LED initialized")

    def button_init(self):
        self.button1 = Button(16)
        self.button2 = Button(4)
        print("Button initialized")

    def lcd_init(self):
        self.lcd = LCD.Adafruit_CharLCD(self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7, self.lcd_columns, self.lcd_rows, self.lcd_backlight)
        print("LCD initialized")

    def display_message(self, message):
        self.lcd.clear()
        self.lcd.message(message)

    def display_welcome_message(self):
        self.display_message("Raspberry PI\nSystem alarmowy");

    def motion_detected(self):
        return self.motion_sensor.wait_for_motion()

    def led_alarm_on(self):
        self.led_orange.off()
        self.led_green.off()
        self.led_red.blink()

    def led_alarm_armed(self):
        self.led_orange.on()
        self.led_green.off()
        self.led_red.off()

    def led_alarm_disarmed(self):
        self.led_orange.off()
        self.led_green.on()
        self.led_red.off()

    def buzzer_alarm_on(self):
        self.buzzer.beep(on_time=2, off_time=1, n=None, background=True)

    def buzzer_alarm_off(self):
        self.buzzer.off()

    def pressed_deactivate_button(self):
        return self.button1.is_pressed

    def pressed_activate_button(self):
        return self.button2.is_pressed