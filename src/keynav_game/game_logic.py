import numpy as np
import time
from enum import Enum
from typing import Optional

class DirectionTypes_e(Enum):
    CROSS = 0
    TWO_DIMS = 1

class Game:

    button_size: tuple[int, int] = (120, 60)
    button_relative_position: tuple[float, float] = (0.5, 0.5)
    click_timestamps: list[float] = []
    button_relative_positions: Optional[list[tuple[float,float]]] = None

    def __init__(self):
        self._get_possible_positions(n_cuts=1)
        self._get_possible_positions(n_cuts=2)

    @property
    def click_count(self) -> int:
        return len(self.click_timestamps)

    @property
    def click_rate(self) -> float:
        _, rate = self._get_click_stats()
        return rate

    @property
    def time_per_click(self) -> float:
        time, _ = self._get_click_stats()
        return time

    @property
    def score_string(self) -> str:
        score: str = ""
        score += f"Clicks: {str(self.click_count)}\n"
        score += f"Average click rate: {str(self.click_rate)} clicks per second\n"
        score += f"Average time per click: {str(self.time_per_click)} seconds"

        return score

    def choose_next_position(self):
        if self.button_relative_position is None:
            x: float = np.random.random()
            y: float = np.random.random()
            self.button_relative_position = (x, y)
        else:
            random_index = np.random.choice(len(self.button_relative_positions))
            random_position = self.button_relative_positions[random_index]
            self.button_relative_position = random_position

    def register_click(self):
        self.click_timestamps.append(time.time())

    def _get_click_stats(self) -> tuple[float, float]:
        timestamps: np.ndarray = np.array(self.click_timestamps)
        deltas: np.ndarray = np.diff(timestamps)

        avg_time_per_click: float = float(np.mean(deltas))

        if avg_time_per_click > 0:
            click_rate: float = 1 / avg_time_per_click
        else:
            click_rate: float = float("inf")

        return avg_time_per_click, click_rate

    def _get_possible_positions(self, n_cuts: int)-> list[tuple[float,float]]:
        
        relative_positions: list[tuple[float, float]] = []
    
        raw_steps: float = (2 ** (n_cuts+1))+1
        raw_range: np.ndarray = np.linspace(0,1,raw_steps)
        trimmed_range = raw_range[1:-1]

        for i in (trimmed_range):
            for j in (trimmed_range):
                relative_positions.append((i,j))

        self.button_relative_positions = relative_positions


