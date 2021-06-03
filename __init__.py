# coding: utf-8
try:
    # Python libraries
    import base64
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

    # Add the module's lib folder to the path
    base_path = tmp_global_obj["basepath"]
    cur_path = base_path + 'modules' + os.sep + 'emailAdvanced' + os.sep + 'libs' + os.sep
    if cur_path not in sys.path:
        sys.path.append(cur_path)

    # external libraries
    import mailparser
    from bs4 import BeautifulSoup
    outenc = sys.stdout.encoding or sys.getfilesystemencoding()

    global pattern_uid
    pattern_uid = re.compile('\d+ \(UID (?P<uid>\d+)\)')

except Exception as e:
    PrintException()
    raise e


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


global  mod_email_advanced_sessions
SESSION_DEFAULT = "gmail"
# Initialize settings for the module here
try:
    if not mod_email_advanced_sessions:
        mod_email_advanced_sessions = {SESSION_DEFAULT: {"email": GetGlobals('email'), "smtp": True, "imap": True}}
except NameError:
    mod_email_advanced_sessions = {SESSION_DEFAULT: {"email": GetGlobals('email'), "smtp": True, "imap": True}}


class EmailAdvanced:
    def __init__(self, host, port, user, password, ssl, imap=False, smtp=False):
        self.IMAP_SERVER = host if imap else None
        self.SMTP_SERVER = host if smtp else None
        self.SMTP_PORT = port if smtp else None
        self.IMAP_PORT = port if imap else None
        self.FROM_EMAIL = user
        self.FROM_PWD = password
        self.SSL = ssl if smtp else None
        self.IMAP_SSL = ssl if imap else None
        self.server_imap = None

    def connect(self):
        pass


module = GetParams('module')
session = GetParams("session")
if not session:
    session = SESSION_DEFAULT
global email_advanced


def parse_uid(tmp):
    print('tmp', tmp)
    try:
        tmp = tmp.decode()
    except:
        pass
    match = pattern_uid.match(tmp)
    return match.group('uid')

try:
    if module == "MoveMail":
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

        imap = mod_email_advanced_sessions[session]["email"]

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

    if module == "LeerTodo":

        id_correo = GetParams('id_correo')
        result = GetParams('result')
        path_mail = GetParams('path_mail')
        path_attachment = GetParams('path_attachment')

        imap = mod_email_advanced_sessions[session]["email"]
        host = imap.IMAP_SERVER
        port = imap.IMAP_PORT
        ssl = imap.IMAP_SSL
        user = imap.FROM_EMAIL
        password = imap.FROM_PWD

        if ssl:
            server = imaplib.IMAP4_SSL(host, port)
        else:
            server = imaplib.IMAP4(host, port)
        
        if user and password:
            server.login(user, password)
        server.select('inbox', readonly=False)

        if id_correo:
            rv, data = server.fetch(id_correo, '(RFC822)')
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
            server.close()
            server.logout()

    if module == "MarkUnread":
        imap = mod_email_advanced_sessions[session]["email"]
        id_correo = GetParams('id_correo')

   
        if imap.IMAP_SSL:
            imap.server_imap = imaplib.IMAP4_SSL(imap.IMAP_SERVER, imap.IMAP_PORT)
        else:
            imap.server_imap = imaplib.IMAP4(imap.IMAP_SERVER, imap.IMAP_PORT)
        imap.server_imap.login(imap.FROM_EMAIL, imap.FROM_PWD)
        imap.server_imap.select(imap.EMAIL_FOLDER, readonly=False)
        imap.server_imap.store(id_correo, '-FLAGS', '(\Seen)')
        imap.server_imap.close()
        imap.server_imap.logout()

    if module == "ListFolder":
        imap = mod_email_advanced_sessions[session]["email"]
        result_ = GetParams('result')

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

    if module == "sendEmail":
        smtp = mod_email_advanced_sessions[session]["email"]
        to_ = GetParams("to")
        subject = GetParams("subject")
        body_ = GetParams("msg")
        cc = GetParams('cc')
        attached_file = GetParams('path')
        files = GetParams('folder')
        filenames = []

        host = smtp.SMTP_SERVER
        port = smtp.SMTP_PORT
        ssl = smtp.SSL
        user = smtp.FROM_EMAIL
        password = smtp.FROM_PWD

        # print(email.SMTP_SERVER, email.SMTP_PORT, type(email.SMTP_PORT))
        if ssl:
            server = smtplib.SMTP_SSL(host, port)
        else:
            server = smtplib.SMTP(host, port)
            server.starttls()

        if user and password:
            server.login(user, password)
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to_
        msg['Cc'] = cc
        msg['Subject'] = subject

        if cc:

            toAddress = to_.split(",") + cc.split(",")
        else:
            toAddress = to_.split(",")

        if not body_:
            body_ = ""
        body = body_.replace("\n", "<br/>")
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
        server.sendmail(user, toAddress, text)
        # server.close()


    if module == "ConnectImap":
        host = GetParams("host")
        port = GetParams("port")
        user = GetParams("user")
        pwd = GetParams("pass")
        ssl = GetParams("ssl")
        result = GetParams("result")

        try:

            ssl = False if ssl is None else eval(ssl)
            port = int(port)
            if ssl:
                server = imaplib.IMAP4_SSL(host, port)
            else:
                server = imaplib.IMAP4(host, port)

            if user and pwd:
                server.login(user, pwd)
            email_advanced = EmailAdvanced(host, port, user, pwd, ssl, imap=True)
            mod_email_advanced_sessions[session] = {"email": email_advanced, "imap": True, "smpt": False}
            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e

    if module == "ConnectSmtp":
        host = GetParams("host")
        port = GetParams("port")
        user = GetParams("user")
        pwd = GetParams("pass")
        ssl = GetParams("ssl")
        result = GetParams("result")

        try:
            ssl = False if ssl is None else eval(ssl)
            port = int(port)
            if ssl:
                server = smtplib.SMTP_SSL(host, port)
            else:
                server = smtplib.SMTP(host, port)

            if user and pwd:
                server.starttls()
                server.login(user, pwd)
            email_advanced = EmailAdvanced(host, port, user, pwd, ssl, smtp=True)
            mod_email_advanced_sessions[session] = {"email": email_advanced, "imap": False, "smpt": True}
            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e
except Exception as e:
        PrintException()
        raise e
