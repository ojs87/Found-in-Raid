loot = ["Paracord", "Corrugated Hose", "Malboro cigarettes", "Wilston cigarettes", "Strike cigarettes", "Horse figurine", "Cat figurine", "Bronze Lion", 
        "Gas analyzer", "Military COFDM wireless signal transmitter", "Uhf RFID reader", "VPX flash storage module", "Virtex programmable processor", 
        "Capacitors", "Wires", "Wd-40 100ml", "Car battery", "Spark plug", "Broken gphone", "CPU fan", "PC CPU", "Printed circuit board", "Graphics card", 
        "Powercord", "T-Shaped plug", "Antique vase", "Antique teapot", "Silver badge", "Clin wiper", "Portable defibrillator", "Medical bloodset", "Ox bleach", 
        "5l propane tank", "Fuel Conditioner", "Heat-exchange alkali surface washer", "Rechargeable battery", "Secure flash drive", "42nd signature blend english tea", 
        "Golden rooster", "Roler submariner gold wrist watch", "Battered antique book", "Fireklean gun lube", "Old firesteel", "Deadlyslob's beard oil", "Golden 1gphone", 
        "6-sten-140-m military battery", "Ofz 30x160mm shell", "KEKtape duct tape", "Raven figurine", "Ripstop cloth", "Aramid fiber cloth", "Fleece cloth", 
        "Polyamide fabric Cordura", "Can of dr. lupo's coffee beans", "Veritas guitar pick" ]

items_file = open("Items.txt", "a")
x=0

while x < len(loot):
    items_file.write(loot[x] + "\n")
    x += 1

items_file.close()