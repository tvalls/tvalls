- 👋 Hi, I’m @tvalls
- 👀 I’m interested in Python
- 🌱 I’m currently learning Python
- 💞️ I’m looking to collaborate on Python
- 📫 How to reach me Py..... I mean... 

      import smtplib
      from email.mime.text import MIMEText
      from email.mime.multipart import MIMEMultipart

      def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
          msg = MIMEMultipart()
          msg['From'] = you
          msg['To'] = 'valls.thiago@gmail.com'
          msg['Subject'] = 'Saw you on github'

          msg.attach(MIMEText(message, 'plain'))

          try:
              server = smtplib.SMTP(smtp_server, smtp_port)
              server.starttls()

              server.login(smtp_username, smtp_password)

              server.sendmail(sender_email, receiver_email, msg.as_string())
              print("Email sent successfully!")
          except Exception as e:
              print("Error sending email:", str(e))
          finally:
              server.quit()

<!---
tvalls/tvalls is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
