from threading import Thread, Event
import time

class PomodoroTimer:
    def __init__(self, duration):
        self.duration = duration
        self.time_left = duration
        self.running = False
        self._stop_event = Event()

    def start(self):
        if not self.running:
            self.running = True
            self._stop_event.clear()
            Thread(target=self._run).start()

    def _run(self):
        while self.time_left > 0 and not self._stop_event.is_set():
            time.sleep(1)
            self.time_left -= 1
        self.running = False

    def pause(self):
        self._stop_event.set()
        self.running = False

    def reset(self):
        self.pause()
        self.time_left = self.duration

