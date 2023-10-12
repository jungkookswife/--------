from num2words import num2words

def convert_number_to_words(amount):
    if amount < 1 or amount > 100000:
        return "Сумма должна быть от 1 до 100 000"

    words = num2words(amount, lang='ru')

    last_digit = amount % 10
    if last_digit == 1 and amount % 100 != 11:
        currency = "рубль"
    elif 2 <= last_digit <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        currency = "рубля"
    else:
        currency = "рублей"

    result = words.capitalize() + " " + currency

    return result

amount = int(input("Введите сумму от 1 до 100000: "))
result = convert_number_to_words(amount)
print(result)