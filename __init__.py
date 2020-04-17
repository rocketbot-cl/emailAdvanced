# coding: utf-8
import base64
import email
import os
from email import generator
import imaplib
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'emailAdvanced' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
import mailparser
from bs4 import BeautifulSoup

outenc = sys.stdout.encoding or sys.getfilesystemencoding()

global pattern_uid
pattern_uid = re.compile('\d+ \(UID (?P<uid>\d+)\)')


def parse_mailbox(data):
    flags, b, c = data.partition(' ')
    separator, b, name = c.partition(' ')
    return flags, separator.replace('"', ''), name.replace('"', '')


def get_first_text_block(msg):
    type = msg.get_content_maintype()
    # print('tipo', type)

    if type == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif type == 'text':
        return msg.get_payload()


module = GetParams('module')


def parse_uid(tmp):
    print('tmp', tmp)
    try:
        tmp = tmp.decode()
    except:
        pass
    match = pattern_uid.match(tmp)
    return match.group('uid')


if module == "MoveMail":
    imap = GetGlobals('email')
    origin = GetParams("from_")
    var = GetParams("var")
    id_ = GetParams("id_")
    folder = GetParams("folder")

    if not origin:
        origin = "INBOX"
    
    if not id_:
        raise Exception("No ha ingresado ID de email a mover")
    if not folder:
        raise Exception("No ha ingresado carpeta de destino")
    try:
        # login on IMAP server
        if imap.IMAP_SSL:
            imap.server_imap = imaplib.IMAP4_SSL(imap.IMAP_SERVER, imap.IMAP_PORT)
        else:
            imap.server_imap = imaplib.IMAP4(imap.IMAP_SERVER, imap.IMAP_PORT)
        imap.server_imap.login(imap.FROM_EMAIL, imap.FROM_PWD)
        imap.server_imap.select(origin, readonly=False)
        resp, data = imap.server_imap.fetch(id_, "(UID)")
        msg_uid = parse_uid(data[0])

        result = imap.server_imap.uid('COPY', msg_uid, folder)

        if result[0] == 'OK':
            mov, data = imap.server_imap.uid('STORE', msg_uid, '+FLAGS', '(\Deleted)')
            res = imap.server_imap.expunge()
            if var:
                ret = True if res[0] == 'OK' else False
                SetVar(var, ret)
            imap.server_imap.close()
            imap.server_imap.logout()
        else:
            raise Exception(result)
    except Exception as e:
        raise e

if module == "LeerTodo":
    imap = GetGlobals('email')
    id_correo = GetParams('id_correo')
    result = GetParams('result')
    path_mail = GetParams('path_mail')
    path_attachment = GetParams('path_attachment')

    if imap.IMAP_SSL:
        imap.server_imap = imaplib.IMAP4_SSL(imap.IMAP_SERVER, imap.IMAP_PORT)
    else:
        imap.server_imap = imaplib.IMAP4(imap.IMAP_SERVER, imap.IMAP_PORT)
    imap.server_imap.login(imap.FROM_EMAIL, imap.FROM_PWD)
    imap.server_imap.select(imap.EMAIL_FOLDER, readonly=False)

    try:
        if id_correo:
            rv, data = imap.server_imap.fetch(id_correo, '(RFC822)')
            bt = data[0][1]
            # msg = email.message_from_bytes(data[0][1])
            mm = mailparser.parse_from_bytes(data[0][1])
            # print(mm.attachments)
            bs = ''
            try:
                bs = BeautifulSoup(mm.body, 'html.parser').body.get_text()
            except:
                bs = mm.body
            # print('body', mm.date.__str__())
            to = ", ".join([b for (a, b) in mm.to])
            from_ = ", ".join([b for (a, b) in mm.from_])
            files_ = [ff['filename'] for ff in mm.attachments]
            datos = {
                "from": from_,
                "to": to,
                "date": mm.date.__str__(),
                "body": bs,
                "subject": mm.subject,
                "files": files_
            }
            if path_mail:
                path_mail = os.path.join(path_mail, id_correo + ".eml")
                with open(path_mail, "wb") as file_:
                    a = generator.Generator(file_)
                    a.write(bt)
                    file_.close()

            if path_attachment:
                for att in mm.attachments:
                    name_ = att['filename']

                    fileb = att['payload']
                    cont = base64.b64decode(fileb)

                    with open(os.path.join(path_attachment, name_), 'wb') as file_:
                        file_.write(cont)
                        file_.close()
            if result:
                SetVar(result, datos)
            imap.server_imap.close()
            imap.server_imap.logout()
    except Exception as e:
        PrintException()
        raise e

