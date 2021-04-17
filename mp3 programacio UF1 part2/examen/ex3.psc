Algoritmo sin_titulo
	
	Definir textCodificat, textDescodificat,textComprovat Como Caracter
	Definir abc, codi,lletra Como Caracter
	Definir i,j,l Como Entero
	Dimension abc[26], codi[26]
	
	abc[0]="a"
	abc[1]="b"
	abc[2]="c"
	abc[3]="d"
	abc[4]="e"
	abc[5]="f"
	abc[6]="g"
	abc[7]="h"
	abc[8]="i"
	abc[9]="j"
	abc[10]="k"
	abc[11]="l"
	abc[12]="m"
	abc[13]="n"
	abc[14]="o"
	abc[15]="p"
	abc[16]="q"
	abc[17]="r"
	abc[18]="s"
	abc[19]="t"
	abc[20]="u"
	abc[21]="v"
	abc[22]="w"
	abc[23]="x"
	abc[24]="y"
	abc[25]="z"
	
	codi[0]="!"
	codi[1]="·"
	codi[2]="$"
	codi[3]="%"
	codi[4]="&"
	codi[5]="/"
	codi[6]="("
	codi[7]=")"
	codi[8]="="
	codi[9]="?"
	codi[10]="¿"
	codi[11]="^"
	codi[12]="*"
	codi[13]="["
	codi[14]="]"
	codi[15]="{"
	codi[16]="}"
	codi[17]="+"
	codi[18]="-"
	codi[19]="_"
	codi[20]="ª"
	codi[21]=":"
	codi[22]=";"
	codi[23]=">"
	codi[24]="º"
	codi[25]="<"
	
	textDescodificat = ""
	textCodificat = "L! *!?]+=! %&^- ·][- {+](+!*!%]+- {+](+!*&[, [] {&+}ª& &-{&+&[ $]·+!+ ] {&+ !%ª^!$=] {&+ {!+_ %& {ª·^=$, -=[] {&+}ª& &- %=:&+_=_ {+](+!*!+ L=[ª- T]+:!^%-"
	
	l =Longitud(textCodificat)
	
	para i=0 hasta l
		lletra=Subcadena(textCodificat,i,i)
		
		para j=0 hasta 24 Hacer
			si codi[j] == lletra Entonces
				lletra=abc[j]
			FinSi
		FinPara
		textDescodificat = textDescodificat + lletra
	FinPara
	
	Escribir textDescodificat
	
FinAlgoritmo
