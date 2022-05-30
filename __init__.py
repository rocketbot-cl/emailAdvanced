# coding: utf-8

GetParams = GetParams  # type: ignore
GetGlobals = GetGlobals  # type: ignore
SetVar = SetVar  # type: ignore
PrintException = PrintException  # type:ignore
tmp_global_obj = tmp_global_obj  # type: ignore
alert = alert  # type: ignore

try:
    # Python libraries
    import base64
    import os
    from email import generator
    import email
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
    cur_path = (
        base_path + "modules" + os.sep + "emailAdvanced" + os.sep + "libs" + os.sep
    )
    if cur_path not in sys.path:
        sys.path.append(cur_path)

    # external libraries
    import mailparser  # type: ignore
    from bs4 import BeautifulSoup  # type: ignore

    outenc = sys.stdout.encoding or sys.getfilesystemencoding()

    global pattern_uid
    pattern_uid = re.compile("\d+ \(UID (?P<uid>\d+)\)")

except Exception as e:
    PrintException()
    raise e


def parse_mailbox(data):
    flags, b, c = data.partition(" ")
    separator, b, name = c.partition(" ")
    return flags, separator.replace('"', ""), name.replace('"', "")


def get_first_text_block(msg):
    type = msg.get_content_maintype()
    # print('tipo', type)

    if type == "multipart":
        for part in msg.get_payload():
            if part.get_content_maintype() == "text":
                return part.get_payload()
    elif type == "text":
        return msg.get_payload()


# Globals declared here
global mod_email_advanced_sessions

# Default declared here
SESSION_DEFAULT = "default"

# Initialize settings for the module here
try:
    if not mod_email_advanced_sessions:  # type: ignore
        mod_email_advanced_sessions = {
            SESSION_DEFAULT: {"email": GetGlobals("email"), "smtp": True, "imap": True}
        }
except NameError:
    mod_email_advanced_sessions = {
        SESSION_DEFAULT: {"email": GetGlobals("email"), "smtp": True, "imap": True}
    }


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


# get the running session, otherwise get the default session
session = GetParams("session")
if not session:
    session = SESSION_DEFAULT
global email_advanced


def parse_uid(tmp):
    print("tmp", tmp)
    try:
        tmp = tmp.decode()
    except:
        pass
    match = pattern_uid.match(tmp)
    return match.group("uid")


