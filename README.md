# SupportBot
Este es un bot muy sencillo de hacer y facil de hacer o desplegar, aqui abajo tendran el indice :

[1. Despliegue a Heroku](https://github.com/AresDza/SupportBot/blob/master/README.md#despliegue-a-heroku-)
[2. Funcionamiento](https://github.com/AresDza/SupportBot/blob/master/README.md#funcionamiento-)


## Despliegue a Heroku :

<b>1ro : </b>Has un BOT de Telegram :

   ◓ Ve a Bot Father en Telegram y Usa /newbot

   ◓ Ponle un Nombre y después un Usuario

   ◓ Luego te pondrá un Mensaje con el Enlace a tu Bot y su Token

   ◓ Buscas la parte del Token y lo copias y lo guardamos para el despliegue
     
   ◓ Salimos de Telegram y Volvemos a Github

<b>2do : </b>Pulsa el Botón <b>[DEPLOY TO HEROKU]</b>.

<b>3ro : </b>Ponle un Nombre a la APP de Heroku (<i>Obligatorio</i>) y Selecciona la Región (<i>Para Cuba la Mejor es Estados Unidos</i>)

<b>4to : </b>Pon tu Nombre de Usuario de Telegram (<i>Ejemplo : @Ejemplo, pero quitás el @, quedaría : Ejemplo</i>)

<b>5to : </b>Pon el token del Bot que creamos al Principio y pulsa en <b>[Deploy App]</b>

Una vez hayamos Desplegado la APP :

<b>1ro : </b>Pulsa en el Botón <b>[Manage APP]</b>

<b>2do : </b>Vamos a la pestaña (Resources)

<b>3ro : </b>Debajo de Free Dynos, hay una que pone worker python3 main.py, tocamos en el Lápiz de Editar y Activamos el Dyno, pulsamos en confirmar y ya nuestro Bot estará Funcionando ....


## Funcionamiento :

El funcionamiento de este ChatBot es simple pero eficiente, al iniciarce, se crea una lista de destinatarios con los ID de los administradores, una vez entre un mensaje al bot pasa por una proceso de verificacion del mensaje, si el mensaje es de un admin va a revisarse que le este respondiendo a un usuario para luego enviarle la respuesta, en caso de no estar respondiendo a un mensaje de un usuario devuelve un mensaje de advertencia, y si el mensaje es escrito por un usuario al ser verificado, sera enviado a los administradores, el funcionamiento del bot no esta limitado solo a mensajes, funciona con cualquier tipo de entradas (texto, voz, videos, imagenes, documentos, contactos, ubicaciones ....), las respuestas de los administradores es totalmente anonima, mientras que la de los usuarios muestran el remitente (Esto pasa porque especifique que los mensajes de los users serian reenviados y los de los admins copiados)

*Mensajes Copiados de los Admins : Esta es la mejor opcion para las respuestas a los usuarios, ya que mantienes el anonimato y pueden ser atendidos por un grupo de admins sin problemas ni confusiones.

*Mensajes Reenviados de los Users : Mejor opcion para este caso, ya que ayuda al bot a obtener el ID del usuario que ha enviado la solicitud para poder enviarle sus respuestas y tambien favorece a la hora de contactar de manera privada al usuario.




[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AresDza/SupportBot) <b>↣ Despliega directo en Heroku</b>
