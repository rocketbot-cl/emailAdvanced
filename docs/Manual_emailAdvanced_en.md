# Manual Email Advanced

This module is an Rocketbot Email command extension. It purpose is to extend new functionality to the base email module of Rocketbot

![banner](img/Banner_emailAdvanced.png)

## How to install this module

**Download** and **install** the content in `modules` folder in Rocketbot path

## Description of commands

### Send advanced email

Command to send html format email, cc and multiple files.

| Parameters            | Description                      | Example                        |
| --------------------- | -------------------------------- | ------------------------------ |
| To                    | Recipient of the email           | user@email.com                 |
| CC                    | Carbon Copy the email to ...     | cc@email.com                   |
| Subject               | Subject of the email             | Checkout this Rocketbot msg    |
| Message               | Body of the email                | Hi. This is a body of an email |
| Attachment            | File attachments                 | File.txt                       |
| Attach multiple files | Attach all the files of a folder | C:\path\to\folder\             |

### Move email to folder

Module to move emails from server folders to IMAP folders

| Parameters                | Description                                                                             | Example  |
| ------------------------- | --------------------------------------------------------------------------------------- | -------- |
| Email ID                  | ID of email to move (if only)                                                           | 254346   |
| Origin Folder             | Folder to move                                                                          | Work     |
| Destination Folder        | Title of the form which will be created                                                 | New_work |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result   |

### Read all data from email

Read all the data from a single email, by its ID

| Parameters                | Description                                                                             | Example                                |
| ------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------- |
| Email ID                  | ID of email to read                                                                     | 254346                                 |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result                                 |
| Email save path           | Path to save the email in the PC                                                        | C:\Users\my_user\Downloads\            |
| Attachments save path     | Path to save the attachments in the PC                                                  | C:\Users\my_user\Downloads\attackments |

### Marks as unread

Marks an email as unread, by email ID

| Parameters | Description                | Example |
| ---------- | -------------------------- | ------- |
| Email ID   | ID of email to mark unread | 254346  |

### List email folders

List all the folders in the server

| Parameters                | Description                                                                             | Example |
| ------------------------- | --------------------------------------------------------------------------------------- | ------- |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result  |

### Validate emails

Check if an email is valid

| Parameters                | Description                                                                             | Example |
| ------------------------- | --------------------------------------------------------------------------------------- | ------- |
| Email ID                  | ID of email to check                                                                    | 254346  |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result  |

### Connect IMAP (optional)

An alternative way to connect to IMAP, if the base email module does not work properly

| Parameters                | Description                                                                             | Example        |
| ------------------------- | --------------------------------------------------------------------------------------- | -------------- |
| User                      | Name of the user                                                                        | 254346         |
| Password                  | Password of the user                                                                    | badpassword123 |
| Server                    | Name of the imap server                                                                 | host.imap.xyz  |
| Port                      | Port of the imap server                                                                 | 517            |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result         |
| SSL Connection            | Check if it is an SSL Connection                                                        | True           |

### Connect SMTP (optional)

An alternative way to connect to SMTP, if the base email module does not work properly

| Parameters                | Description                                                                             | Example        |
| ------------------------- | --------------------------------------------------------------------------------------- | -------------- |
| User                      | Name of the user                                                                        | 254346         |
| Password                  | Password of the user                                                                    | badpassword123 |
| Server                    | Name of the smtp server                                                                 | host.smtp.xyz  |
| Port                      | Port of the smtp server                                                                 | 517            |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result         |
| SSL Connection            | Check if it is an SSL Connection                                                        | True           |
