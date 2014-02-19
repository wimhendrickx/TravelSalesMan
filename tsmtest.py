from biz.country import country
from biz.country import city

from Tkinter import *

master = Tk()


w = Canvas(master, width=1000, height=1000)
w.pack()

c = country(10,500,500)
c.printCities()
c.drawCities(w)
print('---')
c1 = c.getRandomCity()
print(c1)
c2 = c.GetClosestCity(c1)
print(c2)

w.create_line(c1.getXLoc(),c1.getYLoc(),c2.getXLoc(),c2.getYLoc(),arrow="last")

mainloop()

