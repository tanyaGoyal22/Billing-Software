from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x800+0+0")
        self.root.title("Billing Software")
        bg_color="#003399"
        title=Label(self.root,text = "Billing Software",border= 12,relief = GROOVE,bg=bg_color,fg ="yellow",font=("baloo bhai",25,"bold"),pady=2).pack(fill = X)
        #========variables======
        #===========COMETICS VARIABLES=====
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_gel=IntVar()
        self.hair_oil=IntVar()
        self.body_lotion=IntVar()

        #============GROCERY VARIABLES======
        self.rice=IntVar()
        self.cooking_oil=IntVar()
        self.wheat_flour=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.biscuits=IntVar()

        #========FASHION VARIABLES============
        self.handbags=IntVar()
        self.sunglasses=IntVar()
        self.foot_wear=IntVar()
        self.luggage=IntVar()
        self.watch=IntVar()
        self.jewellery=IntVar()

        #======TOTAL PRODUCT PRICE & TAX VARIABLES=====
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.fashion_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.fashion_tax=StringVar()

        #========CUSTOMER=============
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()




        #=========Customer Details Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("baloo bhai",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=70,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font =("baloo bhai",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="inherit 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font =("baloo bhai",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="inherit 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="white",font =("baloo bhai",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="inherit 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text ="Search",command=self.find_bill,width = 15,bd=7,font="inherit 12 bold").grid(row=0,column=6,padx =10,pady=10)

        #==========Cosmetics Frame ============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("baloo bhai",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=315,height=365)

        bath_lbl=Label(F2,text="Soap",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2,text="Face Wash",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hairg_lbl=Label(F2,text="Hair Gel",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hairg_txt=Entry(F2,width=10,textvariable=self.hair_gel,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_o_lbl=Label(F2,text="Hair Oil",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_o_txt=Entry(F2,width=10,textvariable=self.hair_oil,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_l_lbl=Label(F2,text="Body Lotion",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_l_txt=Entry(F2,width=10,textvariable=self.body_lotion,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #==========Grocery Frame ============
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("baloo bhai",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=325,y=170,width=315,height=365)

        g1_lbl=Label(F3,text="Rice",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Cooking Oil",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.cooking_oil,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Wheat Flour",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.wheat_flour,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Sugar",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.sugar,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Tea",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.tea,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Biscuits",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.biscuits,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #==========Fashion Frame ============
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Fashion",font=("baloo bhai",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=645,y=170,width=315,height=365)

        fa1_lbl=Label(F4,text="Handbags",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        fa1_txt=Entry(F4,width=10,textvariable=self.handbags,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        fa2_lbl=Label(F4,text="SunGlasses",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        fa2_txt=Entry(F4,width=10,textvariable=self.sunglasses,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        fa3_lbl=Label(F4,text="Footwear",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        fa3_txt=Entry(F4,width=10,textvariable=self.foot_wear,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        fa4_lbl=Label(F4,text="Luggage",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        fa4_txt=Entry(F4,width=10,textvariable=self.luggage,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        fa5_lbl=Label(F4,text="Watch",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        fa5_txt=Entry(F4,width=10,textvariable=self.watch,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        fa6_lbl=Label(F4,text="Jewellery",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        fa6_txt=Entry(F4,width=10,textvariable=self.jewellery,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #========Bill Area=====
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=965,y=170,width=330,height=365)
        bill_title=Label(F5,text="Bill Area",font="inherit 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=======Button Frame======
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("baloo bhai",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=540,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Fashion Price",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.fashion_price,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Fashion Tax",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.fashion_tax,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=690,width=560,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",width=11,font="inherit 13 bold",bd=5,pady=13).grid(row=0,column=0,padx=5,pady=5)
        gb_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",width=11,font="inherit 13 bold",bd=5,pady=13).grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",width=11,font="inherit 13 bold",bd=5,pady=13).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",width=11,font="inherit 13 bold",bd=5,pady=13).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()


    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*100
        self.c_hg_p=self.hair_gel.get()*80
        self.c_ho_p=self.hair_oil.get()*60
        self.c_bl_p=self.body_lotion.get()*300
        self.total_cosmetic_price=float(self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hg_p+
                                    self.c_ho_p+
                                    self.c_bl_p
                                    )

        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.g_r_p=self.rice.get()*80
        self.g_co_p=self.cooking_oil.get()*135
        self.g_wf_p=self.wheat_flour.get()*180
        self.g_s_p=self.sugar.get()*56
        self.g_t_p=self.tea.get()*99
        self.g_b_p=self.biscuits.get()*30


        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_co_p+
                                    self.g_wf_p+
                                    self.g_s_p+
                                    self.g_t_p+
                                    self.g_b_p
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))



        self.f_h_p=self.handbags.get()*700
        self.f_s_p=self.sunglasses.get()*890
        self.f_fw_p=self.foot_wear.get()*560
        self.f_l_p=self.luggage.get()*1060
        self.f_w_p=self.watch.get()*1000
        self.f_j_p=self.jewellery.get()*550
        self.total_fashion_price=float(
                                    self.f_h_p+
                                    self.f_s_p+
                                    self.f_fw_p+
                                    self.f_l_p+
                                    self.f_w_p+
                                    self.f_j_p
                                    )
        self.fashion_price.set("Rs. "+str(self.total_fashion_price))
        self.f_tax=round((self.total_fashion_price*0.06),2)
        self.fashion_tax.set("Rs. "+str(self.f_tax))

        self.Total_bill=float( self.total_cosmetic_price+
                               self.total_grocery_price+
                               self.total_fashion_price+
                               self.c_tax+
                               self.g_tax+
                               self.f_tax
                               )


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to Supermart\n")
        self.txtarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n===================================")
        self.txtarea.insert(END,"\n Products\t\tQTY\t Price")
        self.txtarea.insert(END,f"\n===================================")
    
    def bill_area(self):
        if self.c_name.get()==""or self.c_phone.get=="":
            messagebox.showerror("Error","Customer details are must")

        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.fashion_price.get()=="Rs. 0.0" :
            messagebox.showerror("Error","No product purchased")   
        else:   

            self.welcome_bill()
            #============Cosmetics qty=======
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Soap\t\t{self.soap.get()}\t{self.c_s_p}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")

            if self.hair_gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.hair_gel.get()}\t{self.c_hg_p}")

            if self.hair_oil.get()!=0:
                self.txtarea.insert(END,f"\n Hair Oil\t\t{self.hair_oil.get()}\t{self.c_ho_p}")

            if self.body_lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.body_lotion.get()}\t\t{self.c_bl_p}")

            #=============grocery========

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t{self.g_r_p}")

            if self.cooking_oil.get()!=0:
                self.txtarea.insert(END,f"\n Cooking oil\t\t{self.cooking_oil.get()}\t{self.g_co_p}")


            if self.wheat_flour.get()!=0:
                self.txtarea.insert(END,f"\n Wheat flour\t\t{self.wheat_flour.get()}\t{self.g_wf_p}")

            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t{self.g_s_p}")

            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t{self.g_t_p}")

            if self.biscuits.get()!=0:
                self.txtarea.insert(END,f"\n Biscuits\t\t{self.biscuits.get()}\t{self.g_b_p}")

            #=========fashion========

            if self.handbags.get()!=0:
                self.txtarea.insert(END,f"\n Handbag\t\t{self.handbags.get()}\t{self.f_hb_p}")
            
            if self.sunglasses.get()!=0:
                self.txtarea.insert(END,f"\n Sun glasses\t\t{self.sunglasses.get()}\t{self.f_s_p}")

            if self.foot_wear.get()!=0:
                self.txtarea.insert(END,f"\n Footwear\t\t{self.foot_wear.get()}\t{self.f_fw_p}")

            if self.luggage.get()!=0:
                self.txtarea.insert(END,f"\n Luggage\t\t{self.luggage.get()}\t{self.f_l_p}")

            if self.watch.get()!=0:
                self.txtarea.insert(END,f"\n Watch\t\t{self.watch.get()}\t{self.f_w_p}")


            if self.jewellery.get()!=0:
                self.txtarea.insert(END,f"\n Jewellery \t\t{self.jewellery.get()}\t{self.f_j_p}")


            self.txtarea.insert(END,f"\n-----------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t{self.cosmetic_tax.get()}")
            

            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t{self.grocery_tax.get()}")


            if self.fashion_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Fashion Tax\t\t{self.fashion_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill :\t\t Rs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n-----------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no.:{self.bill_no.get()} saved successfully")
        else:
            return 

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END) 
                self.txtarea.insert(END,f1)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.") 

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear? ") 
        if op>0:
            

            #===========COMETICS VARIABLES=====
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_gel.set(0)
            self.hair_oil.set(0)
            self.body_lotion.set(0)

            #============GROCERY VARIABLES======
            self.rice.set(0)
            self.cooking_oil.set(0)
            self.wheat_flour.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            self.biscuits.set(0)

            #========FASHION VARIABLES============
            self.handbags.set(0)
            self.sunglasses.set(0)
            self.foot_wear.set(0)
            self.luggage.set(0)
            self.watch.set(0)
            self.jewellery.set(0)

            #======TOTAL PRODUCT PRICE & TAX VARIABLES=====
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.fashion_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.fashion_tax.set("")

            #========CUSTOMER=============
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit? ") 
        if op>0:
            self.root.destroy()



        









root =Tk()
obj = Bill_App(root)
root.attributes('-fullscreen',True)
root.mainloop()