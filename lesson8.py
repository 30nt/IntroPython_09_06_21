# методы словарей

symbols = {symbol: ord(symbol) for symbol in 'eyuioa'}

persons = {"John": 12, "Jack": 34, "Anna": 27}

# print(persons["Anna"])

persons["Jackob"] = 59
persons["John"] = len("Test")
# persons.clear()
# persons = {}
# print(persons.get("Vova", -1))

result = "Anna" in persons  # in проверяет ТОЛЬКО КЛЮЧИ!!

key = "Anna"
# if key not in persons:
#     persons[key] = 41
#
for key in persons:
    print(key, persons[key])
value = persons.pop("Jackob")
print(">>>>>", value)
for key, value in persons.items():
    print(key, value)

# print(type(persons.keys()), persons.keys())
# print(type(persons.values()), persons.values())

max_age = max(persons.values())

# print("\m\\a\\x\_\\a\\g\\e")
#
# value = input()
# print(value)