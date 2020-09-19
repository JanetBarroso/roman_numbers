def romans(entero):
    if entero <= 0:
        return "not possible to convert " +\
                         str(entero)+ " to romans"

    equivalents = {1: "I", 5: "V"}
    return equivalents[entero]
