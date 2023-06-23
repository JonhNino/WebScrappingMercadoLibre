from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.mercadolibre.com.co/")
print(driver.title)
search_bar = driver.find_element(By.CLASS_NAME, "nav-search-input")
search_bar.clear()
search_bar.send_keys("Celulares")
search_bar.send_keys(Keys.RETURN)

pagination =driver.find_element(By.XPATH,"//li[contains(@class, 'andes-pagination__page-count')]").text
pagination =[int(s) for s in pagination.split() if s.isdigit()][0]
print("La Paginacion es de : ")
print(pagination)

records=[]

for page in range(1,pagination+1):
    if page != pagination:
        next_page_button = driver.find_element(By.CSS_SELECTOR, "a[title='Siguiente']")
    
        links_products = driver.find_elements(By.XPATH,"//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a[1]")
        links_products =[link.get_attribute("href") for link in links_products]
        print(links_products)

    images = driver.find_elements(By.XPATH,"//img[contains(@class, 'ui-search-result-image__element shops__image-element')]")
    images = [image.get_attribute("data-src") 
              if image.get_attribute("data-src") 
              else image.get_attribute("src") for image in images]
    print(images)

    descriptions = []
    colors = []
    condicions = []
    marcas = []
    # Iterar sobre cada link y extraer la información deseada
    for link in links_products:
        driver.get(link)
        try:
            marca = driver.find_element(By.CSS_SELECTOR, ".ui-pdp-title")
            marca = marca.text.split()[0]
        except :
            marca = "El Vendedor no dejo Marca"
        print(marca)
        marcas.append(marca)
        try:
            description = driver.find_element(By.CSS_SELECTOR, "p.ui-pdp-description__content").text
            description = description.replace(",", " ").replace("\n", " ").replace(".", " ").replace("ñ", "n").replace("á", "a").replace("Á", "A").replace("é", "e").replace("É", "E").replace("í", "i").replace("Í", "I").replace("ó", "o").replace("Ó", "O").replace("ú", "u").replace("Ú", "U")
        except:
            description = "Vendedor No coloco Descripcion"
        descriptions.append(description)
        #print(description) 
        try:
            #color_element = driver.find_element(By.XPATH, "//*[@id='picker-label-COLOR']/span").text
            color = driver.find_element(By.XPATH, "//span[@id='picker-label-COLOR']").text
        except:
            try:
                color = driver.find_element(By.CLASS_NAME, "ui-pdp-variations__selected-label.ui-pdp-color--BLACK").text
            except:
                color = "NO-COLOR"
        print(color)
        colors.append(color)
        #print(color)   
        try:
            condicion = driver.find_element(By.XPATH, "//span[@class='ui-pdp-subtitle']")
            text = condicion.text
            # Dividir el texto en palabras y obtener la primera
            first_word = text.split()[0]
            # Verificar si la primera palabra es "Nuevo" o "Usado"
            if first_word == "Nuevo":
                condicion=first_word
            else:
                condicion=first_word          
        except:
            condicion= "Vendedor No establacio Condicion"
        condicions.append(condicion)
        
        #condicions.append("Vendedor No establacio Condicion")
        # Regresar a la página de resultados de búsqueda
        driver.back()
    #time.sleep(15)
    title_products = driver.find_elements(By.XPATH,"//h2[@class='ui-search-item__title shops__item-title']")
    title_products =[title.text for title in title_products]
    print(title_products)

    price = driver.find_elements(By.XPATH,"//li[@class='ui-search-layout__item shops__layout-item']//div[@class='ui-search-result__content-columns shops__content-columns']//div[@class='ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left']/div[1]/div//div[@class='ui-search-price__second-line shops__price-second-line']//span[@class='price-tag-amount']//span[2]")
    price =[price.text for price in price]
    print(price)
    # Check that all arrays have the same length
    #assert len(title_products) == len(condicions) == len(price) == len(links_products) == len(descriptions) == len(colors) == len(images)
    
    data_products = {
                "name_product": title_products,
                "price_product": price,
                "link_product": links_products,
                "marca": marcas,
                "description_product": descriptions,
                "color_product": colors,
                "condicion": condicions,
                "images": images
            }

    df=pd.DataFrame(data_products)
    records.append(df)
    if page == 4:
        break
    next_page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Siguiente']")))
    driver.execute_script("arguments[0].click()", next_page_button)
df =pd.concat(records)
df.to_csv("Celulares.csv")
time.sleep(2)
driver.close()