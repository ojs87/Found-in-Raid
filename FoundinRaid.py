from tkinter import *
import sqlite3

root = Tk()
root.title("Hello")

# alphabetically sorted list for the label name
loot = ['42nd signature blend english tea', '5l propane tank', '6-sten-140-m military battery', 'Antique teapot', 'Antique vase', 'Aramid fiber cloth', 'Battered antique book', 'Broken gphone', 'Bronze Lion', 'CPU fan', "Can of dr. lupo's coffee beans", 'Capacitors', 'Car battery', 'Cat figurine', 'Clin wiper', 'Corrugated Hose', "Deadlyslob's beard oil", 'Fireklean gun lube', 'Fleece cloth', 'Fuel Conditioner', 'Gas analyzer', 'Golden 1gphone', 'Golden rooster', 'Graphics card', 'Heat-exchange alkali surface washer', 'Horse figurine', 'KEKtape duct tape', 'Malboro cigarettes', 'Medical bloodset', 'Military COFDM wireless signal transmitter', 'Ofz 30x160mm shell', 'Old firesteel', 'Ox bleach', 'PC CPU', 'Paracord', 'Polyamide fabric Cordura', 'Portable defibrillator', 'Powercord', 'Printed circuit board', 'Raven figurine', 'Rechargeable battery', 'Ripstop cloth', 'Roler submariner gold wrist watch', 'Secure flash drive', 'Silver badge', 'Spark plug', 'Strike cigarettes', 'T-Shaped plug', 'Uhf RFID reader', 'VPX flash storage module', 'Veritas guitar pick', 'Virtex programmable processor', 'Wd-40 100ml', 'Wilston cigarettes', 'Wires']

conn = sqlite3.connect('item_book.db')
c = conn.cursor()
c.execute("SELECT *, oid FROM addresses")
records=c.fetchall()
conn.commit()
conn.close()

x=0
#create the initial labels/buttons and values in the database
def createButtons():
    x=0
    for a in records:
        questadd = a[2] + a[3]
        records1 = str(a[5]) + " / " + str(questadd)
        showcurrent = Label(root, text=records1, width=10)

        if x < len(records)/2:
            showcurrent.grid(row=x, column=2)
        else:
            showcurrent.grid(row=int(x-28), column=6)

        x += 1

    x=0
    while x < 28:
        Label(root, text=loot[x], width=35).grid(row=x, column=0)
        x += 1

    while x < 55:
        Label(root, text=loot[x], width=35).grid(row=x-28, column=4)
        x += 1

    x=0
    while x < 28:
        Button(root, text="-", width=4, command=lambda x=x+1:subone(x)).grid(row=x, column=1) #lambda x=x+1 used so the button command will take the value of x+1 at the time of creating, not the last value of x(ie 54)
        x += 1

    while x < 55:
        Button(root, text="-", width=4, command=lambda x=x+1:subone(x)).grid(row=x-28, column=5)
        x += 1

    x=0
    while x < 28:
        Button(root, text="+", width=4, command=lambda x=x+1:addone(x)).grid(row=x, column=3)
        x += 1

    while x < 55:
        Button(root, text="+", width=4, command=lambda x=x+1:addone(x)).grid(row=x-28, column=7)
        x += 1

#function for adding 1 to the database value and redrawing the value on screen
def addone(record_id):

    conn = sqlite3.connect('item_book.db')
    c = conn.cursor()

    c.execute("UPDATE addresses SET mycount=mycount + 1 WHERE oid = :oid", {'oid': record_id})

    c.execute("SELECT *, oid FROM addresses WHERE oid = :oid",{'oid': record_id})
    records = c.fetchall()

    questadd = records[0][2] + records[0][3]
    records1 = str(records[0][5]) + " / " + str(questadd)
    showcurrent = Label(root, text=records1, width=10)

    if record_id - 1 < 28:
        showcurrent.grid(row=record_id - 1, column = 2)
    else:
        showcurrent.grid(row=record_id - 29, column = 6)

    conn.commit()
    conn.close()

#function for subtracting 1 to the database value and redrawing the value on screen
def subone(record_id):

    conn = sqlite3.connect('item_book.db')
    c = conn.cursor()

    c.execute("UPDATE addresses SET mycount=mycount - 1 WHERE oid = :oid", {'oid': record_id})

    c.execute("SELECT *, oid FROM addresses WHERE oid = :oid",{'oid': record_id})
    records = c.fetchall()

    if records[0][5] < 0:
        return

    questadd = records[0][2] + records[0][3]
    records1 = str(records[0][5]) + " / " + str(questadd)
    showcurrent = Label(root, text=records1, width=10)



    if record_id - 1 < 28:
        showcurrent.grid(row=record_id - 1, column = 2)
    else:
        showcurrent.grid(row=record_id - 29, column = 6)

    conn.commit()
    conn.close()

createButtons()

root.mainloop()
