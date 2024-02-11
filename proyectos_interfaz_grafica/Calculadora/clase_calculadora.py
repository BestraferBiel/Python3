import tkinter as tk


class Calculadora:  
        
         def __init__(self, ventana):   
          self.ventana = ventana
          self.display = tk.Entry(self.ventana, font="Arial 20", width=22, borderwidth=10, background="#6495DE", justify="right")    
          self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
        
         
         def crear_botones(self):  
             row = 1
             column = 0
             botones = [
             '7', '8', '9', '/',
             '4', '5', '6', '*',
             '1', '2', '3', '-',
             '0', '.', '=', '+',
             '(', ')', 'C', 'CE',
                  ]
        
             for boton in botones:
                 command = lambda x=boton: self.click(x)
                 tk.Button(self.ventana, text=boton, font=2, width=6, height=2, command=command).grid(row=row, column=column)#crea los botones y los ubica en la ventana
                 column += 1
                 if column > 3:
                     column = 0
                     row += 1   
         
         def click(self, text):  
             if text == "=":
                 try:
                     result = eval(self.display.get())
                     self.display.delete(0, tk.END)
                     self.display.insert(tk.END, str(result))
                 except:
                     self.display.insert(tk.END, "-> Error!")
             elif text == "C":
                 self.display.delete(0, tk.END)
             elif text == "CE":
                 self.display.delete(len(self.display.get())-1, tk.END)
             else:
                 self.display.insert(tk.END, text)          
