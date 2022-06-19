from tkinter import *
from tkinter import messagebox
import random
from datetime import datetime
import time


class Billing_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Management")
        self.root.config(bg="#2c3e50")
        title = Label(self.root, text="SuperMarket Billing Mangaement System", relief=GROOVE, bg="#535c68", fg="White",
                      font=("Arial", 18, "bold"), pady=2).pack(fill=X)

        # =============Variables==================
        self.basmati_rice = IntVar()
        self.pasta = IntVar()
        self.black_beans = IntVar()
        self.oatmeal = IntVar()
        self.white_sugar = IntVar()
        self.salt = IntVar()
        self.vegetable_oil = IntVar()
        self.tomatoes = IntVar()
        self.carrots = IntVar()
        self.caulflower = IntVar()
        self.onion = IntVar()
        self.apple = IntVar()
        self.orange = IntVar()
        self.grapes = IntVar()
        self.butter = IntVar()
        self.eggs = IntVar()
        self.milk = IntVar()
        self.body_wash = IntVar()
        self.facial_cleanser = IntVar()
        self.hand_soap = IntVar()
        self.perfume = IntVar()
        self.customer_name = StringVar()
        self.customer_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.txtarea = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.total_bf = StringVar()
        self.total_con = StringVar()
        self.total_veg = StringVar()
        self.total_fru = StringVar()
        self.total_per = StringVar()
        self.total_dairy = StringVar()
        self.tax_bf = StringVar()
        self.tax_con = StringVar()
        self.tax_veg = StringVar()
        self.tax_fru = StringVar()
        self.tax_per = StringVar()
        self.tax_dairy = StringVar()
        self.bulkfoods_price = StringVar()
        self.condiments_price = StringVar()
        self.vegetables_price = StringVar()
        self.fruits_price = StringVar()
        self.personalcare_price = StringVar()
        self.dairy_price = StringVar()
        self.bulkfoods_tax = StringVar()
        self.condiments_tax = StringVar()
        self.vegetables_tax = StringVar()
        self.fruits_tax = StringVar()
        self.personalcare_tax = StringVar()
        self.dairy_tax = StringVar()
        self.total = IntVar()

        # =====================Customer Detail Frame=====================================================================================
        details = LabelFrame(self.root, text="Customer Details", font=("Arial", 12, "bold"), bg="#535c68", fg="white")
        details.place(x=0, y=46, relwidth=1)

        cust_name = Label(details, text="Customer Name :", font=("Arial", 14, "bold"), bg="#535c68", fg="white").grid(
            row=0, column=0, padx=10)
        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.customer_name).grid(row=0, column=1,
                                                                                                   padx=8)

        contact_name = Label(details, text="Contact No :", font=("Arial", 14, "bold"), bg="#535c68", fg="white").grid(
            row=0, column=2, padx=10)
        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.customer_phone).grid(row=0, column=3,
                                                                                                       padx=8)

        bill_name = Label(details, text="Bill.No :", font=("Arial", 14, "bold"), bg="#535c68", fg="white").grid(row=0,
                                                                                                                column=4,
                                                                                                                padx=10)
        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

        self.date.set(time.strftime("%d/%m/%y"))
        self.time.set(time.strftime("%I:%M:%p"))

        Date_lbl = Label(details, text="DATE :", bg="#535c68", fg="White", font=("Arial", 14, "bold")).grid(row=0,
                                                                                                            column=6,
                                                                                                            padx=10)
        Date_text = Entry(details, borderwidth=4, width=25, textvariable=self.date).grid(row=0, column=7, padx=8)
        # =======================================Bulk Food frame=========================================================================
        bulk_foods = LabelFrame(self.root, text="BULK FOODS", font=("Arial", 12, "bold"), bg="#535c68", fg="white",
                                relief=GROOVE)
        bulk_foods.place(x=5, y=110, height=200, width=290)

        item1 = Label(bulk_foods, text="Basmati Rice", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  pady=11)
        item1_entry = Entry(bulk_foods, borderwidth=2, width=20, textvariable=self.basmati_rice).grid(row=0, column=1,
                                                                                                      padx=10)

        item2 = Label(bulk_foods, text="Pasta", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=1,
                                                                                                           column=0,
                                                                                                           pady=11)
        item2_entry = Entry(bulk_foods, borderwidth=2, width=20, textvariable=self.pasta).grid(row=1, column=1, padx=10)

        item3 = Label(bulk_foods, text="Black Beans", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 pady=11)
        item3_entry = Entry(bulk_foods, borderwidth=2, width=20, textvariable=self.black_beans).grid(row=2, column=1,
                                                                                                     padx=10)

        item4 = Label(bulk_foods, text="Oatmeal", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=3,
                                                                                                             column=0,
                                                                                                             pady=11)
        item4_entry = Entry(bulk_foods, borderwidth=2, width=20, textvariable=self.oatmeal).grid(row=3, column=1,
                                                                                                 padx=10)
        # =======================================Condiments Frame================================================================================
        condiments = LabelFrame(self.root, text="CONDIMENTS", font=("Arial", 12, "bold"), bg="#535c68", fg="white",
                                relief=GROOVE)
        condiments.place(x=5, y=320, height=155, width=290)

        item5 = Label(condiments, text="White Sugar", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=4,
                                                                                                                 column=0,
                                                                                                                 pady=11)
        item5_entry = Entry(condiments, borderwidth=2, width=20, textvariable=self.white_sugar).grid(row=4, column=1,
                                                                                                     padx=10)

        item6 = Label(condiments, text="Salt", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=5,
                                                                                                          column=0,
                                                                                                          pady=11)
        item6_entry = Entry(condiments, borderwidth=2, width=20, textvariable=self.salt).grid(row=5, column=1, padx=10)

        item7 = Label(condiments, text="Vegetable oil", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(
            row=6, column=0, pady=11)
        item7_entry = Entry(condiments, borderwidth=2, width=20, textvariable=self.vegetable_oil).grid(row=6, column=1,
                                                                                                       padx=10)
        # ===================================Vegetables Frame=====================================================================================
        vegetables = LabelFrame(self.root, text="VEGETABLES", font=("Arial", 12, "bold"), relief=GROOVE, bg="#535c68",
                                fg="white")
        vegetables.place(x=305, y=110, height=200, width=290)

        item8 = Label(vegetables, text="Tomatoes", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=0,
                                                                                                              column=0,
                                                                                                              pady=11)
        item8_entry = Entry(vegetables, borderwidth=2, width=20, textvariable=self.tomatoes).grid(row=0, column=1,
                                                                                                  padx=10)

        item9 = Label(vegetables, text="Carrots", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=1,
                                                                                                             column=0,
                                                                                                             pady=11)
        item9_entry = Entry(vegetables, borderwidth=2, width=20, textvariable=self.carrots).grid(row=1, column=1,
                                                                                                 padx=10)

        item10 = Label(vegetables, text="Caulflower", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 pady=11)
        item10_entry = Entry(vegetables, borderwidth=2, width=20, textvariable=self.caulflower).grid(row=2, column=1,
                                                                                                     padx=10)

        item11 = Label(vegetables, text="Onion", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=3,
                                                                                                            column=0,
                                                                                                            pady=11)
        item11_entry = Entry(vegetables, borderwidth=2, width=20, textvariable=self.onion).grid(row=3, column=1,
                                                                                                padx=10)
        # ===================================Fruits Frame==========================================================================================
        fruits = LabelFrame(self.root, text="FRUITS", font=("Arial", 12, "bold"), relief=GROOVE, bg="#535c68",
                            fg="white")
        fruits.place(x=305, y=320, height=155, width=290)

        item12 = Label(fruits, text="Apple", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=4, column=0,
                                                                                                        pady=11)
        item12_entry = Entry(fruits, borderwidth=2, width=20, textvariable=self.apple).grid(row=4, column=1, padx=10)

        item13 = Label(fruits, text="Orange", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=5,
                                                                                                         column=0,
                                                                                                         pady=11)
        item13_entry = Entry(fruits, borderwidth=2, width=20, textvariable=self.orange).grid(row=5, column=1, padx=10)

        item14 = Label(fruits, text="Grapes", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=6,
                                                                                                         column=0,
                                                                                                         pady=11)
        item14_entry = Entry(fruits, borderwidth=2, width=20, textvariable=self.grapes).grid(row=6, column=1, padx=10)
        # ========================================Personal Care Frame===============================================================================
        personal_care = LabelFrame(self.root, text="PERSONAL CARE", font=("Arial", 12, "bold"), relief=GROOVE,
                                   bg="#535c68", fg="white")
        personal_care.place(x=605, y=110, height=200, width=290)

        item15 = Label(personal_care, text="Body wash", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(
            row=0, column=0, pady=11)
        item15_entry = Entry(personal_care, borderwidth=2, width=20, textvariable=self.body_wash).grid(row=0, column=1,
                                                                                                       padx=10)

        item16 = Label(personal_care, text="Facial cleanser", font=("Arial", 11, "bold"), bg="#535c68",
                       fg="white").grid(row=1, column=0, pady=11)
        item16_entry = Entry(personal_care, borderwidth=2, width=20, textvariable=self.facial_cleanser).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10)

        item17 = Label(personal_care, text="Hand soap", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(
            row=2, column=0, pady=11)
        item17_entry = Entry(personal_care, borderwidth=2, width=20, textvariable=self.hand_soap).grid(row=2, column=1,
                                                                                                       padx=10)

        item18 = Label(personal_care, text="Perfume", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=3,
                                                                                                                 column=0,
                                                                                                                 pady=11)
        item18_entry = Entry(personal_care, borderwidth=2, width=20, textvariable=self.perfume).grid(row=3, column=1,
                                                                                                     padx=10)
        # ========================================Dairy Frame========================================================================================
        dairy = LabelFrame(self.root, text="DAIRY", font=("Arial", 12, "bold"), relief=GROOVE, bg="#535c68", fg="white")
        dairy.place(x=605, y=320, height=155, width=290)

        item19 = Label(dairy, text="Milk", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=4, column=0,
                                                                                                      pady=11)
        item19_entry = Entry(dairy, borderwidth=2, width=20, textvariable=self.milk).grid(row=4, column=1, padx=10)

        item20 = Label(dairy, text="Eggs", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=5, column=0,
                                                                                                      pady=11)
        item20_entry = Entry(dairy, borderwidth=2, width=20, textvariable=self.eggs).grid(row=5, column=1, padx=10)

        item21 = Label(dairy, text="Butter", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=6, column=0,
                                                                                                        pady=11)
        item21_entry = Entry(dairy, borderwidth=2, width=20, textvariable=self.butter).grid(row=6, column=1, padx=10)
        # =================================================Billing summery(Total price & Tax amount)===========================================================
        billing_summery = Frame(self.root, bg="#535c68")
        billing_summery.place(x=5, y=480, width=970, height=70)

        bill_title = Label(billing_summery, text="Billing Summery(Total Price Amount & Tax Amount)", relief=GROOVE,
                           font=("Arial", 15, "bold"), bg="#2c3e50", fg="white")
        bill_title.place(height=50, width=940, x=10, y=10)

        # =================================================Total price=========================================================================================
        total_price = LabelFrame(self.root, text="Total price Amount", font=("Arial", 12, "bold"), relief=GROOVE,
                                 bg="#535c68", fg="white")
        total_price.place(x=5, y=560, width=595, height=140)

        total_bulkfoods = Label(total_price, text="Bulk foods", font=("Arial", 11, "bold"), bg="#535c68",
                                fg="white").grid(row=0, column=0, padx=25)
        total_bulkfoods_entry = Entry(total_price, width=20, borderwidth=2, textvariable=self.bulkfoods_price).grid(
            row=0, column=1, padx=10, pady=8)

        total_condiments = Label(total_price, text="Condiments ", font=("Arial", 11, "bold"), bg="#535c68",
                                 fg="white").grid(row=1, column=0, padx=25)
        total_condiments_entry = Entry(total_price, width=20, borderwidth=2, textvariable=self.condiments_price).grid(
            row=1, column=1, pady=8)

        total_vegetables = Label(total_price, text="Vegetables", font=("Arial", 11, "bold"), bg="#535c68",
                                 fg="white").grid(row=2, column=0, padx=25)
        total_vegetables_entry = Entry(total_price, width=20, borderwidth=2, textvariable=self.vegetables_price).grid(
            row=2, column=1, padx=10, pady=8)

        total_fruits = Label(total_price, text="Fruits", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(
            row=0, column=2, padx=25)
        total_fruits_entry = Entry(total_price, width=20, borderwidth=2, textvariable=self.fruits_price).grid(row=0,
                                                                                                              column=3,
                                                                                                              padx=10,
                                                                                                              pady=8)

        total_personal_care = Label(total_price, text="Personal care", font=("Arial", 11, "bold"), bg="#535c68",
                                    fg="white").grid(row=1, column=2)
        total_personal_care_entry = Entry(total_price, width=20, borderwidth=2,
                                          textvariable=self.personalcare_price).grid(row=1, column=3, padx=10, pady=8)

        total_dairy = Label(total_price, text="Dairy", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=2,
                                                                                                                  column=2,
                                                                                                                  padx=25)
        total_dairy_entry = Entry(total_price, width=20, borderwidth=2, textvariable=self.dairy_price).grid(row=2,
                                                                                                            column=3,
                                                                                                            padx=10,
                                                                                                            pady=8)
        # =================================================Tax Amount=========================================================================================
        tax_price = LabelFrame(self.root, text="Tax Amount", font=("Arial", 12, "bold"), relief=GROOVE, bg="#535c68",
                               fg="white")
        tax_price.place(x=610, y=560, width=590, height=140)

        tax_bulkfoods = Label(tax_price, text="Bulk foods", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(
            row=0, column=0, padx=25)
        tax_bulkfoods_entry = Entry(tax_price, width=20, borderwidth=2, textvariable=self.bulkfoods_tax).grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=8)

        tax_condiments = Label(tax_price, text="Condiments ", font=("Arial", 11, "bold"), bg="#535c68",
                               fg="white").grid(row=1, column=0, padx=25)
        tax_condiments_entry = Entry(tax_price, width=20, borderwidth=2, textvariable=self.condiments_tax).grid(row=1,
                                                                                                                column=1,
                                                                                                                pady=8)

        tax_vegetables = Label(tax_price, text="Vegetables", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(
            row=2, column=0, padx=25)
        tax_vegetables_entry = Entry(tax_price, width=20, borderwidth=2, textvariable=self.vegetables_tax).grid(row=2,
                                                                                                                column=1,
                                                                                                                padx=10,
                                                                                                                pady=8)

        tax_fruits = Label(tax_price, text="Fruits", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=0,
                                                                                                                column=2,
                                                                                                                padx=25)
        tax_fruits_entry = Entry(tax_price, width=20, borderwidth=2, textvariable=self.fruits_tax).grid(row=0, column=3,
                                                                                                        padx=10, pady=8)

        tax_personal_care = Label(tax_price, text="Personal care", font=("Arial", 11, "bold"), bg="#535c68",
                                  fg="white").grid(row=1, column=2)
        tax_personal_care_entry = Entry(tax_price, width=20, borderwidth=2, textvariable=self.personalcare_tax).grid(
            row=1, column=3, padx=10, pady=8)

        tax_dairy = Label(tax_price, text="Dairy", font=("Arial", 11, "bold"), bg="#535c68", fg="white").grid(row=2,
                                                                                                              column=2,
                                                                                                              padx=25)
        tax_dairy_entry = Entry(tax_price, width=20, borderwidth=2, textvariable=self.dairy_tax).grid(row=2, column=3,
                                                                                                      padx=10, pady=8)
        # ==============Billing================================================================================
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#535c68")
        billarea.place(x=905, y=107, width=445, height=365)
        bill_title = Label(billarea, text="CASH RECIPT", font=("arial", 15, "bold"), relief=GROOVE, bg="#535c68",
                           fg="white").pack(fill=X)
        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        def total():

            # ========================Total Bulkfoods=============================================
            self.a1 = self.basmati_rice.get()
            self.a2 = self.pasta.get()
            self.a3 = self.black_beans.get()
            self.a4 = self.oatmeal.get()
            self.total_bulkfoods_price = (self.a1 + self.a2 + self.a3 + self.a4)
            self.bulkfoods_price.set("RS." + str(self.total_bulkfoods_price))
            self.bf_tax = round((self.total_bulkfoods_price * 0.02), 2)
            self.bulkfoods_tax.set("Rs." + str(self.bf_tax))
            # =======================Total Condiments==============================================
            self.a5 = self.white_sugar.get()
            self.a6 = self.salt.get()
            self.a7 = self.vegetable_oil.get()
            self.total_condiments_price = (self.a5 + self.a6 + self.a7)
            self.condiments_price.set("Rs." + str(self.total_condiments_price))
            self.c_tax = round((self.total_condiments_price * 0.02), 2)
            self.condiments_tax.set("Rs." + str(self.c_tax))
            # ======================Total Vegetables================================================
            self.veg1 = (self.tomatoes.get())
            self.veg2 = (self.carrots.get())
            self.veg3 = (self.caulflower.get())
            self.veg4 = (self.onion.get())
            self.total_vegetables_price = (self.veg1 + self.veg2 + self.veg3 + self.veg4)
            self.vegetables_price.set("Rs." + str(self.total_vegetables_price))
            self.v_tax = round((self.total_vegetables_price * 0.02), 2)
            self.vegetables_tax.set("Rs." + str(self.v_tax))
            # ======================Total Fruits=======================================================
            self.fru1 = (self.apple.get())
            self.fru2 = (self.orange.get())
            self.fru3 = (self.grapes.get())
            self.total_fruits_price = (self.fru1 + self.fru2 + self.fru3)
            self.fruits_price.set("Rs." + str(self.total_fruits_price))
            self.f_tax = round((self.total_fruits_price * 0.02), 2)
            self.fruits_tax.set("Rs." + str(self.f_tax))
            # ======================Total Personal care===============================================
            self.pc1 = (self.body_wash.get())
            self.pc2 = (self.hand_soap.get())
            self.pc3 = (self.facial_cleanser.get())
            self.pc4 = (self.perfume.get())
            self.total_personalcare_price = (self.pc1 + self.pc2 + self.pc3 + self.pc4)
            self.personalcare_price.set("Rs." + str(self.total_personalcare_price))
            self.pc_tax = round((self.total_personalcare_price * 0.02), 2)
            self.personalcare_tax.set("Rs." + str(self.pc_tax))
            # ======================Total Dairy==============================================================
            self.dry1 = (self.butter.get())
            self.dry2 = (self.eggs.get())
            self.dry3 = (self.milk.get())
            self.total_dairy_price = (self.dry1 + self.dry2 + self.dry3)
            self.dairy_price.set("Rs." + str(self.total_dairy_price))
            self.d_tax = round((self.total_dairy_price * 0.02), 2)
            self.dairy_tax.set("Rs." + str(self.d_tax))

            self.total = ("Rs." + str(
                self.total_bulkfoods_price + self.total_condiments_price + self.total_vegetables_price +
                self.total_fruits_price + self.total_personalcare_price + self.total_dairy_price +
                self.bf_tax + self.c_tax + self.v_tax + self.f_tax + self.pc_tax + self.d_tax))

        def generate_bill():

            if (self.customer_name.get() == "" or self.customer_phone.get() == ""):
                messagebox.showerror("Error", " You Fill in the Customer Details!!")

            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\t      WELCOME TO MOTHER SUPERMARKET")
            self.txtarea.insert(END, f"\n    BILL NO   :{self.bill_no.get()}")
            self.txtarea.insert(END, f"\n    DATE      :{self.date.get()}\t   Time :{self.time.get()}")
            self.txtarea.insert(END, f"\nCUSTOMER NAME :{self.customer_name.get()}")
            self.txtarea.insert(END, f"\nCUSTOMER_PHONE:{self.customer_phone.get()}")
            self.txtarea.insert(END, f"\n==================================================")
            self.txtarea.insert(END, f"\n    PRODUCTS\t\tQUANTITY\t\tPRICE")
            self.txtarea.insert(END, f"\n==================================================")

            # ======bulkfoods&condiments=========

            if self.basmati_rice.get() != 0:
                self.txtarea.insert(END, f"\n Basmati Rice\t\t{self.basmati_rice.get()}\t\tRs.{self.a1}")
            if self.pasta.get() != 0:
                self.txtarea.insert(END, f"\n Pasta\t\t{self.pasta.get()}\t\tRs.{self.a2}")
            if self.black_beans.get() != 0:
                self.txtarea.insert(END, f"\n Black Beans\t\t{self.black_beans.get()}\t\tRs.{self.a3}")
            if self.oatmeal.get() != 0:
                self.txtarea.insert(END, f"\n Oatmeal\t\t{self.oatmeal.get()}\t\tRs.{self.a4}")
            if self.white_sugar.get() != 0:
                self.txtarea.insert(END, f"\n White Sugar\t\t{self.white_sugar.get()}\t\tRs.{self.a5}")
            if self.salt.get() != 0:
                self.txtarea.insert(END, f"\n Salt\t\t{self.salt.get()}\t\tRs.{self.a6}")
            if self.vegetable_oil.get() != 0:
                self.txtarea.insert(END, f"\n Vegetables oil\t\t{self.vegetable_oil.get()}\t\tRs.{self.a7}")

            # =========Vegetables&Fruits=======================
            if self.tomatoes.get() != 0:
                self.txtarea.insert(END, f"\n Tomatoes\t\t{self.tomatoes.get()}\t\tRs.{self.veg1}")
            if self.carrots.get() != 0:
                self.txtarea.insert(END, f"\n Carrots\t\t{self.carrots.get()}\t\tRs.{self.veg2}")
            if self.caulflower.get() != 0:
                self.txtarea.insert(END, f"\n Caul flower\t\t{self.caulflower.get()}\t\tRs.{self.veg3}")
            if self.onion.get() != 0:
                self.txtarea.insert(END, f"\n Onion\t\t{self.onion.get()}\t\tRs.{self.veg4}")
            if self.apple.get() != 0:
                self.txtarea.insert(END, f"\n Apple\t\t{self.apple.get()}\t\tRs.{self.fru1}")
            if self.orange.get() != 0:
                self.txtarea.insert(END, f"\n Orange\t\t{self.orange.get()}\t\tRs.{self.fru2}")
            if self.grapes.get() != 0:
                self.txtarea.insert(END, f"\n Grapes\t\t{self.grapes.get()}\t\tRs.{self.fru3}")

            # =========Personalcare&Dairy=================
            if self.body_wash.get() != 0:
                self.txtarea.insert(END, f"\n Body Wash\t\t{self.body_wash.get()}\t\tRs.{self.pc1}")
            if self.hand_soap.get() != 0:
                self.txtarea.insert(END, f"\n Hand Soap\t\t{self.hand_soap.get()}\t\tRs.{self.pc2}")
            if self.facial_cleanser.get() != 0:
                self.txtarea.insert(END, f"\n Facial Cleanser\t\t{self.facial_cleanser.get()}\t\tRs.{self.pc3}")
            if self.perfume.get() != 0:
                self.txtarea.insert(END, f"\n Perfume\t\t{self.perfume.get()}\t\tRs.{self.pc4}")
            if self.butter.get() != 0:
                self.txtarea.insert(END, f"\n Butter\t\t{self.butter.get()}\t\tRs.{self.dry1}")
            if self.eggs.get() != 0:
                self.txtarea.insert(END, f"\n Eggs\t\t{self.eggs.get()}\t\tRs.{self.dry2}")
            if self.milk.get() != 0:
                self.txtarea.insert(END, f"\n Milk\t\t{self.milk.get()}\t\tRs.{self.dry3}")

            self.txtarea.insert(END, "\n--------------------------------------------------")

            if self.bulkfoods_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Bulkfoods Tax     :\t\t{self.bulkfoods_tax.get()}")
            if self.condiments_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Condiments Tax    :\t\t{self.condiments_tax.get()}")
            if self.vegetables_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Vegetables Tax    :\t\t{self.vegetables_tax.get()}")
            if self.fruits_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Fruits Tax        :\t\t{self.fruits_tax.get()}")
            if self.personalcare_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Personal Care Tax :\t\t{self.personalcare_tax.get()}")
            if self.dairy_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Dairy Tax         :\t\t{self.dairy_tax.get()}")

            self.txtarea.insert(END, f"\n--------------------------------------------------")

            self.txtarea.insert(END, f"\n Total Amount      :\t\t{self.total}")

            self.txtarea.insert(END, f"\n--------------------------------------------------")

        def clear():
            self.txtarea.delete('1.0', END)
            # ========Bulkfoods&Condiments===============
            self.basmati_rice.set(0)
            self.pasta.set(0)
            self.black_beans.set(0)
            self.oatmeal.set(0)
            self.white_sugar.set(0)
            self.salt.set(0)
            self.vegetable_oil.set(0)
            # ====Vegetables&Fruites====
            self.tomatoes.set(0)
            self.carrots.set(0)
            self.caulflower.set(0)
            self.onion.set(0)
            self.apple.set(0)
            self.orange.set(0)
            self.grapes.set(0)
            # ====Personalcare&Dairy======
            self.body_wash.set(0)
            self.hand_soap.set(0)
            self.facial_cleanser.set(0)
            self.perfume.set(0)
            self.butter.set(0)
            self.eggs.set(0)
            self.milk.set(0)
            # ====Total price and Tax====
            self.bulkfoods_price.set("")
            self.condiments_price.set("")
            self.vegetables_price.set("")
            self.fruits_price.set("")
            self.personalcare_price.set("")
            self.dairy_price.set("")

            self.bulkfoods_tax.set("")
            self.condiments_tax.set("")
            self.vegetables_tax.set("")
            self.fruits_tax.set("")
            self.personalcare_tax.set("")
            self.dairy_tax.set("")
            # ======Customer=====
            self.customer_name.set("")
            self.customer_phone.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set("")
            self.bill_no.set(str(x))

        clear()

        def exit1():
            self.root.destroy()

        # ==================================================Button frame========================================================================================
        button_frame = Frame(self.root, relief=GROOVE, bg="#535c68")
        button_frame.place(x=980, y=480, width=370, height=66)

        button_total = Button(button_frame, text="Total ", font=("Arial", 15, "bold"), pady=7, bg="#2c3e50", fg="white",
                              command=total).grid(row=0, column=0, padx=7, pady=5)

        button_clear = Button(button_frame, text="Clear bill", font=("Arial", 15, "bold"), pady=7, bg="#2c3e50",
                              fg="white", command=clear).grid(row=0, column=1, padx=7, pady=5)

        button_exit = Button(button_frame, text="Exit", width=10, font=("Arial", 15, "bold"), pady=7, bg="#2c3e50",
                             fg="white", command=exit1).grid(row=0, column=2, padx=7, pady=5)

        print_area = Frame(self.root, relief=GROOVE, bg="#535c68")
        print_area.place(x=1210, y=560, width=140, height=140)

        print_statement = Button(print_area, text="GENERATE\nBILL", font=("Arial", 17, "bold"), relief=GROOVE,
                                 bg="#2c3e50", fg="white", command=generate_bill).grid(padx=2, pady=35)


root = Tk()
super_market = Billing_app(root)
root.mainloop()

