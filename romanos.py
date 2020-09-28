
def arabic2roman(entero):

    if entero <= 0:
        return "not possible to convert " + \
               str(entero) + " to romans"

    roman = entero * "I"

    if entero >= 5:
        nV = int(entero / 5)
        roman = roman.replace(5*nV*"I", nV*"V")
        nX = int(nV / 2)
        roman = roman.replace(2*nX*"V", nX*"X")
        nL = int(nX / 5)
        roman = roman.replace(5*nL*"X", nL*"L")
        nC = int(nL / 2)
        roman = roman.replace(2*nC*"L", nC*"C")
        nD =int(nC / 5)
        roman = roman.replace(5*nD*"C", nD*"D")
        nM = int(nD / 2)
        roman = roman.replace(2*nM*"D", nM*"M")
    return roman