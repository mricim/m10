#objFitxer.read(n): llegeix tot el fitxer
#objFitxer.readline(): llegeix una línia
#objFitxer.readlines(): llegeix totes les línies a una llista

with open("testfile.txt") as f:
    for line in f:
        print(line,end='*')