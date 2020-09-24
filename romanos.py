EQUIVALENTS = {1: "I", 5: "V", 10: "X", 50: "L",
               100: "C", 500: "D", 1000: "M"}


def romans(entero):
    if entero <= 0:
        return "not possible to convert " + \
               str(entero) + " to romans"
    if entero <= 3:
        roman = EQUIVALENTS[1] * entero
    elif entero == 4:
        roman = "IV"
    elif entero == 6:
        roman = "VI"
    else:
        roman = EQUIVALENTS[entero]
    return roman


def haz_palitos(entero):
    return EQUIVALENTS[1] * entero


def string_patterns(string_palitos):
    cuantos_palitos = string_palitos.count("I")
    if cuantos_palitos in list(EQUIVALENTS):
        return string_palitos.replace(
            string_palitos, EQUIVALENTS[cuantos_palitos]
        )
    elif list(EQUIVALENTS)[1] < cuantos_palitos < list(EQUIVALENTS)[2]:
        return "V" + haz_palitos(cuantos_palitos % list(EQUIVALENTS)[1])

    elif list(EQUIVALENTS)[2] < cuantos_palitos < list(EQUIVALENTS)[3]:
        how_many_X = int(cuantos_palitos / list(EQUIVALENTS)[2])#
        resto = cuantos_palitos - (how_many_X * 10)
        if resto in list(EQUIVALENTS):
            return "X" * how_many_X + EQUIVALENTS[resto]
        return "X"*how_many_X + haz_palitos(resto)
    return string_palitos
