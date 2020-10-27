#A Program for quickly determening if an item is needed to be found in raid for a quest.

from tkinter import *
loot = ["Paracord", "Corrugated Hose", "Malboro cigarettes", "Wilston cigarettes", "Strike cigarettes", "Horse figurine", "Cat figurine", "Bronze Lion", "Gas analyzer", "Military COFDM wireless signal transmitter", "uhf RFID reader", "VPX flash storage module", "Virtex programmable processor", "Capacitors", "Wires", "Wd-40 100ml", "Car battery", "Spark plug", "Broken gphone", "CPU fan", "PC CPU", "Printed circuit board", "Graphics card", "Powercord", "T-Shaped plug", "Antique vase", "Antique teapot", "Silver badge", "Clin wiper", "Portable defibrillator", "Medical bloodset", "Ox bleach", "5l propane tank", "Fuel Conditioner", "Heat-exchange alkali surface washer", "Rechargeable battery", "Secure flash drive", "42nd signature blend english tea", "Golden rooster", "Roler submariner gold wrist watch", "Battered antique book", "Fireklean gun lube", "Old firesteel", "Deadlyslob's beard oil", "Golden 1gphone", "6-sten-140-m military battery", "Ofz 30x160mm shell", "KEKtape duct tape", "Raven figurine", "Ripstop cloth", "Aramid fiber cloth", "Fleece cloth", "Polyamide fabric Cordura", "Can of dr. lupo's coffee beans", "Veritas guitar pick" ]
x=0
root = Tk()

# Creating a Label Widget
while x<len(loot)-1:
    evenList = Label(root, text=loot[x])
    evenList.grid(row=x, column=0)
    x=x+1
    oddList = Label(root, text=loot[x])
    oddList.grid(row=x-1, column=1)
    x=x+1

root.mainloop()
