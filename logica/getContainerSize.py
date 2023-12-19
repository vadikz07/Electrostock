def get_container_size(num): 
    # tuples => minimo maximo
    xxl = (1,12) 
    l = (13,24)
    m = (25,48)
    s = (48,99)
    match num:
        case num if xxl[0]<= num <= xxl[1]:
            return "XL"
        case num if l[0]<= num <= l[1]:
            return "GRANDE"
        case num if m[0]<= num <= m[1]:
            return "MEDIANO"
        case num if s[0]<= num <= s[1]:
            return "PEQUEÑO"
        case _:
            return "INPUT NO VALIDO"