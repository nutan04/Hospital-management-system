import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registration:
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
        


        

        


        

if __name__ == '__main__':
    root=Tk()
    app=Registration(root)
    root.mainloop()
