import smtplib
import random

# Define your email settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = '02230293.cst@rub.edu.bt'  # Your Gmail username or email address
smtp_password = 'bcfp xjhd nnkc hmsw'  # Your Gmail password or app-specific password
sender_email = '02230293.cst@rub.edu.bt'#need other user email to send email
recipient_email = 'bhutab2018@gmail.com'

# List of daily quotes (you can fetch quotes from an API if needed)
#creating a dictonary
daily_quotes = [
   "The only way you can do it is by doing it by yourself",
    "If you think the price of winning is high, wait until you get the bill of regret",
    "In the end, we only regret the chances we didn't take",
    "If you don't want to run, you will be left behind by everyone",
    "It's nice to be important, but it's more important to be nice",
    "Enjoy your little detours in life"
]

# Select a random quote
daily_quote = random.choice(daily_quotes)

# Create the email message
subject = "Daily Inspiration"
message = f"Subject: {subject}\n\n{daily_quote}"

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message)
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")