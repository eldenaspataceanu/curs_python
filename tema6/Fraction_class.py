class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    @staticmethod
    def __add__(self, secondfraction):
        new_num = self.numerator * secondfraction.denominator + self.denominator * secondfraction.numerator
        new_den = self.denominator * secondfraction.denominator

        return Fraction(new_num, new_den)

    @staticmethod
    def __sub__(self, secondfraction):
        new_num = self.numerator * secondfraction.denominator - self.denominator * secondfraction.numerator
        new_den = self.denominator * secondfraction.denominator

        return Fraction(new_num, new_den)

    def inverse (self):
        return str(self.denominator) + "/" + str(self.numerator)


my_fr = Fraction(2, 5)
my_fr_2 = Fraction(1, 2)

print(my_fr.__str__())
print(my_fr.__add__(my_fr, my_fr_2))
print(my_fr.__sub__(my_fr, my_fr_2))
print(my_fr.inverse())
