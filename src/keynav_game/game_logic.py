import numpy as np
import time


class Game:

    button_size: tuple[int, int] = (120, 60)
    button_relative_position: tuple[float, float] = (0.5, 0.5)
    click_timestamps: list[float] = []

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
        x: float = np.random.random()
        y: float = np.random.random()

        self.button_relative_position = (x, y)

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
