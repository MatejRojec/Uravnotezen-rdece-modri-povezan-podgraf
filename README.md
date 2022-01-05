# Uravnotezen-rdece-modri-povezan-podgraf

## Opis problema
    Naj bo $G = (V, E)$ graf. Vsako vozlišče $v \in V $ je obarvano rdeče ali modro. 
    Najti želimo največji povezani podgraf $G' = (V', E')$, ki ima enako število rdečih in modrih vozlišč.
    Velikost podgrafa je število njegovih vozlišč. Ta problem je v splošnem NP-težek, kar pomeni da ga ne moremo
    rešiti v polinomskem času.
    Osredotočili se bomo na optimalen algoritem za reševanje problema na mrežah oblike $1 \times n$ (pot), $2 \times n$, 
    $3 \times n$ in $4 \times n$.
    Naš algoritem bomo testirali na grafih, kjer bomo vožlišča obarvali rdeče z verjetnostjo $p \in (0,1)$ 
    in modro z verjetnostjo $1 - p$.


## Zaženi program
<ol>
    <li>Kolnirajte repozitorij</li>
    <li>Poženite vmesnik.py z ukazom v terminalu (pot kjer se nahaja repozitorij/ <b>$ python spletni_vmesnik.py </b>)</li>
</ol>

### Opombe
<ul>
    <li>pomebna koda ter funkcije se nahajajo v $ model.py</li>
    <li>uporabili smo pakete:</li>
</ul>
