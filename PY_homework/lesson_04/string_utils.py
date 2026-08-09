
# класс для обработки и анализа строк
class StringUtils:

    # в переданном тексте делает первую букву заглавной
    def capitalize(self, string: str) -> str:
        return string.capitalize()

# в переданном тексте удаляет пробелы только в начале строки
    def trim(self, string: str) -> str:
        witespace = " "
        while string.startswith(witespace):
            string = string.removeprefix(witespace)
        return string

# ищет заданный символ: если есть - True, если нет - False
    def contains(self, string: str, symbol: str):
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass
        return res

# удаляет указанный символ из заданной строки
    def delete_symbol(self, string: str, symbol: str):
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string
