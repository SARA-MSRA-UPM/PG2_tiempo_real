# external imports
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.artist import Artist
from matplotlib.patches import Polygon
# internal imports
from ..actors.radar import Radar
from ..actors.points.point import Point


class MapView:
    def __init__(self):
        pass

    def init_plot(self) -> list[Artist] | None:
        """
        Initializes the plot by setting limits and static features.
        """
        return None

    def update(self, frame, radars: list[Radar], points: list[Point]):
        """
        Updates the radar and points for each frame of the animation.
        """
        return

    def animate(self, radars: list[Radar], points: list[Point], interval=30):
        """
        Creates the animation using FuncAnimation.
        """
        return