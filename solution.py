import pandas as pd
import numpy as np


chat_id = 1369690762 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha=.06
    if abs(x_success/x_cnt - y_success/y_cnt) > alpha:
        return True
    else:
        return False
