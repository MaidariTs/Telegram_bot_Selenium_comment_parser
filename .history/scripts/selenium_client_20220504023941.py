'''
Клиент `Selenium`, выбирает самую активную трансляцию и сохраняет её чат и
снимок экрана.

1) Заходит на vk.com.
2) Переходит в live-трансляции.
3) Выбирает открывает трансляцию, идующую первой (наиболее популярную).
4) Раз в минуту обновляет снимок экрана и сохраняет в файл новые поступившие 
сообщения в чат.
'''
from selenium import webdriver


class _VkSeleniumClientPipeline:
    def _open_chrome(self):
        '''
        Открытие браузера.
        '''
        self._driver = webdriver.Chrome('./chromedriver')


    def run(self):
        '''
        Вызов всех функций - одна за одной.
        '''
        self._open_chrome()
        self._login()
        self._goto_live_broadcasts()
        self._open_broadcast()
        self._save_results()            


if __name__ == '__main__':
    # Точка входа.
    _VkSeleniumClientPipeline().run()