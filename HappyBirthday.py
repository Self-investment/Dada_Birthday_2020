from argparse import ArgumentParser,SUPPRESS
from datetime import datetime
import os
def main(args=None):
    # Use argparse to get arguments of your script:
    parser = ArgumentParser("Today")
    parser.add_argument("dada", action="store", help="A lovely and incredible member of our family")
    parser.add_argument("day_bth", action="store", help="A happy and an incredible day in our life")
    parser.add_argument("month_bth", action="store", help="Such a magnificent month")
    parser.add_argument("decrypt", action="store", help="what is my currency ;) ")
    #parser.add_argument("--optional", "-p", action="store",
                        #help="this is just for futur development")
    
    
    
    birthday = parser.parse_args() if args is None else parser.parse_args(args)          
    #assert(birthday.month_bth %m and birthday.training_ratio >=0), "Training ratio has to be in [0,1]."
    #assert(birthday.optional in ["Soudi", "Soudabeh", "Sister"]), "Unknown fabuleus person: {0}".format(birthday.optional)


dict_family = { 'daddy': ['baba jan', 'MEHRZAD Jan Pesare Azizam TAVALODET MOBARAK'],  'mommy':['maman jan','Pesarake Azizam :) TAVALODET MOBARAK'], 'sister': ['khahar azizam', '\nSalam bar aziz, moones va jegare khahar. Tavalodet hezaran hezar bar mobarake man ke aziz delei mesle shoma ro Khoda bem dadeh.\nAzizi ke yadegare madar azizam hastesh va moonesi ke midoonam saddarsad vojoodesh saie dareh behem komak kone va HICH vaght kam nazashteh he besiar besiar \nbishtar az oonchekeh bayad anjam bedeh dadeh. Aziz khahar bayad eteraf konam oonghadr ke man dar shoma az khod gozashtegi didam dar khodam nadidam \nsokhan kootah konam, vaghan az vojood, seresht va labkhandeh ghashanget lezat mibaram va behem aramesh mideh \nBARADAR AZIZAM TAVALODET MOBARAK, Bon Anniversaire. shado salamat bashi azizam.'], 'emio': ['emio', 'she is just beside you']}
#current date and time
now = datetime.now()  

#date format: dd-mm-yyyy
format = "%d-%m-%Y"

#format datetime using strftime()
date1 = now.strftime(format)


print("Formatted Date:", date1)

lst=['daddy','mommy','emio','sister']
for i in range(0,len(lst)):
    s=True
    while s:
        print ("how do you call your %s?"%lst[i])
        nom = input()
        if nom==dict_family[lst[i]][0]:
            print("-----",nom)
            print (dict_family[lst[i]][1])
            s = False
        else: 
            s = True

if __name__ =='__main__':
       main() 
