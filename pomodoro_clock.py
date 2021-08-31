from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.clock import Clock


Builder.load_file("pomodoroclock_design.kv")


class PomodoroClock(Widget):
    countdown_time = 25
    time_passed = countdown_time

    def timer_start(self):
        self.time_passed = self.countdown_time
        self.ids.time_label.text = str(self.time_passed)
        Clock.schedule_interval(self.timer_callback, 1)

    def timer_callback(self, dt):

        if self.time_passed <= 0:
            return False
        else:
            self.time_passed -= 1

        self.ids.time_label.text = str(self.time_passed)


class PomodoroClockApp(App):
    def build(self):
        self.title = "Pomodoro Clock"
        self.icon = "icon\icon.ico"
        return PomodoroClock()


if __name__ == "__main__":
    PomodoroClockApp().run()
