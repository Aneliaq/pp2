import time

class MickeyClock:
    def get_time_angles(self):
        t = time.localtime()

        seconds = t.tm_sec
        minutes = t.tm_min

    
        seconds_angle = seconds * 6

        minutes_angle = (minutes + seconds / 60) * 6

        return minutes_angle, seconds_angle