import flet
from flet import Page
import os, importlib.util
import warnings

"""
La logica de enrutamiento es diferente a la documentación de Flet
Usamos los modulos (archivos de la carpeta paginas) como pares de key:value en un diccionario global, 
de esta manera podemos acceder a cada archivo llamandolo por su key.
"""

#
global _moduleList
_moduleList = {}

# Usamos el método os.walk() para obtener el directorio raiz
for _, dirs, __ in os.walk(r'./'):
    # El os.walk() retorna una tupla con tres items
    # raiz, directorios y archivos => solo nos interesan las carpetas, especificamente la carpeta llamada paginas
    for dir in dirs:
        if dir == 'paginas': # Si la carpeta se llama paginas..
            for filename in os.listdir(dir): # Lista todos los nombres de archivos en la carpeta paginas
                _file = os.path.join(dir, filename)
                # Crea una ruta de archivo para cada archivo
                # revisa si el item es un archivo
                if os.path.isfile(_file):
                    filename = filename[:-3] # Borra los ultimos tres caracteres (extensiones)
                    
                    _moduleList[
                        "/" + filename
                    ] = importlib.util.spec_from_file_location(filename, _file)
                    # Aca se guarda la key como "/" + Lo que sea que el nombre del archivo es, asi que seria /login, /registro, /index, etc ...
                    # El valor para cada uno sera la ubicacion de los archivos y la habilidad de ser cargada como módulo.
                    

def main(page: Page):
    page.title = 'Aplicación Web y Autenticación con Flet'
    warnings.filterwarnings(
    "ignore", 
    message="The python_jwt module is deprecated"
)
    warnings.filterwarnings(
    "ignore", 
    message="UserControl is deprecated since version 0.21.0"
)
    # La primera pagina sera la vista login
    # Ya que la logica ya esta puesta, se puede asignar la primera vista
    page.views.append(
        _moduleList['/login'].loader.load_module()._view_()
    )
    # se asigna el url
    page.go("/login")
    page.update()
    pass

if __name__ == '__main__':
    flet.app(target=main, view=flet.WEB_BROWSER, port=8550)