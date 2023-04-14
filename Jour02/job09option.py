def triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b :
        if a == b == c :
            return("équilatérale")
        elif a == b or b == c or c == a :
            if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
                return("rectangle isocèle")
            else:
                    return("isocèle")
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            return("rectangle")
        else :
            return("quelconque")
    else:
        return("pas de triangle possible")
    
print(triangle(20, 20, 12))
print(triangle(20, 20, 20))
print(triangle(5, 4, 3))
print(triangle(10, 21, 18))