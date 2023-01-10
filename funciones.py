import random

def sorteoEscalas():
    mayor = ["Jónico", "dórico", "frigio", "lidio", "mixolido", "eólico", "locrio"]
    menorMelodico = ["menor melódico", "dórico b9", "lídia Aumentada", "lidia b7", "mixolidia b13", "locria n9", "alterada"]
    menorArmonico = ["menor armónico", "locria n13", "jónica aumentada", "dórica #4", "mixolidia b9 b13", "lidia #9", "alterada bb7"]
    disminuida = ["semitono tono", "tono semitono"]
    notas = [("C","C"),("Db","C#"),("D","D"),("Eb","D#"),("E","E"),("F","F"),("Gb","F#"),("G","G"),("Ab","G#"),("A","A"),("Bb","A#"),("B","B")]
    comienzo = ["primera","segunda","tercera","cuarta","quinta","sexta","séptima"]
    sorteoPrimero1 = "Escala " + elegirNota(notas) + " " + random.choice(mayor) + ", desde la  " + random.choice(comienzo)
    sorteoPrimero2 = "Escala " + elegirNota(notas) + " " + random.choice(mayor) + ", desde la  " + random.choice(comienzo)
    sorteoPrimero3 = "Escala " + elegirNota(notas) + " " + random.choice(mayor) + ", desde la  " + random.choice(comienzo)
    sorteoPrimero4 = "Escala " + elegirNota(notas) + " " + random.choice(mayor) + ", desde la  " + random.choice(comienzo)
    sorteoSegundo1 = "Escala " + elegirNota(notas) + " " + random.choice(menorMelodico) + ", desde la  " + random.choice(comienzo)
    sorteoSegundo2 = "Escala " + elegirNota(notas) + " " + random.choice(menorMelodico) + ", desde la  " + random.choice(comienzo)
    sorteoSegundo3 = "Escala " + elegirNota(notas) + " " + random.choice(menorMelodico) + ", desde la  " + random.choice(comienzo)
    sorteoSegundo4 = "Escala " + elegirNota(notas) + " " + random.choice(menorMelodico) + ", desde la  " + random.choice(comienzo)
    sorteoTercero1 = "Escala " + elegirNota(notas) + " " + random.choice(menorArmonico) + ", desde la  " + random.choice(comienzo)
    sorteoTercero2 = "Escala " + elegirNota(notas) + " " + random.choice(menorArmonico) + ", desde la  " + random.choice(comienzo)
    sorteoTercero3 = "Escala " + elegirNota(notas) + " " + random.choice(menorArmonico) + ", desde la  " + random.choice(comienzo)
    sorteoTercero4 = "Escala " + elegirNota(notas) + " " + random.choice(menorArmonico) + ", desde la  " + random.choice(comienzo)
    sorteoCuarto = sorteoPrimero4 + "\n" + sorteoSegundo4 + "\n" + sorteoTercero4 + "\n" + "Escala " + elegirNota(notas) + " " + random.choice(disminuida) + ", desde la  " + random.choice(comienzo) + "\n" + "Escala " + elegirNota(notas) + " de tonos" + ", desde la " + random.choice(comienzo)
    resultado = "<p>ESCALAS PRIMERO"+ "\n"  + sorteoPrimero1 +"\n" + sorteoPrimero2 + "\n" + sorteoPrimero3 + "\n\n" + "ESCALAS SEGUNDO" + "\n" + sorteoSegundo1 + "\n" + sorteoSegundo2 + "\n" + sorteoSegundo3 + "\n\n" + "ESCALAS TERCERO" + "\n" + sorteoTercero1 + "\n" + sorteoTercero2 + "\n" + sorteoTercero3 + "\n\n" + "ESCALAS CUARTO\n" + sorteoCuarto + "</p>"
    resultado = resultado.replace("\n", "<br>")

    return resultado


def elegirNota(notas):
    duplas = random.choice(notas)
    elemento = random.choice(duplas)
    return elemento

def sorteoTemas():
    primero = ['Straight no Chaser', 'Now is the time', 'Autumn Leaves', 'Au privae', 'All of me', 'Billies Bounce', 'Lady Bird', 'Blue Bossa', 'I got Rithm', 'Take the "A" Train', 'Softly as a morning', 'Solar', 'Equinox', 'Recordame', 'What is this thing called love', 'There will never be another you']
    segundo = ['Stella By a Starlight', 'Alone together', 'All the things you are', 'Blue in green', 'You dont know what love is', 'Have you meet miss Jones', 'Days of Wine and Roses', 'There is no greater love', 'Donna Lee', 'Someday my prince will come', 'Blues for Alice', 'On Green dolphin Street', 'Ill remember April', 'Oleo', 'Just friends', 'Out of nowhere']
    tercero = ['Joy Spring', 'Lazy Bird', 'Body and Soul', 'How insensitive', 'Footprints', 'A night in Tunnisia', 'Beatrice', 'Yardbird suite', 'Giant Steps', 'Cherokee', 'darn that Dream', 'Dexterity', 'Seven Steps to Heaven', 'Invitation', 'Whisper Not', 'It could happen to you']
    cuarto1 = ['Straight no Chaser', 'Now is the time', 'Autumn Leaves', 'Au privae', 'All of me', 'Billies Bounce', 'Lady Bird', 'Blue Bossa', 'I got Rithm', 'Take the "A" Train', 'Softly as a morning', 'Solar', 'Equinox', 'Recordame', 'What is this thing called love', 'There will never be another you', 'Stella By a Starlight', 'Alone together', 'All the things you are', 'Blue in green', 'You dont know what love is', 'Have you meet miss Jones', 'Days of Wine and Roses', 'There is no greater love', 'Donna Lee', 'Someday my prince will come', 'Blues for Alice', 'On Green dolphin Street', 'Ill remember April', 'Oleo', 'Just friends', 'Out of nowhere', 'Joy Spring', 'Lazy Bird', 'Body and Soul', 'How insensitive', 'Footprints', 'A night in Tunnisia', 'Beatrice', 'Yardbird suite', 'Giant Steps', 'Cherokee', 'Darn That Dream', 'Dexterity', 'Seven Steps to Heaven', 'Invitation', 'Whisper Not', 'It could happen to you']
    cuarto2 = ["Very Early", "Round Midnight", "Yes or No", "Falling Grace", "Milestones (Old Version)", "Tema Propio 1", "Tema Propio 2", "Naima", "Dolphin Dance", "Inner Urge", "Tema Propio 3", "Tema Propio 4", "Tema Propio 5", "Tema a elegir"]
    random.shuffle(primero)
    random.shuffle(segundo)
    random.shuffle(tercero)
    random.shuffle(cuarto1)
    random.shuffle(cuarto2)
    while len(primero) < len(cuarto1):
        primero.append("")
    while len(segundo) < len(cuarto1):
        segundo.append("")
    while len(tercero) < len(cuarto1):
        tercero.append("")
    while len(cuarto2) < len(cuarto1):
        cuarto2.append("")
    filas = {}
    
    for i in range(len(cuarto1)):
        filas[i] = (i +1 ,primero[i], segundo[i], tercero[i], cuarto1[i], cuarto2[i])
    
    for x in filas:
        print(filas[x])  

    return filas
#sorteoTemas()

