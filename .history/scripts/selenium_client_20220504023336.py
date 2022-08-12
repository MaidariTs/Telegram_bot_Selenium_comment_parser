'''
Клиент `Selenium`, выбирает самую активную трансляцию и сохраняет её чат и
снимок экрана.

1) Заходит на vk.com.
2) Переходит в live-трансляции.
3) Выбирает открывает трансляцию, идующую первой (наиболее популярную).
4) Раз в минуту обновляет снимок экрана и сохраняет в файл новые поступившие 
сообщения в чат.
'''

class VkSeleniumClientPipeline:
    def run():
        '''
        Точка входа. Вызов всех функций - одна за одной.
        '''
        self._open_browser()
        self._login()
        self._go_to_live_broadcasts()        


if __name__ == '__main__':
