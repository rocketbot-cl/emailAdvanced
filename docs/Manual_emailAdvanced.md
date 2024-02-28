# Advanced email
  
Module with advanced options for handling emails  

*Read this in other languages: [English](Manual_emailAdvanced.md), [Português](Manual_emailAdvanced.pr.md), [Español](Manual_emailAdvanced.es.md)*
  
![banner](imgs/Banner_emailAdvanced.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## How to use this module
The emailAdvanced module must be used in conjunction with the native email module. As a first action, we must go to the modules section and look for the "Email" module, then "SMTP-IMAP" and use the "Configure server" command. We must complete the fields with the data of the server, port, password and mail. Check SSL if necessary. Once this is done, we will be able to use the module commands.


## Description of the commands

### Send advanced email
  
Command to send html format email, cc and multiple files
|Parameters|Description|example|
| --- | --- | --- |
|To|Here we put the recipients to whom we want to send an email|user@email.com,person@mail.net|
|Cc|Here we put the recipients to whom we want to send a copy of the email|cc@email.com,cc2@mail.net|
|Subject|Here we put the subject of the email|Check out this Rocketbot message|
|Message|Here we put the message that we want to send|Hi person. This message was sent from Rocketbot. Bye|
|Attachment|Here we put the files that we want to attach|path/to/file.ext|
|attach multiple files|Here we put the files that we want to attach|path/to/folder|

### Move email to folder
  
This command allows you to move an email to another folder
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|ID of the mail to move|ID mail|
|Origin folder|We put the origin folder|Carpeta origen|
|Destination folder|We put the destination folder|carpeta|
|Set to variable|We put the variable to which the result will be assigned|variable|

### Get all emails
  
This command allows you to get all emails from a folder with the option to filter
|Parameters|Description|example|
| --- | --- | --- |
|Filter|We put the filter that we want to apply|SUBJECT "Test Rocketbot"|
|Folder|We put the folder from which we want to obtain the emails|inbox|
|Set to variable|We put the variable where we want to save the data|variable|

### Read all data from email
  
Read all data from email
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|We put the ID of the mail to read|ID|
|Folder|We put the folder from which we want to obtain the emails|inbox|
|Set to variable|We put the variable where we want to save the data|variable|
|Email save path|We put the path where we want to save the mail|C:/Users/User/Desktop|
|Attachment save path|We put the path where we want to save the attachments|C:/Users/User/Desktop|

### Mark mail as unread
  
Mark mail as unread by ID
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|We put the ID of the mail to mark as unread.|ID|

### List email folders
  
List email folders
|Parameters|Description|example|
| --- | --- | --- |
|Set to var|We put the variable where we want to save the result.|Variable|

### Connect Imap
  
User only if native command not working to read emails
|Parameters|Description|example|
| --- | --- | --- |
|User|User of the email account|user@example.com|
|Password|Password of the email account or application key|******|
|Server|Email server|host.imap.xys|
|Port|Connection port|517|
|Assign result to a Variable|Variable where the result of the connection will be saved|Variable|
|SSL Conection|Connect with SSL|True|

### Connect SMTP
  
User only if native command not working connection
|Parameters|Description|example|
| --- | --- | --- |
|Usuario|Enter the e-mail with which we will connect to the server|user@example.com|
|Password|Password of the email account or application key|******|
|Server|Enter the server with which we will connect to the server|host.smtp.xys|
|Port|Enter the port with which we will connect to the server|517|
|Assign result to a Variable|Enter the name of the variable in which we want to save the result|Variable|
|SSL Conection|Activate the SSL connection|True|

### Validate emails
  
Validate emails
|Parameters|Description|example|
| --- | --- | --- |
|Email|Put the email to validate if exists|example_mail@server.com|
|Assign result to a variable|Result of the validation|resultado_email|

### Forward email for ID
  
This command allows you to forward an email by ID
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Email ID to forward|355|
|Email|Email that will receive the mail|test@email.com|
|Subject|Subject of the email|Subject|
