def get_container_size(num): 
    # tuples => minimo maximo
    xxl = (1,8) 
    l = (9,32)
    m = (33,50)
    s = (51,99)
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