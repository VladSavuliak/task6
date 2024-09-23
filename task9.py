class Discriminant:

    def discriminant(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print(f"Перше значення: {a}, Друге значення: {b}, Третє значення: {c}")


    def calculation(self):
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + D**0.5) / 2 * a
            x2 = (-b - D**0.5) / 2 * a
            return D
        elif D == 0:
            x = -(b/2*a)
            return D
        else:
            return "Дискримінант коренів немає"

discriminant = Discriminant()
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
discriminant.discriminant(a, b, c)
result = discriminant.calculation()
print(result)