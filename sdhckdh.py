import tkinter as tk
from tkinter import messagebox
from preprocessingAlgorithm.tokenizeAlgorithm import tokenization
from preprocessingAlgorithm.loweercaseAlgorithm import lowercase
from preprocessingAlgorithm.frequencyCounterAlgorithm import frequencyCounter
from preprocessingAlgorithm.porterStemmerAlgorithm import to_stem





color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'


preprocessing_label = "Preprocessing"
classification_label = "Classification"
information_retrieval_label = "IR"


def create_root():
    root = tk.Tk()
    root.title("Welcome to NLP world!")
    root.geometry("700x800+100+100")
    root.resizable(width=False, height=False)
    return root


def create_main_frame(root):
    main_frame = tk.Frame(root, bg=color1, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=4)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    return main_frame



root = create_root()
main_frame = create_main_frame(root)



def create_button(main_frame, label, command):
    button = tk.Button(
        main_frame,
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightcolor='WHITE',
        width=13,
        height=2,
        border=3,
        cursor='Spider',
        text=label,
        command=command
    )
    return button




def create_preprocessing_frame(main_frame):
    preprocessing_frame = tk.Frame(main_frame, bg=color1, pady=40)
    preprocessing_frame.grid(row=0, column=1, rowspan=5, sticky='NSEW', padx=20, pady=10)


    

    
    def read_text_file(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return text


    file_path = '61085-0.txt'
    text = read_text_file(file_path)   

    def tokenizing():

        tokens = tokenization(text)
        text_field.delete(1.0 , tk.END)
        tokenized_text = "\n".join(tokens)
        text_field.insert(tk.END , tokenized_text)
        

    def lowercasing():

        lowercased_text = lowercase(text)
        text_field.delete(1.0 , tk.END)
        text_field.insert(tk.END , lowercased_text)
        

    def stemming():
        stemmed_text = to_stem(text)
        text_field.delete(1.0 , tk.END)
        text_field.insert(tk.END ,stemmed_text)

    def frequencyCounting() :

        frequencies = frequencyCounter(text)
        text_field.delete(1.0 , tk.END)
        text_field.insert(tk.END ,frequencies)
        



    scrollbar = tk.Scrollbar(preprocessing_frame)
    scrollbar.grid(row=3, column=1, rowspan=2, sticky='NS', padx=(0, 20), pady=10) 


    text_field = tk.Text(
    preprocessing_frame,
    width=50,
    height=40,
    background='WHITE',
    highlightbackground=color2,
    highlightcolor=color2,
    bd=3,
    highlightthickness=2,
    relief=tk.SOLID,
    yscrollcommand=scrollbar.set,
)
    

    
    
    text_field.grid(column=0, row=4, rowspan=2, sticky='W', padx=20, pady=10)
    text_field.insert(tk.END, text)

    scrollbar.config(command=text_field.yview)

    tokenize_btn = create_button(preprocessing_frame, "Tokenize", tokenizing)
    lowercase_btn = create_button(preprocessing_frame, "Lowercase", lowercasing)
    frequency_counter_btn = create_button(preprocessing_frame, "Frequency Counter" ,frequencyCounting)
    stemming_btn = create_button(preprocessing_frame, "Stemming", stemming)

    tokenize_btn.grid(column=0, row=0, sticky='W', padx=20, pady=10)
    lowercase_btn.grid(column=0, row=1, sticky='W', padx=20, pady=10)
    frequency_counter_btn.grid(column=0, row=2, sticky='W', padx=20 , pady=10) 
    stemming_btn.grid(column=0, row=3, sticky='W', padx=20, pady=10)

    
    


def preprocessing_btn_click():
    create_preprocessing_frame(main_frame)


def classification_btn_click():
    messagebox.showinfo("Button Clicked", "Classification button clicked!")


def information_retrieval_btn_click():
    messagebox.showinfo("Button Clicked", "Information Retrieval button clicked!")





preprocessing_btn = create_button(main_frame, preprocessing_label, preprocessing_btn_click)
classification_btn = create_button(main_frame, classification_label, classification_btn_click)
information_retrieval_btn = create_button(main_frame, information_retrieval_label, information_retrieval_btn_click)


preprocessing_btn.grid(column=0, row=0, sticky='W', padx=20, pady=10)
classification_btn.grid(column=0, row=1, sticky='W', padx=20, pady=10)
information_retrieval_btn.grid(column=0, row=2, sticky='W', padx=20, pady=10)    





root.mainloop()