# capture the name of the running command and session
module = GetParams("module")

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

        result = imap.server_imap.uid("COPY", msg_uid, folder)

        if result[0] == "OK":
            mov, data = imap.server_imap.uid("STORE", msg_uid, "+FLAGS", "(\Deleted)")
            res = imap.server_imap.expunge()
            if var:
                ret = True if res[0] == "OK" else False
                SetVar(var, ret)
            imap.server_imap.close()
            imap.server_imap.logout()
        else:
            raise Exception(result)

    if module == "LeerTodo":

        id_correo = GetParams("id_correo")
        result = GetParams("result")
        path_mail = GetParams("path_mail")
        path_attachment = GetParams("path_attachment")

        imap = mod_email_advanced_sessions[session]["email"]
        host = imap.IMAP_SERVER
        port = imap.IMAP_PORT
        ssl = imap.IMAP_SSL
        user = imap.FROM_EMAIL
        password = imap.FROM_PWD

        print(
            f"""
        imap: {imap}
        host: {host}
        port: {port}
        ssl: {ssl}
        user: {user}
        password: *********
        """
        )

        if ssl:
            server = imaplib.IMAP4_SSL(host, port)
        else:
            server = imaplib.IMAP4(host, port)

        if user and password:
            server.login(user, password)
        server.select("inbox", readonly=False)

        if id_correo:
            rv, data = server.fetch(id_correo, "(RFC822)")
            bt = data[0][1]
            try:
                raw_email_string = bt.decode("utf-8")
            except:
                raw_email_string = bt.decode("latin-1")
            email_message = email.message_from_string(raw_email_string)
            # msg = email.message_from_bytes(data[0][1])
            mm = mailparser.parse_from_string(raw_email_string)
            if mm.attachment is not None:
                # print(mm.attachments)
                pass
            bs = ""
            try:
                bs = BeautifulSoup(mm.body, "html.parser").body.get_text()
            except:
                bs = mm.body

            bs = bs.split("--- mail_boundary ---")[0]
            # print('body', mm.date.__str__())
            to = ", ".join([b for (a, b) in mm.to])
            from_ = ", ".join([b for (a, b) in mm.from_])
            files_ = [ff["filename"] for ff in mm.attachments]
            # print(f'los archivos son: {files_}')
            # creo una variable datos para guardar en SetVar(result)
            datos = {
                "from": from_,
                "to": to,
                "date": mm.date.__str__(),
                "body": bs,
                "subject": mm.subject,
                "files": files_,
            }
            if path_mail:
                path_mail = os.path.join(path_mail, id_correo + ".eml")
                with open(path_mail, "wb") as file_:
                    a = generator.Generator(file_)
                    a.write(bt)
                    file_.close()

            if path_attachment:
                for att in mm.attachments:
                    name_ = att["filename"]
                    # if there are any \r\n, replace them
                    name_ = name_.replace("\r\n", "")
                    contents = att["payload"]
                    # check if the first line is endoded with base64
                    pattern64 = r"^[A-Za-z0-9+/\r\n\\n]+"
                    matches64 = re.match(pattern64, contents)

                    if matches64 is None:
                        # if it DOESNT match base64 pattern means that you doesn't have to decode the file
                        # just write to disk
                        print(f"File {name_} is already decoded. Writing to disk")
                        with open(os.path.join(path_attachment, name_), "w") as file_:
                            file_.write(contents)
                            file_.close()
                    else:
                        print(f"File {name_} is encoded. Decoding and writing to disk")
                        decoded_contents = base64.b64decode(contents)
                        with open(os.path.join(path_attachment, name_), "wb") as file_:
                            file_.write(decoded_contents)
                            file_.close()
            if result:
                SetVar(result, datos)
            server.close()
            server.logout()

    if module == "MarkUnread":
        imap = mod_email_advanced_sessions[session]["email"]
        id_correo = GetParams("id_correo")

        if imap.IMAP_SSL:
            imap.server_imap = imaplib.IMAP4_SSL(imap.IMAP_SERVER, imap.IMAP_PORT)
        else:
            imap.server_imap = imaplib.IMAP4(imap.IMAP_SERVER, imap.IMAP_PORT)
        imap.server_imap.login(imap.FROM_EMAIL, imap.FROM_PWD)
        imap.server_imap.select(imap.EMAIL_FOLDER, readonly=False)
        imap.server_imap.store(id_correo, "-FLAGS", "(\Seen)")
        imap.server_imap.close()
        imap.server_imap.logout()

    if module == "ListFolder":
        imap = mod_email_advanced_sessions[session]["email"]
        result_ = GetParams("result")

        if imap.IMAP_SSL:
            imap.server_imap = imaplib.IMAP4_SSL(imap.IMAP_SERVER, imap.IMAP_PORT)
        else:
            imap.server_imap = imaplib.IMAP4(imap.IMAP_SERVER, imap.IMAP_PORT)
        imap.server_imap.login(imap.FROM_EMAIL, imap.FROM_PWD)
        resp, data = imap.server_imap.list('""', "*")
        if resp == "OK":
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
        cc = GetParams("cc")
        attached_file = GetParams("path")
        files = GetParams("folder")
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

        if user and password:
            try:
                server.starttls()
            except:
                pass
            server.login(user, password)

        msg = MIMEMultipart()
        msg["From"] = user
        msg["To"] = to_
        msg["Cc"] = cc
        msg["Subject"] = subject

        if cc:

            toAddress = to_.split(",") + cc.split(",")
        else:
            toAddress = to_.split(",")

        if not body_:
            body_ = ""
        body = body_.replace("\n", "<br/>")
        msg.attach(MIMEText(body, "html"))

        if files:
            for f in os.listdir(files):
                f = os.path.join(files, f)
                filenames.append(f)

            if filenames:
                for file in filenames:
                    filename = os.path.basename(file)
                    attachment = open(file, "rb")
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload((attachment).read())
                    attachment.close()
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition", "attachment; filename= %s" % filename
                    )
                    msg.attach(part)

        else:
            if attached_file:
                if os.path.exists(attached_file):
                    filename = os.path.basename(attached_file)
                    attachment = open(attached_file, "rb")
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload((attachment).read())
                    attachment.close()
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition", "attachment; filename= %s" % filename
                    )
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
            mod_email_advanced_sessions[session] = {
                "email": email_advanced,
                "imap": True,
                "smpt": False,
            }
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
            try:
                server.starttls()
            except:
                pass
            if user and pwd:
                server.login(user, pwd)
            email_advanced = EmailAdvanced(host, port, user, pwd, ssl, smtp=True)
            mod_email_advanced_sessions[session] = {
                "email": email_advanced,
                "imap": False,
                "smpt": True,
            }
            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e

    if module == "validate_email":
        from validate_email import validate_email  # type:ignore
        import DNS  # type: ignore

        email = GetParams("email")
        result = GetParams("result")
        try:
            is_valid = validate_email(email, verify=True)
            if is_valid:
                SetVar(result, True)
            else:
                SetVar(result, False)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e

except Exception as e:
    PrintException()
    raise e
