from tkinter import*
import math, random
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#003399"
        title=Label(self.root,text = "Billing Software",border= 12,relief = GROOVE,bg=bg_color,fg ="yellow",font=("baloo bhai",25,"bold"),pady=2).pack(fill = X)
        #=============variables=========
        #========cosmetics======
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.hair_gel=IntVar()
        self.body_lotion=IntVar()
        self.hair_oil=IntVar()
        #=========grocery========
        self.rice=IntVar()
        self.cooking_oil=IntVar()
        self.wheat_flour=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.Biscuits=IntVar()
        #============fashion======
        self.Handbags=IntVar()
        self.sun_glasses=IntVar()
        self.Footwear=IntVar()
        self.Luggage=IntVar()
        self.Watch=IntVar()
        self.Jwellery=IntVar()
        #=====customer=========
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        
        self.search_bill=StringVar()
        #===========total product price & tax variable======
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.fashion_price=StringVar()
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.fashion_tax=StringVar()

            

            #=========Customer Details Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("baloo bhai",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=70,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font =("baloo bhai",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="inherit 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font =("baloo bhai",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="inherit 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="white",font =("baloo bhai",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="inherit 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text ="Search",width = 15,bd=7,font="inherit 12 bold").grid(row=0,column=6,padx =10,pady=10)

        #==========Cosmetics Frame ============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("baloo bhai",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=325,height=365)

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
        F3.place(x=335,y=170,width=325,height=365)

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
        g6_txt=Entry(F3,width=10,textvariable=self.Biscuits,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #==========Fashion Frame ============
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Fashion",font=("baloo bhai",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=665,y=170,width=325,height=365)

        fa1_lbl=Label(F4,text="Handbags",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        fa1_txt=Entry(F4,width=10,textvariable=self.Handbags,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        fa2_lbl=Label(F4,text="SunGlasses",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        fa2_txt=Entry(F4,width=10,textvariable=self.sun_glasses,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        fa3_lbl=Label(F4,text="Footwear",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        fa3_txt=Entry(F4,width=10,textvariable=self.Footwear,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        fa4_lbl=Label(F4,text="Luggage",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        fa4_txt=Entry(F4,width=10,textvariable=self.Luggage,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        fa5_lbl=Label(F4,text="Watch",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        fa5_txt=Entry(F4,width=10,textvariable=self.Watch,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        fa6_lbl=Label(F4,text="Jwellery",font = ("baloo bhai",13,"bold"),bg=bg_color,fg="#66ff33").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        fa6_txt=Entry(F4,width=10,textvariable=self.Jwellery,font=("baloo bhai",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #========Bill Area=====
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=995,y=170,width=290,height=365)
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
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Fashion Price",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.fashion_price,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Fashion Tax",bg=bg_color,font=("baloo bhai" ,12,"bold"),fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.fashion_tax,font=("inherit",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=690,width=560,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",width=11,font="inherit 13 bold",bd=5,pady=13).grid(row=0,column=0,padx=5,pady=5)
        gb_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",width=11,font="inherit 13 bold",bd=5,pady=13).grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",width=11,font="inherit 13 bold",bd=5,pady=13).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="exit",bg="cadetblue",fg="white",width=11,font="inherit 13 bold",bd=5,pady=13).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*50
        self.c_fw_p=self.face_wash.get()*80
        self.c_hg_p=self.hair_gel.get()*100
        self.c_ho_p=self.hair_oil.get()*40
        self.c_bl_p=self.body_lotion.get()*200

        self.total_cosmetic_price=float(   
                                            self.c_s_p+
                                            self.c_fc_p+
                                            self.c_fw_p+
                                            self.c_hg_p+
                                            self.c_ho_p+
                                            self.c_bl_p

                                                 
                                                 )
        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.c_tax=self.total_cosmetic_price*0.05
        self.cosmetic_tax.set(str(self.c_tax))


        self.c_rc_p=self.rice.get()*40
        self.c_co_p=self.cooking_oil.get()*50
        self.c_wf_p=self.wheat_flour.get()*80
        self.c_sug_p=self.sugar.get()*100
        self.c_bis_p=self.Biscuits.get()*200
        self.c_tea_p=self.tea.get()*60


        self.total_grocery_price=float(
                                                self.c_rc_p+
                                                self.c_co_p+
                                                self.c_wf_p+
                                                self.c_sug_p+
                                                self.c_bis_p+
                                                self.c_tea_p
                                                 
                                                 )
        self.grocery_price.set(str(self.total_grocery_price))
        self.g_tax=self.total_grocery_price*0.05
        self.grocery_tax.set(str(self.g_tax))


        self.c_lug_p=self.Luggage.get()*400
        self.c_hb_p=self.Handbags.get()*500
        self.c_sg_p=self.sun_glasses.get()*800
        self.c_jwel_p=self.Jwellery.get()*1000
        self.c_w_c=self.Watch.get()*400
        self.c_ftw_p=self.Footwear.get()*200

        self.total_fashion_price=float( 
                                                self.c_lug_p+
                                                self.c_hb_p+
                                                self.c_sg_p+
                                                self.c_jwel_p+
                                                self.c_w_c+
                                                self.c_ftw_p
                                                 
                                                 )
        self.fashion_price.set(str(self.total_fashion_price))
        self.f_tax=self.total_fashion_price*0.05
        self.fashion_tax.set(str(self.f_tax))

        self.Total_bill=float(
                                     self.total_cosmetic_price+
                                     self.total_fashion_price+
                                     self.total_fashion_price+
                                     self.c_tax+
                                     self.f_tax+
                                     self.c_tax
                             )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Webcode Retail")
        self.txtarea.insert(END,f"\n bill number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\ncustomer name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number:{self.c_phone.get()}")
        self.txtarea.insert(END,f"\n==============================")
        self.txtarea.insert(END,f"\nProducts\t\tQTY\tPrice")
        self.txtarea.insert(END,f"\n==============================")

    def bill_area(self):
        if self.c_name.get()==""  or self.c_phone.get()=="":
            messagebox.showerror("Error","customer Details are must.")
        elif self.cosmetic_price.get()=="0.0" and self.grocery_price.get()=="0.0" and self.fashion_price.get()=="0.0":
             messagebox.showerror("error","no product is selected")
        else:    

           self.welcome_bill()
        #=======cosmetics=======
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n bath soap\t\t{self.soap.get()}\t{self.c_s_p}")

        if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\n face cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")

        if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\n face wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")

        if self.hair_gel.get()!=0:
            self.txtarea.insert(END,f"\n hair gel \t\t{self.hair_gel.get()}\t{self.c_hg_p}")

        if self.hair_oil.get()!=0:
            self.txtarea.insert(END,f"\n hair oil \t\t{self.hair_oil.get()}\t{self.c_ho_p}")
        
        if self.body_lotion.get()!=0:
            self.txtarea.insert(END,f"\n body lotion \t\t{self.body_lotion.get()}\t{self.c_bl_p}")

        #=============grocery========

        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n rice  \t\t{self.rice.get()}\t{self.c_rc_p}")

        if self.cooking_oil.get()!=0:
            self.txtarea.insert(END,f"\ncooking oil \t\t{self.cooking_oil.get()}\t{self.c_co_p}")


        if self.wheat_flour.get()!=0:
            self.txtarea.insert(END,f"\nwheat flour\t\t{self.wheat_flour.get()}\t{self.c_wf_p}")

        if self.sugar.get()!=0:
            self.txtarea.insert(END,f"\n suagr\t\t{self.suagr.get()}\t{self.c_sug_p}")

        if self.Biscuits.get()!=0:
            self.txtarea.insert(END,f"\nbiscuits\t\t{self.Biscuits.get()}\t{self.c_bis_p}")

        if self.tea.get()!=0:
            self.txtarea.insert(END,f"\ntea\t\t{self.tea.get()}\t{self.c_tea_p}")

        #=========fashion========

        if self.Luggage.get()!=0:
            self.txtarea.insert(END,f"\nluggage  \t\t{self.Luggage.get()}\t{self.c_lug_p}")

        if self.sun_glasses.get()!=0:
            self.txtarea.insert(END,f"\nsun glasses  \t\t{self.sun_glasses.get()}\t{self.c_sg_p}")

        if self.Jwellery.get()!=0:
            self.txtarea.insert(END,f"\n jwellery \t\t{self.jwellery.get()}\t{self.c_jwel_p}")

        if self.Handbags.get()!=0:
            self.txtarea.insert(END,f"\nhandbag \t\t{self.Handbags.get()}\t{self.c_hb_p}")

        if self.Watch.get()!=0:
           self.txtarea.insert(END,f"\nwatch\t\t{self.Watch.get()}\t{self.c_w_c}")

        if self.Footwear.get()!=0:
            self.txtarea.insert(END,f"\nfootwear \t\t{self.Footwear.get()}\t{self.c_ftw_p}")

        self.txtarea.insert(END,f"\n-------------------------------")
        if self.cosmetic_tax.get()!="0.0":
            self.txtarea.insert(END,f"\ncosmetic tax\t\t{self.cosmetic_tax.get()}")
        

        if self.grocery_tax.get()!="0.0":
            self.txtarea.insert(END,f"\ngrocery tax\t\t{self.grocery_tax.get()}")
        

        if self.fashion_tax.get()!="0.0":
            self.txtarea.insert(END,f"\nfashion tax\t\t{self.fashion_tax.get()}")

        self.txtarea.insert(END,f"\nTotal Bill\t\t{self.Total_bill}")
        self.txtarea.insert(END,f"\n-------------------------------")



root =Tk()
obj = Bill_App(root)
root.mainloop()
