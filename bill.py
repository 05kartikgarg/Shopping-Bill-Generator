from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bgcolor="#074463"
        title=Label(self.root,text="Billing Area",bd=12,relief=GROOVE,bg=bgcolor,fg="white",font=("times new roman",15,"bold")).pack(fill=X)
        ################################################################################################################################################33
        #cosmetics
        self.bath=IntVar()
        self.cream=IntVar()
        self.wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()
        #Grocery
        self.rice=IntVar()
        self.oil=IntVar()
        self.dal=IntVar()
        self.wht=IntVar()
        self.sugr=IntVar()
        self.tea=IntVar()
        #cold drnk
        self.mz=IntVar()
        self.coc=IntVar()
        self.frot=IntVar()
        self.thums=IntVar()
        self.lim=IntVar()
        self.spt=IntVar()
        # Total price and tax
        self.cosmeticp=StringVar()
        self.groceryp=StringVar()
        self.coldp=StringVar()
        self.cosmetict=StringVar()
        self.groceryt=StringVar()
        self.coldt=StringVar()
        #customer
        self.cname=StringVar()
        self.cphn=StringVar()
        self.billn=StringVar()
        x=random.randint(1000,9999)
        self.billn.set(x)
        self.serchb=StringVar()

        
        
        
        ####################################################################################################################################################


        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bgcolor)
        F1.place(x=0,y=50,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cnametxt=Entry(F1,width=20,textvariable=self.cname,font=("arial",15),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5)

        cphn_lbl=Label(F1,text="Customer Mobile No.",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphntxt=Entry(F1,width=20,textvariable=self.cphn,font=("arial",15),bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5)

        cbill_lbl=Label(F1,text="Bill No.",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbilltxt=Entry(F1,width=20,textvariable=self.serchb,font=("arial",15),bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5)

        search=Button(F1,text="Search",command=self.find_bill,font=("times new roman",15,"bold")).grid(row=0,column=6,pady=5,padx=20)

        ############################################cosmetics############################

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bgcolor)
        F2.place(x=4,y=135,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.bath,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cream_lbl=Label(F2,text="Face Cream",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cream_txt=Entry(F2,width=10,textvariable=self.cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        wash_lbl=Label(F2,text="Face Wash",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        wash_txt=Entry(F2,width=10,textvariable=self.wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        spray_lbl=Label(F2,text="Hair Spray",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        spray_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        gel_lbl=Label(F2,text="Hair Gel",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        gel_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        lotion_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

    ####################################################### Grocery ###########################################################################

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bgcolor)
        F3.place(x=340,y=135,width=325,height=380)

        rice_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        oil_lbl=Label(F3,text="Food Oil",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        oil_txt=Entry(F3,width=10,textvariable=self.oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        dal_lbl=Label(F3,text="Daal",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        dal_txt=Entry(F3,width=10,textvariable=self.dal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        wht_lbl=Label(F3,text="Wheat",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wht_txt=Entry(F3,width=10,textvariable=self.wht,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sug_lbl=Label(F3,text="Sugar",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sug_txt=Entry(F3,width=10,textvariable=self.sugr,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_lbl=Label(F3,text="Tea",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         ####################################################### cold driks###########################################################################

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bgcolor)
        F4.place(x=675,y=135,width=325,height=380)

        mz_lbl=Label(F4,text="Maza",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        mz_txt=Entry(F4,width=10,textvariable=self.mz,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        coc_lbl=Label(F4,text="Coca Cola",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coc_txt=Entry(F4,width=10,textvariable=self.coc,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        frot_lbl=Label(F4,text="Frooti",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frot_txt=Entry(F4,width=10,textvariable=self.frot,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        thms_lbl=Label(F4,text="Thumbs Up",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        thms_txt=Entry(F4,width=10,textvariable=self.thums,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        lim_lbl=Label(F4,text="Limka",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        lim_txt=Entry(F4,width=10,textvariable=self.lim,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        spt_lbl=Label(F4,text="Sprite",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        spt_txt=Entry(F4,width=10,textvariable=self.spt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ####################################################### Bill Area ##########################################################################

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=135,width=340,height=380)
        billtitle=Label(F5,text="Bill Preview",font=("times new roman",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)

        scrolly=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.txtarea.yview)
        self.txtarea.pack()

        ################################################### Button Area ##########################################################################

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bgcolor)
        F6.place(x=0,y=525,relwidth=1,height=170)

        m1lbl=Label(F6,text="Total Cosmetics Price",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=0,column=0,padx=20,pady=5,sticky="w")
        m1txt=Entry(F6,width=18,textvariable=self.cosmeticp,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2lbl=Label(F6,text="Total Grocery Price",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=1,column=0,padx=20,pady=5,sticky="w")
        m2txt=Entry(F6,width=18,textvariable=self.groceryp,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3lbl=Label(F6,text="Total Cold Drink Price",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=2,column=0,padx=20,pady=5,sticky="w")
        m3txt=Entry(F6,width=18,textvariable=self.coldp,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1lbl=Label(F6,text=" Cosmetics Tax",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=0,column=2,padx=20,pady=5,sticky="w")
        c1txt=Entry(F6,width=18,textvariable=self.cosmetict,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2lbl=Label(F6,text=" Grocery Tax",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=1,column=2,padx=20,pady=5,sticky="w")
        c2txt=Entry(F6,width=18,textvariable=self.groceryt,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3lbl=Label(F6,text=" Cold Drink Tax",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=2,column=2,padx=20,pady=5,sticky="w")
        c3txt=Entry(F6,width=18,textvariable=self.coldt,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btnF=Frame(F6,bd=7,relief=GROOVE)
        btnF.place(x=750,width=575,height=115)

        totalbtn=Button(btnF,text="Total",command=self.total,bg="cadetblue",fg="white",bd=4,pady=15,width=11,font=("arial 12 bold")).grid(row=0,column=0,padx=5,pady=15)
        Gbillbtn=Button(btnF,text="Generate Bill",command=self.billpreview,bg="cadetblue",fg="white",bd=4,pady=15,width=11,font=("arial 12 bold")).grid(row=0,column=1,padx=5,pady=15)
        Clearbtn=Button(btnF,text="Clear",bg="cadetblue",fg="white",bd=4,pady=15,width=11,font=("arial 12 bold")).grid(row=0,column=2,padx=5,pady=15)
        Exitbtn=Button(btnF,text="Exit",command=self.Exit,bg="cadetblue",fg="white",bd=4,pady=15,width=11,font=("arial 12 bold")).grid(row=0,column=3,padx=5,pady=15)
        self.welcome()
        

    def total(self):

        self.cbp=self.bath.get()*40
        self.ccp=self.cream.get()*120
        self.cwp=self.wash.get()*60
        self.csp=self.spray.get()*180
        self.cgp=self.gel.get()*140
        self.clp=self.lotion.get()*180
        self.tcosp=float(
                            (self.cbp)+
                            (self.ccp)+
                            (self.cwp)+
                            (self.csp)+
                            (self.cgp)+
                            (self.clp)
                        )
        self.cosmeticp.set(str(self.tcosp))
        self.cosmetic_tax=round(self.tcosp*0.12,2)
        self.cosmetict.set(str(self.cosmetic_tax))

        self.grp=self.rice.get()*100
        self.gop=self.oil.get()*200
        self.gdp=self.dal.get()*80
        self.gwp=self.wht.get()*30
        self.gsp=self.sugr.get()*50
        self.gtp=self.tea.get()*50
        self.tgp=float(
                            (self.grp)+
                            (self.gop)+
                            (self.gdp)+
                            (self.gwp)+
                            (self.gsp)+
                            (self.gtp)
                        )
        self.groceryp.set(str(self.tgp))
        self.grocery_tax=round(self.tgp*0.8,2)
        self.groceryt.set(str(self.grocery_tax))

        self.dmp=self.mz.get()*60
        self.dcp=self.coc.get()*70
        self.dfp=self.frot.get()*40
        self.dtp=self.thums.get()*40
        self.dlp=self.lim.get()*50
        self.dsp=self.spt.get()*50
        self.tcoldp=float(
                            (self.dmp)+
                            (self.dcp)+
                            (self.dfp)+
                            (self.dtp)+
                            (self.dlp)+
                            (self.dsp)
                        )
        self.coldp.set(str(self.tcoldp))
        self.drink_tax=round(self.tcoldp*0.18,2)
        self.coldt.set(str(self.drink_tax))

        self.total_bill=(   self.tcosp+
                            self.tgp+
                            self.tcoldp+
                            self.drink_tax+
                            self.cosmetic_tax+
                            self.grocery_tax
                         )

    def welcome(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Chinu Retails\n")
        self.txtarea.insert(END,f"\nBill No:{self.billn.get()}")
        self.txtarea.insert(END,f"\nCustomer Name:{self.cname.get()}")
        self.txtarea.insert(END,f"\nCustomer Mobile No:{self.cphn.get()}")
        self.txtarea.insert(END,"\n*************************************")
        self.txtarea.insert(END,f"\nProduct\t\tQty\t\tPrice")
        self.txtarea.insert(END,"\n*************************************")
       
    def billpreview(self):
        self.welcome()
        #cosmetics
        if self.bath.get()!=0:
            self.txtarea.insert(END,f"\n Bath Soap\t\t{self.bath.get()}\t\t{self.cbp}")
        if self.cream.get()!=0:
            self.txtarea.insert(END,f"\n Face Cream\t\t{self.cream.get()}\t\t{self.ccp}")
        if self.wash.get()!=0:
            self.txtarea.insert(END,f"\n Face Wash\t\t{self.wash.get()}\t\t{self.cwp}")
        if self.spray.get()!=0:
            self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.csp}")
        if self.gel.get()!=0:
            self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gel.get()}\t\t{self.cgp}")
        if self.lotion.get()!=0:
            self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.clp}")

        #Grocery
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n Bath Soap\t\t{self.rice.get()}\t\t{self.grp}")
        if self.oil.get()!=0:
            self.txtarea.insert(END,f"\n Food Oil\t\t{self.oil.get()}\t\t{self.gop}")
        if self.dal.get()!=0:
            self.txtarea.insert(END,f"\n Dal\t\t{self.dal.get()}\t\t{self.gdp}")
        if self.wht.get()!=0:
            self.txtarea.insert(END,f"\n Wheat\t\t{self.wht.get()}\t\t{self.gwp}")
        if self.sugr.get()!=0:
            self.txtarea.insert(END,f"\n Sugar\t\t{self.sugr.get()}\t\t{self.gsp}")
        if self.tea.get()!=0:
            self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.gtp}")

         #Cold Drink
        if self.mz.get()!=0:
            self.txtarea.insert(END,f"\n Maza\t\t{self.mz.get()}\t\t{self.dmp}")
        if self.coc.get()!=0:
            self.txtarea.insert(END,f"\n Coca-Cola\t\t{self.coc.get()}\t\t{self.dcp}")
        if self.frot.get()!=0:
            self.txtarea.insert(END,f"\n Frooti\t\t{self.frot.get()}\t\t{self.dfp}")
        if self.thums.get()!=0:
            self.txtarea.insert(END,f"\n Thumbs-Up\t\t{self.thums.get()}\t\t{self.dtp}")
        if self.lim.get()!=0:
            self.txtarea.insert(END,f"\n Limca\t\t{self.lim.get()}\t\t{self.dlp}")
        if self.spt.get()!=0:
            self.txtarea.insert(END,f"\n Sprite\t\t{self.spt.get()}\t\t{self.dsp}")

        self.txtarea.insert(END,"\n-------------------------------------")
        if self.cosmetict.get()!="0.0":
            self.txtarea.insert(END,f"\nCosmetics Tax\t\t\t\t{self.cosmetict.get()}")
        if self.groceryt.get()!="0.0":
            self.txtarea.insert(END,f"\nGrocery Tax\t\t\t\t{self.groceryt.get()}")
        if self.coldt.get()!="0.0":
            self.txtarea.insert(END,f"\nCold Drink Tax\t\t\t\t{self.coldt.get()}")
        self.txtarea.insert(END,"\n-------------------------------------")
        self.txtarea.insert(END,f"\n Total Amount\t\t\t{self.total_bill}")
        self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save Bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open(str(self.billn.get())+'.txt',"w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir():
            if i.split('.')[0]==self.serchb.get():
                f1=open(f"{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
            else:
                messagebox.showerror("Error","Bill not Found!!")

    def Exit(self):
        op=messagebox.askyesno("Exit","Do you really want to quit?")
        if op>0:
            self.root.destroy()
       






root=Tk()
obj=Bill_app(root)
root.mainloop()