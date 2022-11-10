from tkinter import *
import googletrans
import textblob
from tkinter import ttk,messagebox

root = Tk()
root.title('translator Application')
root.geometry("880x300")

def translate_it():
    translated_text.delete(1.0,END)
    try:
        for key,value in languages.items():
            if(value == original_combo.get()):
                from_languages_key = key

        for key,value in languages.items():
            if(value == translated_combo.get()):
                to_languages_key = key
    
        words = textblob.TextBlob(original_text.get(1.0,END))
        words = words.translate(from_lang=from_languages_key,to=to_languages_key)
        translated_text.insert(1.0,words)
    
    except Exception as e: 
        messagebox.showerror("Translator" ,e )
    
def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)
    
#grap languages
languages = googletrans.LANGUAGES
language_list = list(languages.values())



#text box
original_text = Text(root,height=10,width=40)
original_text.grid(row=0,column=0,pady=20,padx=10)

translated_button= Button(root,text="translate",font=("Helvetica",24),command=translate_it)
translated_button.grid(row=0,column=1,padx=10)

translated_text = Text(root,height=10,width=40)
translated_text.grid(row=0,column=2,pady=20,padx=10)

#combo boxes
original_combo=ttk.Combobox(root,width=50,values=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)

translated_combo=ttk.Combobox(root,width=50,values=language_list)
translated_combo.current(26)
translated_combo.grid(row=1,column=2)

#clear button
clear_button = Button(root,text="clear",command=clear)
clear_button.grid(row=2,column=1) 


root.mainloop()