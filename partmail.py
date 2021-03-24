import smtplib, ssl
import pandas as pd

df = pd.read_excel('link_with_python.xlsx')


value_dict = df.set_index("grade") ["email_list"].to_dict()

value_dict2 = df.set_index("email_list") ["grade"].to_dict()


for email_list in value_dict2:
    email = email_list
    splitmail = email.split('@')[0]
   # print (splitmail)
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "stanleywealth1998@gmail.com"
    receiver_email = (email_list)
    password = input ("Type your password email password: ")
    for grade in value_dict:
        hold = int(grade)
        if grade > 70:
            message =  (f"Hi {splitmail}, Congratulations, your score in the last test was", hold,  "therefore, you have qualified for the final stage")
        else:
            message =  (f"Hi {splitmail}, I am sorry to inform you that you scored", hold, "in your interview test which is less than the pass mark,  your journey ends with us here and we wish you all the best")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL( smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

        print("success")