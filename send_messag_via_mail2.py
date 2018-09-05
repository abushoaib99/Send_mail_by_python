import smtplib,webbrowser,getpass
def get_mail():
    servicesAvailable=['hotmail','outlook','gmail','yahoo']
    while True:
        mail_id=input("E-mail: ")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos=mail_id.find("@")
            dotcom_pos=mail_id.find(".com")
            sp=mail_id[symbol_pos+1:dotcom_pos]
            if sp in servicesAvailable:
                return mail_id,sp
                break
            else:
                print("we don't provide service for "+sp)
                print("we provide service only for: hotmail/outlook,gamil,yahoo ")
                continue

        else:
            print("invalid E-mail retype again ")
            continue

def set_smtp_domain(serviceProvider):
    if serviceProvider=='gmail':
        return "smtp.gmail.com"
    elif serviceProvider=='outlook' or serviceProvider=='hotmail':
        return "smtp.outlook.com"
    elif serviceProvider=='yahoo':
        return "smtp.yahoo.com"

print('Welcome you can send an E-mail through this program ')
print('Please enter your E-mail and Password: ')
e_mail,serviceProvider=get_mail()
print("your service provider is "+serviceProvider)
password=getpass.getpass("Password: ")

while True:
    try:
        smtpDomain=set_smtp_domain(serviceProvider)
        connection=smtplib.SMTP(smtpDomain)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail,password)
        
    except:
        if serviceProvider=="gmail":
            print("Login unseccessfull, there are  two reasons: ")
            print("1.) You typed wrong username or password")
            print("2.) You are using Gmail there is an option in gmail 'allow lesssecureapps")
            print("Do you want us to open a webpage from where you can enable this option")
            answer=input("yes or no? : ")
            while True:
                if answer=="yes":
                    webbrowser.open("https://myaccount.google.com/lesssecureapps")
                    break
                elif answer=="no":
                    print("we won't open webbrowser for you, you can go to 'http://myaccount.google.com/lesssecureapps'")
                    print("Please retype your e-mail and password also ")
                    e_mail,serviceProvider=get_mail()
                    password=getpass.getpass("Password: ")
                    break
                    continue
                else:
                    print("Wrong input, Please Try again")
                    answer=input("yes or no? : ")
                    
        else:
            print("login unsuccessfull, most possible you typed wrong username or pasword")
            print("please retype your e-mail address and password")
            e_mail,serviceProvider=get_mail()
            password=getpass.getpass("Password: ")
            continue  
    else:
        print("login successfull")
        break

print("please type receiver's E-mail address")
receiverAddress,receiverSP=get_mail()
print("Now please type Subject and Message ")
Subject=input("Subject: ")
Message=input("Message: ")
connection.sendmail(e_mail,receiverAddress,("Subject: "+str(Subject)+"\n\n"+ str(Message)))
print("E-mail send successfully ")
connection.quit()
