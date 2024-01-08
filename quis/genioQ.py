from tkinter import *
from tkinter import messagebox as mB
import json

window = Tk()
window.geometry('450x900')
window.title('=={Genio Q}==')
window.anchor(anchor='center')

class genio:
    
    def __init__(self) -> None:
        self.quest_No = 0
        self.show_Title()
        self.show_Quest()
        self.oP_Chosen = IntVar()
        self.option = self.radio_buttons()
        self.show_Options()
        self.buttons()
        self.data_Size = len(Quest)
        self.correct = 0
        
    def show_result(self):
        counter_err = self.data_Size - self.correct
        correct = f'right: {self.correct}'
        err = f'Erros: {counter_err}'
        
        score = int(self.correct/ self.data_Size * 100)
        
        result = f'Score: {score}'
        
        mB.showinfo('Result', f'{result}\n{correct}\n{err}')
    
    def see_Quest(self, quest_No) -> bool:
        
        if self.oP_Chosen.get() == response[quest_No]:
            return True

    def btn_Next(self):
        if self.see_Quest(self.quest_No):
            self.correct += 1
            self.quest_No += 1
            
            if self.quest_No == self.data_Size:
                self.show_result()
                window.destroy()
            else:
                self.show_Quest()
                self.show_Options()
    
    def radio_buttons(self):
        
        q_list = []
        
        y_pos = 150
        
        while len(q_list) < 4:
            
            radio_btn = Radiobutton(window, text = ' ',variable = self.option,
            value = len(q_list) + 1,font = ('arial', 14))
            
            q_list.append(radio_btn)
            
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
    
        return q_list
    
    def show_options(self):
        val = 0
        
        self.option.set(0)

        for op in options[self.pergunta_no]:
            self.opcao[val]['text'] = op
            val += 1
               
    def buttons(self):
        btnNext = Button(window, text= 'next', command=self.btn_Next,width=10,bg= 'black', fg= 'white',font=('ariel , 16, bold'))
        btnNext.place(x=350,y=850)
        
        btnExit = Button(window, text= 'Exit', command= window.destroy,width=10,bg= 'black', fg= 'white',font=('ariel , 16, bold'))
        btnExit.place(x=400,y=100)
        
with open('./quis/dadosQ.json') as f:
    dado = json.load(f)

quest = (dado['perguntas'])
options = (dado['opcoes'])
response = (dado['resposta'])

    
window.mainloop()