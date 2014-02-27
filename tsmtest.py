from biz.country import country
from biz.country import city

from Tkinter import *


master = Tk()


w = Canvas(master, width=500, height=500)
w.pack()

c = country(12,500,500)
c.printCities()
c.drawCities(w)
c1 = c.getRandomCity()
c2 = c.GetClosestCity(c1)
c.printAllPermutations(w)

#w.create_line(c1.getXLoc(),c1.getYLoc(),c2.getXLoc(),c2.getYLoc(),arrow="last")

mainloop()

