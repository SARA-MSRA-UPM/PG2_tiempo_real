# external imports
import math
from threading import Thread, Event
from time import sleep
# internal imports
from ..actors.points.point import Point
from ..base.monitor import Monitor
from ..helpers.helpers import translate_figure, rotate_figure

TRIANGLE = [(0, 0.5), (0, -0.5), (1, 0)]

class Radar(Thread):
    def __init__(self,
                 name: str,
                 position: tuple[float, float],
                 detection_range: float,
                 orientation_initial: float,
                 increment: float,
                 revolutions_per_second: int,
                 detectable_points: list[Point],
                 monitor: Monitor):
        super().__init__()
        # Radar properties
        self.name = name
        self.x, self.y = position
        self.detection_range = detection_range
        self.detection = self.detection_range
        self.orientation_initial = orientation_initial
        self.facing = 0
        self._revolutions_per_second = revolutions_per_second
        self._increment = increment
        self.detectable_points = detectable_points

        self._monitor = monitor
        # Threads properties
        self._stop_event = Event()

    # Thread methods
    def run(self):
        while not self._stop_event.is_set():
            self._update()
            self.detect(self.detectable_points)
            sleep(self._increment/(360.0*self._revolutions_per_second))

    def stop(self):
        self._stop_event.set()

    # Private Radar methods
    def _update(self):
        self.facing = (self.facing + self._increment) % 360
        self.detection = self.detection_range

    def _in_sector(self, point: Point, sector: float) -> bool:
        angle = self._angle(point)
        return abs(sector - angle) < self._increment/2

    def _angle(self, point: Point):
        return (math.degrees(
            math.atan2(point.y - self.y, point.x - self.x)) + 360) % 360

    def _distance(self, point: Point) -> float:
        return math.hypot(point.x - self.x, point.y - self.y)

    def detect(self, points: list[Point]):
        # determine sector
        sector = (self.orientation_initial + self.facing) % 360
        for point in points:
            if self._in_sector(point, sector):
                distance = self._distance(point)
                if distance < self.detection:
                    self.detection = distance

        if self.detection != self.detection_range:
            self._monitor.add_data(
                radar=self,
                distance=self.detection,
                facing_angle=self.facing
            )

    # Public Radar methods
    ## Methods for graphication
    def facing_point(self):
        """
        Return two points making a line where the radar is facing (counting the
        orientation)
        """
        pass

    def detection_line(self):
        pass

    def detection_area(self):
        pass

