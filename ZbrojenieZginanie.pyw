from ZbrZgBaza.ZbrZg import znajdz
from ZbrZgBaza.ZbrZg2 import Wartosci
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


class Gui(Frame):
    def __init__(self,master):
        super(Gui,self).__init__(master)

        self.lbl1=Label(master,text="Moment obliczeniowy MEd [kNm]:")
        self.lbl1.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        self.entr1=Entry(master,justify='center')
        self.entr1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.entr1.insert(END,"150")

        self.lbl001 = Label(master, text="Siła osiowa NEd [kNm]:"+"\n"+"(wartość dodatnia - rozciąganie)")
        self.lbl001.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.entr1001=Entry(master,justify='center')
        self.entr1001.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self.entr1001.insert(END,"0")

        self.lbl2 = Label(master, text="Szerokość elementu b [mm]:")
        self.lbl2.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.entr2 = Entry(master, justify='center')
        self.entr2.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.entr2.insert(END, "200")

        self.lbl002 = Label(master, text="Wysokość elementu h [mm]:")
        self.lbl002.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        self.entr1002 = Entry(master, justify='center')
        self.entr1002.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.entr1002.insert(END, "500")

        self.lbl3 = Label(master, text="Wymiar a1 [mm]:")
        self.lbl3.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.entr3 = Entry(master, justify='center')
        self.entr3.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        self.entr3.insert(END, "50")

        self.lb500 = Label(master, text="Wymiar a2 [mm]:")
        self.lb500.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        self.entr500 = Entry(master, justify='center')
        self.entr500.grid(row=5, column=1, padx=5, pady=5, sticky=W)
        self.entr500.insert(END, "50")

        self.lbl4 = Label(master, text="Klasa betonu:")
        self.lbl4.grid(row=6, column=0, padx=5, pady=5, sticky=W)

        self.combo1 = Combobox(master,values=("C12/15","C16/20","C20/25","C25/30","C30/37","C35/45","C40/50","C45/55","C50/60"))
        self.combo1.grid(row=6, column=1, padx=5, pady=5, sticky=W)
        self.combo1.current(4)

        self.lbl5 = Label(master, text="Współczynnik bezpieczeństwa gc:")
        self.lbl5.grid(row=7, column=0, padx=5, pady=5, sticky=W)

        self.entr5 = Entry(master, justify='center')
        self.entr5.grid(row=7, column=1, padx=5, pady=5, sticky=W)
        self.entr5.insert(END, "1.4")

        self.lbl6 = Label(master, text="Współczynnik bezpieczeństwa acc:")
        self.lbl6.grid(row=8, column=0, padx=5, pady=5, sticky=W)

        self.entr6 = Entry(master, justify='center')
        self.entr6.grid(row=8, column=1, padx=5, pady=5, sticky=W)
        self.entr6.insert(END, "1.00")

        self.btt1=Button(master,text="OBLICZ",command=self.zbrojenie)
        self.btt1.grid(row=9,column=0,columnspan=2,padx=5,pady=5,sticky=W+E+N+S)

        self.btt2 = Button(master,text="ZAMKNIJ",command=self.close_window)
        self.btt2.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=W + E + N + S)


        self.lbll7 = Label(master, text="Wytrzymałość betonu fcd [MPa]:")
        self.lbll7.grid(row=11, column=0, padx=5, pady=5, sticky=W)

        self.lbll8 = Label(master, text="")
        self.lbll8.grid(row=11, column=1, padx=5, pady=5, sticky=W)

        self.lbll9 = Label(master, text="Współczynnik w:")
        self.lbll9.grid(row=13, column=0, padx=5, pady=5, sticky=W)

        self.Etr01 = Entry(master,justify='center')
        self.Etr01.grid(row=13, column=1, padx=5, pady=5, sticky=W)

        self.lbl11 = Label(master, text="Naprężenia w stali Ss1 [MPa]:")
        self.lbl11.grid(row=14, column=0, padx=5, pady=5, sticky=W)

        self.Etr02 = Entry(master,justify='center')
        self.Etr02.grid(row=14, column=1, padx=5, pady=5, sticky=W)

        self.lbl13 = Label(master, text="Zbrojenie wymagane As1,erf [cm2]:")
        self.lbl13.grid(row=15, column=0, padx=5, pady=5, sticky=W)

        self.Etr03 = Entry(master,justify='center')
        self.Etr03.grid(row=15, column=1, padx=5, pady=5, sticky=W)

        self.lbl1400 = Label(master, text="Zbrojenie wymagane As2,erf [cm2]:")
        self.lbl1400.grid(row=16, column=0, padx=5, pady=5, sticky=W)

        self.Etr0004 = Entry(master, justify='center')
        self.Etr0004.grid(row=16, column=1, padx=5, pady=5, sticky=W)

        self.lbl201 = Label(master, text="Współczynnik ni:")
        self.lbl201.grid(row=12, column=0, padx=5, pady=5, sticky=W)

        self.Etr04 = Entry(master,justify='center')
        self.Etr04.grid(row=12, column=1, padx=5, pady=5, sticky=W)

    def close_window(self):
        self.master.destroy()

    def zbrojenie(self):

        self.Etr04.delete(0,END)
        self.Etr01.delete(0,END)
        self.Etr02.delete(0,END)
        self.Etr03.delete(0,END)
        self.Etr0004.delete(0, END)

        MEd=float(self.entr1.get())
        NEd = float(self.entr1001.get())
        h = float(self.entr1002.get()) / 1000
        b=float(self.entr2.get())/1000
        d1=float(self.entr3.get())/1000

        d=h-d1

        d2=float(self.entr500.get())/1000
        d2d=d2/d

        zs1=d-0.5*h

        MEds=MEd-NEd*zs1

        #messagebox.showerror("Error", d2d)


        fcd=float(self.combo1.get()[1:3])*float(self.entr6.get())/float(self.entr5.get())*1000
        self.lbll8["text"]=str(round(fcd/1000,2))

        ni=MEds/(b*d**2*fcd)

        if ni <= 0.371:
            self.Etr04.insert(END, str(round(ni, 5)))

            ss1 = znajdz(ni)[5] * 1000
            self.Etr02.insert(END, str(ss1 / 1000))

            w = znajdz(ni)[0]
            self.Etr01.insert(END, str(round(w, 5)))

            As1 = 1 / ss1 * (w * b * d * fcd+NEd) * 10000
            self.Etr03.insert(END, str(round(As1, 2)))

            As2=0
            self.Etr0004.insert(END, str(round(As2, 2)))

        elif ni>0.371 and ni<0.38:

            self.Etr04.insert(END, str(round(ni, 5)))

            ss1 = znajdz(0.371)[5] * 1000
            self.Etr02.insert(END, str(ss1 / 1000))

            w = znajdz(0.371)[0]
            self.Etr01.insert(END, str(round(w, 5)))

            As1 = 1 / ss1 * (w * b * d * fcd+NEd) * 10000
            self.Etr03.insert(END, str(round(As1, 2)))

            As2 = 0
            self.Etr0004.insert(END, str(round(As2, 2)))

        elif ni>=0.38 and ni <=0.60:

            self.Etr04.insert(END, str(round(ni, 5)))

            #ss1 = znajdz(0.371)[5] * 1000
            self.Etr02.insert(END, "")

            #w = znajdz(0.371)[0]
            self.Etr01.insert(END, "")

            w1=Wartosci(ni,d2d)[0]
            w2=Wartosci(ni, d2d)[1]

            As1 = 1 / 434.8 * (w1 * b * d * fcd/1000+NEd)*10000
            self.Etr03.insert(END, str(round(As1, 2)))

            As2 = w2*b*d*fcd/434.8/1000*10000
            self.Etr0004.insert(END, str(round(As2, 2)))

            #print(d)












#czesc glowna
okno=Tk()
okno.title("Zbrojenie na zginanie")
okienko = Gui(okno)
okno.mainloop()

#MEd=4900
#b=0.25
#d=2.565
#fcd=19800
#ni=MEd/(b*d**2*fcd)

#ss1=znajdz(ni)[5]*1000
#w=znajdz(ni)[0]

#As1=1/ss1*(w*b*d*fcd)*10000

#print('Omega w= '+str(round(w,5)))
#print('Naprężenia ss1= '+str(ss1/1000)+' MPa')
#print('Zbrojenie wymagane As1= '+str(round(As1,2))+' cm2')
