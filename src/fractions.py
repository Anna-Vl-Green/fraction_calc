class Fraction:
    """
    Класс для представления дроби и осуществления математических операций с простыми дробями:
    сложение, вычитание, умножение, деление, сравнение.
    """
    numerator: int
    denominator: int

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Сложение"""
        first_numerator = self.numerator * other.denominator
        second_numerator = other.numerator * self.denominator
        common_denominator = self.denominator * other.denominator
        res_numerator = first_numerator + second_numerator
        divider = self.euclid(res_numerator, common_denominator)
        return f'{int(res_numerator / divider)}/{int(common_denominator / divider)}'

    def __sub__(self, other):
        """Вычитание"""
        first_numerator = self.numerator * other.denominator
        second_numerator = other.numerator * self.denominator
        common_denominator = self.denominator * other.denominator
        res_numerator = first_numerator - second_numerator
        divider = self.euclid(res_numerator, common_denominator)
        return f'{int(res_numerator / divider)}/{int(common_denominator / divider)}'

    def __mul__(self, other):
        """Умножение"""
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        divider = self.euclid(numerator, denominator)
        return f'{int(numerator / divider)}/{int(denominator / divider)}'

    def __truediv__(self, other):
        """Деление"""
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        divider = self.euclid(numerator, denominator)
        return f'{int(numerator / divider)}/{int(denominator / divider)}'

    def __lt__(self, other):
        """Сравнение меньше"""
        first_numerator = self.numerator * other.denominator
        second_numerator = other.numerator * self.denominator
        return first_numerator < second_numerator

    def __le__(self, other):
        """Сравнение меньше или равно"""
        first_numerator = self.numerator * other.denominator
        second_numerator = other.numerator * self.denominator
        return first_numerator <= second_numerator

    def __gt__(self, other):
        """Сравнение больше"""
        first_numerator = self.numerator * other.denominator
        second_numerator = other.numerator * self.denominator
        return first_numerator > second_numerator

    def __ge__(self, other):
        """Сравнение больше или равно"""
        first_numerator = self.numerator * other.denominator
        second_numerator = other.numerator * self.denominator
        return first_numerator >= second_numerator

    @staticmethod
    def abs(num):
        return max(-num, num)

    @staticmethod
    def euclid(a, b):
        """
        Метод для поиска наибольшего общего делителя (знаменателя).
        :param a: int
        :param b: int
        :return: int
        """
        a = abs(a)
        b = abs(b)
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b
