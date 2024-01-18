import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from doctor import *

def main():
    root=Tk()
    app=windows1(root)
    root.mainloop()

class windows1:
    def __init__(self,master):
        self.master=master
        self.master.title("Pharamcy Management System")
        self.master.geometry('1350x750+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
        self.frame=Frame(self.master)
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.LabelTitle=Label(self.frame,text="   Pharamcy management system   ",font=("arial",40,"bold"),
        bd=10,relief="sunken")

        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.Loginframe1 = Frame(self.frame,width=1000,height=300,bd=10,relief="groove")
        self.Loginframe1.grid(row=1,column=0)


        self.Loginframe2 = Frame(self.frame,width=1000,height=100,bd=10,relief="groove")
        self.Loginframe2.grid(row=2,column=0 ,pady=15)

        self.Loginframe3 = Frame(self.frame,width=1000,height=200,bd=10,relief="groove")
        self.Loginframe3.grid(row=6,column=0,pady=5)

        self.button_reg=Button(self.Loginframe3,text="Patient Management System",state=DISABLED, font=("arial",15,"bold"),
                                  command=self.Registration_window)
        self.button_reg.grid(row=0,column=0,padx=10,pady=10)

        self.button_Hosp=Button(self.Loginframe3,text="Hospital Management System",state=DISABLED, font=("arial",15,"bold"),
                                 command=self.Hospital_window)
        self.button_Hosp.grid(row=0,column=1,padx=10,pady=10)

         
        self.button_Dr_appt=Button(self.Loginframe3,text="Doctor Management System",state=DISABLED, font=("arial",15,"bold"),
                                 command=self.Dr_Appoint_window)
        self.button_Dr_appt.grid(row=1,column=0,padx=10,pady=10)

        self.button_med_stock=Button(self.Loginframe3,text="Medicine Management System",state=DISABLED, font=("arial",15,"bold"),
                                 command=self.Medicine_stock)
        self.button_med_stock.grid(row=1,column=1,padx=10,pady=10)
        
        #now we will make user name and password frame
         
        self.LabelUsername=Label(self.Loginframe1,text="User name", font=("arial",20,"bold"),bd=3)
        self.LabelUsername.grid(row=0,column=0)
        
        
        self.textUsername=Entry(self.Loginframe1,font=("arial",20,"bold"),bd=3,textvariable=self.Username)
        self.textUsername.grid(row=0,column=1,padx=48,pady=15)

        self.LabelPassword=Label(self.Loginframe1,text="Password", font=("arial",20,"bold"),bd=3)
        self.LabelPassword.grid(row=1,column=0)

        self.textPassword=Entry(self.Loginframe1,font=("arial",20,"bold"),show="*",bd=3,textvariable=self.Password)
        self.textPassword.grid(row=1,column=1,padx=48,pady=15)


        self.button_login=Button(self.Loginframe2,text="Login",width=20,font=("arial",18,"bold"),
        command=self.login_system)
        self.button_login.grid(row=0,column=0,padx=10,pady=10)

        self.button_reset=Button(self.Loginframe2,text="Reset",width=20,font=("arial",18,"bold"),
        command=self.reset_btn)
        self.button_reset.grid(row=0,column=3,padx=10,pady=10)

        self.button_exit=Button(self.Loginframe2,text="Exit",width=20,font=("arial",18,"bold")
        ,command= self.exit_btn)
        self.button_exit.grid(row=0,column=6,padx=10,pady=10)


    def login_system(self):
        user=self.Username.get()
        pswd=self.Password.get()

        if (user==str("admin") and (pswd==str("admin"))):
            self.button_reg.config(state=NORMAL)
            self.button_Hosp.config(state=NORMAL)
            self.button_Dr_appt.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharamacy Management System","You have entered an invalid user name or password")
            self.button_reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_appt.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)
             # if usename and password ios disable state

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    
    def reset_btn(self):
        self.button_reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_appt.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)
        # because when we will reset we havent given correct user and password
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()
        


    def exit_btn(self):
        self.exit_btn=tkinter.messagebox.askyesno("Pharamcy Management System","Are you want to exit")
        if self.exit_btn>0:
            #We will close that master screen
            self.master.destroy()
            return










#First we will defimne all ours windows

    def Registration_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=windows2(self.newWindow)

    def Hospital_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=windows3(self.newWindow)

    def Dr_Appoint_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=windows4(self.newWindow)

    def Medicine_stock(self):
        self.newWindow=Toplevel(self.master)
        self.app=windows5(self.newWindow)





