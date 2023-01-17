####################################################################
#        FONCTION PRINCIPALE À APPELER POUR REMPLIR LA BDD         #
# UTILISATION DU MULTIPROCESSING AVEC POOL POUR ACCÉLÉRER LE SCRAP #
####################################################################



from db_scrap.scrap import *
from db_scrap.connect import *
from multiprocessing import *
import time




urlsParc=["https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
    "https://www.tripadvisor.fr/Attraction_Review-g226865-d285990-Reviews-Walt_Disney_Studios_Park-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
    "https://www.tripadvisor.fr/Hotel_Review-g1182377-d262678-Reviews-Disney_Hotel_New_York_The_Art_of_Marvel-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_F.html",
    "https://www.tripadvisor.fr/Hotel_Review-g1182377-d262679-Reviews-Disney_Newport_Bay_Club-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
    "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262682-Reviews-Disney_Sequoia_Lodge-Coupvray_Seine_et_Marne_Ile_de_France.html",
    "https://www.tripadvisor.fr/Hotel_Review-g226865-d262686-Reviews-Disney_Hotel_Cheyenne-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
    "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262683-Reviews-Disney_Hotel_Santa_Fe-Coupvray_Seine_et_Marne_Ile_de_France.html",
    "https://www.tripadvisor.fr/Hotel_Review-g1221082-d564634-Reviews-Disney_Davy_Crockett_Ranch-Bailly_Romainvilliers_Seine_et_Marne_Ile_de_France.html"
    ]



def main(url):
    i=0
    if 'Hotel' in url:
        avis = scrap_hotel(url)
        while(True):
            i += 10
            new_url = url[:url.find('Reviews')+len('Reviews')]+'-or'+str(i)+url[url.find('Reviews')+len('Reviews'):]
            a = write_db(avis)
            try:
                time.sleep(1)
                avis = scrap_hotel(new_url)
            except:
                print(new_url)
                break
            if a== 0 or len(avis) == 0:
                print(f'zéro avis:\t{new_url}')
                break
    else:
        avis = scrap_parc(url)
        while(True):
            i += 10
            new_url = url[:url.find('Reviews')+len('Reviews')]+'-or'+str(i)+url[url.find('Reviews')+len('Reviews'):]
            a = write_db(avis)
            try:
                time.sleep(1)
                avis = scrap_parc(new_url)
            except:
                print(f'{new_url} ne répond pas')
                break
            if a == 0 or len(avis) == 0:
                print(f'zéro avis:\t{new_url}')
                break



def load_db():
    p = Pool()
    p.map(main, urlsParc)
    p.close()
    p.join()


