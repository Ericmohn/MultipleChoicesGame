import PySimpleGUI as sg
class MultipleChoiceGame:
    def __init__(self):
        self.question1 = 'Were you born in the northern realm or in the southern realm? (Northern/Southern)' # northern = Aside, southern = Bside
        self.question2 = 'Would you rather have a sword or a shield? (Sword/Shield)' # sword = 1side, shield = 2side
        self.question3 = 'What is your specialty? (Frontline/Tactical)' # frontline = 1side, tactical = 2side
        self.ending1 = 'You will be a hero in the frontlines!'
        self.ending2 = 'You will be a hero protecting our troops!'
        self.ending3 = 'You will be a important sacrifice in battle!'
        self.ending4 = 'You can not fight this battle!'

        
    def Start(self):
        # Layout
        layout = [
            [sg.Output(size=(70,10))],
            [sg.Input(size=(25,0),key='choice')],
            [sg.Button('Start'),sg.Button('Confirm')]
        ]
        # Window
        self.window = sg.Window('Multiple Choices game!',layout=layout)
        while True:
            # Read data
            self.ReadValues()
            # run the data
            if self.event == 'Start':
                print(self.question1)
                self.ReadValues()
                if self.values['choice'] == 'Northern':
                    print(self.question2)
                    self.ReadValues()
                    if self.values['choice'] == 'Sword':
                        print(self.ending1)
                    if self.values['choice'] == 'Shield':
                        print(self.ending2)
                if self.values['choice'] == 'Southern':
                    print(self.question3)
                    self.ReadValues()
                    if self.values['choice'] == 'Frontline':
                        print(self.ending3)
                    if self.values['choice'] == 'Tactical':
                        print(self.ending4)
        
    def ReadValues(self):
        self.event, self.values = self.window.Read()

game = MultipleChoiceGame()
game.Start()