# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik.
# Kétféle italt ismerünk: sör és kóla.
# Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
# Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
# Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")

kor = int(input("Hány éves? "))
ital = input("Írja be, hogy sör, vagy kóla az amit szeretne?")
if (ital=="sör" and kor < 18):
    print("Sajnos nem adhatok sört, mert kiskorú!")
elif (ital=="kóla" and kor > 60):
    print("A koffein megemelheti a vérnyomását!")
elif ital=="sör":
    print("Parancsoljon, a söre.")
elif ital=="kóla":
    print("Parancsoljon,a kólája.")
elif (ital != "sör" or ital != "kóla"):
    print("Csak sört és kólát tudunk adni!")
