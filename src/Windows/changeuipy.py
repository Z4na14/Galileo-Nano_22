import os
archivo = str(input("Como se llama el archivo: "))
longitud = len(archivo)
os.system(f"C:/Users/jorge/Desktop/Repos/Galieo-Nano_22/Scripts/pyuic5.exe {archivo} -o {archivo[:longitud-3]+'.py'}")
