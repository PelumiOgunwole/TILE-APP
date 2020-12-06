from tkinter import *
from tkinter import DoubleVar
from tkinter import PhotoImage
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



        root.wm_title("Tiles Number Calculation App",)
        #photo = PhotoImage(file ='tilespicture.png')
        #root.iconphoto(False,photo)
        root.geometry('400x400')
        root.resizable=(False, False)

        # Label Widgets
        unit_lbl=Label(root,text="General Units").grid(row=0,column=2)
        skirt_unit_lbl= Label(root,text="Units Of Skirting Height",).grid(row=0,column=0)



        room_length_Label = Label(root, text="Insert length of room",padx=15,)
        room_length_Label.grid(row=1, column=0,sticky=W)

        room_length_unit= Label(root,textvariable=self.unit).grid(row=1,column =2)

        room_width_Label = Label(root, text="Insert width of room",padx=10 )
        room_width_Label.grid(row=2, column=0,sticky=W)

        room_width_unit = Label(root, textvariable=self.unit).grid(row=2, column=2)

        tile_length_Label=Label(root,text="Insert Tile Length",)
        tile_length_Label.grid(row=3, column=0,sticky=W)

        tile_length_unit = Label(root, textvariable=self.unit).grid(row=3, column=2)

        tile_breadth_Label=Label(root,text="Insert Tile Width",padx=10,)
        tile_breadth_Label.grid(row=4, column=0,sticky=W)

        tile_width_unit = Label(root, textvariable=self.unit).grid(row=4, column=2)

        no_of_tile_in_pack=Label(root,text="No of Tiles in Pack",)
        no_of_tile_in_pack.grid(row=5, column=0,sticky=W)

        no_of_tilepack_unit = Label(root, text="pieces").grid(row=5, column=2)

        totalOpeningSizes = Label(root, text="Total opening Values")
        totalOpeningSizes.grid(row=6, column=0, )

        totalOpeningSizes_value = Label(root, textvariable=self.cum_opening_length, justify=RIGHT)
        totalOpeningSizes_value.grid(row=6, column=1, )

        total_opening__unit = Label(root, textvariable=self.unit).grid(row=6, column=2)

        room_perimeter_label = Label(root, text='Room Perimeter', justify=LEFT)
        room_perimeter_label.grid(row=7,column=0)

        room_perimeter_label_value= Label(root,textvariable=self.perimeter_var_result, justify=RIGHT)
        room_perimeter_label_value.grid(row=7, column=1)
        room_perimeter_unit = Label(root, textvariable=self.unit).grid(row=7, column=2)

        room_area_label = Label(root,text="Floor Area", justify=LEFT)
        room_area_label.grid(row=8, column=0)

        room_area_label_value = Label(root, textvariable=self.area_var_result,justify= RIGHT)
        room_area_label_value.grid(row=8, column=1)
        room_area_unit = Label(root, textvariable=self.unit,text="^2").grid(row=8, column=2)

        tile_area_label = Label(root, text="Area of Tiles in Pack", justify=RIGHT)
        tile_area_label.grid(row=9, column=0, )

        tile_area_label_value=Label(root, textvariable=self.tile_area_var,justify= RIGHT)
        tile_area_label_value.grid(row=9, column=1,)

        tile_area_unit = Label(root, textvariable=self.unit,text="^2").grid(row=9, column=2)


        final_no_of_tiles_Label=Label(root, text="Total Tiles Pack Needed: ",justify= RIGHT )
        final_no_of_tiles_Label.grid(row=10,column=0)

        final_no_of_tiles_Label_value = Label(root, textvariable=self.final_tiles_var, justify=RIGHT)
        final_no_of_tiles_Label_value.grid(row=10, column=1)

        final_packs_unit = Label(root, text='packs').grid(row=10, column=2)


        skirting_height_labels= Label(root, text="Select Skirting Height",justify=RIGHT).grid(row=11, column=0)


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

        # Skirting Height Unit converter
        self.optionlist= {'metres':0.001,'millimeters':1,'feet':0.00328084}

        self.skirt_unit.set('millimeters')
        self.Skirt_unit=OptionMenu(root,self.skirt_unit, *self.optionlist).grid(row=0,column=1)

        # Option Menu Widget

        self.skirt_height.set(150)
        self.Skirting_Height=OptionMenu(root, variable=self.skirt_height,value=100,).grid(row=11,column=1)

        self.unit.set('millimeters')
        self.general_units=OptionMenu(root, self.unit, *self.optionlist).grid(row=0,column=3)

        # Button Widget
        tiles_Button= Button(root,text="Estimate Tile Packs Needed", command=self.tiles_needed).grid(row=12, column=1)


        root.mainloop()

    # added this file to my github profile
    def perimeter_of_room(self):
        perimeter= 2 * (self.length_var.get() + self.width_var.get()) *  self.optionlist[self.unit.get()]
        return round(perimeter,2)

    def area_of_room(self):
        area= self.length_var.get() * self.width_var.get() * self.optionlist[self.unit.get()]* self.optionlist[self.unit.get()]
        return round(area,2)


    def tile_area(self):
        area_of_tiles= self.tile_length_var.get() * self.tile_width_var.get() * self.no_of_tile_value.get()*self.optionlist[self.unit.get()]
        return round(area_of_tiles,2)


    def skirting(self):

        skirting_from_a_tile= self.length_var.get()/ (self.skirt_height.get() * self.optionlist[self.skirt_unit.get()] )
        openings= self.cum_opening_length.get() # Total opening length in a room
        length_need_skirting= self.perimeter_var_result.get() - openings
        no_of_skirting_needed= length_need_skirting / self.tile_length_var.get()
        no_of_tiles_for_req= no_of_skirting_needed /skirting_from_a_tile
        no_of_packs_for_skirting= no_of_tiles_for_req / self.no_of_tile_value.get()
        print(no_of_packs_for_skirting)
        #self.skirting_var.set(no_of_packs_for_skirting)
        return no_of_packs_for_skirting


    def tiles_needed(self):
        self.perimeter_var_result.set(self.perimeter_of_room())
        self.area_var_result.set(self.area_of_room())
        self.tile_area_var.set(self.tile_area())

        no_of_tiles_needed_for_room= self.area_of_room() / self.tile_area()

        tiles= no_of_tiles_needed_for_room + self.skirting()
        waste = 0.1 * tiles
        total_tiles_needed = waste + tiles
        self.final_tiles_var.set(round(total_tiles_needed,2))
        #return self.final_tiles_var


Tiling()
