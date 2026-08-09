import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# 1
@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ('Здравствуйте, наставник', 'Здравствуйте, наставник'),  # корректный текст
    ('skypro', 'Skypro'),                           # первая строчная, латиница
    ('PYTHON', 'Python'),                                       # все заглавные
    ('зОЛотоЕ СечЕниЕ', 'Золотое сечение')                  # смешанный регистр
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# 2
@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ('skypro', 'skypro'),                                 # без лишних пробелов
    ('    skypro', 'skypro'),                       # пробелы вначале, латиница
    ('    привет', 'привет'),                      # пробелы вначале, кириллица
    ('Python   ', 'Python   '),                               # пробелы в конце
    ('зол от ое с ечени е', 'зол от ое с ечени е')      # пробелы внутри строки
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


# 3
@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol_str, expected', [
    ('Skypro', 'S', True),                               # в начале, латиница
    ('привет', 'и', True),                            # в середине, кириллица
    ('ПРИВЕТ', 'Т', True),                               # в конце, заглавные
    ('привет мир', 'мир', True),                         # несколько символов
    ('12345', '2', True),                                  # число как строка
    ('', '', True)                                            # пустая строка
])
def test_contais_positive(input_str, symbol_str, expected):
    assert string_utils.contains(input_str, symbol_str) == expected


# 4
@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol_str, expected', [
    ('Skypro', 'S', 'kypro'),                             # в начале, латиница
    ('привет', 'и', 'првет'),                          # в середине, кириллица
    ('ПРИВЕТ', 'Т', 'ПРИВЕ'),                             # в конце, заглавные
    ('привет мир', 'мир', 'привет '),                     # несколько символов
    ('абракадабра', 'а', 'бркдбр'),                     # повторяющийся символ
    ('aaaaaaaaaa', 'a', ''),                          # удаление всех символов
    ('', '', '')                                               # пустая строка
])
def test_delete_symbol_positive(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected


# 1
@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ('456skypro', '456skypro'),                     # строка начинается с цифры
    ('', ''),                                                   # пустая строка
    ('    ', '    ')                                       # строка из пробелов
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# 2
@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    (' ', ''),                                       # строка из одного пробела
    ('     ', ''),                                         # несколько пробелов
    ('', ''),                                                   # пустая строка
    (123456, AttributeError)                                  # цифры как число
    ])
def test_trim_negative(input_str, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected


# 3
@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol_str, expected', [
    ('Skypro', 's', False),                                   # разный регистр
    ('привет', 'я', False),                             # отсутствующий символ
    (112233, '3', AttributeError),                                     # цифры
    ('привет мир', ' ', True),                                 # поиск пробела
    ('', 'в', False),                                  # поиск в пустой строке
    ('привет', 'v', False),                        # несовпадение языка текста
])
def test_contais_negative(input_str, symbol_str, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            string_utils.trim(input_str)
    else:
        assert string_utils.contains(input_str, symbol_str) == expected


# 4
@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol_str, expected', [
    ('Skypro', 's', 'Skypro'),                                 # разный регистр
    ('привет', 'приви', 'привет'),                      # несовпадение символов
    (12345, '2', AttributeError),                                       # цифры
    ('привет %', '%', 'привет '),                        # наличие спецсимволов
    ('', '       ', '')                       # удаляем пробелы в пустой строке
])
def test_delete_symbol_negative(input_str, symbol_str, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            string_utils.delete_symbol(input_str, symbol_str)
    else:
        assert string_utils.delete_symbol(input_str, symbol_str) == expected
