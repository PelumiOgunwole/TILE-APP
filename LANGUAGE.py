class German():
    '''Internationalization'''
    def __init__(self, language):
        if language == 'en': self.resourceLanguageEnglish()
        elif language == 'de': self.resourceLanguageGerman()
        else: raise NotImplementedError('Unsupported language.')

    def resourceLanguageEnglish(self):
       pass


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
