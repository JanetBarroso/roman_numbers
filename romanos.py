def romans(entero):
    if entero <= 0:
        return "not possible to convert " + \
               str(entero) + " to romans"

    equivalents = {1: "I", 5: "V", 10: "X", 50: "L",
                   100: "C", 500: "D", 1000: "M"}
    if entero <= 3:
        roman = equivalents[1] * entero
    else:
        roman = equivalents[entero]
    return roman
