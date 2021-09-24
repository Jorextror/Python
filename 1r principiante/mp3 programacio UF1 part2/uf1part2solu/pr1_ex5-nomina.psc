Algoritmo pr1_ex5
    //Fes un algorisme que calculi el sou mensual (4 setmanes)
    //d’un treballador. El treballador cobra 15€/h les hores 
    //normals i 25€/h les hores extraordinàries. A final de mes
    //el treballador introdueix el seu nom, i les hores TOTALS, 
    //incloses les extraordinàries treballades cada setmana, 
    //la jornada laboral ordinària és de 40 hores setmanals.
    
	//L’algorisme ha de tenir la següent sortida:
	//“La Nòmina de (nom) és:
	//Hores Ordinàries: YY equivalen a ZZ euros
    //Hores Extraordinàries SS equivalen a TT euros
    
    //En total aquest mes XX cobrarà TOTAL euros”
    
    Definir C_EUR_NORM, C_EUR_EXTRA, C_HORES_NORM Como Real
    Definir nom Como Caracter
    Definir hores_tot, hores_norm, hores_extra como Real
    Definir eur_tot, eur_norm, eur_extra como Real
    
    C_EUR_NORM = 15
    C_EUR_EXTRA = 25
    C_HORES_NORM = 40 * 4
    
    Escribir "Introdueix el teu nom: "
    Leer nom
    Escribir "Introdueix les hores totals: "
    Leer hores_tot
    
    si hores_tot >= C_HORES_NORM
        hores_norm = C_HORES_NORM 
        hores_extra = hores_tot - hores_norm
    SiNo
        hores_norm = hores_tot
        hores_extra = 0
    FinSi
    
    eur_norm = hores_norm * C_EUR_NORM
    eur_extra = hores_extra * C_EUR_EXTRA
    eur_tot = eur_norm + eur_extra
    
    Escribir "La Nòmina de " nom " és: " eur_tot " euros"
    Escribir "Hores Ordinàries: " hores_norm " equivalen a " eur_norm " euros"
    Escribir "Hores Extraordinàries " hores_extra " equivalen a " eur_extra " euros"
    Escribir "En total aquest mes " nom " cobrarà " eur_tot " euros"

FinAlgoritmo
