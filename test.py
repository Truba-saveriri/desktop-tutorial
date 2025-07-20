def calculate():
    try:
        expression = input("Введите выражение: ")
        part = expression.split()

        if len(part) != 3:
            raise ValueError("Выражение введено неверно")

        a_str, sim, b_str = part

        if sim not in ('+', '-', '*', '/'):
            raise ValueError("Операция невозможна")

        try:
            a = int(a_str)
            b = int(b_str)
        except ValueError:
            raise ValueError("Числа должны быть целыми")

        if not (1 <= a <= 10) or not (1 <= b <= 10):
            raise ValueError("Числа должны быть от 1 до 10")

        if sim == '+':
            result = a + b
        elif sim == '-':
            result = a - b
        elif sim == '*':
            result = a * b
        elif sim == '/':
            result = a // b

        print(result)

    except Exception as e:
        print(f"Ошибка: {e}")
        exit(1)

if __name__ == "__main__":
    calculate()