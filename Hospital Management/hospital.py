import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Hospital:
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
        


        

        


        

if __name__ == '__main__':
    root=Tk()
    app=Hospital(root)
    root.mainloop()
