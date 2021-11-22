#%%
from funciones import tomar_resultados_presidenciales, tomar_resultados_otras

lista_region = [    
                    'METROPOLITANA DE SANTIAGO', 
                    'DE ARICA Y PARINACOTA', 
                    'DE TARAPACA', 
                    'DE ANTOFAGASTA', 
                    'DE ATACAMA', 
                    'DE COQUIMBO', 
                    'DE VALPARAISO', 
                    "DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS", 
                    'DEL MAULE', 
                    'DE ÑUBLE', 
                    'DEL BIOBIO', 
                    'DE LA ARAUCANIA', 
                    'DE LOS RIOS', 
                    'DE LOS LAGOS', 
                    'DE AYSEN DEL GENERAL CARLOS IBAÑEZ DEL CAMPO', 
                    'DE MAGALLANES Y DE LA ANTARTICA CHILENA']


lista_region_senatorial =   [   'METROPOLITANA DE SANTIAGO', 
                                'DE ANTOFAGASTA', 
                                'DE COQUIMBO',  
                                "DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS", 
                                'DE ÑUBLE', 
                                'DEL BIOBIO', 
                                'DE LOS RIOS', 
                                'DE LOS LAGOS', 
                                'DE MAGALLANES Y DE LA ANTARTICA CHILENA']

tipo_eleccion = ["presidencial",
                 "senatorial",
                 "diputados",
                 "cores"]

#%%
tomar_resultados_presidenciales(lista_region)

#%%
tomar_resultados_otras("senatorial", lista_region_senatorial)

#%%
tomar_resultados_otras("diputados", lista_region)
#%%
tomar_resultados_otras("cores", lista_region)
# %%


