import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from loguru import logger
from constants.email_credentials import *


class EmailSender:
    def __init__(self) -> None:
        """
        Initializes the EmailSender instance.
        """
        self.email = user_email
        self.password = password_email

    def send_email_with_attachment(self):
        """
        Sends an email with the only PDF file present in the "data" folder as an attachment.
        """
        try:
            # Diretório de downloads
            download_dir = os.path.join(os.getcwd(), "data")

            # Lista arquivos na pasta
            files = os.listdir(download_dir)
            pdf_files = [file for file in files if file.endswith('.pdf')]

            if len(pdf_files) != 1:
                raise FileNotFoundError("Não há um único arquivo PDF na pasta 'data'.")

            # Caminho do arquivo PDF
            pdf_file = pdf_files[0]
            pdf_file_path = os.path.join(download_dir, pdf_file)

            # Configuração do e-mail
            from_address = self.email
            to_address = self.email  
            subject = "Boleto Faculdade"
            body = "Segue em anexo o documento baixado para pagamento da mensalidade."

            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Anexar o arquivo
            with open(pdf_file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(pdf_file_path)}")
                msg.attach(part)

            # Enviar o e-mail
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.starttls()
            server.login(from_address, self.password)
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)
            server.quit()

            logger.success("E-mail enviado com sucesso!")

        except Exception as e:
            logger.error(f"Erro ao enviar o e-mail: {str(e)}")
