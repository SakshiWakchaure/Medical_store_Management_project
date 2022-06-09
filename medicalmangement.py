
from re import L
from  tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
import random
import os





class PharmacyManagementSystem:
        def __init__(self,root):
                self.root=root
                self.root.title("Pharmacy Managment System")
                self.root.geometry("1550x800+0+0")

#*************************AddVAriable***********************************************
                self.addMed_var=StringVar()
                self.refMed_var=StringVar()


#**********************MAinVariable********************************************
                self.ref_no_var=StringVar()
                self.campanyName=StringVar()
                self.TypeMed=StringVar()
                self.Medicinename=StringVar()
                self.LotNo=StringVar()
                self.IssueDate=StringVar()
                self.ExpDate=StringVar()
                self.SideEff=StringVar()
                self.Symptom=StringVar()
                self.Precaution=StringVar()
                self.Dosage=StringVar()
                self.price=StringVar()
                self.ProductQt=StringVar()



                lbltitle=Label(self.root,text="MEDICAL MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                        bg='white',fg="darkblue",font=("times new roman",50,"bold"),padx=2,pady=4)
                lbltitle.pack(side=TOP,fill=X)
                
                img1=Image.open("D:\Project\logo.jpg")
                img1=img1.resize((80,80),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                b1=Button(self.root,image=self.photoimg1,borderwidth=0)
                b1.place(x=60,y=15)

                #*******************DataFrame*********************
                DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
                DataFrame.place(x=0,y=120,width=1530,height=400)


                DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                        fg="Darkblue",font=("Arial",12,"bold"))
                DataFrameLeft.place(x=0,y=5,width=900,height=350)

                ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
                ButtonFrame.place(x=0,y=520,width=1530,height=65)


        # ************************ButtonsFrame*******************************
                btnAddData=Button(ButtonFrame,command=self.AddData,text=("Medicine Add"),font=("Arial",13,"bold"),bg="Darkblue",fg="white")
                btnAddData.grid(row=0,column=0)

                btnupdmed=Button(ButtonFrame,command=self.Update,text=("UPDATE"),font=("Arial",13,"bold"),width=14,bg="Darkblue",fg="white")
                btnupdmed.grid(row=0,column=1)

                btndelMed=Button(ButtonFrame,command=self.Delete,text=("DELETE"),font=("Arial",13,"bold"),width=14,bg="Darkred",fg="white")
                btndelMed.grid(row=0,column=2)

                btnResetMed=Button(ButtonFrame,command=self.ResetData,text=("RESET"),font=("Arial",13,"bold"),width=14,bg="Darkblue",fg="white")
                btnResetMed.grid(row=0,column=3)

                btnExitMed=Button(ButtonFrame,command=self.open_registration_window,text=("BILL"),font=("Arial",13,"bold"),width=13,bg="Darkblue",fg="white")
                btnExitMed.grid(row=0,column=4)

        # ****************************Serach BY*******************************

                iblSearch=Label(ButtonFrame,text=("Search By"),font=("arial",17,"bold"),padx=2,bg="red",fg="white")
                iblSearch.grid(row=0,column=5,sticky=W)

                self.search_var=StringVar()
                search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17,"bold"),state="readonly")
                search_combo["values"]=("Medicinename","Symptom")
                search_combo.grid(row=0,column=6)
                search_combo.current(0)

                self.searchtxt_var=StringVar()

                txtSearch=Entry(ButtonFrame,textvariable=self.searchtxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
                txtSearch.grid(row=0,column=7)

                btnSearch=Button(ButtonFrame,command=self.SearchDate,text=("SEARCH"),font=("Arial",13,"bold"),width=14,bg="Darkblue",fg="white")
                btnSearch.grid(row=0,column=8)

                btnShowAll=Button(ButtonFrame,command=self.Fetch_data,text=("SHOW All"),font=("Arial",13,"bold"),width=14,bg="Darkblue",fg="white")
                btnShowAll.grid(row=0,column=9)

        # ******************************Labels And Entry********************************

                iblrefno=Label(DataFrameLeft,text=("Medicine Name"),font=("arial",12,"bold"),padx=2)
                iblrefno.grid(row=0,column=0,sticky=W)

                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()
                my_cursor.execute("select MedName from med")
                med=my_cursor.fetchall()

                search_comboMedname=ttk.Combobox(DataFrameLeft,textvariable=self.Medicinename,width=27,font=("arial",13,"bold"),state="write")
                search_comboMedname["values"]=med
                search_comboMedname.current(0)
                search_comboMedname.grid(row=0,column=1)
                  

                iblcmp=Label(DataFrameLeft,text=("Company Name:"),font=("arial",12,"bold"),padx=2)
                iblcmp.grid(row=1,column=0,sticky=W)       
                iblcmp=Entry(DataFrameLeft,textvariable=self.campanyName,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                iblcmp.grid(row=1,column=1)

                ibltym=Label(DataFrameLeft,text=("Types of Medicine"),font=("arial",12,"bold"),padx=2)
                ibltym.grid(row=2,column=0,sticky=W)

                search_combotym=ttk.Combobox(DataFrameLeft,textvariable=self.TypeMed,width=27,font=("arial",13,"bold"),state="readonly")
                search_combotym["values"]=("Tablet","Liquid","Capsules","Drops","Creams","Injections")
                search_combotym.current(0) 
                search_combotym.grid(row=2,column=1)

                iblMedname=Label(DataFrameLeft,text=("Reference No"),font=("arial",12,"bold"),padx=2,pady=6)
                iblMedname.grid(row=3,column=0,sticky=W)

                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()
                my_cursor.execute("select RefName from med")
                row=my_cursor.fetchall()

                search_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_no_var,width=27,font=("arial",13,"bold"),state="readonly")
                search_combo["values"]=(row)
                search_combo.grid(row=3,column=1)
                search_combo.current(0) 

                ibllot=Label(DataFrameLeft,text=("Lot No:"),font=("arial",12,"bold"),padx=2,pady=6)
                ibllot.grid(row=4,column=0,sticky=W)
                ibllot=Entry(DataFrameLeft,textvariable=self.LotNo,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                ibllot.grid(row=4,column=1)

                iblissue=Label(DataFrameLeft,text=("Issue Date:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblissue.grid(row=5,column=0,sticky=W)
                iblissue=Entry(DataFrameLeft,textvariable=self.IssueDate,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                iblissue.grid(row=5,column=1)

                iblexpdt=Label(DataFrameLeft,text=("Exp Date:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblexpdt.grid(row=6,column=0,sticky=W)
                iblexpdt=Entry(DataFrameLeft,textvariable=self.ExpDate,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                iblexpdt.grid(row=6,column=1)


                iblUses=Label(DataFrameLeft,text=("Symptom"),font=("arial",12,"bold"),padx=2,pady=6)
                iblUses.grid(row=7,column=0,sticky=W)
                iblUses=Entry(DataFrameLeft,textvariable=self.Symptom,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                iblUses.grid(row=7,column=1)
                
                iblsideeff=Label(DataFrameLeft,text=("Side Effect:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblsideeff.grid(row=8,column=0,sticky=W)
                iblsideeff=Entry(DataFrameLeft,textvariable=self.SideEff,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                iblsideeff.grid(row=8,column=1)

                iblPre=Label(DataFrameLeft,text=("Precaution:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblPre.grid(row=0,column=2,sticky=W)
                iblPre=Entry(DataFrameLeft,textvariable=self.Precaution,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                iblPre.grid(row=0,column=3)

                ibldos=Label(DataFrameLeft,text=("Dosage:"),font=("arial",12,"bold"),padx=2,pady=6)
                ibldos.grid(row=1,column=2,sticky=W)
                ibldos=Entry(DataFrameLeft,textvariable=self.Dosage,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                ibldos.grid(row=1,column=3)

                iblTb=Label(DataFrameLeft,text=("Tablets Price:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblTb.grid(row=2,column=2,sticky=W)
                iblTb=Entry(DataFrameLeft,textvariable=self.price,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                iblTb.grid(row=2,column=3)

                iblprod=Label(DataFrameLeft,text=("Product QT:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblprod.grid(row=3,column=2,sticky=W)
                iblprod=Entry(DataFrameLeft,textvariable=self.ProductQt,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"))
                iblprod.grid(row=3,column=3)

        #*********************************Images**************************
                img2=Image.open("D:\Project\Inget.jpg")
                img2=img2.resize((150,135),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)
                b1=Button(self.root,image=self.photoimg2,borderwidth=0)
                b1.place(x=480,y=300)  
                
                img3=Image.open("D:\Project\Med.jpg")
                img3=img3.resize((150,135),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)
                b1=Button(self.root,image=self.photoimg3,borderwidth=0)
                b1.place(x=635,y=300) 

                img4=Image.open("D:\Project\Capsule.jpg")
                img4=img4.resize((135,135),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)
                b1=Button(self.root,image=self.photoimg4,borderwidth=0)
                b1.place(x=790,y=300) 
                
        # **********************************DataFrame Right********************************
                
                DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Add New Medicine",
                                        fg="Darkblue",font=("Arial",12,"bold"))
                DataFrameRight.place(x=900,y=5,width=550,height=350)

                img5=Image.open("D:\Project\Presc.jpg")
                img5=img5.resize((200,90),Image.ANTIALIAS)
                self.photoimg5=ImageTk.PhotoImage(img5)
                b1=Button(self.root,image=self.photoimg5,borderwidth=0)
                b1.place(x=950,y=170)

                img6=Image.open("D:\Project\Doct.jpg")
                img6=img6.resize((165,90),Image.ANTIALIAS)
                self.photoimg6=ImageTk.PhotoImage(img6)
                b1=Button(self.root,image=self.photoimg6,borderwidth=0)
                b1.place(x=1100,y=170)

                img7=Image.open("D:\Project\shop.jpg")
                img7=img7.resize((200,150),Image.ANTIALIAS)
                self.photoimg7=ImageTk.PhotoImage(img7)
                b1=Button(self.root,image=self.photoimg7,borderwidth=0)
                b1.place(x=1270,y=160)

                iblrefno=Label(DataFrameRight,text=("Reference No:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblrefno.place(x=0,y=100)
                iblprod=Entry(DataFrameRight,textvariable=self.refMed_var,bd=2,relief=RIDGE,width=14,font=("arial",15,"bold"))
                iblprod.place(x=135,y=100)

                iblrefno=Label(DataFrameRight,text=("Medicine Name:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblrefno.place(x=0,y=130)
                iblprod=Entry(DataFrameRight,textvariable=self.addMed_var,bd=2,relief=RIDGE,width=14,font=("arial",15,"bold"))
                iblprod.place(x=135,y=130)

        #************************************SideFrame********************
                side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="White")
                side_frame.place(x=0,y=160,width=294,height=160)

                sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
                sc_x.pack(side=BOTTOM,fill=X)
                sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
                sc_y.pack(side=RIGHT,fill=Y)

                self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
                sc_x.config(command=self.medicine_table.xview)
                sc_y.config(command=self.medicine_table.yview)

                self.medicine_table.heading("ref",text="Ref")
                self.medicine_table.heading("medname",text="Medicine Name")

                self.medicine_table["show"]="headings"
                self.medicine_table.pack(fill=BOTH,expand=1)

                self.medicine_table.column("ref",width=100)
                self.medicine_table.column("medname",width=100)

                self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        #*********************************Medicine AddButtons*****************************************
                
                down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkblue")
                down_frame.place(x=330,y=150,width=135,height=165)

                btnAddMed=Button(down_frame,command=self.AddMed,text=("ADD"),font=("Arial",12,"bold"),width=12,bg="lime",fg="white",pady=4.3)
                btnAddMed.grid(row=0,column=0)

                btnUpdateMed=Button(down_frame,command=self.UpdateMed,text=("UPDATE"),font=("Arial",12,"bold"),width=12,bg="darkred",fg="white",pady=4.3)
                btnUpdateMed.grid(row=1,column=0)
 
                btnDeleteMed=Button(down_frame,command=self.DeleteMed,text=("DELETE"),font=("Arial",12,"bold"),width=12,bg="purple",fg="white",pady=4.3)
                btnDeleteMed.grid(row=2,column=0)

                btnClearMed=Button(down_frame,command=self.ClearMed,text=("CLEAR"),font=("Arial",12,"bold"),width=12,bg="orange",fg="white",pady=4.3)
                btnClearMed.grid(row=3,column=0)
        
        #********************************FrameDetails********************************************************

                framedetails=Frame(self.root,bd=15,relief=RIDGE)
                framedetails.place(x=0,y=580,width=1530,height=210)

                Table_frame=Frame(framedetails,bd=15,relief=RIDGE)
                Table_frame.place(x=0,y=1,width=1500,height=180)
                
                scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
                scroll_y.pack(side=RIGHT,fill=Y)

                self.pharmacy_table=ttk.Treeview(Table_frame,columns=("ref_no","companyname","TypeMed","Medicinename","LotNo","IssueDate",
                                                                "ExpDate","Symptom","SideEff","Precaution","Dosage","price","ProductQt")
                                                                ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.pharmacy_table.xview)
                scroll_x.config(command=self.pharmacy_table.xview)

                self.pharmacy_table.heading("ref_no",text="Ref")
                self.pharmacy_table.heading("companyname",text="Comapany Name")
                self.pharmacy_table.heading("TypeMed",text="Type")
                self.pharmacy_table.heading("Medicinename",text="MedicineName")
                self.pharmacy_table.heading("LotNo",text="Lot No")
                self.pharmacy_table.heading("IssueDate",text="Issue Date")
                self.pharmacy_table.heading("ExpDate",text="Exp Date")
                self.pharmacy_table.heading("Symptom",text="Symptom")
                self.pharmacy_table.heading("SideEff",text="Side Effect")
                self.pharmacy_table.heading("Precaution",text="Precaution")
                self.pharmacy_table.heading("Dosage",text="Dosage")
                self.pharmacy_table.heading("price",text="price")
                self.pharmacy_table.heading("ProductQt",text="ProductQt")
                self.pharmacy_table["show"]="headings"
                self.pharmacy_table.pack(fill=BOTH,expand=1)

                self.pharmacy_table.column("ref_no",width=20)
                self.pharmacy_table.column("companyname",width=20)
                self.pharmacy_table.column("TypeMed",width=20)
                self.pharmacy_table.column("Medicinename",width=20)
                self.pharmacy_table.column("LotNo",width=20)
                self.pharmacy_table.column("IssueDate",width=20)
                self.pharmacy_table.column("ExpDate",width=20)
                self.pharmacy_table.column("Symptom",width=20)
                self.pharmacy_table.column("SideEff",width=20)
                self.pharmacy_table.column("Precaution",width=20)
                self.pharmacy_table.column("Dosage",width=20)
                self.pharmacy_table.column("price",width=20)
                self.pharmacy_table.column("ProductQt",width=20)
                self.fetch_dataMed()
                self.Fetch_data()
                self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.pharmacy_table.bind("<<ComboboxSelected>>",self.get_cursor)
                
        
#***************************Add Medicine Funtionality**********************************************************
        def AddMed(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into med(RefName,MedName) values(%s,%s)",( 
                                                                self.refMed_var.get(),
                                                                self.addMed_var.get()


                                                                ))
                conn.commit()
                self.fetch_dataMed()
                self.Medget_cursor()
                conn.close()
                messagebox.showinfo("Success","Medicine Added")

        def fetch_dataMed(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from med")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.medicine_table.delete(*self.medicine_table.get_children())
                        for i in rows:
                                self.medicine_table.insert("",END,values=i)
                        conn.commit()
                conn.close()
#********************************MedDatacursor*******************************************************

        def Medget_cursor(self,event=""):
                cursor_row=self.medicine_table.focus()
                content=self.medicine_table.item(cursor_row)
                row=content["values"]
                self.refMed_var.set(row[0])
                self.addMed_var.set(row[1])
        
        def UpdateMed(self):
                if self.refMed_var.get()=="" or self.addMed_var.get()=="":
                        messagebox.showerror("Error","All fields are Required")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                        my_cursor=conn.cursor()
                        my_cursor.execute("Update med set MedName=%s where RefName=%s",(
                                                                                        self.addMed_var.get(),
                                                                                        self.refMed_var.get(),
                                                                                  ))   
                        my_cursor.execute("Update med set RefName=%s where MedName=%s",(
                                                                                        self.refMed_var.get(),
                                                                                        self.addMed_var.get(),
                                                                                        
                                                                                  ))                                                          
                        conn.commit()
                        self.fetch_dataMed()
                        conn.close() 
                        messagebox.showinfo("Success","Medicine has been Updated")
        
                

        def DeleteMed(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()

                sql="delete from med where RefName=%s"
                val=(self.refMed_var.get(),)
                my_cursor.execute(sql,val)

                conn.commit()
                self.fetch_dataMed()
                conn.close()
                messagebox.showinfo("Success","Medicine has been Deleted")

        def ClearMed(self):
                self.refMed_var.set("")
                self.addMed_var.set("")    

#**************************Main Table*************************************************************

        def AddData(self):
                if self.ref_no_var.get()=="" or self.LotNo.get()=="":
                        messagebox.showerror("Error","All feilds are required")
                elif (self.IssueDate.get() < self.ExpDate.get()):
                                messagebox.showerror("Failed","Please Enter valid date")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                        my_cursor=conn.cursor()   
                        my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.ref_no_var.get(),
                                                                                        self.campanyName.get(),
                                                                                        self.TypeMed.get(),
                                                                                        self.Medicinename.get(),
                                                                                        self.LotNo.get(),
                                                                                        self.IssueDate.get(),
                                                                                        self.ExpDate.get(),
                                                                                        self.Symptom.get(),
                                                                                        self.SideEff.get(),
                                                                                        self.Precaution.get(),
                                                                                        self.Dosage.get(),
                                                                                        self.price.get(),
                                                                                        self.ProductQt.get()
                                                                                  ))                                                           
                        conn.commit()
                        self.Fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Details has been Added")


        def Fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor() 
                my_cursor.execute("Select * from pharmacy")
                row=my_cursor.fetchall()
                if len(row)!=0:
                        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                        for i in row:
                                self.pharmacy_table.insert("",END,values=i)
                        conn.commit()
                conn.close()

        def get_cursor(self,event=""):
                cursor_row=self.pharmacy_table.focus()
                content=self.pharmacy_table.item(cursor_row)
                row=content["values"]

                self.ref_no_var.set(row[0]),
                self.campanyName.set(row[1]),
                self.TypeMed.set(row[2]),
                self.Medicinename.set(row[3]),
                self.LotNo.set(row[4]),
                self.IssueDate.set(row[5]),
                self.ExpDate.set(row[6]),
                self.Symptom.set(row[7]),
                self.SideEff.set(row[8]),
                self.Precaution.set(row[9]),
                self.Dosage.set(row[10]),
                self.price.set(row[11]),
                self.ProductQt.set(row[12])

        def Update(self):
                if self.ref_no_var.get()=="" or self.LotNo.get()=="":
                        messagebox.showerror("Error","All fields are Required")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                        my_cursor=conn.cursor()
                        my_cursor.execute("Update pharmacy set companyname=%s,TypeMed=%s,Medicinenname=%s,LotNo=%s,IssueDate=%s,ExpDate=%s,Symptom=%s,SideEff=%s,Precaution=%s,Dosage=%s,price=%s,ProductQt=%s where Ref_no=%s",(
                                                                                        self.campanyName.get(),
                                                                                        self.TypeMed.get(),
                                                                                        self.Medicinename.get(),
                                                                                        self.LotNo.get(),
                                                                                        self.IssueDate.get(),
                                                                                        self.ExpDate.get(),
                                                                                        self.Symptom.get(),
                                                                                        self.SideEff.get(),
                                                                                        self.Precaution.get(),
                                                                                        self.Dosage.get(),
                                                                                        self.price.get(),
                                                                                        self.ProductQt.get(),
                                                                                        self.ref_no_var.get()
                                                                                  ))                                                           
                        conn.commit()
                        self.Fetch_data()
                        conn.close() 
                        messagebox.showinfo("UPDATE","Record has been Updated")

        def Delete(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()

                sql="delete from Pharmacy where Ref_no=%s"
                val=(self.ref_no_var.get(),)
                my_cursor.execute(sql,val)

                conn.commit()
                self.Fetch_data()
                conn.close()
                messagebox.showinfo("DELETE","Record has been Deleted")

        def ResetData(self):
               # self.ref_no_var.set(r"")
                self.campanyName.set(""),
               # self.TypeMed.set(""),
               # self.Medicinename.set(""),
                self.LotNo.set(""),
                self.IssueDate.set(""),
                self.ExpDate.set(""),
                self.Symptom.set(""),
                self.SideEff.set(""),
                self.Precaution.set(""),
                self.Dosage.set(r""),
                self.price.set(r""),
                self.ProductQt.set(r"")
                

        def SearchDate(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from pharmacy where"+str(self.search_var.get())+"LIKE"+str(self.searchtxt_var.get()+"%"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                        for i in rows:
                                self.pharmacy_table.insert("",END,values=i)
                        conn.commit()
                conn.close()

        def open_registration_window(self):
                self.root.destroy()
                if __name__ =="__main__":  
                        root=Tk()
                        obj=BillingSystem(root)
                        root.mainloop()
                
               

class BillingSystem:
        def __init__(self,root):
                self.root=root
                self.root.title("Pharmacy Managment System")
                self.root.geometry("1550x800+0+0")
#VAriables******************************************
                self.cname=StringVar()
                self.phone=StringVar()
                self.email=StringVar()
                self.billno=StringVar()
                self.price=IntVar()
                self.qty=IntVar()  
                self.MedicineName=StringVar()     
                self.total=IntVar()    
                x=random.randint(1000,9999)
                self.billno.set(str(x))

                global l
                l=[]
#***********************************************************              
                lbltitle=Label(self.root,text="MEDICAL MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                        bg='white',fg="darkblue",font=("times new roman",50,"bold"),padx=2,pady=4)
                lbltitle.pack(side=TOP,fill=X)

                img1=Image.open("D:\Project\logo.jpg")
                img1=img1.resize((80,80),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                b1=Button(self.root,image=self.photoimg1,borderwidth=0)
                b1.place(x=60,y=15)
#********************************Main Frame*************************************
                DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
                DataFrame.place(x=0,y=120,width=1530,height=670)

                
                

#**********************************LEft Farme ************************************
                DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                        fg="Darkblue",font=("Arial",12,"bold"))
                DataFrameLeft.place(x=0,y=5,width=450,height=150)

                iblCust=Label(DataFrameLeft,text=("Customer Name:"),font=("arial",12,"bold"))
                iblCust.grid(row=0,column=0,sticky=W,padx=5,pady=2)       
                iblCust=ttk.Entry(DataFrameLeft,textvariable=self.cname,width=24,font=("arial",13,"bold"))
                iblCust.grid(row=0,column=1,sticky=W,padx=5,pady=2)

                iblPhone=Label(DataFrameLeft,text=("Phone:"),font=("arial",12,"bold"),bd=6)
                iblPhone.grid(row=1,column=0,sticky=W,padx=5,pady=2)       
                iblPhone=ttk.Entry(DataFrameLeft,textvariable=self.phone,width=24,font=("arial",13,"bold"))
                iblPhone.grid(row=1,column=1,sticky=W,padx=5,pady=2)

                iblMail=Label(DataFrameLeft,text=("Email:"),font=("arial",12,"bold"),bd=6)
                iblMail.grid(row=2,column=0,sticky=W,padx=5,pady=2)       
                iblMail=ttk.Entry(DataFrameLeft,textvariable=self.email,width=24,font=("arial",13,"bold"))
                iblMail.grid(row=2,column=1,sticky=W,padx=5,pady=2)



#*****************************Middle Frame***************************************
                DataFrameMiddle=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Product Details",
                                        fg="Darkblue",font=("Arial",12,"bold"))
                DataFrameMiddle.place(x=457,y=5,width=650,height=150)

                iblCust=Label(DataFrameMiddle,text=("Bill No:"),font=("arial",12,"bold"))
                iblCust.grid(row=0,column=0,sticky=W,padx=5,pady=2)       
                iblCust=ttk.Entry(DataFrameMiddle,textvariable=self.billno,width=22,font=("arial",13,"bold"))
                iblCust.grid(row=0,column=1,sticky=W,padx=5,pady=2)
                
                iblMedname=Label(DataFrameMiddle,text=("Medicine Name :"),font=("arial",12,"bold"),padx=2,pady=6)
                iblMedname.grid(row=1,column=0,sticky=W)
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()
                my_cursor.execute("select MedName from med")
                med=my_cursor.fetchall()

                search_comboMedname=ttk.Combobox(DataFrameMiddle,textvariable=self.MedicineName,width=20,font=("arial",13,"bold"),state="readonly")
                search_comboMedname["values"]=med
                search_comboMedname.current(0)
                search_comboMedname.grid(row=1,column=1)

                iblTb=Label(DataFrameMiddle,text=("Tablets Price:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblTb.grid(row=2,column=0,sticky=W)
                iblTb=Entry(DataFrameMiddle,textvariable=self.price,bd=2,relief=RIDGE,width=22,font=("arial",13,"bold"))
                iblTb.grid(row=2,column=1)


                iblTb=Label(DataFrameMiddle,text=("Quantity:"),font=("arial",12,"bold"),padx=4,pady=6)
                iblTb.grid(row=0,column=3,sticky=W)
                iblTb=Entry(DataFrameMiddle,textvariable=self.qty,bd=2,relief=RIDGE,width=19,font=("arial",13,"bold"))
                iblTb.grid(row=0,column=4)
#*******************************Middleframe1************************************************

                DataFrameMiddle1=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,
                                        fg="Darkblue",font=("Arial",12,"bold"))
                DataFrameMiddle1.place(x=0,y=170,width=1110,height=400)
               
                
                sc_y=ttk.Scrollbar(DataFrameMiddle1,orient=VERTICAL)
                self.textarea=Text(DataFrameMiddle1,yscrollcommand=sc_y.set,bg="white",font=("arial",13,"bold"),width=65,fg="blue")
                sc_y.pack(side=RIGHT,fill=Y)
                sc_y.config(command=self.textarea.yview)
                self.textarea.pack(fill=Y,expand=1)

                

                

#*******************************BottomButtons**********************************************
                 
                ButtonFrame1=Frame(self.root,bd=15,relief=RIDGE,padx=20)
                ButtonFrame1.place(x=25,y=710,width=1122,height=65)

                btnAddMed=Button(ButtonFrame1,command=self.additem,text=("ADD TO CART"),font=("Arial",12,"bold"),width=12,bg="lime",fg="white",pady=4.3,padx=60)
                btnAddMed.grid(row=0,column=0)

                btnUpdateMed=Button(ButtonFrame1,command=self.gen_bill,text=("GENERATE BILL"),font=("Arial",12,"bold"),width=12,bg="darkred",fg="white",pady=4.3,padx=60)
                btnUpdateMed.grid(row=0,column=1)
 
                btnDeleteMed=Button(ButtonFrame1,command=self.Save,text=("SAVE"),font=("Arial",12,"bold"),width=12,bg="purple",fg="white",pady=4.3,padx=60)
                btnDeleteMed.grid(row=0,column=2)

                btnClearMed=Button(ButtonFrame1,command=self.Exit,text=("EXIT"),font=("Arial",12,"bold"),width=12,bg="orange",fg="white",pady=4.3,padx=60)
                btnClearMed.grid(row=0,column=3)
                self.welcome()

                self.l=[]
                

        def welcome(self):
                self.textarea.delete(1.0,END)
                self.textarea.insert(END,"\t\t\tWelcome to Medical Store")
                self.textarea.insert(END,f"\nBill NO: {self.billno.get()}")
                self.textarea.insert(END,f"\nCustomer Name: {self.cname.get()}")
                self.textarea.insert(END,f"\nPhone Number: {self.phone.get()}")
                self.textarea.insert(END,f"\nEmail: {self.email.get()}")
                self.textarea.insert(END,f"\n==========================================================")
                self.textarea.insert(END,f"\nMedicine Name\t\t\t\tQty\t\t\tPrice")
                self.textarea.insert(END,f"\n==========================================================")

        def additem(self):
                self.n=self.price.get()
                self.m=self.qty.get()*self.n
                l.append(self.m)
                
                if self.MedicineName==" ":
                        messagebox.showerror("Error!","Please select the medicine name")
                else:
                        self.textarea.insert(END,f"\n{self.MedicineName.get()}\t\t\t\t{self.qty.get()}\t\t\t{self.m}")
                        

        def gen_bill(self):
                if self.MedicineName==" ":
                        messagebox.showerror("Error!","Please select the medicine name")
                else:
                        text=self.textarea.get(9.0,(9.0+float(len(l))))
                        self.welcome()
                        self.textarea.insert(END,text)
                        self.textarea.insert(END,f"\nTotal Amount:\t{sum(l)}")

        def Save(self):
                op=messagebox.askyesno("Save Bill","Do you want to save bill")
                if op>0:
                        self.bill_data=self.textarea.get(1.0,END)
                        f1=open("Bills/"+str(self.billno.get())+"txt",'w')
                        f1.write(self.bill_data)
                        op=messagebox.askyesno("Save Bill","Bill has been Save ")
                        f1.close()

        def Exit(self):
                op=messagebox.askyesno("Save Bill","Do you want to Exit")
                if op>0:
                        self.root.destroy()


if __name__ =="__main__":  
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
