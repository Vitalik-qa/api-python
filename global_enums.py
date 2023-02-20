from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Полученный код статуса не равен ожидаемому"
    WRONG_ELEMENT_COUNT = "Количество элементов не равно ожидаемому"
    WRONG_ELEMENT_PARAM = "Полученный параметр не равен ожидаемому"

