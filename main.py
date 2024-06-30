import telebot
import random
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token del bot desde la variable de entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Diccionario de nombres con sus respectivas URLs de imágenes
who_urls = {
    "Pennywise": "https://s1.ppllstatics.com/diariosur/www/multimedia/201909/05/media/cortadas/Pennywise-knlC-U90651765752iF-1248x770@Diario%20Sur.jpg",
    "El Jinete sin Cabeza": "https://cdn.atomix.vg/wp-content/uploads/2022/06/jinete.jpg",
    "Un selenita": "https://www.turismodeestrellas.com/media/files/6343_habitante-la-luna.png",
    "Un ser venido de otro planeta":"https://inboxlatinonyhome.files.wordpress.com/2019/07/img_6593.jpg?w=730",
    "Godzilla":"https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2016/05/592268-godzilla-2-godzilla-vs-kong-retraso-fechas-estreno.jpg?tf=3840x",
    "Drácula":"https://4.bp.blogspot.com/-7GdQ1lmu7mQ/XtUK9YuXo4I/AAAAAAAAOK8/VtItg2XfTNoIpS-F8MJE2tB3b2SCeoYDwCK4BGAYYCw/s640/lugosidracula.jpg",
    "Cthulhu":"https://static.wikia.nocookie.net/lovecraft/images/7/72/Lovecraft-cthulhu.jpg/revision/latest?cb=20140210145556&path-prefix=es",
    "El Hombre Lobo":"https://static.wikia.nocookie.net/seres-mitologicos/images/4/4b/Werewolf.jpg/revision/latest/scale-to-width-down/1200?cb=20141212161948&path-prefix=es",
    "El Yeti":"https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/4ea3/live/8686b820-9b57-11ee-84bb-07160cedaa67.jpg",
    "La Momia":"https://t2.uc.ltmcdn.com/es/posts/9/5/5/como_hacer_un_disfraz_de_momia_21559_600.jpg",
    "El Fantasma de la Ópera":"https://lamanodelextranjero.files.wordpress.com/2018/08/el-escalofriante-maquillaje-de-lon-chaney-para-el-fantasma-de-la-opera.jpg",
    "La Bruja":"https://images.ecestaticos.com/BT3jtmRxFE6LW2sHzN4HflB70VY=/0x0:1607x904/1200x900/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2Ffa9%2Fa39%2F558%2Ffa9a39558637f505a4cc28136cb13c9e.jpg",
    "El Monstruo del Lago Ness":"https://eldiariony.com/wp-content/uploads/sites/2/2023/08/Ilustracion-del-huevo-de-flamenco-descubierto-en-Mexico.-1.jpg?w=2600",
    "El Hombre Invisible":"https://externos.uma.es/cultura/fancine/2016/wp-content/uploads/2016/10/hombreinvisible.jpg",
    "El Alienígena":"https://us.123rf.com/450wm/vikaviktoria007/vikaviktoria0072310/vikaviktoria007231001201/216291294-pesadilla-de-ciencia-ficci%C3%B3n-invasor-alien%C3%ADgena-en-la-tierra.jpg?ver=6",
    "La Criatura del Pantano":"https://static.wikia.nocookie.net/arrow/images/2/2d/Cosa_del_Pantano.jpg/revision/latest?cb=20200331232140&path-prefix=es",
    "El Vampiro":"https://static.wikia.nocookie.net/mangakaart/images/c/cc/Vampiro.jpg/revision/latest?cb=20130411164312&path-prefix=es",
    "El Demonio":"https://img.freepik.com/fotos-premium/demonio-cuernos_855892-1004.jpg",
    "El Zombi":"https://img.europapress.es/fotoweb/fotonoticia_20220822152105_1200.jpg"

    # Añade más nombres y URLs según sea necesario
}

action = [
    "comió",
    "destruyó",
    "quemó",
    "desintegró",
    "pulverizó",
    "escondió",
    "partió",
    "trituró",
    "devoró",
    "aplastó",
    "rompió",
    "hundió",
    "robo",
    "consumió",
    "abdujo",
    "derritió",
    "borró",
    "contaminó",
    "envenenó"
]

what = [
    "las llaves de mi casa",
    "el tejado del vecino",
    "mi coche nuevo",
    "las gafas de mi abuela",
    "los apuntes de HTML",
    "el monopatín de mi hermano pequeño",
    "el teléfono móvil",
    "el ordenador portátil",
    "el control remoto de la televisión",
    "la carta de amor",
    "el pastel de cumpleaños",
    "el libro de hechizos",
    "la lámpara mágica",
    "el trofeo del torneo",
    "la joya del museo",
    "la fórmula secreta",
    "el mapa del tesoro",
    "la varita mágica",
    "la poción de la juventud"
]

when = [
    "después del almuerzo",
    "justo a tiempo",
    "después del concierto",
    "durante el viaje de fin de curso",
    "después de las clases",
    "durante la misa del domingo",
    "durante la proyección de la película",
    "en plena noche",
    "al amanecer",
    "en pleno día",
    "en la hora de la siesta",
    "durante la cena",
    "en la hora punta",
    "durante la tormenta",
    "en la luna llena",
    "en pleno eclipse",
    "en el momento más inesperado",
    "en el peor momento posible",
    "justo antes de la boda"
]

# CREACION DE LOS COMANDOS BASICOS

#Comando /start
@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = """
    ¡Hola! Bienvenido a uno de mis primeros proyectos de bot de Telegram.
    
    Puedes usar los siguientes comandos conmigo:
    
    /start - Inicia una conversación conmigo
    /about - Muestra información sobre este bot
    /excusa - Elabora una excusa convincente
    
    ¡Espero que disfrutes usando este bot!
    """
    bot.reply_to(message, start_text)

#Comando /about
@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
    ¡Hola! Soy un bot de Telegram creado por EduardoHernandezGuzman para ayudarte en tus tareas diarias.
    
    Este bot fue creado como parte de mi primer proyecto de desarrollo de un bot de Telegram.
    """
    bot.reply_to(message, about_text)

# Comando /excusa
@bot.message_handler(commands=['excusa'])
def send_random_excuse(message):
    random_who = random.choice(list(who_urls.keys()))  # Escoger un nombre al azar del diccionario
    random_action = random.choice(action)
    random_what = random.choice(what)
    random_when = random.choice(when)
    random_excuse = f"{random_who} {random_action} {random_what} {random_when}."

    # Verificar si el nombre tiene una URL asociada y enviar la imagen correspondiente
    if random_who in who_urls:
        image_url = who_urls[random_who]
        bot.send_photo(message.chat.id, image_url)  # Enviar la foto directamente sin necesidad de guardarla

    # Enviar la excusa como mensaje de texto
    bot.reply_to(message, random_excuse)



if __name__ == "__main__":
    bot.polling(none_stop=True)