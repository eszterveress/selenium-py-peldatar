# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
# Írja ki ezek után a beolvasott számok összegét!

osszeg = int()
igaz = True
while igaz:
    szam = int(input("Írj be egy számot! "))
    if szam < 10:
        osszeg += szam
    else:
        igaz = False

print(osszeg)
