import sys
def ft_spec_mois(j, a, trente, fev, valide, bisextile):
#Récupération des spécificités du mois#
    if  (trente == True and  (0 >= j or j > 30)):
        print ("Nombre de jour incorrect :",j)
        sys.exit(0)
    elif(trente == False) and (fev == False) and (valide == True) \
        and (0 >= j or j > 31):
        print ("Nombre de jour incorrect :",j)
        sys.exit(0)
    elif (fev == True) and (bisextile == False) and (0 >= j or j > 28):
        print ("Nombre de jour incorrect :",j)
        sys.exit(0)
    elif (fev == True) and (bisextile == True) and (0 >= j or j > 29):
        print ("Nombre de jour incorrect :",j)
        sys.exit(0)
    if a < 0:
        print ("Année incorrecte :",a)
        sys.exit(0)

    if  (0 > m) and (m > 13):
        print ("Le mois ", m ,"est incorrect il doit être compris entre 1 et 12.")
        sys.exit(0)

    if (a % 400 == 0) or ((a % 100 != 0) and (a % 4 == 0)) :
        print ("L'année", a ,"est bisextile.")
        bisextile = True

    else :
        print ("L'année ", a ,"n'est pas bisextile.")
        bisextile = False


#Affichage du nombre de jours par mois
    if ( trente == True):
        print ("En",Dico_mois[m], a,"il y a 30 jours.")
    elif (trente == False) and (fev == False) and (valide == True):
        print ("En",Dico_mois[m], a,"il y a 31 jours.")
    elif (fev == True) and (bisextile == False):
        print ("En Fevrier",a,"il y a 28 jours.")
    elif (fev == True) and (bisextile == True):
        print ("En Fevrier",a,"il y a 29 jours.")
    else :
        sys.exit(0)


def ft_count_days(j, m, a):
#Récupération du jour depuis le 1/1/1#
    Dico_jmois = {1:0, 2:31, 3:59, 4:90, \
             5:120, 6:151, 7:181,8:212, \
             9:243, 10:273, 11:304, \
             12:334}
    y = a - 1
    days = ((y * 365) + (((y//4)-(y//100))+(y//400)))
    print ("Il s'est écoulé",days,"jours depuis le 1/1/1")
    if bisextile == False:
        d_since_syear = Dico_jmois[m]
        print ("Il s'est écoulé",d_since_syear,"jours entre le 1/1",a,"et le 1/",m,"/",a)
    elif bisextile == True and m > 2:
        d_since_syear = Dico_jmois[m] + 1
        print ("Il s'est écoulé",d_since_syear,"jours entre le 1/1",a,"et le 1/",m,"/",a)
    else:
        d_since_syear = Dico_jours[m]
        print ("Il s'est écoulé",d_since_syear,"jours entre le 1/1",a,"et le 1/",m,"/",a)

    d_since_smonth = d_since_syear + j
    print ("Le",j,"/",m,"/",a,"est le",d_since_smonth,"eme jour de l'année",a)

    Dico_jours = {0:"Dimanche", 1:"Lundi", 2:"Mardi", 3:"Mercredi", \
              4:"Jeudi", 5:"Vendredi", 6: "Samedi"}
    
    d_all = d_since_syear + d_since_smonth 
    d_week = (d_all // 7)
    print(Dico_jours[d_week])

def ft_season(m, j):
#Récupération de la saison
    if ((m == 3 and j > 19) or (m == 4 or m == 5) or (m == 6 and j < 20)):
        print ("Cette date est au Printemps.")
    elif ((m == 6 and j > 19) or (m == 7 or m == 8) or (m == 9 and j <22)):
        print ("Cette date est en Été.")
    elif ((m == 9 and j > 21) or (m == 10 or m == 11) or (m == 12 and j <19)):
        print ("Cette date est en Automne.")
    else :
        print ("Cette date est en Hiver.")

#Dictionnaire des mois#
Dico_mois = { 1:"Janvier", 2:"Fevrier", 3:"Mars", 4:"Avril", \
             5:"Mai", 6:"Juin", 7:"Juillet",8:"Aout", \
             9:"Septembre", 10:"Octobre", 11:"Novembre", \
             12:"Decembre"}

valide = True
trente = False
fev = False
bisextile = False #Variable necessaire pour le mois de Fevrier#
a = int(input("Année:")) #Variable de l'année#
m = int(input("Mois:")) #Variable du mois#
j = int(input("Jour:")) #Variable du jour#

if m <= 12 and m >= 1:
    if m == 11 or m == 4 or m == 6 or m == 9:
        trente = True
        fev = False
    elif m == 2:
        trente = False
        fev = True
    else :
        fev = False
        trente = False
else :
    valide = False

print ("La date choisie est ",j,"/",m,"/",a,".")
ft_spec_mois(j, a, trente, fev, valide, bisextile)
ft_season(m,j)
ft_count_days(j, m, a)
print(ft_day_date(j, m, a))
