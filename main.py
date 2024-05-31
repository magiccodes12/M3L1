import random
from flask import Flask
import string

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
]

password_list = [
    "4","f",'t','f','y','d','r','h','d','5','7','f','g','h','d','a','i','e','o','u','x','@','*'
]


@app.route("/")
def hello_world():
    return """
    <h1>Hello, World!</h1>
    <a href="/random_fact">¡Ver un dato aleatorio!</a><br>
    <a href="/Generador_automático_de_contraseñas">Generador de contraseñas</a>
    """

@app.route("/bienvenido")
def Bienvenidos():
    return '<h1>Bienvenidos!</h1>'

@app.route("/random_fact")
def Random_Facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/Generador_automático_de_contraseñas")
def Generador_de_contraseñas():
    password = ''.join(random.choice(password_list) for i in range(16))
    return f'<p>{password}'

app.run(debug=True)