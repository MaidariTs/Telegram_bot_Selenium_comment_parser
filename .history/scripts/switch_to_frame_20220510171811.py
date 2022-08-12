'''
Функция переключения на другой фрейм.
'''
from contextlib import contextmanager

@contextmanager
def switch_to_frame(frame_id):
    
    self._driver.switch_to.frame('chatframe')