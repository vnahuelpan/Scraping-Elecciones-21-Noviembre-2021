
#%%
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#%%

def tomar_lista(xpath, driver):
    '''
    Input: full xpath de una lista desplegable
    
    Output: 
    unidad_combo: 
    opcion_unidad: lista de todos los elementos de la lista desplegable
    unidad: elemento de la lista desplegable
    '''
    
    unidad = driver.find_element_by_xpath(xpath)
    unidad_combo = Select(unidad)
    time.sleep(3)
    
    opcion_unidad = [x.get_attribute("text") for x in unidad.find_elements_by_tag_name("option")]
    opcion_unidad = opcion_unidad[1:len(opcion_unidad)]

    return unidad_combo, opcion_unidad, unidad


#%%
#xpath0 = "/html/body/div[2]/div[1]/div[2]/div/ul/li[3]/a"
xpath1 = "/html/body/div[2]/div[1]/div[2]/div/form/select[4]"
xpath2 = "/html/body/div[2]/div[1]/div[2]/div/form/select[5]"
xpath3 = "/html/body/div[2]/div[1]/div[2]/div/form/select[6]"
xpath4 = "/html/body/div[2]/div[1]/div[2]/div/form/select[9]"
xpath5 = "/html/body/div[2]/div[1]/div[2]/div/form/select[10]"
xpath6 = "/html/body/div[2]/div[1]/div[2]/div/form/select[11]"
xpath7 = "/html/body/div[2]/div[1]/div[2]/div/form/select[12]"


#%%
def tomar_resultados_presidenciales(lista_region):
    
    assert type(lista_region) == list, "lista_region debe ser una lista"
    xpath0 = "/html/body/div[2]/div[1]/div[2]/div/ul/li[3]/a"
        
    link = "http://www.servelelecciones.cl/"

    driver = webdriver.Chrome(executable_path= "driver/chromedriver.exe")
    driver.get(link)
    time.sleep(2)
    
    driver.find_element_by_xpath(xpath0).click()
    time.sleep(2)

    select_region, _ ,_ = tomar_lista(xpath1, driver)

    for region in lista_region:
        select_region.select_by_visible_text(region)
        select_distrito, lista_distrito, _ = tomar_lista(xpath3, driver)
        
        for distrito in lista_distrito:
            select_distrito.select_by_visible_text(distrito)
            select_comuna, lista_comuna, _ = tomar_lista(xpath4, driver)

            df_resultados= pd.DataFrame()
            
            for comuna in lista_comuna:
                select_comuna.select_by_visible_text(comuna)
                select_cirscunscripcion, lista_cirscunscripcion,_ = tomar_lista(xpath5, driver)

                for cirscunscripcion in lista_cirscunscripcion:
                    select_cirscunscripcion.select_by_visible_text(cirscunscripcion)
                    select_local, lista_locales, _ = tomar_lista(xpath6, driver)
                    
                    for local in lista_locales:
                        select_local.select_by_visible_text(local)
                        select_mesa, lista_mesas, mesa= tomar_lista(xpath7, driver)
                
                        for mesa in lista_mesas:                          
                            select_mesa.select_by_visible_text(mesa)
                            
                            time.sleep(1)
                            
                            while True:
                                
                                try:
                                                                            
                                    df_aux= pd.read_html(driver.page_source)[0]
                                    df_aux.drop(columns = ['Unnamed: 4', 'Unnamed: 5'], inplace = True)
                                    
                                    df_aux["Region"] = region
                                    df_aux["Distrito"] = distrito
                                    df_aux["Comuna"]= comuna
                                    df_aux["Lista Electoral"]= cirscunscripcion
                                    df_aux["Local"]=local
                                    df_aux["Mesa"] = mesa

                                    df_aux = df_aux[df_aux["Nombre de los Candidatos"].notna()]
                                    df_resultados = df_resultados.append(df_aux)
                                    
                                except:
                                    continue
                                
                                else:
                                    break
                                    

                            print(comuna, local, mesa)
            

            df_resultados.to_csv("resultados_presidencial/"+distrito + ".csv",encoding="utf-8")

    driver.close()

#%%
def tomar_resultados_otras(eleccion, lista_region):
    
    assert type(lista_region) == list, "lista_region debe ser una lista"  
    assert eleccion in tipo_eleccion, "las opciones validas son senatorial, diputados y cores"
         
    if eleccion == "senatorial":
        xpath0 = "/html/body/div[2]/div[1]/div[1]/menu-elecciones/div/nav/div/div[2]/ul/li[2]/a"
    
    if eleccion == "diputados":
        xpath0 = "/html/body/div[2]/div[1]/div[1]/menu-elecciones/div/nav/div/div[2]/ul/li[3]/a"
        
    if eleccion == "cores":
        xpath0= "/html/body/div[2]/div[1]/div[1]/menu-elecciones/div/nav/div/div[2]/ul/li[4]/a"
           
    link = "http://www.servelelecciones.cl/"

    #df = pd.DataFrame(columns=["Region", "Distrito", "Comuna","Lista Electoral" ,"Local", "Mesa"])
    #df_resultados= pd.DataFrame()
    
    driver = webdriver.Chrome(executable_path= "driver/chromedriver.exe")
    driver.get(link)
    time.sleep(2)
    
    driver.find_element_by_xpath(xpath0).click()
    time.sleep(2)

    select_region, _ ,_ = tomar_lista(xpath1, driver)

    for region in lista_region:
        select_region.select_by_visible_text(region)
        select_distrito, lista_distrito, _ = tomar_lista(xpath3, driver)
        
        for distrito in lista_distrito:
            select_distrito.select_by_visible_text(distrito)
            select_comuna, lista_comuna, _ = tomar_lista(xpath4, driver)

            df_resultados= pd.DataFrame()
            
            for comuna in lista_comuna:
                select_comuna.select_by_visible_text(comuna)
                select_cirscunscripcion, lista_cirscunscripcion,_ = tomar_lista(xpath5, driver)

                for cirscunscripcion in lista_cirscunscripcion:
                    select_cirscunscripcion.select_by_visible_text(cirscunscripcion)
                    select_local, lista_locales, _ = tomar_lista(xpath6, driver)
                    
                    for local in lista_locales:
                        select_local.select_by_visible_text(local)
                        select_mesa, lista_mesas, mesa= tomar_lista(xpath7, driver)
                
                        for mesa in lista_mesas:                          
                            select_mesa.select_by_visible_text(mesa)
                            
                            time.sleep(1)
                            
                            while True:
                                
                                try:
                                                                            
                                    df_aux= pd.read_html(driver.page_source)[0]
                                    df_aux.drop(columns = ['Unnamed: 5'], inplace = True)
                                    
                                    df_aux["Region"] = region
                                    df_aux["Distrito"] = distrito
                                    df_aux["Comuna"]= comuna
                                    df_aux["Lista Electoral"]= cirscunscripcion
                                    df_aux["Local"]=local
                                    df_aux["Mesa"] = mesa
                                    
                                    df_aux = df_aux[df_aux["Lista/Pacto"].notna()]
                                    df_resultados = df_resultados.append(df_aux)
                                    
                                except:
                                    continue
                                
                                else:
                                    break
                                    

                            print(comuna, local, mesa)
            

            df_resultados.to_csv("resultados_"+str(eleccion)+"/"+distrito + ".csv",encoding="utf-8")

    driver.close()




# %%
