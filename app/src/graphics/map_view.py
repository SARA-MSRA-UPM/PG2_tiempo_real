# external imports
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
import math
# internal imports
from src.actors.radar import Radar
from src.actors.points.point import Point    

class MapView:
    def __init__(
            self,
            width: int,
            height: int,
            axes: plt.axes):
        self.width = width
        self.height = height
        self.axes = axes

    def init_plot(self):
        """
        Initializes the plot by setting limits and static features.
        """
        pass

    def animate(self, radars: list[Radar], points: list[Point], interval=100):
        """
        Creates the animation using FuncAnimation.
        """
        pass

    def update(self, frame, radars: list[Radar], points: list[Point]):
        """
        Updates the radar and points for each frame of the animation.
        """
        pass

