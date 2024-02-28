# Email avanzado
  
Módulo con opciones avanzadas para el manejo de correos  

*Read this in other languages: [English](Manual_emailAdvanced.md), [Português](Manual_emailAdvanced.pr.md), [Español](Manual_emailAdvanced.es.md)*
  
![banner](imgs/Banner_emailAdvanced.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Enviar email avanzado
  
Comando para enviar email con formato html, cc y multiples archivos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Para|Aqui colocamos el o los destinatarios a los que deseamos enviar un mail|user@email.com,person@mail.net|
|Cc|Aqui colocamos el o los destinatarios a los que deseamos enviar una copia del mail|cc@email.com,cc2@mail.net|
|Asunto|Aqui colocamos el asunto del mail|Check out this Rocketbot message|
|Mensaje|Aqui colocamos el mensaje que deseamos enviar|Hi person. This message was sent from Rocketbot. Bye|
|Adjunto|Aqui colocamos el o los archivos adjuntos|path/to/file.ext|
|Adjuntar multiples archivos|Aqui colocamos el o los archivos adjuntos|path/to/folder|

### Mover email de carpeta
  
Este comando te permite mover un email a otra carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de mail|ID del mail a mover|ID mail|
|Carpeta origen|Colocamos la carpeta origen|Carpeta origen|
|Carpeta de destino|Colocamos la carpeta de destino|carpeta|
|Asignar a variable|Colocamos la variable a la que se asignará el resultado|variable|

### Obtener todos los emails
  
Este comando te permite obtener todos los emails de una carpeta con la opción de filtrar
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Colocamos el filtro que deseamos aplicar|SUBJECT "Test Rocketbot"|
|Carpeta|Colocamos la carpeta de la que queremos obtener los emails|inbox|
|Asignar a variable|Colocamos la variable donde queremos que se guarde la data|variable|

### Leer toda la data de un email
  
Puedes leer toda la data de un email
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de mail|Colocamos el ID del mail a leer|ID|
|Carpeta|Colocamos la carpeta de la que queremos obtener los emails|inbox|
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
|Usuario|Usuario de la cuenta de correo|user@example.com|
|Contraseña|Contraseña de la cuenta de correo o clave de aplicación|******|
|Servidor|Servidor de correo|host.imap.xys|
|Puerto|Puerto de conexión|517|
|Asignar resultado a variable|Variable donde se guardará el resultado de la conexión|Variable|
|Conexión SSL|Conectar con SSL|True|

### Conexión SMTP
  
Usar solo si el comando nativo no permite la conexión
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|User|Colocamos el mail con el cual nos conectaremos|user@example.com|
|Contraseña|Contraseña de la cuenta de correo o clave de aplicación|******|
|Servidor|Colocamos el servidor con el cual nos conectaremos|host.smtp.xys|
|Puerto|Colocamos el puerto con el cual nos conectaremos|517|
|Asignar resultado a variable|Colocamos el nombre de la variable en la que queremos guardar el resultado|Variable|
|Conexión SSL|Activamos la conexión con SSL|True|

### Validar email
  
Valida un email
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Email|Colocamos el mail a validar si existe|example_mail@server.com|
|Asignar resultado a variable|Resultado de la validación|resultado_email|

### Reenviar email por ID
  
Este comando permite reenviar un email por ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Email|ID del email a reenviar|355|
|Email|Email que recibira el mail|test@email.com|
|Asunto|Asunto del email|Subject|
