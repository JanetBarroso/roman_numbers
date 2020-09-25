
EQUIVALENTS = {1: "I", 5: "V", 10: "X", 50: "L",
               100: "C", 500: "D", 1000: "M"}
EQ_VAL = list(EQUIVALENTS)

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
    if cuantos_palitos in EQ_VAL:
        return string_palitos.replace(
            string_palitos, EQUIVALENTS[cuantos_palitos]
        )
    elif EQ_VAL[1] < cuantos_palitos < EQ_VAL[2]:
        return "V" + haz_palitos(cuantos_palitos%EQ_VAL[1])

    elif EQ_VAL[2] < cuantos_palitos < EQ_VAL[3]:
        how_many_X = int(cuantos_palitos / EQ_VAL[2])
        resto = cuantos_palitos - (how_many_X * 10)
        if resto in EQ_VAL:
            return "X" * how_many_X + EQUIVALENTS[resto]
        return "X"*how_many_X + haz_palitos(resto)
    elif cuantos_palitos==4:
        return "IV"
    return string_palitos