class windows2:
    #def __init__(self,master):
        # self.master=master
        # self.master.title("Patient Management System")
        # self.master.geometry('1350x750+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
        # self.frame=Frame(self.master)
        # self.frame.pack()

    def __init__(self,root):
        self.root=root
        self.root.title("Pharamcy Management System")
        self.root.geometry('1350x750+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
        self.root.configure(background="black")


        #we will take live time date by using time module

        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref=StringVar()
        Mobile_no=StringVar()
        Pincode=StringVar()
        Address=StringVar()
        FirstName=StringVar()
        LastName=StringVar()
        Gender=StringVar()

        #this var1,2,3,4,5
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=IntVar() #we will keep as int bcz we will keep here numerical value

        Membership=StringVar()
        Membership.set("0") #When membership checkbox is unclicked or reset has been done it will automatically set 
        

        #############functions###################
        def exitbtt():
            exitbtt=tkinter.messagebox.askyesno("Member Registration Form","Are you sure you want to exit ?")
            if exitbtt > 0:
                root.destroy()
                return
        
        def resetbtt():
            FirstName.set("")
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            LastName.set("")
            Gender.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_membertypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt(state=DISABLED)

        def reeesetbtn():
            reeesetbtn=tkinter.messagebox.askokcancel("member Registration Form","you want to add as new Record")
            if reeesetbtn>0:
                resetbtt()
            elif reeesetbtn<=0:
                resetbtt()
                detail_labeltxt.delete("1.0",END)
                return

        
        def Reference_number():
            ranumber=random.randint(10000,9999999)
            randomnumber=str(ranumber)
            Ref.set(randomnumber)

        def membership_fees():

            if(var5.get()==1):  #when checkbox is clicked
                member_membershiptxt.configure(state=NORMAL)
                item=float(15000) #it is price of membership plan you can change according"
                Membership.set(str(item)+ "Rs")
            elif(var5.get()==0):
                #when unchecked
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")
        
        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END,"\t" +Date_of_Registration.get() + "\t\t"+Ref.get()+"\t" +
            FirstName.get() +"  \t"+LastName.get()+"\t\t"+ Mobile_no.get()+"\t "+Address.get()+"\t"+Pincode.get()+'\t' + member_gendercmb.get()+
            "\t\t"+Membership.get()+"\n")
            #detail_labeltxt.insert(END,"\t "+Date_of_Registration.get()+"\t  "+Ref.get()+"\t\t"+FirstName.get()+"\t  "+LastName.get()+"\t   "+Mobile_no.get()+"\t"+Address.get()+"\t\t"+Pincode.get()+"\t"+member_gendercmb.get()+"\t"+Membership.get()+"\n")





        ##################TITLE################

        title=Label(self.root,text="Patient Registration Form" ,font=("monotype corsive",20,"bold"),bd=5,
        relief=GROOVE,bg="#E6005C",fg="#000000")
        title.pack(side=TOP,fill=X)

        ################Member Frame###############
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#001a66")
        Manage_Frame.place(x=20,y=100,width=450,height=630)


        ###############Detail Frame################
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#001a66")
        detail_frame.place(x=500,y=100,width=820,height=630) 

        detail_label=Label(detail_frame,font=("arial",11,"bold"),pady=10,padx=2,width=95,
             text="Date\t Ref Id\t Firstname    Lastname    Mobile No    Address    Pincode    Gender    Membership")
        detail_label.grid(row=0,column=0,columnspan=4,sticky="w")
        detail_labeltxt=Text(detail_frame,width=123,height=34,font=("arial",10))
        detail_labeltxt.grid(row=1,column=0,columnspan=4)
        

        #################### We Will Add the button in detail frame###################
        recieptbtn=Button(detail_frame,padx=15,bd=5,font=("arial",12,"bold"),
        bg="#ff9966",width=20,text="Reciept",command=Receipt )
        recieptbtn.grid(row=2,column=0) 

        resetbtn=Button(detail_frame,padx=15,bd=5,font=("arial",12,"bold"),
        bg="#ff9966",width=20,text="Reset", command=reeesetbtn)
        resetbtn.grid(row=2,column=1) 

        exitbtn=Button(detail_frame,padx=15,bd=5,font=("arial",12,"bold"),
        bg="#ff9966",width=20,text="Exit", command=exitbtt)
        
        exitbtn.grid(row=2,column=2)



        #################text label comboboxes in Manage frame#########

        Cus_title=Label(Manage_Frame,text="Patient Detail",font=("arial",20,"bold"),bg="#001a66",fg="white")
        Cus_title.grid(row=0,columnspan=2,pady=5)

        member_datelb1=Label(Manage_Frame,text="Date",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_datelb1.grid(row=1,column=0,pady=5,padx=10,sticky="w")

        member_datetxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=Date_of_Registration)
        member_datetxt.grid(row=1,column=1,pady=5,padx=10,sticky="w")

        member_reflbl=Label(Manage_Frame,text="Reference ID",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_reflbl.grid(row=2,column=0,pady=5,padx=10,sticky="w")

        member_reftxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=Ref)
        member_reftxt.grid(row=2,column=1,pady=5,padx=10,sticky="w")

        member_fnamelbl=Label(Manage_Frame,text="First Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_fnamelbl.grid(row=3,column=0,pady=5,padx=10,sticky="w")

        member_fnametxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=FirstName)
        member_fnametxt.grid(row=3,column=1,pady=5,padx=10,sticky="w")

        member_lnamelbl=Label(Manage_Frame,text="Last Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_lnamelbl.grid(row=4,column=0,pady=5,padx=10,sticky="w")

        member_lnametxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=LastName)
        member_lnametxt.grid(row=4,column=1,pady=5,padx=10,sticky="w")

        member_mobnolbl=Label(Manage_Frame,text="Mobile Number",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_mobnolbl.grid(row=5,column=0,pady=5,padx=10,sticky="w")

        member_mobnotxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=Mobile_no)
        member_mobnotxt.grid(row=5,column=1,pady=5,padx=10,sticky="w")

        member_addresslbl=Label(Manage_Frame,text="Address",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_addresslbl.grid(row=6,column=0,pady=5,padx=10,sticky="w")

        member_addresstxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=Address)
        member_addresstxt.grid(row=6,column=1,pady=5,padx=10,sticky="w")

        member_pincodelbl=Label(Manage_Frame,text="Pincode",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_pincodelbl.grid(row=7,column=0,pady=5,padx=10,sticky="w")

        member_pincodetxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=Pincode)
        member_pincodetxt.grid(row=7,column=1,pady=5,padx=10,sticky="w")
        
        member_genderlbl=Label(Manage_Frame,text="Gender",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_genderlbl.grid(row=8,column=0,pady=5,padx=10,sticky="w")

        member_gendercmb=ttk.Combobox(Manage_Frame,text=var4,state="randonly",font=("arial",15,"bold"),width=19)
        member_gendercmb['values']=("","Male","Female","Other")
        member_gendercmb.current(0) #No values Is in that table 
        member_gendercmb.grid(row=8,column=1,pady=5,padx=10,sticky="w")   
        

        member_id_prooflbl=Label(Manage_Frame,text="ID Proof",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_id_prooflbl.grid(row=9,column=0,pady=5,padx=10,sticky="w")

        member_id_proofcmb=ttk.Combobox(Manage_Frame,text=var3,state="randonly",font=("arial",15,"bold"),width=19)
        member_id_proofcmb['values']=("","Adhar Card","Passport","Driving License","Pan Card","Student Id")
        member_id_proofcmb.current(0) #No values Is in that table 
        member_id_proofcmb.grid(row=9,column=1,pady=5,padx=10,sticky="w")

        member_membertypelbl=Label(Manage_Frame,text="Member Type",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_membertypelbl.grid(row=10,column=0,pady=5,padx=10,sticky="w")

        member_membertypecmb=ttk.Combobox(Manage_Frame,text=var2,state="randonly",font=("arial",15,"bold"),width=19)
        member_membertypecmb['values']=("","Ayushman Card","Insurance","Pay Immediately","Pay When Leavng")
        member_membertypecmb.current(0) #No values Is in that table 
        member_membertypecmb.grid(row=10,column=1,pady=5,padx=10,sticky="w")   
        

        member_paymentwithlbl=Label(Manage_Frame,text="Payment With",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_paymentwithlbl.grid(row=11,column=0,pady=5,padx=10,sticky="w")

        member_paymentwithcmb=ttk.Combobox(Manage_Frame,text=var1,state="randonly",font=("arial",15,"bold"),width=19)
        member_paymentwithcmb['values']=("","Cash","Debit Card - RuPay","Debit Card - Visa","Debit Card - MasterCard","Credit Card","Phonepe" "GooglePay","Paytm")
        member_paymentwithcmb.current(0) #No values Is in that table 
        member_paymentwithcmb.grid(row=11,column=1,pady=5,padx=10,sticky="w")

        member_membership=Checkbutton(Manage_Frame,text="Membership Fees",variable=var5,onvalue=1,offvalue=0,
         font=("arial",15,"bold"),bg="#001a66",fg="white", command=membership_fees)

        member_membership.grid(row=12,column=0,sticky="w")

        member_membershiptxt=Entry(Manage_Frame,font=("arial",15,"bold"),state=DISABLED,justify=RIGHT,
        textvariable=Membership)
        member_membershiptxt.grid(row=12,column=1,pady=5,padx=10,sticky="w")
        

        



class windows3:
    # def __init__(self,master):
        # self.master=master
        # self.master.title("Hospital Management System")
        # self.master.geometry('1350x750+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
        # self.frame=Frame(self.master)
        # self.frame.pack()
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry('1700x900+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
        self.root.configure(background="black")



        ##################Variable Description###############
        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref=StringVar()
        cmbTabletNames=StringVar()
        HospitalCode=StringVar()
        Number_of_Tablets=StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpiryDate=StringVar()
        DailyDose=StringVar()
        SideEffects=StringVar()
        MoreInformation=StringVar()
        StorageAdvice=StringVar()
        Medication=StringVar()
        PatientId=StringVar()
        PatientName=StringVar()
        PatientNHnumber=StringVar()
        DateofBirth=StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()
        NHSnumber=StringVar()

      #To generate Random Number
        def Reference_num():
            ranumber=random.randint(10000,9999999)
            randomnumber=str(ranumber)
            Ref.set(randomnumber)


        def Prescriptiondata():
            Reference_num()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"+PatientName.get()+"\t\t"+DateofBirth.get()+"\t\t"+NHSnumber.get()+"\t"+Tabletcmb.get()+"\t"+Number_of_Tablets.get()+"\t\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+StorageAdvice.get()+"\t\t"+PatientId.get()+"\n")
            return

        def Prescriptionfun():
            Reference_num()
            TextPrescription.insert(END,"Patient ID: \t\t"+PatientId.get()+"\n")
            TextPrescription.insert(END,"Patient Name: \t\t"+PatientName.get()+"\n")
            TextPrescription.insert(END,"Tablet: \t\t"+Tabletcmb.get()+"\n")
            TextPrescription.insert(END,"Number of Tablet: \t\t"+Number_of_Tablets.get()+"\n")
            TextPrescription.insert(END,"Daily Dose: \t\t"+DailyDose.get()+"\n") 
            TextPrescription.insert(END,"Issued Date: \t\t"+IssuedDate.get()+"\n")
            TextPrescription.insert(END,"Expiry Date: \t\t"+ExpiryDate.get()+"\n")
            TextPrescription.insert(END,"Storage: \t\t"+StorageAdvice.get()+"\n")
            TextPrescription.insert(END,"More Information: \t\t"+MoreInformation.get()+"\n")
            return 

        def Exitbtn():
            Exitbtn=tkinter.messagebox.askyesno("Hospital Management System","Are you sure you want to exit ?")
            if Exitbtn > 0:
                root.destroy()
                return

        def DeletFun():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientName.set("")
            PatientNHnumber.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return

        def Restfun():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientName.set("")
            PatientNHnumber.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            return






        





    ##################TITLE################

        title=Label(self.root,text="Hospital Management System" ,font=("monotype corsive",42,"bold"),bd=5,
        relief=GROOVE,bg="#2eb8b8",fg="black")
        title.pack(side=TOP,fill=X)

    ################ FRAME ###############
        Manage_Frame=Frame(self.root,width=1510,height=400,bd=4,relief=RIDGE,bg="#0099cc")
        Manage_Frame.place(x=10,y=80)

        Button_Frame=Frame(self.root,width=1510,height=55,bd=4,relief=RIDGE,bg="#328695")
        Button_Frame.place(x=10,y=460)

        Data_Frame=Frame(self.root,width=1510,height=270,bd=4,relief=RIDGE,bg="#266e73")
        Data_Frame.place(x=10,y=510)

    ####################Inner Frame #######################

        Data_FrameLeft=LabelFrame(Manage_Frame,width=1050,text="General Information",font=("arial",20,"italic bold"),height=390,bd=7,relief=RIDGE,bg="#0099cc")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight=LabelFrame(Manage_Frame,width=1050,text="Prescription",font=("arial",15,"italic bold"),height=390,bd=7,relief=RIDGE,bg="#0099cc")
        Data_FrameRight.pack(side=RIGHT)


        Data_Framedata=LabelFrame(Data_Frame,width=1050,text="Prescription Data",font=("arial",12,"italic bold"),height=390,bd=4,relief=RIDGE,bg="#3eb7bb")
        Data_Framedata.pack()


        ############## Data of left frame#################

        Datelb1=Label(Data_FrameLeft,text="Date",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        Datelb1.grid(row=0,column=0,pady=5,padx=10,sticky=W)

        Datetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=Date_of_Registration)
        Datetxt.grid(row=0,column=1,pady=5,padx=10,sticky=E)

        ####### Ref #################
        Reflb1=Label(Data_FrameLeft,text="Ref",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        Reflb1.grid(row=1,column=0,pady=5,padx=10,sticky=W)

        Reftxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,state=DISABLED,textvariable=Ref)
        Reftxt.grid(row=1,column=1,pady=5,padx=10,sticky=E)
        
        ######  Patient Id#################
        PatientIdlb1=Label(Data_FrameLeft,text="Patient Id",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        PatientIdlb1.grid(row=2,column=0,pady=5,padx=10,sticky=W)

        PatientIdtxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=PatientId)
        PatientIdtxt.grid(row=2,column=1,pady=5,padx=10,sticky=E)

        ###############Patient Name ###############
        PatientNamelb1=Label(Data_FrameLeft,text="Patient Name",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        PatientNamelb1.grid(row=3,column=0,pady=5,padx=10,sticky=W)
        PatientNametxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=PatientName)
        PatientNametxt.grid(row=3,column=1,pady=5,padx=10,sticky=E)
        ###########Date of Birth########################
        DateofBirthlb1=Label(Data_FrameLeft,text="Date of Birth",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        DateofBirthlb1.grid(row=4,column=0,pady=5,padx=10,sticky=W)
        DateofBirthtxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=DateofBirth)
        DateofBirthtxt.grid(row=4,column=1,pady=5,padx=10,sticky=E)

        ###############Addresss##############
        Addresslb1=Label(Data_FrameLeft,text="Address",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        Addresslb1.grid(row=5,column=0,pady=5,padx=10,sticky=W)
        Addresstxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=PatientAddress)
        Addresstxt.grid(row=5,column=1,pady=5,padx=10,sticky=E)

        ###################NHsNumber#########

        NHSnumberlb1=Label(Data_FrameLeft,text="NHS Unique Number",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        NHSnumberlb1.grid(row=6,column=0,pady=5,padx=10,sticky=W)
        NHSnumbertxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6,column=1,pady=5,padx=10,sticky=E)

        #################### Tablet Name####

        Tabletlb1=Label(Data_FrameLeft,text="Tablet",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        Tabletlb1.grid(row=7,column=0,pady=5,padx=10,sticky=W)
        Tabletcmb=ttk.Combobox(Data_FrameLeft,textvariable=cmbTabletNames,state="randonly",font=("arial",15,"bold"),width=25)
        Tabletcmb['values']=("","Paracetamol","Dan-p","Dio-l One","calpol","amlodipine Besylate","Nexium","Singulair","Plavix","Amoxicillian","Azithromycin","Limcin-900")
        Tabletcmb.current(0) #No values Is in that table 
        Tabletcmb.grid(row=7,column=1,pady=5,padx=10)

        ##################No of tablets Take############
        
        No_of_Tabletlb1=Label(Data_FrameLeft,text="No. of Tablets",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        No_of_Tabletlb1.grid(row=8,column=0,pady=5,padx=10,sticky=W)
        No_of_Tablettxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=Number_of_Tablets)
        No_of_Tablettxt.grid(row=8,column=1,pady=5,padx=10,sticky=E)
        ##########Now will make 2nd  column for  list

        ##########hospital code

        HospitalCodelb1=Label(Data_FrameLeft,text="Hospital Code",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        HospitalCodelb1.grid(row=0,column=2,pady=5,padx=10,sticky=W)
        HospitalCodetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=HospitalCode)
        HospitalCodetxt.grid(row=0,column=3,pady=5,padx=10,sticky=E)
        
        #Storage Advice to Keep medicine 
        StorageAdvicelb1=Label(Data_FrameLeft,text="Storage Advice",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        StorageAdvicelb1.grid(row=1,column=2,pady=5,padx=10,sticky=W)
        StorageAdvicecmb=ttk.Combobox(Data_FrameLeft,textvariable=StorageAdvice,state="randonly",font=("arial",15,"bold"),width=25)
        StorageAdvicecmb['values']=("","Under room Temperature","Below 5 Degree Celcious","Below 0 Degree Celcious","Refrigration")
        StorageAdvicecmb.current(0) #No values Is in that table 
        StorageAdvicecmb.grid(row=1,column=3,pady=5,padx=10)

        ###############Lot number medicine################
        Lot_nolb1=Label(Data_FrameLeft,text="Lot number",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        Lot_nolb1.grid(row=2,column=2,pady=5,padx=10,sticky=W)
        Lot_notxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=Lot)
        Lot_notxt.grid(row=2,column=3,pady=5,padx=10,sticky=E)

        ################Issued Date#####################
        IssuedDatelb1=Label(Data_FrameLeft,text="Date of Issue",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        IssuedDatelb1.grid(row=3,column=2,pady=5,padx=10,sticky=W)
        IssuedDatetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=IssuedDate)
        IssuedDatetxt.grid(row=3,column=3,pady=5,padx=10,sticky=E)

        ################Expiry Date######################
        ExpiryDatelb1=Label(Data_FrameLeft,text="Date of Expiry",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        ExpiryDatelb1.grid(row=4,column=2,pady=5,padx=10,sticky=W)
        ExpiryDatetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4,column=3,pady=5,padx=10,sticky=E)

        #######################Daily Dose###################
        Dailydoselb1=Label(Data_FrameLeft,text="Dose",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        Dailydoselb1.grid(row=5,column=2,pady=5,padx=10,sticky=W)
        Dailydosetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=DailyDose)
        Dailydosetxt.grid(row=5,column=3,pady=5,padx=10,sticky=E)

        ##############Side Effects##################
        SideEffectlb1=Label(Data_FrameLeft,text="Side Effects",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        SideEffectlb1.grid(row=6,column=2,pady=5,padx=10,sticky=W)
        SideEffecttxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=SideEffects)
        SideEffecttxt.grid(row=6,column=3,pady=5,padx=10,sticky=E)
        
        ##############More Information like meet to dr or any other related to patient which is important

        MoreInformationlb1=Label(Data_FrameLeft,text="More Information",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        MoreInformationlb1.grid(row=7,column=2,pady=5,padx=10,sticky=W)
        MoreInformationtxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=MoreInformation)
        MoreInformationtxt.grid(row=7,column=3,pady=5,padx=10,sticky=E)

        ###########Mediation yes or no
        Medicationlb1=Label(Data_FrameLeft,text="Medication",font=("arial",12,"bold"),width=20,bg="#0099cc",fg="white")
        Medicationlb1.grid(row=8,column=2,pady=5,padx=10,sticky=W)
        Medicationtxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=Medication)
        Medicationtxt.grid(row=8,column=3,pady=5,padx=10,sticky=E)


        #Text Field for Prescription

        TextPrescription=Text(Data_FrameRight,font=("arial",12,"bold"),width=55,height=17, pady=5,padx=3)
        TextPrescription.grid(row=0,column=0)

        #Text for Prescription data

        TextPrescriptionData=Text(Data_Framedata,font=("arial",12,"bold"),width=203,height=17)
        TextPrescriptionData.grid(row=1,column=0)

        #Now we add Button to our middle frame

        prescriptionbtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="#ff9966",width=22,text="Prescription",command=Prescriptionfun)
        prescriptionbtn.grid(row=0,column=0,padx=15) 

        Prescriptiondatabtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="#ff9966",width=22,text="Prescription Data",command=Prescriptiondata)
        Prescriptiondatabtn.grid(row=0,column=1,padx=15)

        Deletebtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="#ff9966",width=22,text="Delete",command=DeletFun)
        Deletebtn.grid(row=0,column=2,padx=15)

        Resetbtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="#ff9966",width=22,text="Reset",command=Restfun)
        Resetbtn.grid(row=0,column=3,padx=15)

        Exitbtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="#ff9966",width=22,text="Exit",command=Exitbtn)
        Exitbtn.grid(row=0,column=4,padx=15)

        Deletebtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="#ff9966",width=22,text="Delete",command=DeletFun)
        Deletebtn.grid(row=0,column=5,padx=15)

        Prescriptiondatarow=Label(Data_Framedata,bg="white",font=("arial",12,"bold"),
        text="Date\tReference Id\tPatient Name\tDate of Birth\tNHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice\tPatientID")
        Prescriptiondatarow.grid(row=0,column=0,sticky=W)




