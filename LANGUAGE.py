class ENGLISH():
    '''Internationalization'''
    def __init__(self, language):
        if language == 'en': self.resourceLanguageEnglish()
        elif language == 'de': self.resourceLanguageGerman()
        else: raise NotImplementedError('Unsupported language.')

    def resourceLanguageEnglish(self):
        self.title = "Tiles Estimation App"

    self.tile_menu[label] = "File"
    self.new = "New"
    self.exit = "Exit"
    self.help = "Help"
    self.about = "About"
    self.unit_lbl["text"]= ""
    self.skirt_unit_lbl["text"] = ""
    self.room_length_Label["text"] = ""
    self.room_width_Label["text"] = ""
    self.tile_length_Label["text"] = ""
    self.tile_breadth_Label["text"] = ""
    self.no_of_tile_in_pack["text"] = ""
    self.totalOpeningSizes["text"] = ""
    self.room_perimeter_label["text"]=""
    self.room_area_label["text"] = ""
    self.tile_area_label["text"] = ""
    self.final_no_of_tiles_Label["text"] = ""



class GERMAN():
    '''Internationalization'''
    def __init__(self, language):
        if language == 'en': self.resourceLanguageEnglish()
        elif language == 'de': self.resourceLanguageGerman()
        else: raise NotImplementedError('Unsupported language.')

    def resourceLanguageGerman(self):
        self.file = "Datei"

    self.new = "Neu"
    self.exit = "Schliessen"
    self.help = "Hilfe"
    self.about = "Ueber"
    self.WIDGET_LABEL = ' Widgets Rahmen '
    self.disabled = "Deaktiviert"
    self.unChecked = "Nicht Markiert"
    self.toggle = "Markieren"
    # Radiobutton list
    self.colors = ["Blau", "Gold", "Rot"]
    self.colorsIn = ["in Blau", "in Gold", "in Rot"]
    self.labelsFrame = ' Etiketten im Rahmen '
    self.chooseNumber = "Waehle eine Nummer:"
    self.label2 = "Etikette 2"
    self.mgrFiles = ' Dateien Organisieren '
    self.browseTo = "Waehle eine Datei... "
    self.copyTo = "Kopiere Datei zu : "