from Client import *
import tkinter as tk
from PIL import Image, ImageTk

from Pixiv import UpdateImageFolder


def GUI(user, tag, offset, limit):
    def send():
        global selected_List
        AddSticker([imageList[i] for i in selected_List])
        for i in selected_List:
            clickevent(i)
        selected_List = []

    def clickevent(index):
        if buttonList[index].cget('relief') == tk.RAISED: 
            buttonList[index].config(relief=tk.SUNKEN, borderwidth=5)
            selected_List.append(index) 
        else:
            buttonList[index].config(relief=tk.RAISED, borderwidth=1.5)
            selected_List.remove(index)

    window = tk.Tk()
    window.title('更新圖片')
    window.attributes('-topmost', True)

    selectFrame = tk.Frame(window)
    selectFrame.grid(row=0, column=0, pady=5)
    selected_List = []

    operationFrame = tk.Frame(window)
    operationFrame.grid(row=1, column=0, pady=5)

    imageList = UpdateImageFolder(user=user, tag=tag, offset=offset, limit=limit)
    num_in_a_row = 5
    buttonList: List[tk.Button] = []
    imagetkList: List[ImageTk.PhotoImage] = []

    for i in range(len(imageList)):
        img = Image.open(imageList[i])
        #Resize the Image using resize method
        resized_image= img.resize((100, 100), Image.LANCZOS)
        imagetkList.append(ImageTk.PhotoImage(resized_image))

    for i in range(len(imageList)):
        button = tk.Button(selectFrame, image=imagetkList[i])
        button.grid(row=(i//num_in_a_row), column=(i%num_in_a_row), padx=2, pady=2)
        button.config(command=lambda x = i: clickevent(x))
        buttonList.append(button)

    send_button = tk.Button(operationFrame, text="Send")
    send_button.config(command=send)
    send_button.grid()

    window.mainloop()