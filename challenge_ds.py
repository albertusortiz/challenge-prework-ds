import pandas as pd
import numpy as np
# pd.__version__

print ('Strating ...')
file_name = 'INAH_detallado_2019.xlsx' #Saving file name in a variable
df_inah = pd.read_excel(file_name) #Reading from Excel file with Pandas.
pd.options.display.float_format = '{:,.1f}'.format #Quitando la notacion cientifica a la tabla que muestra las cualidades estadisticas del dataframe

print('===+++ Welcome from data INAH 2019 +++===\n') #Show message that program is run
print('Make sure you have the file *INAH_detallado_2019.xlsx* in the same folder as this program please\n')
print('Please, choose a number option:')
print ('1: Totales por Estado por temporalidad (Mes y Año)')
print ('2: Totales por Estado por tipo de visitante')
print ('3. Totales por Estado por tipo de visitante y temporalidad (Mes y Año)')
print ('4. Totales por Centro de trabajo y temporalidad (Mes y año)')
print ('5. Totales por Centro de trabajo por tipo de visitante (Año)')
print ('6. Promedio de visitantes totales por estado (Mes y Año)')
print ('7. Promedio de visitantes por tipo de visitante, por estado (Mes y Año)')

option_menu = int(input("Put number option: "))

if (option_menu == 1):
    #- Totales por Estado por temporalidad (Mes y Año)
    print (df_inah.groupby(['Estado','A�o','Mes'])['N�mero de visitas'].sum().rename('Total').to_frame())
    
elif (option_menu == 2):
    #- Totales por Estado por tipo de visitante
    print (df_inah.groupby(['Estado','Tipo de visitantes'])['N�mero de visitas'].sum().rename('Total').to_frame())
elif (option_menu == 3):
        #- Totales por Estado por tipo de visitante y temporalidad (Mes y Año)
        print (df_inah.groupby(['Estado','A�o','Mes','Tipo de visitantes'])['N�mero de visitas'].sum().rename('Total').to_frame())
elif (option_menu == 4):
        # - Totales por Centro de trabajo y temporalidad (Mes y año)
        print (df_inah.groupby(['Centro de trabajo','A�o','Mes'])['N�mero de visitas'].sum().rename('Total').to_frame())
elif (option_menu == 5):
        # - Totales por Centro de trabajo por tipo de visitante (Año)
        print (df_inah.groupby(['Centro de trabajo','A�o','Tipo de visitantes'])['N�mero de visitas'].sum().rename('Total').to_frame())
elif (option_menu == 6):
        #- Promedio de visitantes totales por estado (Mes y Año)
        print (df_inah.groupby(['Estado','A�o','Mes'])['N�mero de visitas'].mean().rename('Promedio').to_frame())
elif (option_menu == 7):
        #- Promedio de visitantes por tipo de visitante, por estado (Mes y Año)
        print (df_inah.groupby(['Estado','A�o','Mes','Tipo de visitantes'])['N�mero de visitas'].mean().rename('Promedio').to_frame())
else:
    print('Sorry, the option no exist')
