from tkinter import *
from tkinter import messagebox

class Form():
    def __init__(self):
        window = Tk()
        window.title("The Member Information Form")
        window.geometry("500x300")
        self._frame = Frame(window, width=500, height=400)
        self._frame.place(x=15,y=25)

        # label

        lblWarning = Label(window, text="Please fill the options respectively!", fg="purple")
        lblWarning.place(x=15,y=25)

        # Radiobuttons

        rbVar = StringVar()
        rbVar.set(" ")
        rbPersonal = Radiobutton(window, text="Personal Informations", variable=rbVar, value="1",command=self.personal)
        rbEducation = Radiobutton(window, text="Education Informations", variable=rbVar, value="2",command=self.education)
        rbExperience = Radiobutton(window, text="Your Experiences", variable=rbVar, value="3",command=self.experience)
        rbHobbies = Radiobutton(window, text="Your Hobbies", variable=rbVar, value="4",command=self.hobby)

        rbPersonal.place(x=15,y=50)
        rbEducation.place(x=15,y=75)
        rbExperience.place(x=15,y=100)
        rbHobbies.place(x=15,y=125)

        
        window.mainloop()

    def personal(self):

        for i in self._frame.winfo_children():
            i.destroy()

        # labels 

        lblName = Label(self._frame, text="Name:", fg="dark green")
        lblSurname = Label(self._frame, text="Surname:", fg="dark green")
        lblId = Label(self._frame, text="Id:", fg="dark green")


        lblName.place(x=200,y=25)
        lblSurname.place(x=200,y=50)
        lblId.place(x=200,y=75)

        # entry boxes

        self._nameVar = StringVar()
        self._surnameVar = StringVar()
        self._idVar = StringVar()

        entryName = Entry(self._frame, textvariable=self._nameVar)
        entrySurname = Entry(self._frame, textvariable=self._surnameVar)
        entryId = Entry(self._frame, textvariable=self._idVar)

        entryName.place(x=270, y=25)
        entrySurname.place(x=270,y=50)
        entryId.place(x=270,y=75)

        # button

        btnSavePersonal = Button(self._frame, text="Save",fg="dark red", command=self.savePersonal)
        btnSavePersonal.place(x=315,y=105)

    def education(self):

        for i in self._frame.winfo_children():
            i.destroy()
        
        # labels

        lblPrimarySchool = Label(self._frame, text="Primary School:",fg="dark green")
        lblMiddleSchool = Label(self._frame, text="Middle School:", fg="dark green")
        lblHighSchool = Label(self._frame, text="High School:", fg="dark green")
        lblUniversity = Label(self._frame, text="University:", fg="dark green")

        lblPrimarySchool.place(x=200,y=25)
        lblMiddleSchool.place(x=200,y=50)
        lblHighSchool.place(x=200,y=75)
        lblUniversity.place(x=200,y=100)

        # entry boxes

        self._PrimarySchoolVar = StringVar()
        self._MiddleSchoolVar = StringVar()
        self._HighSchoolVar = StringVar()
        self._UniversityVar = StringVar()

        entryPrimary = Entry(self._frame, textvariable=self._PrimarySchoolVar)
        entryMiddle = Entry(self._frame, textvariable=self._MiddleSchoolVar)
        entryHigh = Entry(self._frame, textvariable=self._HighSchoolVar)
        entryUniversity = Entry(self._frame, textvariable=self._UniversityVar)

        entryPrimary.place(x=300, y=25)
        entryMiddle.place(x=300,y=50)
        entryHigh.place(x=300,y=75)
        entryUniversity.place(x=300,y=100)

        # button

        btnSaveEducation = Button(self._frame, text="Save", command=self.saveEducation)
        btnSaveEducation.place(x=340,y=130)

    def experience(self):

        for i in self._frame.winfo_children():
            i.destroy()

        # label

        lblWarning = Label(self._frame, text="Please click the save button after every experience!", fg="dark red")
        lblWarning.place(x=200,y=25)

        # entry boxes

        self._experienceVar = StringVar()
        entryExperience = Entry(self._frame, textvariable=self._experienceVar)
        entryExperience.place(x=250, y=50)

        btnSaveExperience = Button(self._frame, text="Save", command=self.saveExperience)
        btnSaveExperience.place(x=290,y=80)

    def hobby(self):

        for i in self._frame.winfo_children():
            i.destroy()
        
        # label

        lblWarning = Label(self._frame, text="Please click the save button after every hobby!", fg="dark red")
        lblWarning.place(x=200,y=25)

        # entry boxes

        self._hobbyVar = StringVar()
        entryHobby = Entry(self._frame, textvariable=self._hobbyVar)
        entryHobby.place(x=250, y=50)

        btnSaveHobby = Button(self._frame, text="Save", command=self.saveHobby)
        btnSaveHobby.place(x=290,y=80)

    def savePersonal(self):

        if len(self._idVar.get()) == 11 and len(self._nameVar.get())!=0 and len(self._surnameVar.get())!=0:
            with open("members.txt","a",encoding="utf-8") as file:
                file.write(f"Name: {self._nameVar.get()}\nSurname: {self._surnameVar.get()}\nId: {self._idVar.get()}\n")
            messagebox.showinfo("To Inform","Your personal informations were saved.")
            self._nameVar.set("")
            self._surnameVar.set("")
            self._idVar.set("")
        else:
            messagebox.showinfo("To Inform","Please enter your name and surname. Your id should be 11 digits.")
    
    def saveEducation(self):

        if len(self._PrimarySchoolVar.get()) !=0 and len(self._MiddleSchoolVar.get())!=0 and len(self._HighSchoolVar.get())!=0 and len(self._UniversityVar.get())!=0:
            with open("members.txt","a",encoding="utf-8") as file:
                file.write(f"Primary School: {self._PrimarySchoolVar.get()}\nMiddle School: {self._MiddleSchoolVar.get()}\nHigh School: {self._HighSchoolVar.get()}\nUniversity: {self._UniversityVar.get()}\n")
            messagebox.showinfo("To Inform","Your education informations were saved.")
            self._PrimarySchoolVar.set("")
            self._MiddleSchoolVar.set("")
            self._HighSchoolVar.set("")
            self._UniversityVar.set("")
        else:
            messagebox.showinfo("To Inform","Please enter your primary school, middle school, high school, university.")

    def saveExperience(self):
        if len(self._experienceVar.get()) !=0:
            with open("members.txt","a",encoding="utf-8") as file:
                file.write(f"Experience: {self._experienceVar.get()}\n")
            messagebox.showinfo("To Inform","Your experience information was saved.")
            self._experienceVar.set("")
        else:
            messagebox.showinfo("To Inform","Please enter your experience.")
            
    def saveHobby(self):
        if len(self._hobbyVar.get())!=0:
            with open("members.txt","a",encoding="utf-8") as file:
                file.write(f"Hobby: {self._hobbyVar.get()}\n")
            messagebox.showinfo("To Inform","Your hobby information was saved.")
            self._hobbyVar.set("")
        else:
            messagebox.showinfo("To Inform","Please enter your hobby.")

Form()