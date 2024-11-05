""" 
Pagina de Vistas
Aqui es donde la entrada del usuario entra primero.
Cuando un usuario interactúa con la app, como por ej al iniciar sesión, la vista manejará los datos y lo enviará al back end para procesarlo.
Para ello utilizaremos Firebase con un wrapper de Python llamado Pyrebase como el backend.
Esto no significa que funcione solo con Firebase, se puede utilizar cualquier Base de Datos como SQLite, POSTGRES, Mongo, etc...
"""

# Modulos
import pyrebase
from main import  _moduleList # Nuestros pares key:value globales
from datetime import datetime
from controls import postControl

# Este es el archivo principal de configuración que necesitamos para configurar la API Firebase
CONFIG = {
  "apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "databaseURL": "",
}

# Ahora, cuando el usuario se loguee, debemos de almacenar un poco de la información como para poder usar las funciones.
# Flet ya posee una función de sesión, pero este proyecto se hizo antes de que existiera eso
global SESSION
SESSION = {}

# Inicializamos la API
firebase = pyrebase.initialize_app(CONFIG)
auth = firebase.auth() # auth se utilizará para comandos de autenticación
db = firebase.database() # db se utilizará para la función de base de datos

# Función simple de enrutamiento entre la pagina de login y registro.
def ChangeRoute(e, page_route): # Esto aceptará dos argumentos
    global _moduleList # Necesitamos el diccionario que almacene las paginas
    # Cuando esta función sea llamada, queremos limpiar primero la lista de vistas
    e.page.views.clear()

    # Ahora queremos revisar cual pagina está siendo llamada para mostrarla
    if page_route == "/register":
        # Ahora podemos agregar la lista de vistas con el modulo
        e.page.views.append(
            # Aca, nuestras claves son simplemente nombres de archivos con un /
            # Asi que es / + registro. Podemos luego pasar la clave como para cargar el módulo, el cual está almacenado en un valor de pares.
            _moduleList[page_route]
            .loader.load_module()
            ._view_()
        )
        e.page.go("/register")

    if page_route == "/login":
        e.page.views.append(_moduleList[page_route].loader.load_module()._view_())
        e.page.go("/login")
        e.page.go("/register")
    
    
    # Aca si el usuario presiona en home, lo redireccionara al index
    if page_route == "/index":
        e.page.views.append(
            _moduleList[page_route].loader.load_module()._view_(
                # debemos de pasar dos argumentos
                SESSION["firstName"],
                SESSION["lastName"],
            )
        )
        # Luego debemos de volver a mostrar las tareas del usuario
        DisplayTask(e)
        # finalmente cambiamos la URL
        e.page.go("/index")

    if page_route == "/profile": # la pagina interna
        # Aca mostramos informacion adicional sobre la cuenta
        created_on, last_login, first_name, last_name, email = ProfileUserData()
        e.page.views.append(
            _moduleList[page_route]
            .loader.load_module()
            ._view_(created_on, last_login, first_name, last_name, email)
        )
        e.page.go("profile")
    else:
        pass
    
    e.page.update()

def LogUserOut(e):
    # Limpiar datos de sesión
    SESSION.clear()
    
    # Redirigir al usuario a la página de login
    ChangeRoute(e, "/login")
    
    # Actualizar la página
    e.page.update()

# Esta funcion se encarga de obtener y mostrar la informacion de la cuenta
def ProfileUserData():
    global _moduleList
    user_info = []
    # Pasamos el id principal del usuario ya que lo hemos almacenado
    info = auth.get_account_info(SESSION["users"]["idToken"])
    # estos items de la lista son las claves para la informacion
    data = ["createdAt", "lastLoginAt"]
    for key in info:
        if key == "users":
            for item in data:
                user_info.append(
                datetime.fromtimestamp(int(info[key][0][item]) / 1000).strftime(
                        "%D - %H:%M %p"
                    )
                )
    user_info.append(SESSION["firstName"])
    user_info.append(SESSION["lastName"])
    user_info.append(SESSION["users"]["email"])

    return user_info