class windows4:
    # def __init__(self,master):
    #     self.master=master
    #     self.master.title("Doctor Management System")
    #     self.master.geometry('1350x750+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
    #     self.frame=Frame(self.master)
    #     self.frame.pack()
    def __init__(self,root):
        self.root=root
        self.root.title("Doctor Management System")
        self.root.geometry('1700x900+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
        self.root.configure(background="black")



        ##################Variable Description###############
        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        DoctorId=StringVar()
        ExprienceYrs=StringVar()
        DoctorMobno=StringVar()
        NursesUDr=StringVar()
        AppointTime=StringVar()
        PatientAge=StringVar()
        PatientAdd=StringVar()
        PatientMob=StringVar()
        PatientDis=StringVar()
        Case=StringVar()
        PatientName=StringVar()
        BenefitsCard=StringVar()
        DoctorName=StringVar()
        DateofBirth=StringVar()
        PatientNHnumber=StringVar()
        Specialization=StringVar()
        GovtPrivate=StringVar()
        Prescription=StringVar()
        TotalSurgry=StringVar()

      #To generate Random Number
        def Reference_num():
            ranumber=random.randint(10000,9999999)
            randomnumber=str(ranumber)
            DoctorId.set(randomnumber)


        def Prescriptiondata():
            Reference_num()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DoctorId.get()+"\t\t"+DateofBirth.get()+"\t\t"+Specialization.get()+"\t\t"+TotalSurgry.get()+"\t"+Tabletcmb.get()+"\t"+NursesUDr.get()+"\t\t\t"+PatientAge.get()+"\t\t"+PatientAdd.get()+"\t\t"+PatientMob.get()+"\t\t"+PatientName.get()+"\t\t"+DoctorName.get()+"\n")
            return

        def Prescriptionfun():
            Reference_num()
            TextPrescription.insert(END,"Doctor Name: \t\t"+DoctorName.get()+"\n")
            TextPrescription.insert(END,"Date of Birth: \t\t"+DateofBirth.get()+"\n")
            TextPrescription.insert(END,"Experience in years: \t\t"+Tabletcmb.get()+"\n")
            TextPrescription.insert(END,"Nurses Under Doctor: \t\t"+NursesUDr.get()+"\n")
            TextPrescription.insert(END,"Patient Name: \t\t"+PatientName.get()+"\n")
            TextPrescription.insert(END,"Patient Mob No: \t\t"+PatientMob.get()+"\n") 
            TextPrescription.insert(END,"Patient Age: \t\t"+PatientAge.get()+"\n")
            TextPrescription.insert(END,"Patient Address: \t\t"+PatientAdd.get()+"\n")
            TextPrescription.insert(END,"Cases: \t\t"+Case.get()+"\n")
            return 

        def Exitbtn():
            Exitbtn=tkinter.messagebox.askyesno("Doctor Management System","Are you sure you want to exit ?")
            if Exitbtn > 0:
                root.destroy()
                return

        def DeletFun():
            DoctorId.set("")
            ExprienceYrs.set("")
            DoctorMobno.set("")
            NursesUDr.set("")
            AppointTime.set("")
            PatientAge.set("")
            PatientAdd.set("")
            PatientMob.set("")
            PatientDis.set("")
            Case.set("")
            PatientName.set("")
            BenefitsCard.set("")
            DoctorName.set("")
            DateofBirth.set("")
            PatientNHnumber.set("")
            Specialization.set("")
            GovtPrivate.set("")
            Prescription.set("")
            TotalSurgry.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return

        def Restfun():
            DoctorId.set("")
            ExprienceYrs.set("")
            DoctorMobno.set("")
            NursesUDr.set("")
            AppointTime.set("")
            PatientAge.set("")
            PatientAdd.set("")
            PatientMob.set("")
            PatientDis.set("")
            Case.set("")
            PatientName.set("")
            BenefitsCard.set("")
            DoctorName.set("")
            DateofBirth.set("")
            PatientNHnumber.set("")
            Specialization.set("")
            GovtPrivate.set("")
            Prescription.set("")
            TotalSurgry.set("")
            TextPrescription.delete("1.0",END)
            return



    



        





    ##################TITLE################

        title=Label(self.root,text="Doctor Management System" ,font=("monotype corsive",42,"bold"),bd=5,
        relief=GROOVE,bg="goldenrod1",fg="black")
        title.pack(side=TOP,fill=X)

    ################ FRAME ###############
        Manage_Frame=Frame(self.root,width=1510,height=400,bd=4,relief=RIDGE,bg="DodgerBlue2")
        Manage_Frame.place(x=10,y=80)

        Button_Frame=Frame(self.root,width=1510,height=55,bd=4,relief=RIDGE,bg="#328695")
        Button_Frame.place(x=10,y=460)

        Data_Frame=Frame(self.root,width=1510,height=270,bd=4,relief=RIDGE,bg="#266e73")
        Data_Frame.place(x=10,y=510)

    ####################Inner Frame #######################

        Data_FrameLeft=LabelFrame(Manage_Frame,width=1050,text="General Information",font=("arial",20,"italic bold"),height=390,bd=7,relief=RIDGE,bg="DodgerBlue2")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight=LabelFrame(Manage_Frame,width=1050,text="Prescription",font=("arial",15,"italic bold"),height=390,bd=7,relief=RIDGE,bg="DodgerBlue2")
        Data_FrameRight.pack(side=RIGHT)


        Data_Framedata=LabelFrame(Data_Frame,width=1050,text="Prescription Data",font=("arial",12,"italic bold"),height=390,bd=4,relief=RIDGE,bg="#3eb7bb")
        Data_Framedata.pack()


        ############## Data of left frame#################

        Datelb1=Label(Data_FrameLeft,text="Date",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        Datelb1.grid(row=0,column=0,pady=5,padx=10,sticky=W)

        Datetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=Date_of_Registration)
        Datetxt.grid(row=0,column=1,pady=5,padx=10,sticky=E)

        ####### Ref #################
        Reflb1=Label(Data_FrameLeft,text="Doctor Id",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        Reflb1.grid(row=1,column=0,pady=5,padx=10,sticky=W)

        Reftxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,state=DISABLED,textvariable=DoctorId)
        Reftxt.grid(row=1,column=1,pady=5,padx=10,sticky=E)
        
        ######  Patient Id#################
        PatientIdlb1=Label(Data_FrameLeft,text="Doctor Name",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        PatientIdlb1.grid(row=2,column=0,pady=5,padx=10,sticky=W)

        PatientIdtxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=DoctorName)
        PatientIdtxt.grid(row=2,column=1,pady=5,padx=10,sticky=E)

        ###############Patient Name ###############
        PatientNamelb1=Label(Data_FrameLeft,text="Date of Birth",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        PatientNamelb1.grid(row=3,column=0,pady=5,padx=10,sticky=W)
        PatientNametxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=DateofBirth)
        PatientNametxt.grid(row=3,column=1,pady=5,padx=10,sticky=E)
        ###########Date of Birth########################
        DateofBirthlb1=Label(Data_FrameLeft,text="Speciallization",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        DateofBirthlb1.grid(row=4,column=0,pady=5,padx=10,sticky=W)
        DateofBirthtxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=Specialization)
        DateofBirthtxt.grid(row=4,column=1,pady=5,padx=10,sticky=E)

        ###############Addresss##############
        Addresslb1=Label(Data_FrameLeft,text="GovtPrivate",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        Addresslb1.grid(row=5,column=0,pady=5,padx=10,sticky=W)
        Addresstxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=GovtPrivate)
        Addresstxt.grid(row=5,column=1,pady=5,padx=10,sticky=E)

        ###################NHsNumber#########

        NHSnumberlb1=Label(Data_FrameLeft,text="Surgeries",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        NHSnumberlb1.grid(row=6,column=0,pady=5,padx=10,sticky=W)
        NHSnumbertxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=TotalSurgry)
        NHSnumbertxt.grid(row=6,column=1,pady=5,padx=10,sticky=E)

        #################### Tablet Name####

        Tabletlb1=Label(Data_FrameLeft,text="Experience in",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        Tabletlb1.grid(row=7,column=0,pady=5,padx=10,sticky=W)
        Tabletcmb=ttk.Combobox(Data_FrameLeft,textvariable=ExprienceYrs,state="randonly",font=("arial",15,"bold"),width=25)
        Tabletcmb['values']=("","Homopathic","Dentist","NuroSergen","General","MBBS","MD","BAMS","BHMS")
        Tabletcmb.current(0) #No values Is in that table 
        Tabletcmb.grid(row=7,column=1,pady=5,padx=10)

        ##################No of tablets Take############
        
        No_of_Tabletlb1=Label(Data_FrameLeft,text="Nurses under Doctor",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        No_of_Tabletlb1.grid(row=8,column=0,pady=5,padx=10,sticky=W)
        No_of_Tablettxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=NursesUDr)
        No_of_Tablettxt.grid(row=8,column=1,pady=5,padx=10,sticky=E)
        ##########Now will make 2nd  column for  list

        ##########hospital code

        HospitalCodelb1=Label(Data_FrameLeft,text="Dr Mobile No",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        HospitalCodelb1.grid(row=0,column=2,pady=5,padx=10,sticky=W)
        HospitalCodetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=DoctorMobno)
        HospitalCodetxt.grid(row=0,column=3,pady=5,padx=10,sticky=E)
        
        #Storage Advice to Keep medicine 
        StorageAdvicelb1=Label(Data_FrameLeft,text="Patient Name",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        StorageAdvicelb1.grid(row=1,column=2,pady=5,padx=10,sticky=W)
        StorageAdvicetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=PatientName)
        StorageAdvicetxt.grid(row=1,column=3,pady=5,padx=10,sticky=E)

        ###############Lot number medicine################
        Lot_nolb1=Label(Data_FrameLeft,text="Appointment Time",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        Lot_nolb1.grid(row=2,column=2,pady=5,padx=10,sticky=W)
        Lot_notxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=AppointTime)
        Lot_notxt.grid(row=2,column=3,pady=5,padx=10,sticky=E)

        ################Issued Date#####################
        IssuedDatelb1=Label(Data_FrameLeft,text="Patient Age",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        IssuedDatelb1.grid(row=3,column=2,pady=5,padx=10,sticky=W)
        IssuedDatetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=PatientAge)
        IssuedDatetxt.grid(row=3,column=3,pady=5,padx=10,sticky=E)

        ################Expiry Date######################
        ExpiryDatelb1=Label(Data_FrameLeft,text="Patient Address",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        ExpiryDatelb1.grid(row=4,column=2,pady=5,padx=10,sticky=W)
        ExpiryDatetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=PatientAdd)
        ExpiryDatetxt.grid(row=4,column=3,pady=5,padx=10,sticky=E)

        #######################Daily Dose###################
        Dailydoselb1=Label(Data_FrameLeft,text="Patient Mobile Number",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        Dailydoselb1.grid(row=5,column=2,pady=5,padx=10,sticky=W)
        Dailydosetxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=PatientMob)
        Dailydosetxt.grid(row=5,column=3,pady=5,padx=10,sticky=E)

        ##############Side Effects##################
        SideEffectlb1=Label(Data_FrameLeft,text="Patient Disesse",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        SideEffectlb1.grid(row=6,column=2,pady=5,padx=10,sticky=W)
        SideEffecttxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=PatientDis)
        SideEffecttxt.grid(row=6,column=3,pady=5,padx=10,sticky=E)
        
        ##############More Information like meet to dr or any other related to patient which is important

        MoreInformationlb1=Label(Data_FrameLeft,text="Case",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        MoreInformationlb1.grid(row=7,column=2,pady=5,padx=10,sticky=W)
        MoreInformationtxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=Case)
        MoreInformationtxt.grid(row=7,column=3,pady=5,padx=10,sticky=E)

        ###########Mediation yes or no
        Medicationlb1=Label(Data_FrameLeft,text="Benefits Card",font=("arial",12,"bold"),width=20,bg="DodgerBlue2",fg="white")
        Medicationlb1.grid(row=8,column=2,pady=5,padx=10,sticky=W)
        Medicationtxt=Entry(Data_FrameLeft, font=("arial",15,"bold"),width=27,textvariable=BenefitsCard)
        Medicationtxt.grid(row=8,column=3,pady=5,padx=10,sticky=E)


        #Text Field for Prescription

        TextPrescription=Text(Data_FrameRight,font=("arial",12,"bold"),width=55,height=17, pady=5,padx=3)
        TextPrescription.grid(row=0,column=0)

        #Text for Prescription data

        TextPrescriptionData=Text(Data_Framedata,font=("arial",12,"bold"),width=203,height=17)
        TextPrescriptionData.grid(row=1,column=0)

        #Now we add Button to our middle frame

        prescriptionbtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="goldenrod1",width=22,text="Prescription",command=Prescriptionfun)
        prescriptionbtn.grid(row=0,column=0,padx=15) 

        Prescriptiondatabtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="goldenrod1",width=22,text="Prescription Data",command=Prescriptiondata)
        Prescriptiondatabtn.grid(row=0,column=1,padx=15)

        Deletebtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="goldenrod1",width=22,text="Delete",command=DeletFun)
        Deletebtn.grid(row=0,column=2,padx=15)

        Resetbtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="goldenrod1",width=22,text="Reset",command=Restfun)
        Resetbtn.grid(row=0,column=3,padx=15)

        Exitbtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="goldenrod1",width=22,text="Exit",command=Exitbtn)
        Exitbtn.grid(row=0,column=4,padx=15)

        Deletebtn=Button(Button_Frame,font=("arial",15,"bold"),activebackground="#fcceb2",
        bg="goldenrod1",width=22,text="Delete",command=DeletFun)
        Deletebtn.grid(row=0,column=5,padx=15)

        Prescriptiondatarow=Label(Data_Framedata,bg="white",font=("arial",12,"bold"),
        text="Date\tDoctor Id\t  Date of Birth \t Specialization \t Total Surgeries \tExperience yrs \t Nurses\tPatient Age\tPatient Address\tPatient Mob No.\tPatientName\tDoctor Name")
        Prescriptiondatarow.grid(row=0,column=0,sticky=W)
    
