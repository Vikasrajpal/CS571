from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("IIT Mandi Food Corner")
        title=Label(self.root,text="IIT Mandi Food Corner",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
    #variables
        self.burger=IntVar()
        self.noodles=IntVar()
        self.spring_roll=IntVar()
        self.egg_roll=IntVar()
        self.chocolate_shake=IntVar()
        self.silk=IntVar()
        self.momos=IntVar()
        self.maggi=IntVar()
        self.pasta=IntVar()
        self.rice=IntVar()
        self.sauce=IntVar()
        self.sugar=IntVar()
        self.daal=IntVar()
        self.tea=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #customer details label frame
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)
        
        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)
        
        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)
        
        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)
        
        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)
        
        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #Fast_Food label frame
        Fast_Food=LabelFrame(self.root,text="Fast_Food",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        Fast_Food.place(x=5,y=180,height=380,width=325)
        
        item1=Label(Fast_Food,text="Burger(25Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(Fast_Food,borderwidth=2,width=15,textvariable=self.burger).grid(row=0,column=1,padx=10)

        item2=Label(Fast_Food,text="Noodles(40Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(Fast_Food,borderwidth=2,width=15,textvariable=self.noodles).grid(row=1,column=1,padx=10)

        item3=Label(Fast_Food,text="Spring_Roll(30Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(Fast_Food,borderwidth=2,width=15,textvariable=self.spring_roll).grid(row=2,column=1,padx=10)

        item4=Label(Fast_Food,text="Egg_Roll(20Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(Fast_Food,borderwidth=2,width=15,textvariable=self.egg_roll).grid(row=3,column=1,padx=10)

        item5=Label(Fast_Food,text="Chocolate Shake(70Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(Fast_Food,borderwidth=2,width=15,textvariable=self.chocolate_shake).grid(row=4,column=1,padx=10)

        item6=Label(Fast_Food,text="Dairy Milk Silk(60Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(Fast_Food,borderwidth=2,width=15,textvariable=self.silk).grid(row=5,column=1,padx=10)

        item7=Label(Fast_Food,text="Momos(30Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(Fast_Food,borderwidth=2,width=15,textvariable=self.momos).grid(row=6,column=1,padx=10)
        #GROCERY
        grocery=LabelFrame(self.root,text="Grocery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        grocery.place(x=340,y=180,height=380,width=325)

        item8=Label(grocery,text="Maggi(100g)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.maggi).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="Pasta(100g)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Rice(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.rice).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Sauce(1ltr)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.sauce).grid(row=3,column=1,padx=10)

        item12=Label(grocery,text="Sugar(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.sugar).grid(row=4,column=1,padx=10)

        item13=Label(grocery,text="Daal(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.daal).grid(row=5,column=1,padx=10)

        item14=Label(grocery,text="Tea powder(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.tea).grid(row=6,column=1,padx=10)
        #billarea
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)
        
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
        
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #billing menu
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)
        
        total_Fast_Food=Label(billing_menu,text="Total Fast_Food Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_Fast_Food_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)
        
        total_grocery=Label(billing_menu,text="Total Grocery Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)

        tax_Fast_Food=Label(billing_menu,text="Fast_Food Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_Fast_Food_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)
        
        tax_grocery=Label(billing_menu,text="Grocery Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)

        
        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)
        
        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.bu=self.burger.get()*25
    self.no=self.noodles.get()*40
    self.sr=self.spring_roll.get()*30
    self.er=self.egg_roll.get()*20
    self.cs=self.chocolate_shake.get()*70
    self.si=self.silk.get()*60
    self.mo=self.momos.get()*30
    total_Fast_Food_price=(
                self.bu+
                self.no+
                self.sr+
                self.er+
                self.cs+
                self.si+
                self.mo)          
    self.total_sna.set(str(total_Fast_Food_price)+" Rs")
    self.a.set(str(round(total_Fast_Food_price*0.05,3))+" Rs")

    self.ma=self.maggi.get()*12
    self.pa=self.pasta.get()*15
    self.ri=self.rice.get()*50
    self.sa=self.sauce.get()*11
    self.su=self.sugar.get()*45
    self.da=self.daal.get()*110
    self.te=self.tea.get()*150
    total_grocery_price=(
        self.ma+
        self.pa+
        self.ri+
        self.sa+
        self.su+
        self.da+
        self.te)
        
    self.total_gro.set(str(total_grocery_price)+" Rs")
    self.b.set(str(round(total_grocery_price*0.01,3))+" Rs")

    self.total_all_bill=(total_Fast_Food_price+
                total_grocery_price+
                (round(total_grocery_price*0.01,3))+
                (round(total_Fast_Food_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO FOOD CORNER\n\tPhone-No. 9649379348")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.burger.get()!=0:
        self.txtarea.insert(END,f"burger\t\t {self.burger.get()}\t{self.bu}\n")
    if self.noodles.get()!=0:
        self.txtarea.insert(END,f"noodles\t\t {self.noodles.get()}\t{self.no}\n")
    if self.spring_roll.get()!=0:
        self.txtarea.insert(END,f"spring_roll\t\t {self.spring_roll.get()}\t{self.sr}\n")
    if self.egg_roll.get()!=0:
        self.txtarea.insert(END,f"egg_roll\t\t {self.egg_roll.get()}\t{self.er}\n")
    if self.chocolate_shake.get()!=0:
        self.txtarea.insert(END,f"chocolate_shake\t\t {self.chocolate_shake.get()}\t{self.cs}\n")
    if self.silk.get()!=0:
        self.txtarea.insert(END,f"silk\t\t {self.silk.get()}\t{self.si}\n")
    if self.momos.get()!=0:
        self.txtarea.insert(END,f"momos\t\t {self.momos.get()}\t{self.mo}\n")
    if self.maggi.get()!=0:
        self.txtarea.insert(END,f"maggi\t\t {self.maggi.get()}\t{self.ma}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.rice.get()!=0:
        self.txtarea.insert(END,f"rice\t\t {self.rice.get()}\t{self.ri}\n")
    if self.sauce.get()!=0:
        self.txtarea.insert(END,f"sauce\t\t {self.sauce.get()}\t{self.sa}\n")
    if self.sugar.get()!=0:
        self.txtarea.insert(END,f"sugar\t\t {self.sugar.get()}\t{self.su}\n")
    if self.daal.get()!=0:
        self.txtarea.insert(END,f"daal\t\t {self.daal.get()}\t{self.da}\n")
    if self.tea.get()!=0:
        self.txtarea.insert(END,f"tea\t\t {self.tea.get()}\t{self.te}\n")
        
    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Fast_Food Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Grocery Tax : {self.b.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.burger.set(0)
        self.noodles.set(0)
        self.Spring_Rolloll.set(0)
        self.Egg_Roll.set(0)
        self.Chocolate_Shake.set(0)
        self.silk.set(0)
        self.Momos.set(0)
        self.maggi.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.dal.set(0)
        self.tea.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()
            
root=Tk()
obj=Bill_App(root)
root.mainloop()
    
