from num2words import num2words

def convert_number_to_words(amount):
    if amount < 1 or amount > 100000:
        return "Сумма должна быть от 1 до 100 000"