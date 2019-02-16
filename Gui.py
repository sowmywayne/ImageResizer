from tkinter import *
from resize import imConvertor


main_windows = Tk()
main_windows.geometry("700x300")
main_windows.title("Resizer")




input_path = StringVar()
input_ratio = IntVar()

def msg():
	imConvertor(input_path.get(), input_ratio.get())
	l3.config(text = 'Images are resized')



    
l1 = Label(main_windows, text="Enter The Path ").place(x=170, y=54)
input_txt_box1 = Entry(main_windows, textvariable=input_path).place(x=300, y=50)
l2 = Label(main_windows, text = 'Enter the ratio of image').place(x = 170, y = 90)
input_txt_box2 = Entry(main_windows, textvariable = input_ratio).place(x = 350, y = 85)
b1 = Button(main_windows, text="OK", command=msg).place(x=170, y=140)


l3 = Label(main_windows)
l3.place(x = 150, y = 140)

main_windows.mainloop()