# Ahora que el enrutamiento funciona, creamos un usuario con el formulario de registro
# Esta función será activada cuando el usuario apriete el botón de registrarse en la pagina de registro
def RegisterUser(e):
    # Aca, debemos de circular a través de la lista de vistas y elegir la pagina de registro
    for page in e.page.views[:]:
        if page.route == "/register": #page.route es el nombre de la vista
            # Aqui, debemos de acceder a los text fields
            # res ahora está en la columna principal con la entrada
            res = page.controls[0].controls[0].content.controls[4]
            try:
                # usamos la API de autenticación para registrar a un nuevo usuario con email y contraseña
                auth.create_user_with_email_and_password(
                    res.controls[2].content.value,
                    res.controls[3].content.value,
                )
                    
                # Despues de crear un usuario, queremos pasar la información a la base de datos
                data = {
                    "firstName": res.controls[0].content.value,
                    "lastName": res.controls[1].content.value,
                    "email": res.controls[2].content.value,
                    "pass": res.controls[3].content.value,
                }

                # Usamos child para enviar la información al nodo especifico de la base de datos
                # Nota: Antes de escribir a la base de datos, hay que cambiar las reglas de privacidad
                # En nuestro caso está bien, pero para una aplicación de verdad se necesesitaría más parámetros de seguridad para las reglas de la base de datos

                db.child("users").push(data)

                e.page.views.clear()
                e.page.views.append(_moduleList["/login"].loader.load_module()._view_())
                e.page.update()

            except Exception as e:
                print("Error al registrar el usuario:", e)
            finally:
                for item in res.controls[:]:
                    if item.page:
                        item.content.value = None
                        item.content.update()

# Ahora que tenemos el registro de usuario, tenemos que realizar la UI + Lógica para la fase de logueo.
def LogInUser(e):
    first_name, last_name = GetUserDetail(e)
    # Podemos obtener el nombre y apellido autenticando el correo del usuario
    # Si no hay errores, pasamos los datos a la vista /index, y llevamos al usuario a esa pagina
    e.page.views.clear()
    e.page.views.append(_moduleList["/index"].loader.load_module()._view_(first_name, last_name))
    DisplayTask(e) # llamamos la funcion aca
    e.page.go("/index")
    e.page.update()

# Crearemos otra funcion donde obtendremos y almacenaremos todos los datos importantes del usuario
def GetUserDetail(e):
    global _moduleList
    for page in e.page.views[:]:
        if page.route == "/login":
            # Estos son campos de texto con control padre
            res = page.controls[0].controls[0].content.controls[4]
            try:
                # Aca autenticamos el email y contraseña del usuario
                user = auth.sign_in_with_email_and_password(
                    res.controls[0].content.value,
                    res.controls[1].content.value,
                )
                # Si no tenemos ningun error, pasamos el valor retornado del usuario
                SESSION["users"] = user # Guardamos el dato como pares de key:value

                # Ahora, necesitamos acceder a la base de datos primero para obtener el nombre y apellido, asi como tambien el nodo de ruta del usuario
                # La cosa principal con la base de datos de firebase es la ruta
                # abajo, simplemente accedemos a la ruta de usuario y obtenemos los datos
                val = db.child("users").get()  
                for i in val:
                    # Aca, revisamos el email de la base de datos con el email que el usuario quiere autenticar.
                    # Si es el mismo, continua
                    if i.val()["email"] == user["email"]:
                        first_name = i.val()["firstName"]
                        last_name = i.val()["lastName"]
                        SESSION["path"] = i.key() # este es el ID nodo del usuario
                        SESSION["firstName"] = first_name
                        SESSION["lastName"] = last_name
                    
                        return [first_name, last_name]

            except Exception as e:
                print(e)

    return [None, None]