class windows5:
    # def __init__(self,master):
    #     self.master=master
    #     self.master.title("Medicine System")
    #     self.master.geometry('1350x750+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
    #     self.frame=Frame(self.master)
    #     self.frame.pack()
    def __init__(self,root):
        self.root=root
        self.root.title("Medicine Management System")
        self.root.geometry('1350x750+0+0') #x-axis, y-axis 0 0 location from leftmost most part of x an y-axis
        self.root.configure(background="black")


        #we will take live time date by using time module

        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref=StringVar()
        Mobile_no=StringVar()
        ExpiryDate=StringVar()
        MedicineName=StringVar()
        FirstName=StringVar()
        LastName=StringVar()
        ManufactureDate=StringVar()

        #this var1,2,3,4,5
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=IntVar() #we will keep as int bcz we will keep here numerical value

        Membership=StringVar()
        Membership.set("0") #When membership checkbox is unclicked or reset has been done it will automatically set 
        

        #############functions###################
        def exitbtt():
            exitbtt=tkinter.messagebox.askyesno("Medicine Registration Form","Are you sure you want to exit ?")
            if exitbtt > 0:
                root.destroy()
                return
        
        def resetbtt():
            FirstName.set("")
            Ref.set("")
            Mobile_no.set("")
            ExpiryDate.set("")
            MedicineName.set("")
            LastName.set("")
            
            var1.set("") 
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            
            member_paymentwithcmb.current(0)
            member_membershiptxt(state=DISABLED)

        def reeesetbtn():
            reeesetbtn=tkinter.messagebox.askokcancel("Medicine Registration Form","you want to add as new Record")
            if reeesetbtn>0:
                resetbtt()
            elif reeesetbtn<=0:
                resetbtt()
                detail_labeltxt.delete("1.0",END)
                return

        
        def Reference_number():
            ranumber=random.randint(10000,9999999)
            randomnumber=str(ranumber)
            Ref.set(randomnumber)

        def membership_fees():

            if(var5.get()==1):  #when checkbox is clicked
                member_membershiptxt.configure(state=NORMAL)
                item=float() #it is price of membership plan you can change according"
                Membership.set(str(item)+ "Rs")
            elif(var5.get()==0):
                #when unchecked
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")
        
        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END,"\t" +Date_of_Registration.get() + "\t\t"+Ref.get()+"\t" +
            FirstName.get() +"  \t"+LastName.get()+"\t\t"+ Mobile_no.get()+"\t "+MedicineName.get()+"\t"+ExpiryDate.get()+'\t' + member_gendercmb.get()+
            "\t\t"+member_paymentwithcmb.get()+"\n")
            #detail_labeltxt.insert(END,"\t "+Date_of_Registration.get()+"\t  "+Ref.get()+"\t\t"+FirstName.get()+"\t  "+LastName.get()+"\t   "+Mobile_no.get()+"\t"+Address.get()+"\t\t"+Pincode.get()+"\t"+member_gendercmb.get()+"\t"+Membership.get()+"\n")





        ##################TITLE################

        title=Label(self.root,text="Medicine Registration Form" ,font=("monotype corsive",20,"bold"),bd=5,
        relief=GROOVE,bg="brown4",fg="#000000")
        title.pack(side=TOP,fill=X)

        ################Member Frame###############
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="sienna1")
        Manage_Frame.place(x=20,y=100,width=450,height=630)


        ###############Detail Frame################
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="sienna1")
        detail_frame.place(x=500,y=100,width=820,height=630) 

        detail_label=Label(detail_frame,font=("arial",11,"bold"),pady=10,padx=2,width=95,
             text="Date\t Ref Id\t Firstname    Lastname    Mobile No    Medicine Name    Expiry Date    Gender    Payment")
        detail_label.grid(row=0,column=0,columnspan=4,sticky="w")
        detail_labeltxt=Text(detail_frame,width=123,height=34,font=("arial",10))
        detail_labeltxt.grid(row=1,column=0,columnspan=4)
        

        #################### We Will Add the button in detail frame###################
        recieptbtn=Button(detail_frame,padx=15,bd=5,font=("arial",12,"bold"),
        bg="#ffff40",width=20,text="Reciept",command=Receipt )
        recieptbtn.grid(row=2,column=0) 

        resetbtn=Button(detail_frame,padx=15,bd=5,font=("arial",12,"bold"),
        bg="#ffff40",width=20,text="Reset", command=reeesetbtn)
        resetbtn.grid(row=2,column=1) 

        exitbtn=Button(detail_frame,padx=15,bd=5,font=("arial",12,"bold"),
        bg="#ffff40",width=20,text="Exit", command=exitbtt)
        
        exitbtn.grid(row=2,column=2)



        #################text label comboboxes in Manage frame#########

        Cus_title=Label(Manage_Frame,text="Buyers Detail ",font=("arial",20,"bold"),bg="sienna1",fg="white")
        Cus_title.grid(row=0,columnspan=2,pady=5)

        member_datelb1=Label(Manage_Frame,text="Date",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_datelb1.grid(row=1,column=0,pady=5,padx=10,sticky="w")

        member_datetxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=Date_of_Registration)
        member_datetxt.grid(row=1,column=1,pady=5,padx=10,sticky="w")

        member_reflbl=Label(Manage_Frame,text="Reference ID",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_reflbl.grid(row=2,column=0,pady=5,padx=10,sticky="w")

        member_reftxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=Ref)
        member_reftxt.grid(row=2,column=1,pady=5,padx=10,sticky="w")

        member_fnamelbl=Label(Manage_Frame,text="First Name",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_fnamelbl.grid(row=3,column=0,pady=5,padx=10,sticky="w")

        member_fnametxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=FirstName)
        member_fnametxt.grid(row=3,column=1,pady=5,padx=10,sticky="w")

        member_lnamelbl=Label(Manage_Frame,text="Last Name",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_lnamelbl.grid(row=4,column=0,pady=5,padx=10,sticky="w")

        member_lnametxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=LastName)
        member_lnametxt.grid(row=4,column=1,pady=5,padx=10,sticky="w")

        member_mobnolbl=Label(Manage_Frame,text="Mobile Number",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_mobnolbl.grid(row=5,column=0,pady=5,padx=10,sticky="w")

        member_mobnotxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=Mobile_no)
        member_mobnotxt.grid(row=5,column=1,pady=5,padx=10,sticky="w")

        member_addresslbl=Label(Manage_Frame,text="Medicine Name",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_addresslbl.grid(row=8,column=0,pady=5,padx=10,sticky="w")

        member_addresstxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=MedicineName)
        member_addresstxt.grid(row=8,column=1,pady=5,padx=10,sticky="w")

        member_pincodelbl=Label(Manage_Frame,text="Expiry Date",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_pincodelbl.grid(row=10,column=0,pady=5,padx=10,sticky="w")

        member_pincodetxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=ExpiryDate)
        member_pincodetxt.grid(row=10,column=1,pady=5,padx=10,sticky="w")
        
        member_genderlbl=Label(Manage_Frame,text="Gender",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_genderlbl.grid(row=6,column=0,pady=5,padx=10,sticky="w")

        member_gendercmb=ttk.Combobox(Manage_Frame,text=var4,state="randonly",font=("arial",15,"bold"),width=19)
        member_gendercmb['values']=("","Male","Female","Other")
        member_gendercmb.current(0) #No values Is in that table 
        member_gendercmb.grid(row=6,column=1,pady=5,padx=10,sticky="w")   
        

        member_id_prooflbl=Label(Manage_Frame,text="ID Proof",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_id_prooflbl.grid(row=7,column=0,pady=5,padx=10,sticky="w")

        member_id_proofcmb=ttk.Combobox(Manage_Frame,text=var3,state="randonly",font=("arial",15,"bold"),width=19)
        member_id_proofcmb['values']=("","Adhar Card","Passport","Driving License","Pan Card","Student Id")
        member_id_proofcmb.current(0) #No values Is in that table 
        member_id_proofcmb.grid(row=7,column=1,pady=5,padx=10,sticky="w")

        member_membertypelbl=Label(Manage_Frame,text="Manufacture Date",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_membertypelbl.grid(row=9,column=0,pady=5,padx=10,sticky="w")
        member_pincodetxt=Entry(Manage_Frame, font=("arial",15,"bold"),textvariable=ManufactureDate)
        member_pincodetxt.grid(row=9,column=1,pady=5,padx=10,sticky="w")
        

        member_paymentwithlbl=Label(Manage_Frame,text="Payment With",font=("arial",15,"bold"),bg="sienna1",fg="white")
        member_paymentwithlbl.grid(row=11,column=0,pady=5,padx=10,sticky="w")

        member_paymentwithcmb=ttk.Combobox(Manage_Frame,text=var1,state="randonly",font=("arial",15,"bold"),width=19)
        member_paymentwithcmb['values']=("","Cash","Debit Card - RuPay","Debit Card - Visa","Debit Card - MasterCard","Credit Card","Phonepe" "GooglePay","Paytm")
        member_paymentwithcmb.current(0) #No values Is in that table 
        member_paymentwithcmb.grid(row=11,column=1,pady=5,padx=10,sticky="w")

        member_membership=Checkbutton(Manage_Frame,text="Total Bills",variable=var5,onvalue=1,offvalue=0,
         font=("arial",15,"bold"),bg="sienna1",fg="white", command=membership_fees)

        member_membership.grid(row=12,column=0,sticky="w")

        member_membershiptxt=Entry(Manage_Frame,font=("arial",15,"bold"),state=DISABLED,justify=RIGHT,
        textvariable=Membership)
        member_membershiptxt.grid(row=12,column=1,pady=5,padx=10,sticky="w")






if __name__ == '__main__':
    main()
    