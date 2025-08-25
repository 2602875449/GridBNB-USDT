from collections import deque
from enum import Enum
import numpy as np


class Trend(Enum):
    """表示市场趋势"""
    UP = "up"
    DOWN = "down"
    NEUTRAL = "neutral"


class TrendDetector:
    """基于移动平均的简单趋势检测器"""

    def __init__(self, short_window: int = 20, long_window: int = 50, threshold: float = 0.001):
        self.short_window = short_window
        self.long_window = long_window
        self.threshold = threshold
        self.prices = deque(maxlen=long_window)

    def update(self, price: float) -> None:
        """更新最新价格"""
        if price is not None:
            self.prices.append(float(price))

    def get_trend(self) -> Trend:
        """根据均线判断当前趋势"""
        if len(self.prices) < self.long_window:
            return Trend.NEUTRAL

        prices_list = list(self.prices)
        short_ma = np.mean(prices_list[-self.short_window:])
        long_ma = np.mean(prices_list)

        if short_ma > long_ma * (1 + self.threshold):
            return Trend.UP
        if short_ma < long_ma * (1 - self.threshold):
            return Trend.DOWN
        return Trend.NEUTRAL