# Esta funcion se encarga de la habilidad de postear textos
def PostText(e, first_name:str, last_name:str):
    # Obtenemos la fecha primero porque lo vamos a mostrar
    post_date = datetime.now().strftime("%b %d, %Y %I:%M")

    for page in e.page.views[:]:
        if page.route == "/index":
            # Aca esta el indice de la entrada del post que creamos en la vista /index
            res = page.controls[0].controls[0].controls[2].controls[1].controls[0]

            # Establecemos data en un diccionario
            # Usaremos esto dentro del UI del post
            data = {
                "firstName": first_name,
                "lastName": last_name,
                "postDate": post_date,
                "post": res.content.controls[0].content.value,
            }

            # Aca queremos pasar los datos al usuario, pero queremos pasarlo como una nueva "entidad"
            # Ahora mismo la ruta es usuario => nodo_usuario => email, nombre
            # Queremos generar una ruta que se vea así:
            # usuario => usuario_logueado => email, nombre, apellido, tareas
            # tareas: nombre, apellido, fecha_post, post

            # Visualmente seria algo asi
            # Primero, debemos retornar el nodo que vamos a crear cuando enviamos el post a la base de datos 
            # Esto es importante porque tenemos que pasarlo al control si queremos borrarlo
            ref_data = (
                db.child("users" + "/" + SESSION["path"]).child("tasks").push(data)
            )
            # el .child("tasks") va a crear una nueva "tabla" que digamos
            # ahora podemos mostrarlo en el indice de la columna
            page.controls[0].controls[0].controls[2].controls[3].controls.append(
                postControl.DisplayPost(
                    # Ahora pasamos los argumentos
                    first_name,
                    last_name,
                    post_date,
                    res.content.controls[0].content.value, # El post
                    ref_data["name"] # La referencia en si del nodo
                )
            )

            # Para borrar la entrada
            res.content.controls[0].content.value = None
            res.content.controls[0].content.update()
            e.page.update()

# Para mostrar los datos del usuario cuando se loguean
def DisplayTask(e):
    all_tasks = db.child("users").child(SESSION["path"]).child("tasks").get()

    # Revisa si los datos existen o no
    if all_tasks.val() == None:
        pass
    else:
        for page in e.page.views[:]:
            for task in all_tasks:
                page.controls[0].controls[0].controls[2].controls[3].controls.append(
                    postControl.DisplayPost(
                        # Pasamos los valores de la base de datos
                        task.val()["firstName"],
                        task.val()["lastName"],
                        task.val()["postDate"],
                        task.val()["post"],
                        task.key(),
                    )
                )
                e.page.update()

# Esta funcion se encarga de eliminar los items para que sea mas funcional
def DeletePostData(obj, db_node, e):
    # llamamos la funcion cuando el boton borrar del post es presionado
    for page in e.page.views[:]:
        if page.route == "/index":
            # Esto accede a la columna, y pasamos la variable obj el cual es la instancia del post

            # Asi que obtenemos la instancia propia del post y el nodo de firebase porque hace falta borrarlo del display asi como tambien la base de datos

            page.controls[0].controls[0].controls[2].controls[3].controls.remove(obj)
            page.controls[0].controls[0].controls[2].controls[3].update()

            # Ahora debemos acceder al nodo hijo
            db.child("users").child(SESSION["path"]).child("tasks").child(
                # pasamos el nodo aqui
                db_node
            ).remove() # funcion para eliminar


# Menu tipo toggle
def ShowMenu(e):
    for page in e.page.views[:]:
        if page.route == "/index" or page.route == "/profile":
            if e.data == "true":
                # Aca necesitamos el index de control
                page.controls[0].controls[0].controls[0].controls[0].width = 185
                page.update()
            else:
                page.controls[0].controls[0].controls[0].controls[0].width = 60
                page.update()