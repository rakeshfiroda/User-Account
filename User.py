from tkinter import *
from os import path

class start:
    __titlefont = ('Helvetica',20,'bold')
    __optionfont = ('Courier',16,'bold underline')
    __optionfonts = ('Courier',12,'bold underline')
    __inputfont = ('Helvetica',16,'bold')
    __titlefonts = ('Helvetica',16,'bold')
    __inputfonts = ('Helvetica',12,'bold')
    
    main=Tk()
    #initialize start window
    def __init__(self):
        
        # checking required files
        self.requirement()
        
        self.main.iconbitmap(r"C:\Users\#\Downloads\home.ico")
        self.main.title("HOME")
        self.main.geometry("400x400")
        self.main.configure(bg="#E56B1F")
        self.main.resizable(width=False,height=False)
        Label(self.main,text="Welcome!",font=self.__titlefont,bg="#E56B1F",cursor='circle').place(x=130,y=10)
        Label(self.main,text="USERNAME",font=self.__optionfont).place(x=10,y=80)
        Label(self.main,text="PASSWORD",font=self.__optionfont).place(x=10,y=140)
        Label(self.main,text="Don't Have an Account.?",bg="#E56B1F").place(x=130,y=300)
        self.__user=Entry(self.main,width=20,bg='lightblue',fg='red',font=self.__inputfont)
        self.__pass=Entry(self.main,width=20,bg='lightblue',fg='red',font=self.__inputfont,show="*")
        Button(self.main,relief=SOLID,text="Forgot Password?",cursor='hand2',bg="lightgrey",activebackground="grey",command=self.forgot).place(x=220,y=220)
        Button(self.main,relief=RIDGE,borderwidth=2,cursor='hand2',text="LOG-IN",bg="deepskyblue",activebackground="black",activeforeground="white",font=self.__titlefont,command=self.login).place(x=50,y=210)
        Button(self.main,relief=RIDGE,borderwidth=2,cursor='hand2',text="CREATE AN ACCOUNT",bg="lightgreen",activebackground="black",activeforeground="white",font=self.__titlefont,command=self.signup).place(x=40,y=320)
        Button(self.main,relief=RIDGE,borderwidth=1,cursor='hand2',text="EXIT",bg="lightgrey",activebackground="black",activeforeground="white",command=self.main.destroy).place(x=190,y=380)
        self.__pass.bind("<Return>",self.login)
        self.__user.place(x=140,y=80)
        self.__pass.place(x=140,y=140)
        
    # login window
    def login(self,event=None):
        username=self.__user.get()
        password=self.__pass.get()
        userfile=open("username.txt")
        un_list=userfile.readlines()
        # removing \n from end of the usernames
        un_list=[a.strip("\n") for a in un_list]
        # checking username availability..
        if username == "":
            self.__user.config(highlightthickness=2)
            self.__user.config(highlightbackground="red")
            Label(self.main,text="        Username can't be empty, Please enter a valid username.                             ",bg="#E56B1F",fg="red").place(x=50,y=58)

        elif username in un_list:
            self.__user.config(highlightthickness=0)
            position=un_list.index(username)
            pwfile=open("password.txt")
            try:
                pw_list=pwfile.readlines()[position]
                # removing \n from password
                pw_list=pw_list.strip("\n")
                
                if pw_list==password:
                    self.__pass.config(highlightthickness=0)
                    self.__pass.config(highlightbackground="black")
                    Label(self.main,text="                   Congrats! Successfully Loged in.                             ",bg="#E56B1F",fg="green").place(x=50,y=58)
                else:
                    self.__pass.config(highlightthickness=2)
                    self.__pass.config(highlightbackground="red")
                    self.__pass.delete(0,END)
                    Label(self.main,text="            Wrong password entered! try again.                                                  ",bg="#E56B1F",fg="red").place(x=50,y=58)
                    
            except IndexError:
                pass
            
            pwfile.close()
            
        else:
            Label(self.main,text="  User doesn't exist.. Please Create an Account First",bg="#E56B1F",fg="red").place(x=50,y=58)
        
        userfile.close()
             
    # signup window
    def signup(self):
        
        def submit():
            uname=self.__username.get()
            email=self.__email.get()
            password=self.__password.get()
            name=self.__fullname.get()
            
            unfile=open("username.txt")
            un_list=unfile.readlines()
            unfile.close()
            un_list=[a.strip("\n") for a in un_list]
            if  uname in un_list:
                self.__password.config(highlightthickness=0)
                self.__username.delete(0,END)
                Label(signup,text="Username Already exist.. Please Choose a unique username",bg="bisque3",fg="red").place(x=50,y=58)
                self.__username.config(highlightbackground="red")
                self.__username.config(highlightthickness=2)
                
            else:
                self.__username.config(highlightthickness=0)
                if password == "":
                    Label(signup,text="Password can't be blank, Please enter a valid password.        ",bg="bisque3",fg="red").place(x=50,y=58)
                    self.__password.config(highlightbackground="red")
                    self.__password.config(highlightthickness=2)
                else:
                    self.__password.config(highlightthickness=0)
                    emailfile=open("email.txt","a")
                    pwfile=open("password.txt","a")
                    unfile=open("username.txt","a")
                    fnfile=open("fullname.txt","a")
                
                    emailfile.write(email+"\n")
                    pwfile.write(password+"\n")
                    unfile.write(uname+"\n")
                    fnfile.write(name+"\n")
                
                    Label(signup,text="     Account Created Successfully.. Click on LOG-IN                                  .",bg="bisque3",fg="green").place(x=50,y=58)
                
                    emailfile.close()
                    pwfile.close()
                    unfile.close()
                    fnfile.close()
        
        signup=Tk()
        signup.iconbitmap(r"C:\Users\#\Downloads\adduser.ico")
        signup.title("SIGN-UP")
        signup.geometry("390x400")
        signup.configure(bg="bisque3")
        signup.resizable(width=False,height=False)
        Label(signup,text="SIGN-UP",font=self.__titlefont,bg="bisque3",cursor='circle').place(x=130,y=10)
        Label(signup,text="ENTER FULL NAME",font=self.__optionfonts).place(x=10,y=80)
        Label(signup,text="CHOOSE USERNAME",font=self.__optionfonts).place(x=10,y=140)
        Label(signup,text="CHOOSE PASSWORD",font=self.__optionfonts).place(x=10,y=200)
        Label(signup,text="ENTER EMAIL ID ",font=self.__optionfonts).place(x=10,y=260)
        Button(signup,relief=RIDGE,borderwidth=2,cursor='hand2',text="SUBMIT",bg="deepskyblue",activebackground="black",activeforeground="white",font=self.__titlefonts,command=submit).place(x=50,y=320)
        Button(signup,relief=RIDGE,borderwidth=2,cursor='hand2',text="LOG-IN",bg="lightgreen",activebackground="black",activeforeground="white",font=self.__titlefonts,command=signup.destroy).place(x=240,y=320)
        self.__fullname=Entry(signup,width=20,bg='lightblue',fg='red',font=self.__inputfonts)
        self.__username=Entry(signup,width=20,bg='lightblue',fg='red',font=self.__inputfonts)
        self.__password=Entry(signup,width=20,bg='lightblue',fg='red',font=self.__inputfonts)
        self.__email=Entry(signup,width=20,bg='lightblue',fg='red',font=self.__inputfonts)
        self.__fullname.place(x=190,y=80)
        self.__username.place(x=190,y=140)
        self.__password.place(x=190,y=200)
        self.__email.place(x=190,y=260)
        
        signup.mainloop()
        
    
    # forgot password window
    def forgot(self):
        
        def forget_password(enter=None):
            email=self.email.get()
            efile=open("email.txt")
            e_list=efile.readlines()
            efile.close()
            e_list=[a.strip("\n") for a in e_list]
            if email in e_list:
                position=e_list.index(email)
                pwfile=open("password.txt")
                password=pwfile.readlines()[position]
                password=password.strip("\n")
                Label(fp,text="                                                     Your Password: "+password+"                                              ").place(x=0,y=80)
                pwfile.close()
            else:
                Label(fp,text="This Email is not linked with any account. Please Create an account first.",fg="red").place(x=5,y=80)
            
        
        fp=Tk()
        fp.iconbitmap(r"C:\Users\#\Downloads\forget.ico")
        fp.title("Forget Password")
        fp.geometry("400x100")
        fp.resizable(width=False,height=False)
        fp.configure(bg="bisque3")
        Label(fp,text="ENTER EMAIL-ID",font=self.__optionfonts).place(x=10,y=10)
        self.email=Entry(fp,width=23,bg='lightblue',fg='red',font=self.__inputfonts)
        self.email.bind("<Return>",forget_password)
        self.email.place(x=170,y=10)
        Button(fp,relief=RIDGE,borderwidth=2,cursor='hand2',text="SUBMIT",bg="lightgreen",activebackground="black",activeforeground="white",width=10,command=forget_password).place(x=60,y=50)
        Button(fp,relief=RIDGE,borderwidth=2,cursor='hand2',text="CENCEL",bg="lightgrey",activebackground="black",activeforeground="white",width=10,command=fp.destroy).place(x=260,y=50)
        
    # checking required files
    def requirement(self):
        if path.isfile('username.txt')==False:
            file=open("username.txt",'w')
            file.close()
        if path.isfile('password.txt')==False:
            file=open("password.txt",'w')
            file.close()
        if path.isfile('email.txt')==False:
            file=open("email.txt",'w')
            file.close()
        if path.isfile('fullname.txt')==False:
            file=open("fullname.txt",'w')
            file.close()
    
    # mainloop
    def loop(self):
        self.main.mainloop()

        
new=start()
new.loop()













































































































