# Uravnotezen-rdece-modri-povezan-podgraf

## Opis problema
>    Naj bo G = (V, E) graf. Vsako vozlišče v ∈ V je obarvano rdeče ali modro. Najti želimo največji povezani podgraf G' = (V', E'), ki ima enako število rdečih in modrih         vozlišč.
    Velikost podgrafa je število njegovih vozlišč. Ta problem je v splošnem NP-težek, kar pomeni da ga ne moremo
    rešiti v polinomskem času.
    Osredotočili se bomo na optimalen algoritem za reševanje problema na mrežah oblike 1xn (pot), 2xn, 
    3xn in 4xn.
    Naš algoritem bomo testirali na grafih, kjer bomo vožlišča obarvali rdeče z verjetnostjo 0 < p < 1, 
    in modro z verjetnostjo 1 - p.
---

## Sestava repozitorija

* ALGO_BCS
    * Vsebuje model `modelBCS.py` za glavni algoritem `algoritem.py` in nekaj primerov `primeri.py`.
* Kratek_opis
    * Vsebuje katrko poročilo `opis.pdf`.
* Poročilo
    * Vsebuje glavno poročilo z ekperimenti `porocilo.pdf`.
* Eksperimenti
    * Vsebuje excel datoteke s podatki testiranj in datoteko `analiza.R` za analizo in vizualizacijo v R-ju.
* program
    * v pripravi za predstavitev...

