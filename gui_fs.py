from tkinter import*
root = Tk()
root.title("tkinter full screen window")
Label(root,text="Full Screen").grid(row=1,column=1,padx=50,pady=50)
Button(root,text="exit",command=root.destroy).grid(row=2,column=5,padx=55,pady=60)
root.attributes("fullscreen",True)

root.mainloop()