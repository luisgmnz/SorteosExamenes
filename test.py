import random
def sorteoEscalas():
    mayor = ["Jónico", "dórico", "frigio", "lidio", "mixolido", "eólico", "locrio"]
    menorMelodico = ["menor melódico", "dórico b9", "lídia Aumentada", "lidia b7", "mixolidia b13", "locria n9", "alterada"]
    menorArmonico = ["menor armónico", "locria n13", "jónica aumentada", "dórica #4", "mixolidia b9 b13", "lidia #9", "alterada bb7"]
    disminuida = ["semitono tono", "tono semitono"]
    notas = [("C","C"),("Db","C#"),("D","D"),("Eb","D#"),("E","E"),("F","F"),("Gb","F#"),("G","G"),("Ab","G#"),("A","A"),("Bb","A#"),("B","B")]
    comienzo = ["primera","segunda","tercera","cuarta","quinta","sexta","séptima"]
    sorteoPrimero = "Escala " + elegirNota(notas) + " " + random.choice(mayor) + ", desde la  " + random.choice(comienzo)
    sorteoSegundo = "Escala " + elegirNota(notas) + " " + random.choice(menorMelodico) + ", desde la  " + random.choice(comienzo)
    sorteoTercero = "Escala " + elegirNota(notas) + " " + random.choice(menorArmonico) + ", desde la  " + random.choice(comienzo)
    sorteoCuarto = sorteoPrimero + "\n" + sorteoSegundo + "\n" + sorteoTercero + "\n" + "Escala " + elegirNota(notas) + " " + random.choice(disminuida) + ", desde la  " + random.choice(comienzo) + "\n" + "Escala " + elegirNota(notas) + " de tonos" + ", desde la " + random.choice(comienzo)
    resultado = "ESCALAS PRIMERO" + "\n" + sorteoPrimero + "\n" + sorteoPrimero + "\n" + sorteoPrimero + "\n" + "ESCALAS SEGUNDO" + "\n" + sorteoSegundo + "\n" + sorteoSegundo + "\n" + sorteoSegundo + "\n" + "ESCALAS TERCERO" + "\n" + sorteoTercero + "\n" + sorteoTercero + "\n" + sorteoTercero + "\n" + "ESCALAS CUARTO\n" + sorteoCuarto

    print(resultado)
    return resultado


def elegirNota(notas):
    duplas = random.choice(notas)
    elemento = random.choice(duplas)
    return elemento
    
x = sorteoEscalas()
print(x)