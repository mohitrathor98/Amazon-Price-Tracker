# sending mails using smtplib

from email import message
import smtplib

receipent = "mohitrathor8@gmail.com" # MAIL TO WHICH EMAIL TO BE RECEIVED


my_email = "mohitdemo7@gmail.com" # MAIL FROM WHCIH EMAIL TO BE SENT
password = "demopassword" # PASSWORD OF THE SENDER MAIL

def send_mail(body:dict):
    
    item_name, item_price = [item for item in body.items()][0]
    subject = f"Price dropped for an item in your wishlist"
    message_body = f"Price dropped for {item_name}. Current Price Rs.{item_price}. Go check your wishlist."
    
    # first argument - location of smtp of email provider
    # smtp.mail.yahoo.com - smtp of yahoo
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls() # transport layer service -- makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=receipent, 
            msg=f"Subject:{subject}\n\n{message_body}"
        )   
    print("Mail sent for item ", item_name)
