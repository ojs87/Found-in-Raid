from tkinter import *
import sqlite3

root = Tk()
root.title("Found in Raid")

# alphabetically sorted list for the label name

loot = ['3-(b-TG)', '41nd signature blend english tea', '5l propane tank', '6-sten-140-m military battery', 'AHF1-M', 'Antique axe', 'Antique teapot', 'Antique vase', 'Aramid fiber cloth', 'Bars A-2607- 95x18', 'Battered antique book', 'BlackRock chest rig', 'Broken gphone', 'Bronze Lion', 'CMS kit', 'CPU fan', 'Can of beef stew', "Can of dr. lupo's coffee beans", 'Can of sprats', 'Capacitors', 'Car battery', 'Cat figurine', 'Clin wiper', 'Cocktail "Obdolbos"', 'Corrugated Hose', "Deadlyslob's beard oil", 'Fake mustache', 'Fireklean gun lube', 'Fleece cloth', 'Fuel Conditioner', 'Gas analyzer', 'Golden 1gphone', 'Golden rooster', 'Graphics card', 'Heat-exchange alkali surface washer', 'Horse figurine', 'Jar of DevilDog mayo', 'KEKtape duct tape', 'Kotton beanie', 'L1 (Norepinephrine)', 'Lower half-mask', 'M.U.L.E. stimulator', 'Malboro cigarettes', 'Maska 1Sch helmet', 'Medical bloodset', 'Meldonin', 'Military COFDM wireless signal transmitter', 'Morphine injector', 'Ofz 30x160mm shell', 'Old firesteel', 'Ox bleach', 'P22', 'PC CPU', 'Paracord', 'Pestily plague mask', 'Pilgrim tourist backpack', 'Polyamide fabric Cordura', 'Portable defibrillator', 'Powercord', 'Printed circuit board', 'Raven figurine', 'Rechargeable battery', 'Respirator', 'Ripstop cloth', 'Roler submariner gold wrist watch', 'Secure flash drive', 'Shroud half-mask', 'Shturman key', 'Silver badge', 'Spark plug', 'Strike cigarettes', 'T-Shaped plug', 'TT pistol 7.62x25 TT Gold', 'Uhf RFID reader', 'VPX flash storage module', 'Veritas guitar pick', 'Virtex programmable processor', 'Wartech gear rig', 'Wd-40 100ml', 'Wilston cigarettes', 'Wires']

#create the initial value labels from the database
def createLabels():
    #open database
    conn = sqlite3.connect('item_book2.db')

    #create the database cursor
    c = conn.cursor()

    #get all files from database and put them in a list called records
    c.execute("SELECT *, oid FROM fir_items")
    records=c.fetchall()

    #close database
    conn.commit()
    conn.close()

    #create initial valuse for columns 2 and 6 from the records list, i.e 1/3
    x=0
    for a in records:
        questadd = a[2] + a[3]
        records1 = str(a[5]) + " / " + str(questadd)
        showcurrent = Label(root, text=records1, width=10)

        if x < len(records)/2:
            showcurrent.grid(row=x, column=2)
        else:
            showcurrent.grid(row=int(x-41), column=6)

        x += 1

#create the initial labelsfrom the loot list/buttons
def createButtons():

    #create the item name labels from the loot list
    x=0

    #first column
    while x < 41:
        Label(root, text=loot[x], width=35).grid(row=x, column=0)
        x += 1

    #second column
    while x < 81:
        Label(root, text=loot[x], width=35).grid(row=x-41, column=4)
        x += 1

    #create subtract buttons
    x=0
    #first column
    while x < 41:
        Button(root, text="-", width=4, command=lambda x=x+1:subone(x)).grid(row=x, column=1) #lambda x=x+1 used so the button command will take the value of x+1 at the time of creating, not the last value of x(ie 54)
        x += 1
    #second column
    while x < 81:
        Button(root, text="-", width=4, command=lambda x=x+1:subone(x)).grid(row=x-41, column=5)
        x += 1

    #create add buttons
    x=0

    #first column
    while x < 41:
        Button(root, text="+", width=4, command=lambda x=x+1:addone(x)).grid(row=x, column=3)
        x += 1

    #second column
    while x < 81:
        Button(root, text="+", width=4, command=lambda x=x+1:addone(x)).grid(row=x-41, column=7)
        x += 1

#function for adding 1 to the database value and redrawing the value on screen
def addone(record_id):

    conn = sqlite3.connect('item_book2.db')
    c = conn.cursor()

    #add one to the mycount value in the database for the specific button that was pressed
    c.execute("UPDATE fir_items SET mycount=mycount + 1 WHERE oid = :oid", {'oid': record_id})

    #get the specific record for the button that was pressed
    c.execute("SELECT *, oid FROM fir_items WHERE oid = :oid",{'oid': record_id})

    #create a list of 1 for the record
    records = c.fetchall()

    #create variables for updating the labels
    questadd = records[0][2] + records[0][3]
    records1 = str(records[0][5]) + " / " + str(questadd)

    #make the value label pink if mycount equals the number of items needed
    if records[0][5] >= questadd:
        showcurrent = Label(root, text=records1, width=10, bg="pink")
    else:
        showcurrent = Label(root, text=records1, width=10)

    #place the new label onto the screen with grid()
    if record_id - 1 < 41:
        showcurrent.grid(row=record_id - 1, column = 2)
    else:
        showcurrent.grid(row=record_id - 42, column = 6)

    conn.commit()
    conn.close()

#function for subtracting 1 to the database value and redrawing the value on screen
def subone(record_id):

    conn = sqlite3.connect('item_book2.db')
    c = conn.cursor()

    c.execute("UPDATE fir_items SET mycount=mycount - 1 WHERE oid = :oid", {'oid': record_id})

    c.execute("SELECT *, oid FROM fir_items WHERE oid = :oid",{'oid': record_id})
    records = c.fetchall()

    #check if mycount is going to be a negative number and return if so
    if records[0][5] < 0:
        return

    questadd = records[0][2] + records[0][3]
    records1 = str(records[0][5]) + " / " + str(questadd)

    if records[0][5] >= questadd:
        showcurrent = Label(root, text=records1, width=10, bg="pink")
    else:
        showcurrent = Label(root, text=records1, width=10)

    if record_id - 1 < 41:
        showcurrent.grid(row=record_id - 1, column = 2)
    else:
        showcurrent.grid(row=record_id - 42, column = 6)

    conn.commit()
    conn.close()

#run the stuff
createLabels()
createButtons()

root.mainloop()
