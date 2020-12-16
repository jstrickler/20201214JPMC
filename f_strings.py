
person = 'Bill Gates'
city = "Medina"

print("%s lives in %s" % (person, city))  #  python 2.x (legacy)
print("{} lives in {}".format(person, city))   # python 3 (original)
print(f"{person} lives in {city}")  # 3.7+ only

result = 23.7 / 18.61

print(result)
print("{:.3f}".format(result))
print(f"{result:.3f}")