if module == "MarkUnread":
    imap = GetGlobals('email')
    id_correo = GetParams('id_correo')

    try:
        if imap.IMAP_SSL:
            imap.server_imap = imaplib.IMAP4_SSL(imap.IMAP_SERVER, imap.IMAP_PORT)
        else:
            imap.server_imap = imaplib.IMAP4(imap.IMAP_SERVER, imap.IMAP_PORT)
        imap.server_imap.login(imap.FROM_EMAIL, imap.FROM_PWD)
        imap.server_imap.select(imap.EMAIL_FOLDER, readonly=False)
        imap.server_imap.store(id_correo, '-FLAGS', '(\Seen)')
        imap.server_imap.close()
        imap.server_imap.logout()
    except Exception as e:
        PrintException()
        raise e

if module == "ListFolder":
    imap = GetGlobals('email')
    result_ = GetParams('result')
    try:
        if imap.IMAP_SSL:
            imap.server_imap = imaplib.IMAP4_SSL(imap.IMAP_SERVER, imap.IMAP_PORT)
        else:
            imap.server_imap = imaplib.IMAP4(imap.IMAP_SERVER, imap.IMAP_PORT)
        imap.server_imap.login(imap.FROM_EMAIL, imap.FROM_PWD)
        resp, data = imap.server_imap.list('""', '*')
        if resp == 'OK':
            if result_:
                data_ = []
                for mbox in data:
                    flags, separator, name = parse_mailbox(bytes.decode(mbox))
                    tmp = name[2:] if name.startswith("/ ") else name
                    data_.append(tmp)
                SetVar(result_, data_)
        # imap.server_imap.close()
        imap.server_imap.logout()
    except Exception as e:
        PrintException()
        raise e

if module == "sendEmail":
    email = GetGlobals('email')
    to_ = GetParams("to")
    subject = GetParams("subject")
    body_ = GetParams("msg")
    cc = GetParams('cc')
    attached_file = GetParams('path')
    files = GetParams('folder')
    filenames = []

    try:
        print(email.SMTP_SERVER, email.SMTP_PORT, type(email.SMTP_PORT))
        server = smtplib.SMTP(email.SMTP_SERVER, email.SMTP_PORT)
        server.starttls()
        server.login(email.FROM_EMAIL, email.FROM_PWD)
        msg = MIMEMultipart()
        msg['From'] = email.FROM_EMAIL
        msg['To'] = to_
        msg['Cc'] = cc
        msg['Subject'] = subject

        if cc:

            toAddress = to_.split(",") + cc.split(",")
        else:
            toAddress = to_.split(",")

        if not body_:
            body_ = ""
        body = body_
        msg.attach(MIMEText(body, 'html'))

        if files:
            for f in os.listdir(files):
                f = os.path.join(files, f)
                filenames.append(f)

            if filenames:
                for file in filenames:
                    filename = os.path.basename(file)
                    attachment = open(file, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    attachment.close()
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    msg.attach(part)

        else:
            if attached_file:
                if os.path.exists(attached_file):
                    filename = os.path.basename(attached_file)
                    attachment = open(attached_file, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    attachment.close()
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    msg.attach(part)

        text = msg.as_string()
        server.sendmail(email.FROM_EMAIL, toAddress, text)
        # server.close()

    except Exception as e:
        PrintException()
        raise e


