from typing import Sequence, Dict, List, Tuple, Set


# Это множество может принять только целые числа
var_set: Set[int] = {1, 2, 3, 4, 5, 6, }

# Словарь
# Ключ аннотирован как строка, а значение - как целое число
var_dict: Dict[str, int] = {'forty_two': 42, 'hundred': 100, }

# Список
var_list: List[int] = [1, 2, 3, 4, ]

# Кортеж с определённой длиной (перечисляются типы всех элементов)
var_tuple: Tuple[int, int, str, float] = (1, 2, 'привет', 1.618,)

# Кортеж с переменной длиной
# Многоточие (Ellipsis) - это указание для Python, что длина кортежа не определена
var_tuple2: Tuple[float, ...] = (1, 2, 3.4,)

# Универсальный тип Sequence (Последовательность),
# подойдёт для аннотирования списка или множества
# принимает список
var_sequence: Sequence[float] = [1.2, 2, 3, ]
# и принимает множество
var_sequence2: Sequence[float] = {1.2, 2, 3, }
