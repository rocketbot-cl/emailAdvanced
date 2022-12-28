# Email avanzado
  
Módulo con opciones avanzadas para el manejo de correos  

*Read this in other languages: [English](Manual_emailAdvanced.md), [Español](Manual_emailAdvanced.es.md).*  

![banner](imgs/Banner_emailAdvanced.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  


## Como usar este modulo
El modulo de emailAdvanced debe usarse en conjunto con el modulo de email nativo. Como primera accion, debemos ir a la seccion de modulos y buscar el modulo "Email", luego "SMTP-IMAP" y utilizar el comando "Configurar servidor". Debemos completar los campos con los datos del servidor, puerto, contraseña y mail. Marca SSL de ser necesario. Una vez hecho esto, ya podremos utilizar los comandos del modulo.


## Descripción de los comandos

### Enviar email avanzado
  
Comando para enviar email con formato html, cc y multiples archivos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Para|Aqui colocamos el o los destinatarios a los que deseamos enviar un mail|user@email.com,person@mail.net|
|Cc|Aqui colocamos el o los destinatarios a los que deseamos enviar un mail|cc@email.com,cc2@mail.net|
|Asunto|Aqui colocamos el asunto del mail|Check out this Rocketbot message|
|Mensaje|Aqui colocamos el mensaje que deseamos enviar|Hi person. This message was sent from Rocketbot. Bye|
|Adjunto|Aqui colocamos el o los archivos adjuntos|path/to/file.ext|
|Adjuntar multiples archivos|Aqui colocamos el o los archivos adjuntos|path/to/folder|

### Mover Email de carpeta
  
Módulos para mover emails de carpeta para servidores de correos IMAP
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de mail|Colocamos el ID del mail a mover|ID mail|
|Carpeta origen|Colocamos la carpeta origen|Carpeta origen|
|Carpeta de destino|Colocamos la carpeta de destino|carpeta|
|Asignar a variable|Colocamos la variable a la que se asignará el resultado|variable|

### Leer toda la data de un email
  
Puedes leer toda la data de un email
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de mail|Colocamos el ID del mail a leer|ID|
|Asignar a variable|Colocamos la variable donde queremos que se guarde la data|variable|
|Ruta guardar email|Colocamos la ruta donde queremos que se guarde el mail|C:/Users/User/Desktop|
|Ruta donde se descargaran los adjuntos|Colocamos la ruta donde queremos que se guarden los adjuntos|C:/Users/User/Desktop|

### Marcar email como no leído
  
Marcar email como no leído
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de mail|Colocamos el ID del mail para marcar como no leido|ID|

### Listar carpetas
  
Lista carpetas del servidor de correos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar a variable|Colocamos la variable donde queremos que se guarde el resultado|Variable|

### Conexión Imap
  
Usar solo si el comando nativo no permite leer mails
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|User|Usuario de la cuenta de correo|user@example.com|
|Contraseña|Contraseña de la cuenta de correo|******|
|Servidor|Servidor de correo|host.imap.xys|
|Puerto|Puerto de conexión|517|
|Asignar resultado a variable|Variable donde se guardará el resultado|Variable|
|Conexión SSL|Conectar con SSL|True|

### Conexión SMTP
  
Usar solo si el comando nativo no permite la conexión
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|User|Colocamos el mail con el cual nos conectaremos|user@example.com|
|Contraseña|Colocamos la contraseña con la que nos conectaremos|******|
|Servidor|Colocamos el servidor con el cual nos conectaremos|host.smtp.xys|
|Puerto|Colocamos el puerto con el cual nos conectaremos|517|
|Asignar resultado a variable|Colocamos el nombre de la variable en la que queremos guardar el resultado|Variable|
|Conexión SSL|Activamos la conexión con SSL|True|

### Validar email
  
Valida un email
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Email|Colocamos el mail a validar si existe|example_mail@server.com|
|Resultado|Resultado de la validación|resultado_email|

### Reenviar email por ID
  
Reenviar email por ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Email|ID del email a reenviar|355|
|Email|Email que recibira el mail|test@email.com|
|Asunto|Asunto del email|Subject|
