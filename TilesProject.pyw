from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import re


class Tiling():
    def __init__(self,):
        #super().__init__()
        root = Tk()

        self.length_var=DoubleVar()
        self.width_var=DoubleVar()
        self.tile_length_var=DoubleVar()
        self.tile_width_var=DoubleVar()
        self.no_of_tile_value=DoubleVar()
        self.cum_opening_length=DoubleVar()
        self.variables7=DoubleVar()
        self.variables8=DoubleVar()
        self.tile_area_var=DoubleVar()
        self.variables10=DoubleVar()
        self.skirt_height= StringVar()
        self.skirt_unit=StringVar()
        self.variables12=DoubleVar()
        self.final_tiles_var=DoubleVar()
        self.perimeter_var_result=DoubleVar()
        self.area_var_result=DoubleVar()
        self.skirting_var=DoubleVar()
        self.unit= StringVar()
        self.convert_from=StringVar()
        self.room_name_lab=StringVar()

        root.title("FLOOR TILE QUANTITY ESTIMATION APP")
        # Set app icon
        root.iconbitmap(False,'appicon.ico')

        # Submenu Icons
        open = "open.jpg"
        save = "save.ico"
        new = "new.ico"
        exit = "exit.ico"
        about = "about.ico"
        manual = "manual.ico"
        background = "background.jpg"
        switch= "switch.png"

        root.geometry('700x700')
        root.resizable(width=False, height=False)
        root.grid_rowconfigure(0,weight=1)
        root.grid_columnconfigure(0,weight=1)
        root.configure(bg='grey')

        vcmd= (root.register(self.on_validate), '%P')

        # Label Widgets
        unit_lbl=Label(root,text="Convert to",bg='grey',fg='blue').grid(row=0,column=2)
        skirt_unit_lbl= Label(root,text="Convert From",bg='grey',fg='blue').grid(row=0,column=0)


        labelframe=Frame(root,relief='raised')
        labelframe.grid(row=2,column=0)

        labelframe1 = Frame(root, relief='ridge')
        labelframe1.grid(row=3, column=0)

        labelframe2 = Frame(root, relief='ridge')
        labelframe2.grid(row=4, column=0)

        labelframe3 = Frame(root, relief='ridge')
        labelframe3.grid(row=5, column=0)

        labelframe4 = Frame(root, relief='ridge')
        labelframe4.grid(row=6, column=0)

        labelframe5 = Frame(root, relief='ridge')
        labelframe4.grid(row=7, column=0)

        labelframe6 = Frame(root, relief='ridge')
        labelframe6.grid(row=8, column=0)

        labelframe7 = Frame(root, relief='ridge')
        labelframe7.grid(row=9, column=0)

        labelframe8 = Frame(root, relief='ridge')
        labelframe8.grid(row=10, column=0)

        labelframe9 = Frame(root, relief='ridge')
        labelframe9.grid(row=11, column=0)

        labelframe10 = Frame(root, relief='ridge')
        labelframe10.grid(row=12, column=0)

        labelframe11 = Frame(root, relief='ridge')
        labelframe11.grid(row=13, column=0)

        room_name_label = Label(root, text="Insert Name of Room :", bg="grey",fg='blue').grid(row=1, column=0)

        room_length_Label = Label(labelframe,padx=10,text="Room Length :",bg='grey',fg='blue')
        room_length_Label.grid(row=2, column=0)

        room_length_unit= Label(root,textvariable=self.unit,bg='grey',fg='blue').grid(row=2,column =2,sticky=E)

        room_width_Label = Label(labelframe1, text=" Room Width :",padx=10,bg='grey',fg='blue' )
        room_width_Label.grid(row=3, column=0)

        room_width_unit = Label(root, textvariable=self.unit,bg='grey',fg='blue').grid(row=3, column=2,sticky=E)

        tile_length_Label=Label(labelframe2,text="Tile Length :",bg='grey',fg='blue')
        tile_length_Label.grid(row=4, column=0)

        tile_length_unit = Label(root, textvariable=self.unit,bg='grey',fg='blue').grid(row=4, column=2,sticky=E)

        tile_breadth_Label=Label(labelframe3,text="Tile Width :",padx=10,bg='grey',fg='blue')
        tile_breadth_Label.grid(row=5, column=0)

        tile_width_unit = Label(root, textvariable=self.unit,bg='grey',fg='blue').grid(row=5, column=2,sticky=E)

        no_of_tile_in_pack=Label(root,text="No of Tiles in Pack :",bg='grey',fg='blue')
        no_of_tile_in_pack.grid(row=6, column=0)

        no_of_tilepack_unit = Label(root, text="pieces",bg='grey',fg='blue').grid(row=6, column=2,sticky=E)

        totalOpeningSizes = Label(root, text="Total opening Values :",bg='grey',fg='blue')
        totalOpeningSizes.grid(row=7, column=0,)

        total_opening__unit = Label(root, textvariable=self.unit,bg='grey',fg='blue').grid(row=7, column=2,sticky=E)

        room_perimeter_label = Label(labelframe6, text='Room Perimeter :', justify=LEFT,bg='grey',fg='blue')
        room_perimeter_label.grid(row=8,column=0)

        room_perimeter_label_value= Label(root,textvariable=self.perimeter_var_result, justify=RIGHT,bg='grey',fg='blue')
        room_perimeter_label_value.grid(row=8, column=1)
        room_perimeter_unit = Label(root, textvariable=self.unit,bg='grey',fg='blue').grid(row=8, column=2,sticky=E)

        room_area_label = Label(labelframe7,text="Floor Area :", justify=LEFT,bg='grey',fg='blue')
        room_area_label.grid(row=9, column=0)

        room_area_label_value = Label(root, textvariable=self.area_var_result,justify= RIGHT,bg='grey',fg='blue')
        room_area_label_value.grid(row=9, column=1)
        room_area_unit = Label(root, textvariable=self.unit,bg='grey',fg='blue').grid(row=9, column=2,sticky=E)

        tile_area_label = Label(labelframe8, text="Area of Tiles in Pack :", justify=RIGHT,bg='grey',fg='blue')
        tile_area_label.grid(row=10, column=0, )

        tile_area_label_value=Label(root, textvariable=self.tile_area_var,justify= RIGHT,bg='grey',fg='blue')
        tile_area_label_value.grid(row=10, column=1,)

        tile_area_unit = Label(root, textvariable=self.unit,bg='grey',fg='blue').grid(row=10, column=2,sticky=E)


        final_no_of_tiles_Label=Label(labelframe9, text="Total Tiles Pack Needed :",justify= RIGHT,bg='grey',fg='blue' )
        final_no_of_tiles_Label.grid(row=11,column=0)

        final_no_of_tiles_Label_value = Label(root, textvariable=self.final_tiles_var, justify=RIGHT,bg='grey',fg='blue')
        final_no_of_tiles_Label_value.grid(row=11, column=1)

        final_packs_unit = Label(root, text='packs',bg='grey',fg='blue').grid(row=11, column=2,sticky=E)

        skirting_height_labels= Label(labelframe10, text="Select Skirting Height :",justify=RIGHT,bg='grey',fg='blue').grid(row=12, column=0)


        # Entries Widgets

        room_name_ent = Entry(root, text=self.room_name_lab, justify=RIGHT).grid(row=1, column=1, columnspan=3, padx=10,
                                                                                 pady=10, sticky=W)
        room_length = Entry(root, text=self.length_var,justify=RIGHT)
        room_length.grid(row=2, column=1, columnspan=3, padx=10, pady=10,sticky=W)
        room_length.config(validate="key",validatecommand=(vcmd))


        room_width = Entry(root, text=self.width_var, justify=RIGHT)
        room_width.grid(row=3, column=1, columnspan=3, padx=10, pady=10,sticky=W)
        room_width.config(validate="key", validatecommand=(vcmd))

        tile_length = Entry(root, text=self.tile_length_var, justify=RIGHT)
        tile_length.grid(row=4, column=1, columnspan=2, padx=10, pady=10,sticky=W)
        tile_length.config(validate="key", validatecommand=(vcmd))

        tile_breadth = Entry(root, text=self.tile_width_var, justify=RIGHT)
        tile_breadth.grid(row=5, column=1, columnspan=2, padx=10, pady=10,sticky=W)
        tile_breadth.config(validate="key", validatecommand=(vcmd))

        no_of_tile_in_pack_value = Entry(root, text=self.no_of_tile_value, justify=RIGHT)
        no_of_tile_in_pack_value.grid(row=6, column=1, columnspan=2, padx=10, pady=10,sticky=W)
        no_of_tile_in_pack_value.config(validate="key", validatecommand=(vcmd))

        self.total_opening_length = Entry(root, text=self.cum_opening_length, justify=RIGHT)
        self.total_opening_length.grid(row=7, column=1, columnspan=2, padx=10, pady=10,sticky=W)
        self.total_opening_length.config(validate="key", validatecommand=(vcmd))

        # Skirting Height Unit converter Dictionary
        self.optionlist = {
            "millimeters" : {'metres': 0.001, 'millimeters': 1, 'feet': 0.003},
            "metres" : {'metres': 1, 'millimeters': 1000, 'feet': 3.28},
            "feet" : {'metres': 0.30, 'millimeters': 304.8, 'feet': 1}
        }


        # Option Menu Widget

        self.convert_from.set('millimeters')

        skirting_height_list = ("100",
                                "120",
                                "150",
                                "175",
                                "200")

        self.Skirt_unit = OptionMenu(root, self.convert_from, *self.optionlist).grid(row=0, column=1)

        self.skirt_height.set(skirting_height_list[1])
        self.Skirting_Height=OptionMenu(root,self.skirt_height,*skirting_height_list).grid(row=12,column=1)


        self.unit.set('millimeters')
        self.general_units=OptionMenu(root, self.unit, *self.optionlist).grid(row=0,column=3)

        # Button Widget

        update_unit_button= Button(root,text="Update Units",command=lambda: self.unit_conversions(self.convert_from,self.unit)).grid(row=12, column=2)

        tiles_Button= Button(root,text="Estimate Tile Packs Needed", command=self.tiles_needed,bg='white').grid(row=14, column=1)

        #  Creating the Menu Bars
        tile_menu= Menu(root)

        root.config(menu=tile_menu)
        # Image Icons
        image1 = Image.open(open)
        new_img = image1.resize((35, 35))
        test = ImageTk.PhotoImage(new_img)

        image2 = Image.open(save)
        new_img1 = image2.resize((35, 35))
        test1 = ImageTk.PhotoImage(new_img1)

        image3 = Image.open(new)
        new_img2 = image3.resize((35, 35))
        test2 = ImageTk.PhotoImage(new_img2)

        image4 = Image.open(exit)
        new_img3 = image4.resize((35, 35))
        test3 = ImageTk.PhotoImage(new_img3)

        image5 = Image.open(about)
        new_img4 = image5.resize((35, 35))
        test5 = ImageTk.PhotoImage(new_img4)

        image6 = Image.open(manual)
        new_img5 = image6.resize((35, 35))
        test6 = ImageTk.PhotoImage(new_img5)

        image7 = Image.open(switch)
        new_img6 = image7.resize((35, 35))
        test7 = ImageTk.PhotoImage(new_img6)



        file_menu= Menu(tile_menu,tearoff=0) # Submenu of the original Menu bar. Name: File Menu
        tile_menu.add_cascade(label="File",menu=file_menu,) # Add File menu to Menu bar

        file_menu.add_command(label="Save",image=test1,compound='left',command=self.save) # Save button which triggers a command to save
        file_menu.add_separator()
        file_menu.add_command(label="New",image=test2,compound='left', command=self.New_File) # Create a new file
        file_menu.add_separator()
        file_menu.add_command(label="Open",image=test,compound='left', command=self.open_file)  # Triggers the app to quit
        file_menu.add_separator()

        file_menu.add_command(label="Exit",image=test3,compound='left', command=root.quit) # Triggers the app to quit

        # Help Menu
        help_menu = Menu(tile_menu, tearoff=0)  # Submenu of the original Menu bar. Name: File Menu
        tile_menu.add_cascade(label="Help", menu=help_menu)  # Add File menu to Menu bar

        help_menu.add_command(label="About",image=test5,compound='left', command=self.about_app)  # Save button which triggers a command to save
        help_menu.add_separator()
        help_menu.add_command(label="Manual",image=test6,compound='left', command=self.getting_started)  # Create a new file
        help_menu .add_separator()

        # Switch Menu

        switch_menu= Menu(tile_menu,tearoff=0)
        tile_menu.add_cascade(label="Switch",menu=switch_menu)

        switch_menu.add_command(label="Switch",image=test7,compound='left',command=self.switch_to_wall_tiles())
        switch_menu.add_separator()

        root.mainloop()


    def switch_to_wall_tiles(self):
        pass


    def validate(self,string): # This function is meant to filter inputs
        regex = re.compile(r"(\+|\.)?[0-9,]*$|([0-9,]*\.[0-9,]*$)") # Allows Positve numbers only either of type int or float
        result = regex.match(string)
        return (string == ""                        # Allow entry to be empty
                or (string.count('+') <= 1
                    and string.count('-') <= 1
                    and string.count(',') <= 1
                    and result is not None
                    and result.group(0) != ""))


    def on_validate(self,P):
        return self.validate(P)


    def about_app(self):
        # Funtion that manages Information About the App
        root=Tk()
        root.withdraw() # Important because it prevents duplication of TopLevel Windows
        # Gives a brief description of the app
        about_window=Toplevel(root)
        about_window.title(" ABOUT")
        about_window.geometry("200x200")
        about_window.resizable(False,False)

        lbl=Label(about_window,text="FLOOR TILE ESTIMATION APP\nVersion 1.0\n'Copywright 2020'\n\nDeveloper: PeakSimeon\nEmail: simeonontop@gmail.com")
        lbl.pack(ipadx=50, ipady=10, fill='both', expand=True)

        b = tk.Button(about_window, text="OK", command=root.destroy)
        b.pack(pady=10, padx=10, ipadx=20, side='right')


    def getting_started(self):
        root= Tk()
        root.withdraw()  # Important because it prevents duplication of TopLevel Windows
        get_start_window= tk.Toplevel(root)

        get_start_window.geometry("1000x500")
        get_start_window.resizable(True, False)

        lbl1 = Label(get_start_window,
                    text="****TILE NUMBER ESTIMATION APP****\n This app is made to make easy the process for estimatin number of floor tiles needsed to make any room\n"
                         "It is very Simple to use as it features Unit Conversion based on different needs of Users\n"
                         "It supports file saving in text form which can then be printed at anytime. Actually this app is good for estimating tile needed for a whole building.")
        lbl1.pack(ipadx=50, ipady=10, fill='both', expand=True)
        lbl12 = Label(get_start_window,
                     text="****SUPPORTED UNITS****\n(a)Millimeters (b)Metres (c) Feet\nThis app supports conversion from one of thiese units to another")
        lbl12.pack(ipadx=50, ipady=10, fill='both', expand=True)

        lbl13 = Label(get_start_window,
                      text="****HOW TO USE APP****\nIn the first column, there is an option to chose the units to be used  If you decide to change unit, the values entered"
                           " will be converted and the unit being used will appear by the\n sides It is the best practice to use the same Units throughout to obtain correct results. Skirting heights are by default in millimeters "
                           "After entry of all stipulated values, click the lat button by the right for your final results.\n"
                           "")
        lbl13.pack(ipadx=50, ipady=10, fill='both', expand=True)

        lbl14 = Label(get_start_window,
                      text="****TERMS DEFFINITIONS****\nSKIRTING HEIGHT:Skirting tiles are the tiles that laid in the corner of a wall and floor junction.\n\n"
                           "----PURPOSE OF TILE SKIRTING----\n(1)To avoid making dirts on the wall\n(2)To avoid wall Damage\n(3)For Beautification")
        lbl14.pack(ipadx=50, ipady=10, fill='both', expand=True)


        b = tk.Button(get_start_window, text="OK", command=root.destroy)
        b.pack(pady=10, padx=10, ipadx=20, side='right')


    def unit_conversions(self, convert_from, convert_to):
        # This is the function where conversion of unit is triggered
        try:
            assert self.length_var.get()>0
            self.length_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.length_var.get(),3))

            self.width_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.width_var.get(),3))

            self.tile_width_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.tile_width_var.get(),3))

            self.tile_length_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.tile_length_var.get(),3))

            self.cum_opening_length.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.cum_opening_length.get(),3))

            self.skirt_height.set(round(self.optionlist["millimeters"][convert_to.get()] * float(self.skirt_height.get()),5 ))

            self.perimeter_var_result.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.perimeter_var_result.get(),3))

            self.area_var_result.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.area_var_result.get(),3))

            self.tile_area_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.tile_area_var.get()))

            #self.skirt_height.set())

            self.final_tiles_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.final_tiles_var.get()))
        except ZeroDivisionError:
            messagebox.showerror("Error","Check your inputs")


    def open_file(self):
        opendialog= filedialog.askopenfilename(initialdir="C:",title="Pick a file to open",filetypes=(("text files", "*.txt"),("All file types", "*.*")))


    def New_File(self):
        self.length_var.set(0.0)
        self.width_var.set(0.0)
        self.tile_length_var.set(0.0)
        self.tile_width_var.set(0.0)
        self.no_of_tile_value.set(0.0)
        self.cum_opening_length.set(0.0)
        self.perimeter_var_result.set(0.0)
        self.area_var_result.set(0.0)
        self.tile_area_var.set(0.0)
        self.skirt_height.set(0.0)
        self.final_tiles_var.set(0.0)


    def save(self):
        var = ""
        custom_file_name= asksaveasfilename(defaultextension= ".txt", filetypes=(("Text Files", "*.txt"), ("All file types", "*.*")))
        outfile=custom_file_name
        #var=str(self.length_var.get())
        #outfile.write(var)

        #outfile.close()

        with open(outfile,'a+') as saver:
            # The use of var is done to make sure we dont use write() more than once
            var+="\n\n\n\n"
            var+= "Floor Tiles Estimation App".center(20,"*")
            var += ("*****" + str(self.room_name_lab.get()).upper() +  "*****"+ "\n\n").center(20)
            var+="Length of Room: " + str(self.length_var.get())+ " "+ str(self.unit.get()) + "\n\n"
            var+= "Width of Room: " + str(self.width_var.get())+ " "+str(self.unit.get()) + "\n\n"
            var+= "Length of Tiles: " + str(self.tile_length_var.get())+ " "+str(self.unit.get()) + "\n\n"
            var+= "Width of Tiles: " + str(self.tile_width_var.get())+ " "+str(self.unit.get()) + "\n\n"
            var+= "Number of Tiles in Pack: " + str(self.no_of_tile_value.get())+" "+ "\n\n"
            var+= "Total Opening Values: " + str(self.cum_opening_length.get())+" "+ str(self.unit.get()) + "\n\n"
            var+= "Calculated Perimeter of Room: " + str(self.perimeter_var_result.get())+ " "+ str(self.unit.get()) + "\n\n"
            var+= "Calculated Area of Room: " + str(self.area_var_result.get())+ " "+str(self.unit.get()) + str("^2")+"\n\n"
            var+= "Calculated Area Of Tiles: " + str(self.tile_area_var.get())+ " "+ str(self.unit.get()) + str("^2")+ "\n\n"
            var+= "Selected Skirting Height: " + str(self.skirt_height.get())+ " "+str(self.unit.get()) + "\n\n"
            var+= "Total Number Of Tile Packs Needed: " + str(self.final_tiles_var.get()) + " " + str("packs") + "\n\n"

            saver.write(var)
            saver.close()


    def perimeter_of_room(self):
        perimeter= 2 * (self.length_var.get() + self.width_var.get())
        return round(perimeter,2)


    def area_of_room(self):
        area= self.length_var.get() * self.width_var.get()
        return round(area,2)


    def tile_area(self):
        area_of_tiles= self.tile_length_var.get() * self.tile_width_var.get() * self.no_of_tile_value.get()

        return round(area_of_tiles,2)


    def skirting(self):
        skirting_from_a_tile= (self.tile_length_var.get()) / float(self.skirt_height.get()) #
        print("skirt from a tile",skirting_from_a_tile)
        openings= self.cum_opening_length.get() # Total opening length in a room
        length_need_skirting= self.perimeter_var_result.get() - openings
        print("length_need_skirting",length_need_skirting)
        no_of_skirting_needed= length_need_skirting / self.tile_length_var.get()
        print("No of skirting needed",no_of_skirting_needed)
        no_of_tiles_for_req= no_of_skirting_needed /skirting_from_a_tile
        print("no_of_tiles_for_req",no_of_tiles_for_req)
        no_of_packs_for_skirting= no_of_tiles_for_req / self.no_of_tile_value.get()

        print(no_of_packs_for_skirting)
        return no_of_packs_for_skirting


    def tiles_needed(self):
        # Handling Errors to prevent Zero Division Errors
        try:
            self.perimeter_var_result.set(self.perimeter_of_room())
            self.area_var_result.set(self.area_of_room())
            self.tile_area_var.set(self.tile_area())

            no_of_tiles_needed_for_room= self.area_of_room() / self.tile_area()

            tiles= no_of_tiles_needed_for_room + self.skirting()
            waste = 0.1 * tiles
            total_tiles_needed = waste + tiles
            self.final_tiles_var.set(round(total_tiles_needed,2))
        except ZeroDivisionError:
            messagebox.showerror("WARNING","Too Small Tile Area, Check Dimensions Of Tiles")

