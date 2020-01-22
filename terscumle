# Verilen cümleyi tersten yazdıran fonksiyon?
# Sonrasında bu cümleyi decrease ile azaltan fonksiyon?


def desrever(sentence):
    return sentence[::-1]  # https://www.w3schools.com/python/python_howto_reverse_string.asp


reversed_input = desrever(input("Tersten yazılmasını istediğiniz bir cümle yazınız: \n\t"))

print(reversed_input)


def decrease(x):
    if len(x) < 1:
        return x
    else:
        print(x)
        return decrease(x[1:])


print(decrease(reversed_input))
