
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
    elif EQ_VAL[0] < cuantos_palitos < EQ_VAL[1]:
        how_many_I = int(cuantos_palitos / EQ_VAL[1])
        resto = cuantos_palitos - (how_many_I * EQ_VAL[0])
        if resto > 3:
            resto = resto - 3
            return haz_palitos(resto) + "V"

    elif EQ_VAL[1] < cuantos_palitos < EQ_VAL[2]:
        how_many_V = int(cuantos_palitos / 5)
        resto = cuantos_palitos - (how_many_V * 5)
        if resto > 3:
            resto = resto - 3
            return haz_palitos(resto) + "X"

        return "V" * how_many_V + haz_palitos(resto)

    elif EQ_VAL[2] < cuantos_palitos < EQ_VAL[3]:
        how_many_X = int(cuantos_palitos / 10)
        resto = cuantos_palitos - (how_many_X * 10)
        how_many_V = int(resto / 5)
        resto = resto - (how_many_V * 5)
        if resto > 3:
            resto = resto-3
            return "X"*how_many_X + haz_palitos(resto) + "V"

        return "X"*how_many_X + "V"*how_many_V + haz_palitos(resto)

    return string_palitos
