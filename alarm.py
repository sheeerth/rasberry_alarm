class Alarm:
    alarm_armament = False

    def alarm_deactivation(self):
        self.alarm_armament = False

    def alarm_activation(self):
        self.alarm_armament = True

    def is_alarm_on(self):
        return self.alarm_armament == True

    def is_alarm_off(self):
        return self.alarm_armament == False
