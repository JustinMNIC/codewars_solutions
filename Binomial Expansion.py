def expand(expr):
    #breaking down the input str in 2: exponent and the rest

    a_times_unknown_plus_b = expr[:expr.index("^")]
    a_times_unknown_plus_b = a_times_unknown_plus_b.strip("(")
    a_times_unknown_plus_b = a_times_unknown_plus_b.strip(")")

    #breaking further down the expr (str) , to find out the a, unknow, b +++  initializing the variabels

    exponent = expr[expr.index("^")+1:]
    a = ""
    unknown = ""
    b = ""

    #finding out the a,b,unknown

    #unknown
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower():
        if letter in a_times_unknown_plus_b:
            unknown = unknown + letter
    #a
    a = a + a_times_unknown_plus_b[:a_times_unknown_plus_b.index(unknown)]
    if a == "-":
        a = "-1"
    if a == "":
        a = "1"

    #b
    b = b + a_times_unknown_plus_b[a_times_unknown_plus_b.index(unknown)+1:]
    if "+" in b:
        b = b.replace("+", "")

    #dealing with the exponent == 0 , 1 or 2 and b == 0

    if exponent == "0":
        return "1"
    elif b == "0" or b == "-0":
        a_to_the_power = str(int(a) ** int(exponent))
        if a != "1":
            return "{}{}^{}".format(a_to_the_power, unknown, exponent)
        elif a == "1":
            return "{}^{}".format(unknown, exponent)
        elif a == "-1":
            return "-{}^{}".format(unknown, exponent)
    elif exponent == "1":
        if b == "0":
            return "{}{}".format(a, unknown)
        if a == "1":
            return a_times_unknown_plus_b
        else:
            result = "{}{}+{}".format(a, unknown,b)
            result = result.replace("+-","-")
            return result
    elif exponent == "2":
        if a == "-1" or a == "1":
            a_b_times_2 = str(2*int(b)) + unknown
            result = "{}^2+{}+{}".format(unknown,a_b_times_2, str(int(int(b) ** 2)))
            result = result.replace("+-","-")
            return result
        else:
            a_b_times_2 = str(int(a) * 2 * int(b)) + unknown
            result = "{}{}^2+{}+{}".format(str(int(int(a)**2)),unknown,a_b_times_2,str(int(int(b)**2)))
            result = result.replace("+-", "-")
            return result
    else:
        a_int = int(a)
        b_int = int(b)
        exponent_int = int(exponent)
        result = ""
        for k in range(0,exponent_int+1):
            X = n_calls_k(exponent_int,k) * int(a_int ** (exponent_int - k)) * int(b_int ** k)
            if X == 0 or X == 1:
                X = ""
            elif X == -1:
                X = "-"

            if (exponent_int - k) != 0:
                result = result + "{}{}^{}+".format(X, unknown, str(exponent_int - k))
            else:
                if X == "":
                    result = result + "1+"
                else:
                    result = result + "{}+".format(X)

        result = result.replace("+-","-")
        result = result.replace("-+", "-")
        result = result.replace("^1","")
        if result[-1] == "+":
            result = result[:-1]
        return result


def n_factorial(n):
    result = 1
    if n == 0:
        return result
    for i in range(1,n+1):
        result = result * i
    return result

def n_calls_k(n,k):
    result = n_factorial(n) / (n_factorial(k) * n_factorial(n-k))
    return int(result)


print(expand("(p-1)^3"))     # returns "p^3-3p^2+3p-1"
print(expand("(2f+4)^6"))     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
print(expand("(x+1)^1"))
