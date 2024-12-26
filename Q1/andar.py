roda = True
#roda = False

#for
if roda:
    andarmax = 21;
    cont = 0;
    for cont in range(andarmax, 0, -1):
        if(cont != 13):
            print(str(cont) + " andar");
        else:
            continue

#while
else:
    andarmaxW = 20;
    contW = 0;
#   andarmaxW = 0;
#   contw = 20;

    while contW <= andarmaxW:
#   while contW >= andarmaxW:

        if contW == 13:
            contW += 1
#            contW -= 1
            continue
        print(f"Andar: {contW}")
        contW += 1
#       contW -= 1