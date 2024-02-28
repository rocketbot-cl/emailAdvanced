# Email avançado
  
Módulo com opções avançadas para manipulação de emails  

*Read this in other languages: [English](Manual_emailAdvanced.md), [Português](Manual_emailAdvanced.pr.md), [Español](Manual_emailAdvanced.es.md)*
  
![banner](imgs/Banner_emailAdvanced.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Enviar email avançado
  
Comando para enviar email com formato html, cc e múltiplos arquivos
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Para|Aqui colocamos o destinatários para quem queremos enviar um email|user@email.com,person@mail.net|
|Cc|Aqui colocamos o destinatários para quem queremos enviar uma cópia do email|cc@email.com,cc2@mail.net|
|Assunto|Aqui colocamos o assunto do email|Check out this Rocketbot message|
|Mensagem|Aqui colocamos a mensagem que queremos enviar|Hi person. This message was sent from Rocketbot. Bye|
|Anexo|Aqui colocamos o os arquivos anexados|path/to/file.ext|
|anexar múltiplos arquivos|Aqui colocamos o os arquivos anexados|path/to/folder|

### Mover email de pasta
  
Este comando permite mover um email para outra pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do email|ID do email para mover|ID mail|
|Pasta de origem|Colocamos a pasta de origem|Carpeta origen|
|Pasta de destino|Colocamos a pasta de destino|carpeta|
|Definir para variável|Colocamos a variável à qual o resultado será atribuído|variable|

### Obter todos os emails
  
Este comando permite obter todos os emails de uma pasta com a opção de filtrar
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro|Colocamos o filtro que queremos aplicar|SUBJECT "Test Rocketbot"|
|Pasta|Colocamos a pasta da qual queremos obter os emails|inbox|
|Definir para variável|Colocamos a variável onde queremos salvar os dados|variable|

### Leia todos os dados do email
  
Você pode ler todos os dados de um email
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do email|Colocamos o ID do email para ler|ID|
|Pasta|Colocamos a pasta da qual queremos obter os emails|inbox|
|Definir para variável|Colocamos a variável onde queremos salvar os dados|variable|
|Caminho de salvamento do email|Colocamos o caminho onde queremos salvar o email|C:/Users/User/Desktop|
|Caminho de salvamento do anexo|Colocamos o caminho onde queremos salvar os anexos|C:/Users/User/Desktop|

### Marcar email como não lido
  
Marcar email como não lido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do email|Colocamos o ID do email para marcar como não lido|ID|

### Listar pastas
  
Lista pastas do servidor de emails
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Definir para variável|Colocamos a variável onde queremos salvar o resultado|Variável|

### Conectar Imap
  
Usar apenas se o comando nativo não permitir ler emails
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Usuário|Usuário da conta de email|user@example.com|
|Senha|Senha da conta de email ou chave de aplicação|******|
|Servidor|Servidor de email|host.imap.xys|
|Porta|Porta de conexão|517|
|Atribuir resultado a uma variável|Variável onde o resultado da conexão será salvo|Variable|
|Conexão SSL|Conectar com SSL|True|

### Conectar SMTP
  
Usar apenas se o comando nativo não permitir a conexão
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Usuário|Colocamos o e-mail com o qual nos conectaremos|user@example.com|
|Senha|Senha da conta de email ou chave de aplicação|******|
|Servidor|Colocamos o servidor com o qual nos conectaremos|host.smtp.xys|
|Porta|Colocamos a porta com a qual nos conectaremos|517|
|Atribuir resultado a uma variável|Colocamos o nome da variável na qual queremos salvar o resultado|Variable|
|Conexão SSL|Ativar a conexão SSL|True|

### Validar email
  
Valida um email
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email|Colocamos o e-mail para validar se existe|example_mail@server.com|
|Atribuir resultado a uma variável|Resultado da validação|resultado_email|

### Reenviar email por ID
  
Este comando permite reenviar um email por ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Email|ID do email para reenviar|355|
|Email|Email que receberá o email|test@email.com|
|Assunto|Assunto do email|Subject|
