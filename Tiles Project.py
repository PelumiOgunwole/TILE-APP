from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter.filedialog import asksaveasfilename
from PIL import Image
from tkinter import messagebox
from ttkthemes import ThemedStyle


class Tiling:
    def __init__(self,):

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
        self.skirt_height=DoubleVar()
        self.skirt_unit=StringVar()
        self.variables12=DoubleVar()
        self.final_tiles_var=DoubleVar()
        self.perimeter_var_result=DoubleVar()
        self.area_var_result=DoubleVar()
        self.skirting_var=DoubleVar()
        self.unit= StringVar()
        self.convert_from=StringVar()

        theme= tk.style()
        # setting Theme
        style= ThemedStyle(root)
        style.set_theme("scidgrey")
        root.wm_title("Tiles Estimation App",)

        # Set app icon
        root.iconbitmap(False,'appicon.ico')

        root.geometry('600x500')
        root.resizable=(False, False)
        root.grid_rowconfigure(0,weight=1)
        root.grid_columnconfigure(0,weight=1)
        root.config(bg='grey')
        #theme.theme_use()

        # Label Widgets
        unit_lbl=Label(root,text="Convert to",bg='grey').grid(row=0,column=2)
        skirt_unit_lbl= Label(root,text="Convert From",bg='grey').grid(row=0,column=0)

        room_length_Label = Label(root, text="Insert length of room",padx=15,bg='grey')
        room_length_Label.grid(row=1, column=0)

        room_length_unit= Label(root,textvariable=self.unit,bg='grey').grid(row=1,column =2,sticky=E)

        room_width_Label = Label(root, text="Insert width of room",padx=10,bg='grey' )
        room_width_Label.grid(row=2, column=0)

        room_width_unit = Label(root, textvariable=self.unit,bg='grey').grid(row=2, column=2,sticky=E)

        tile_length_Label=Label(root,text="Insert Tile Length",bg='grey')
        tile_length_Label.grid(row=3, column=0)

        tile_length_unit = Label(root, textvariable=self.unit,bg='grey').grid(row=3, column=2,sticky=E)

        tile_breadth_Label=Label(root,text="Insert Tile Width",padx=10,bg='grey')
        tile_breadth_Label.grid(row=4, column=0)

        tile_width_unit = Label(root, textvariable=self.unit,bg='grey').grid(row=4, column=2,sticky=E)

        no_of_tile_in_pack=Label(root,text="No of Tiles in Pack",bg='grey')
        no_of_tile_in_pack.grid(row=5, column=0)

        no_of_tilepack_unit = Label(root, text="pieces",bg='grey').grid(row=5, column=2,sticky=E)

        totalOpeningSizes = Label(root, text="Total opening Values",bg='grey')
        totalOpeningSizes.grid(row=6, column=0,)

        totalOpeningSizes_value = Label(root, textvariable=self.cum_opening_length, justify=RIGHT,bg='grey')
        totalOpeningSizes_value.grid(row=6, column=1, )

        total_opening__unit = Label(root, textvariable=self.unit,bg='grey').grid(row=6, column=2,sticky=E)

        room_perimeter_label = Label(root, text='Room Perimeter', justify=LEFT,bg='grey')
        room_perimeter_label.grid(row=7,column=0)

        room_perimeter_label_value= Label(root,textvariable=self.perimeter_var_result, justify=RIGHT,bg='grey')
        room_perimeter_label_value.grid(row=7, column=1)
        room_perimeter_unit = Label(root, textvariable=self.unit,bg='grey').grid(row=7, column=2,sticky=E)

        room_area_label = Label(root,text="Floor Area", justify=LEFT,bg='grey')
        room_area_label.grid(row=8, column=0)

        room_area_label_value = Label(root, textvariable=self.area_var_result,justify= RIGHT,bg='grey')
        room_area_label_value.grid(row=8, column=1)
        room_area_unit = Label(root, textvariable=self.unit,bg='grey').grid(row=8, column=2,sticky=E)

        tile_area_label = Label(root, text="Area of Tiles in Pack", justify=RIGHT,bg='grey')
        tile_area_label.grid(row=9, column=0, )

        tile_area_label_value=Label(root, textvariable=self.tile_area_var,justify= RIGHT,bg='grey')
        tile_area_label_value.grid(row=9, column=1,)

        tile_area_unit = Label(root, textvariable=self.unit,bg='grey').grid(row=9, column=2,sticky=E)


        final_no_of_tiles_Label=Label(root, text="Total Tiles Pack Needed: ",justify= RIGHT,bg='grey' )
        final_no_of_tiles_Label.grid(row=10,column=0)

        final_no_of_tiles_Label_value = Label(root, textvariable=self.final_tiles_var, justify=RIGHT,bg='grey')
        final_no_of_tiles_Label_value.grid(row=10, column=1)

        final_packs_unit = Label(root, text='packs',bg='grey').grid(row=10, column=2,sticky=E)


        skirting_height_labels= Label(root, text="Select Skirting Height",justify=RIGHT,bg='grey').grid(row=11, column=0)


        # Entries Widgets
        room_length = Entry(root, text=self.length_var, justify=RIGHT)
        room_length.grid(row=1, column=1, columnspan=3, padx=10, pady=10,sticky=W)

        room_width = Entry(root, text=self.width_var, justify=RIGHT)
        room_width.grid(row=2, column=1, columnspan=3, padx=10, pady=10,sticky=W)

        tile_length = Entry(root, text=self.tile_length_var, justify=RIGHT)
        tile_length.grid(row=3, column=1, columnspan=2, padx=10, pady=10,sticky=W)

        tile_breadth = Entry(root, text=self.tile_width_var, justify=RIGHT)
        tile_breadth.grid(row=4, column=1, columnspan=2, padx=10, pady=10,sticky=W)

        no_of_tile_in_pack_value = Entry(root, text=self.no_of_tile_value, justify=RIGHT)
        no_of_tile_in_pack_value.grid(row=5, column=1, columnspan=2, padx=10, pady=10,sticky=W)

        self.total_opening_length = Entry(root, text=self.cum_opening_length, justify=RIGHT)
        self.total_opening_length.grid(row=6, column=1, columnspan=2, padx=10, pady=10,sticky=W)

        # Skirting Height Unit converter Dictionary
        self.optionlist = {
            "millimeters" : {'metres': 0.001, 'millimeters': 1, 'feet': 0.003},
            "metres" : {'metres': 1, 'millimeters': 1000, 'feet': 3.000},
            "feet" : {'metres': 0.30, 'millimeters': 304.8, 'feet': 1}
        }


        # Option Menu Widget

        self.convert_from.set('millimeters')
        self.Skirt_unit = OptionMenu(root, self.convert_from, *self.optionlist).grid(row=0, column=1)

        self.skirt_height.set(150)
        self.Skirting_Height=OptionMenu(root, variable=self.skirt_height,value=100,).grid(row=11,column=1)

        self.unit.set('millimeters')
        self.general_units=OptionMenu(root, self.unit, *self.optionlist).grid(row=0,column=3)

        # Button Widget

        update_unit_button= Button(root,text="Update Units",command=lambda: self.unit_conversions(self.convert_from,self.unit)).grid(row=14, column=1)

        tiles_Button= Button(root,text="Estimate Tile Packs Needed", command=self.tiles_needed).grid(row=14, column=2)

        #  Creating the Menu Bars
        tile_menu= Menu(root)

        root.config(menu=tile_menu)

        file_menu= Menu(tile_menu,tearoff=0) # Submenu of the original Menu bar. Name: File Menu
        tile_menu.add_cascade(label="File",menu=file_menu) # Add File menu to Menu bar

        file_menu.add_command(label="Save",command=self.save) # Save button which triggers a command to save
        file_menu.add_separator()
        file_menu.add_command(label="New", command=self.New_File) # Create a new file
        file_menu.add_separator()
        file_menu.add_command(label="Open", command=self.open_file)  # Triggers the app to quit
        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=root.quit) # Triggers the app to quit

        # Help Menu
        help_menu = Menu(tile_menu, tearoff=0)  # Submenu of the original Menu bar. Name: File Menu
        tile_menu.add_cascade(label="Help", menu=help_menu)  # Add File menu to Menu bar

        help_menu.add_command(label="About This App", command=self.about_app)  # Save button which triggers a command to save
        help_menu.add_separator()
        help_menu.add_command(label="Getting Started", command=self.getting_started)  # Create a new file
        help_menu .add_separator()

        root.mainloop()

    def about_app(self):
        # Gives a brief description of the app
        pass

    def getting_started(self):
        window= tk.Toplevel(self.root)


    def unit_conversions(self, convert_from, convert_to):
        # This is the function where conversion of unit is triggered

        self.length_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.length_var.get(),3))

        self.width_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.width_var.get(),3))

        self.tile_width_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.tile_width_var.get(),3))

        self.tile_length_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.tile_length_var.get(),3))

        self.cum_opening_length.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.cum_opening_length.get(),3))

        self.perimeter_var_result.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.perimeter_var_result.get(),3))

        self.area_var_result.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.area_var_result.get(),3))

        self.tile_area_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.tile_area_var.get()))

        #self.skirt_height.set())

        self.final_tiles_var.set(round(self.optionlist[convert_from.get()][convert_to.get()] * self.final_tiles_var.get()))


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
        with open(outfile,'w') as saver:
            # The use of var is done to make sure we dont use write() more than once
            var+="Length of Room: " + str(self.length_var.get()) + "\n\n"
            var+= "Width of Room: " + str(self.width_var.get()) + "\n\n"
            var+= "Length of Tiles: " + str(self.tile_length_var.get()) + "\n\n"
            var+= "Width of Tiles: " + str(self.tile_width_var.get()) + "\n\n"
            var+= "Number of Tiles in Park: " + str(self.no_of_tile_value.get()) + "\n\n"
            var+= "Total Opening Values: " + str(self.cum_opening_length.get()) + "\n\n"
            var+= "Calculated Perimeter of Room: " + str(self.perimeter_var_result.get()) + "\n\n"
            var+= "Calculated Area of Room: " + str(self.area_var_result.get()) + "\n\n"
            var+= "Calculated Area Of Tiles: " + str(self.tile_area_var.get()) + "\n\n"
            var+= "Selected Skirting Height: " + str(self.skirt_height.get()) + "\n\n"
            var+= "Total Number Of Tile Packs Needed: " + str(self.final_tiles_var.get()) + "\n\n"

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

        skirting_from_a_tile= self.length_var.get()/ (self.optionlist[self.convert_from.get()][self.unit.get()] * self.skirt_height.get())
        openings= self.cum_opening_length.get() # Total opening length in a room
        length_need_skirting= self.perimeter_var_result.get() - openings
        no_of_skirting_needed= length_need_skirting / self.tile_length_var.get()
        no_of_tiles_for_req= no_of_skirting_needed /skirting_from_a_tile
        no_of_packs_for_skirting= no_of_tiles_for_req / self.no_of_tile_value.get()
        print(no_of_packs_for_skirting)
        return no_of_packs_for_skirting


    def tiles_needed(self):
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


Tiling()
