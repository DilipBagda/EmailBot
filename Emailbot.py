# code by Dilip bagda
import smtplib   
from email.message import EmailMessage

# For Access Gmail Account
def login(): 
    print("-----------------------------------------------------------")
    email = input("Enter The Email For Login:")
    password = input("Enter your Password:")
    try:
        # For connect to Sever
        smtp = smtplib.SMTP(host='smtp.gmail.com',port=587)
        smtp.ehlo()
        smtp.starttls() # Standard encryption
        smtp.login(email,password)
        print("\n------------------ Login Successflly --------------------\n")
    except smtplib.SMTPAuthenticationError:
        print("-----------------------------------------------------------")
        print("\nxxxxxxxxxxxxx Please Enter Correct Email and Password xxxxxxxxxxxxx\n")
        login()
    except Exception:
        print("\nServer Error Please try Again") 
        exit()  
    return smtp

def sendEmail(smtp):
    email = EmailMessage()
    print('================== Provide Receiver Detail ================')
    email['from'] = input("From:")
    email['subject'] = input("Subject:")
    email.set_content(input("Message:\n"))
    path = input("Enter Email List path, If List in Current Directory Just Give Name:")
    while True:
        try:
            file = open(path)
            break
        except FileNotFoundError:
            print("\nxxxxxxxxxxxxxxxxxxxxxxxxxx Please Enter The Correct Path xxxxxxxxxxxxxxxxxxxxxxxxxx\n")
            path = input("Enter Correct Path:")        
    # For Count lines in File
    content = file.read().split('\n')
    line = len(content)
    file.seek(0)   # Set file pointer at Starting
    print("--------------------------------------------------------------------------------")
    for i in range(1,line+1) :
        to = file.readline()
        email['to'] = to
        try:   
            smtp.send_message(email)
            print(f"{i} {to} Sended Successfully")
        except Exception as e:
            print(f"\nError Occur : {e} ")
            print("Please Try Again")
            exit()
        del email['to']
    file.close()
    smtp.quit()
    print("--------------------------------------------------------------------------------")
    print("\n=============== Thank You For Using Program =================") 
    exit()

def sendEmailManyTime(smtp):
    email = EmailMessage()
    print('================== Provide Receiver Detail ================')
    try:
        count = int(input("How Many Time You Want To Send Mail:"))
    except Exception:
        print("\nxxxxxxxxxxxxxxx Please Enter Valid Number xxxxxxxxxxxxxxxxxxx")
        sendEmailBobm()
    email['from'] = input("From:")
    email['to'] = input("TO:")
    email['subject'] = input("Subject:")
    email.set_content(input("Message:\n"))
    print("-----------------------------------------------------------")
    for i in range(0,count):
        try:
            smtp.send_message(email)
            print(f"{i+1} Email Sended")
        except Exception:
            print("Something Went Wrong please Try Aain")
            sendEmailBobm()
    print("ALL Done")
    smtp.quit()
    print("=============== Thank You For Using Program =================")
    exit()
            
if __name__ =="__main__":
    print("\n============  Welcome to Email Sending Program  ==============")
    while True :
        print('''
        1) Send Email With List
        2) Send Email Many Time to One Person
        3) Exit 
        ''')
        try:
            choise = int(input("Enter Number What You Want:"))
            if choise==1:
                smtp=login()
                sendEmail(smtp)
            elif choise==2:
                smtp=login()
                sendEmailManyTime(smtp)
            elif choise==3:
                print("\n =============== Thank You For Using Program =================")
                exit()    
            else: print("\nxxxxxxxxxxxxx Please Enter Valid Number xxxxxxxxxxxxxxxxx")
        except Exception:
            print("\nxxxxxxxxxxxxxxx Please Enter Valid Number xxxxxxxxxxxxxxxxxxx")
