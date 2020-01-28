from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

#7el maroc annace f google chrome
browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.marocannonces.com/index.php?a=4")

#dkhal smiya o lpassword dyalk
blassa_dyal_Username = browser.find_element_by_id('username')
blassa_dyal_Username.send_keys("comptedyalchar7@gmail.com")
blassa_dyal_password = browser.find_element_by_id('password')
blassa_dyal_password.send_keys("123456789")

#cliki 3la valider
browser.find_element_by_xpath("//input[@type='submit' and @value='Valider']").click()
#tsena chwiya 15 secande
tsena_chwiya = time.sleep(15)


# man hna aybda i9leb 7et lien dyalk domain dkhedma dyalk
lien1 = "https://www.marocannonces.com/categorie/309/Offres-emploi/annonce/8208308/ASSISTANTE-POLYVALENTE.html"



#fonction dyal dfi3
def postule ( ):
    postuler1 = browser.find_element_by_class_name("btn-reply")
    time.sleep(4)
    postuler1.click()
    time.sleep(12)
    smiya_dyalk = browser.find_element_by_id("c_senders_name")
    smiya_dyalk.send_keys("Ahmed Mohamed")
    num_dyalk = browser.find_element_by_id("c_senders_phone")
    num_dyalk.send_keys("0600012345")
    postuler_final = browser.find_element_by_id("btn_envoyer")
    postuler_final.click()
    retour = browser.find_element_by_class_name("backtoads")
    retour.click()
    time.sleep(4)

lien1_de_depart = browser.get(lien1)


while True:
    try:
        postule()
        anance_suivant = browser.find_element_by_class_name("previous_ad_link")
        anance_suivant.click()
        time.sleep(60)
    except:
        browser.refresh()
        time.sleep(6)







