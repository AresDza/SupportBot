# SupportBot
Este es un bot muy sencillo de hacer y facil de hacer o desplegar, aqui abajo tendran el indice :

1. Despliegue a Heroku
2. Funcionamiento
3. Explicacion del Code


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

### Una vez hayamos Desplegado la APP :

<b>1ro : </b>Pulsa en el Botón <b>[Manage APP]</b>

<b>2do : </b>Vamos a la pestaña (Resources)

<b>3ro : </b>Debajo de Free Dynos, hay una que pone worker python3 main.py, tocamos en el Lápiz de Editar y Activamos el Dyno, pulsamos en confirmar y ya nuestro Bot estará Funcionando ....


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AresDza/SupportBot) <b>↣ Despliega directo en Heroku</b>
