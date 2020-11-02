#A Program for quickly determening if an item is needed to be found in raid for a quest.

#importing the GUI library
from tkinter import *
from Itemclass import Lootinfo
import sqlite3

#Creating the list of loot items
loot = ["Paracord", "Corrugated hose", "Malboro cigarettes", "Wilston cigarettes", "Strike cigarettes", "Horse figurine", "Cat figurine", "Bronze Lion",
        "Gas analyzer", "Military COFDM wireless signal transmitter", "Uhf RFID reader", "VPX flash storage module", "Virtex programmable processor",
        "Capacitors", "Wires", "Wd-40 100ml", "Car battery", "Spark plug", "Broken gphone", "CPU fan", "PC CPU", "Printed circuit board", "Graphics card",
        "Powercord", "T-Shaped plug", "Antique vase", "Antique teapot", "Silver badge", "Clin wiper", "Portable defibrillator", "Medical bloodset", "Ox bleach",
        "5l propane tank", "Fuel Conditioner", "Heat-exchange alkali surface washer", "Rechargeable battery", "Secure flash drive", "42nd signature blend english tea",
        "Golden rooster", "Roler submariner gold wrist watch", "Battered antique book", "Fireklean gun lube", "Old firesteel", "Deadlyslob's beard oil", "Golden 1gphone",
        "6-sten-140-m military battery", "Ofz 30x160mm shell", "KEKtape duct tape", "Raven figurine", "Ripstop cloth", "Aramid fiber cloth", "Fleece cloth",
        "Polyamide fabric Cordura", "Can of dr. lupo's coffee beans", "Veritas guitar pick" ]

#creating loot objects from Lootinfo class
Paracord = Lootinfo(TRUE, "3", "0", "0", 0)
Corrugated_Hose = Lootinfo(TRUE, "2", "2", "26", 0)
Malboro_cigarettes = Lootinfo(TRUE, "5", "0", "0", 0)
Wilston_cigarettes = Lootinfo(TRUE, "5", "0", "0", 0)
Strike_cigarettes = Lootinfo(TRUE, "5", "0", "0", 0)
Horse_figurine = Lootinfo(TRUE, "2", "0", "0", 0)
Cat_figurine = Lootinfo(TRUE, "1", "0", "0", 0)
Bronze_Lion = Lootinfo(TRUE, "2", "0", "4", 0)
Gas_analyzer = Lootinfo(TRUE, "2", "0", "3", 1)
Military_COFDM_wireless_signal_transmitter = Lootinfo(TRUE, "1", "0", "2", 0)
Uhf_RFID_reader = Lootinfo(TRUE, "1", "0", "0", 0)
VPX_flash_storage_module = Lootinfo(TRUE, "1", "0", "2", 0)
Virtex_programmable_processor = Lootinfo(TRUE, "2", "0", "0", 0)
Capacitors = Lootinfo(TRUE, "5", "0", "12", 0)
Wires = Lootinfo(TRUE, "5", "0", "53", 0)
Wd40_100ml = Lootinfo(TRUE, "1", "0", "4", 0)
Car_battery = Lootinfo(TRUE, "4", "0", "5", 0)
Spark_plug = Lootinfo(TRUE, "8", "0", "5", 0)
Broken_gphone = Lootinfo(TRUE, "3", "0", "0", 0)
CPU_fan = Lootinfo(TRUE, "8", "0", "50", 0)
PC_CPU = Lootinfo(TRUE, "3", "0", "0", 0)
Printed_circuit_board = Lootinfo(TRUE, "2", "3", "10", 0)
Graphics_card = Lootinfo(TRUE, "3", "0", "0", 0)
Powercord = Lootinfo(TRUE, "2", "0", "13", 0)
TShaped_plug = Lootinfo(TRUE, "4", "0", "0", 0)
Antique_vase = Lootinfo(TRUE, "2", "0", "0", 0)
Antique_teapot = Lootinfo(TRUE, "3", "0", "0", 0)
Silver_badge = Lootinfo(TRUE, "1", "0", "0", 0)
Clin_wiper = Lootinfo(TRUE, "2", "0", "0", 0)
Portable_defibrillator = Lootinfo(TRUE, "1", "0", "0", 0)
Medical_bloodset = Lootinfo(TRUE, "3", "0", "2", 0)
Ox_bleach = Lootinfo(TRUE, "3", "0", "0", 0)
Fivel_propane_tank = Lootinfo(TRUE, "2", "0", "0", 0)
Fuel_Conditioner = Lootinfo(TRUE, "4", "0", "0", 0)
Heat_exchange_alkali_surface_washer = Lootinfo(TRUE, "2", "0", "2", 0)
Rechargeable_battery = Lootinfo(TRUE, "3", "0", "0", 0)
Secure_flash_drive = Lootinfo(TRUE, "2", "3", "3", 0)
Fortysecond_signature_blend_english_tea = Lootinfo(TRUE, "1", "0", "0", 0)
Golden_rooster = Lootinfo(TRUE, "1", "0", "0", 0)
Roler_submariner_gold_wrist_watch = Lootinfo(TRUE, "1", "0", "4", 0)
Battered_antique_book = Lootinfo(TRUE, "1", "0", "0", 0)
Fireklean_gun_lube = Lootinfo(TRUE, "1", "0", "1", 0)
Old_firesteel = Lootinfo(TRUE, "1", "0", "0", 0)
Deadlyslobs_beard_oil = Lootinfo(TRUE, "1", "0", "0", 0)
Golden_1gphone = Lootinfo(TRUE, "1", "0", "0", "1")
sixsten140m_military_battery = Lootinfo(TRUE, "1", "0", "0", 0)
Ofz_30x160mm_shell = Lootinfo(TRUE, "10", "0", "0", 0)
KEKtape_duct_tape = Lootinfo(TRUE, "5", "0", "0", 0)
Raven_figurine = Lootinfo(TRUE, "1", "0", "0", 0)
Ripstop_cloth = Lootinfo(TRUE, "10", "0", "0", 0)
Aramid_fiber_cloth = Lootinfo(TRUE, "5", "0", "0", 0)
Fleece_cloth = Lootinfo(TRUE, "10", "0", "0", 0)
Polyamide_fabric_Cordura = Lootinfo(TRUE, "10", "0", "0", 0)
Can_of_dr_lupos_coffee_beans = Lootinfo(TRUE, "1", "0", "0", 0)
Veritas_guitar_pick = Lootinfo(TRUE, "1", "0", "0", 0)

root = Tk()
root.title('List of Items That Need Found in Raid Status')

#Create a database or connect to one
conn = sqlite3.connect('item_book.db')

#create cursor
c = conn.cursor()

#create table

# c.execute("""CREATE TABLE addresses (
#         name text,
#         quest1 integer,
#         quest2 integer,
#         hideout integer,
#         mycount integer
# )""")



#commit changes
conn.commit()

#close connection
conn.close()

# Creating a Frame for the listed items
mainFrame = LabelFrame(root)
mainFrame.grid(row=0, column=0, columnspan=8, padx = 5, pady = 5)

#function for displaying how many Found in raid items you need for the first quest
def newwindow(listitem):
    bothquests = int(listitem.quest1) + int(listitem.quest2)
    howmanyitems = Label(mainFrame, text=bothquests, width=35)
    howmanyitems.grid(row=27, column=4)

def addtoclass(listitem):
    # newvalue = listitem.mycount + 1
    # bothquests = int(listitem.quest1) + int(listitem.quest2)
    # #outofhowmany = str(newvalue + "/" + bothquests)
    # howmanyitems = Label(mainFrame, text=str(newvalue) + "/" + str(bothquests))
    # howmanyitems.grid(row=27, column=4)

    #Create a database or connect to one
    conn = sqlite3.connect('item_book.db')

    #create cursor
    c = conn.cursor()
    record_id = listitem + 1


    c.execute("""UPDATE addresses SET
        mycount = mycount + 1
        WHERE oid = :oid""",
        {
        'oid': record_id
        })

    c.execute("SELECT *, oid FROM addresses WHERE oid = :oid",{'oid': record_id})
    records = c.fetchall()


    testlabel = Label(mainFrame, text=records[0][5], width=35)
    testlabel.grid(row=27, column=4)



    #commit changes
    conn.commit()

    #close connection
    conn.close()


def subtractfromclass(listitem):
    conn = sqlite3.connect('item_book.db')

    #create cursor
    c = conn.cursor()
    record_id = listitem + 1


    c.execute("""UPDATE addresses SET
        mycount = mycount - 1
        WHERE oid = :oid""",
        {
        'oid': record_id
        })

    c.execute("SELECT *, oid FROM addresses WHERE oid = :oid",{'oid': record_id})
    records = c.fetchall()

    if records[0][5] == -1:
        return

    testlabel = Label(mainFrame, text=records[0][5], width=35)
    testlabel.grid(row=27, column=4)



    #commit changes
    conn.commit()

    #close connection
    conn.close()

# Creating a Button Widget for each loot item
#while x<len(loot)-1:
   # evenList = Button(mainFrame, text=loot[x], width=35)
   # evenList.grid(row=x, column=0)
   # x=x+1
   # oddList = Button(mainFrame, text=loot[x], width=35)
   # oddList.grid(row=x-1, column=1)
   # x=x+1

#Button widgets for each loot item
Paracordbutton = Button(mainFrame, text="Paracord", width=35, padx=5, command=lambda:newwindow(Paracord))
Corrugated_Hosebutton = Button(mainFrame, text="Corrugated Hose", width=35, padx=5, command=lambda:newwindow(Corrugated_Hose))
Malboro_cigarettesbutton = Button(mainFrame, text="Malboro cigarettes", width=35, padx=5, command=lambda:newwindow(Malboro_cigarettes))
Wilston_cigarettesbutton = Button(mainFrame, text="Wilston cigarettes", width=35, padx=5, command=lambda:newwindow(Wilston_cigarettes))
Strike_cigarettesbutton = Button(mainFrame, text="Strike cigarettes", width=35, padx=5, command=lambda:newwindow(Strike_cigarettes))
Horse_figurinebutton = Button(mainFrame, text="Horse figurine", width=35, padx=5, command=lambda:newwindow(Horse_figurine))
Cat_figurinebutton = Button(mainFrame, text="Cat figurine", width=35, padx=5, command=lambda:newwindow(Cat_figurine))
Bronze_Lionbutton = Button(mainFrame, text="Bronze Lion", width=35, padx=5, command=lambda:newwindow(Bronze_Lion))
Gas_analyzerbutton = Button(mainFrame, text="Gas analyzer", width=35, padx=5, command=lambda:newwindow(Gas_analyzer))
Military_COFDM_wireless_signal_transmitterbutton = Button(mainFrame, text="Military COFDM wireless signal transmitter", width=35, padx=5, command=lambda:newwindow(Military_COFDM_wireless_signal_transmitter))
Uhf_RFID_readerbutton = Button(mainFrame, text="Uhf RFID reader", width=35, padx=5, command=lambda:newwindow(Uhf_RFID_reader))
VPX_flash_storage_modulebutton = Button(mainFrame, text="VPX flash storage module", width=35, padx=5, command=lambda:newwindow(VPX_flash_storage_module))
Virtex_programmable_processorbutton = Button(mainFrame, text="Virtex programmable processor", width=35, padx=5, command=lambda:newwindow(Virtex_programmable_processor))
Capacitorsbutton = Button(mainFrame, text="Capacitors", width=35, padx=5, command=lambda:newwindow(Capacitors))
Wiresbutton = Button(mainFrame, text="Wires", width=35, padx=5, command=lambda:newwindow(Wires))
Wd40_100mlbutton = Button(mainFrame, text="Wd-40 100ml", width=35, padx=5, command=lambda:newwindow(Wd40_100ml))
Car_batterybutton = Button(mainFrame, text="Car battery", width=35, padx=5, command=lambda:newwindow(Car_battery))
Spark_plugbutton = Button(mainFrame, text="Spark plug", width=35, padx=5, command=lambda:newwindow(Spark_plug))
Broken_gphonebutton = Button(mainFrame, text="Broken gphone", width=35, padx=5, command=lambda:newwindow(Broken_gphone))
CPU_fanbutton = Button(mainFrame, text="CPU fan", width=35, padx=5, command=lambda:newwindow(CPU_fan))
PC_CPUbutton = Button(mainFrame, text="PC CPU", width=35, padx=5, command=lambda:newwindow(PC_CPU))
Printed_circuit_boardbutton = Button(mainFrame, text="Printed circuit board", width=35, padx=5, command=lambda:newwindow(Printed_circuit_board))
Graphics_cardbutton = Button(mainFrame, text="Graphics card", width=35, padx=5, command=lambda:newwindow(Graphics_card))
Powercordbutton = Button(mainFrame, text="Powercord", width=35, padx=5, command=lambda:newwindow(Powercord))
TShaped_plugbutton = Button(mainFrame, text="T-Shaped plug", width=35, padx=5, command=lambda:newwindow(TShaped_plug))
Antique_vasebutton = Button(mainFrame, text="Antique vase", width=35, padx=5, command=lambda:newwindow(Antique_vase))
Antique_teapotbutton = Button(mainFrame, text="Antique teapot", width=35, padx=5, command=lambda:newwindow(Antique_teapot))
Silver_badgebutton = Button(mainFrame, text="Silver badge", width=35, padx=5, command=lambda:newwindow(Silver_badge))
Clin_wiperbutton = Button(mainFrame, text="Clin wiper", width=35, padx=5, command=lambda:newwindow(Clin_wiper))
Portable_defibrillatorbutton = Button(mainFrame, text="Portable defibrillator", width=35, padx=5, command=lambda:newwindow(Portable_defibrillator))
Medical_bloodsetbutton = Button(mainFrame, text="Medical bloodset", width=35, padx=5, command=lambda:newwindow(Medical_bloodset))
Ox_bleachbutton = Button(mainFrame, text="Ox bleach", width=35, padx=5, command=lambda:newwindow(Ox_bleach))
Fivel_propane_tankbutton = Button(mainFrame, text="5l propane tank", width=35, padx=5, command=lambda:newwindow(Fivel_propane_tank))
Fuel_Conditionerbutton = Button(mainFrame, text="Fuel Conditioner", width=35, padx=5, command=lambda:newwindow(Fuel_Conditioner))
Heat_exchange_alkali_surface_washerbutton = Button(mainFrame, text="Heat-exchange alkali surface washer", width=35, padx=5, command=lambda:newwindow(Heat_exchange_alkali_surface_washer))
Rechargeable_batterybutton = Button(mainFrame, text="Rechargeable battery", width=35, padx=5, command=lambda:newwindow(Rechargeable_battery))
Secure_flash_drivebutton = Button(mainFrame, text="Secure flash drive", width=35, padx=5, command=lambda:newwindow(Secure_flash_drive))
Fortysecond_signature_blend_english_teabutton = Button(mainFrame, text="42nd signature blend english tea", width=35, padx=5, command=lambda:newwindow(Fortysecond_signature_blend_english_tea))
Golden_roosterbutton = Button(mainFrame, text="Golden rooster", width=35, padx=5, command=lambda:newwindow(Golden_rooster))
Roler_submariner_gold_wrist_watchbutton = Button(mainFrame, text="Roler submariner gold wrist watch", width=35, padx=5, command=lambda:newwindow(Roler_submariner_gold_wrist_watch))
Battered_antique_bookbutton = Button(mainFrame, text="Battered antique book", width=35, padx=5, command=lambda:newwindow(Battered_antique_book))
Fireklean_gun_lubebutton = Button(mainFrame, text="Fireklean gun lube", width=35, padx=5, command=lambda:newwindow(Fireklean_gun_lube))
Old_firesteelbutton = Button(mainFrame, text="Old firesteel", width=35, padx=5, command=lambda:newwindow(Old_firesteel))
Deadlyslobs_beard_oilbutton = Button(mainFrame, text="Deadlyslob's beard oil", width=35, padx=5, command=lambda:newwindow(Deadlyslobs_beard_oil))
Golden_1gphonebutton = Button(mainFrame, text="Golden 1gphone", width=35, padx=5, command=lambda:newwindow(Golden_1gphone))
sixsten140m_military_batterybutton = Button(mainFrame, text="6-sten-140-m military battery", width=35, padx=5, command=lambda:newwindow(sixsten140m_military_battery))
Ofz_30x160mm_shellbutton = Button(mainFrame, text="Ofz 30x160mm shell", width=35, padx=5, command=lambda:newwindow(Ofz_30x160mm_shell))
KEKtape_duct_tapebutton = Button(mainFrame, text="KEKtape duct tape", width=35, padx=5, command=lambda:newwindow(KEKtape_duct_tape))
Raven_figurinebutton = Button(mainFrame, text="Raven figurine", width=35, padx=5, command=lambda:newwindow(Raven_figurine))
Ripstop_clothbutton = Button(mainFrame, text="Ripstop cloth", width=35, padx=5, command=lambda:newwindow(Ripstop_cloth))
Aramid_fiber_clothbutton = Button(mainFrame, text="Aramid fiber cloth", width=35, padx=5, command=lambda:newwindow(Aramid_fiber_cloth))
Fleece_clothbutton = Button(mainFrame, text="Fleece cloth", width=35, padx=5, command=lambda:newwindow(Fleece_cloth))
Polyamide_fabric_Cordurabutton = Button(mainFrame, text="Polyamide fabric Cordura", width=35, padx=5, command=lambda:newwindow(Polyamide_fabric_Cordura))
Can_of_dr_lupos_coffee_beansbutton = Button(mainFrame, text="Can of dr. lupo's coffee beans", width=35, padx=5, command=lambda:newwindow(Can_of_dr_lupos_coffee_beans))
Veritas_guitar_pickbutton = Button(mainFrame, text="Veritas guitar pick", width=35, padx=5, command=lambda:newwindow(Veritas_guitar_pick))

#grid positions for each button widget
Paracordbutton.grid(row=0, column=0)
Corrugated_Hosebutton.grid(row=0, column=4)
Malboro_cigarettesbutton.grid(row=1, column=0)
Wilston_cigarettesbutton.grid(row=1, column=4)
Strike_cigarettesbutton.grid(row=2, column=0)
Horse_figurinebutton.grid(row=2, column=4)
Cat_figurinebutton.grid(row=3, column=0)
Bronze_Lionbutton.grid(row=3, column=4)
Gas_analyzerbutton.grid(row=4, column=0)
Military_COFDM_wireless_signal_transmitterbutton.grid(row=4, column=4)
Uhf_RFID_readerbutton.grid(row=5, column=0)
VPX_flash_storage_modulebutton.grid(row=5, column=4)
Virtex_programmable_processorbutton.grid(row=6, column=0)
Capacitorsbutton.grid(row=6, column=4)
Wiresbutton.grid(row=7, column=0)
Wd40_100mlbutton.grid(row=7, column=4)
Car_batterybutton.grid(row=8, column=0)
Spark_plugbutton.grid(row=8, column=4)
Broken_gphonebutton.grid(row=9, column=0)
CPU_fanbutton.grid(row=9, column=4)
PC_CPUbutton.grid(row=10, column=0)
Printed_circuit_boardbutton.grid(row=10, column=4)
Graphics_cardbutton.grid(row=11, column=0)
Powercordbutton.grid(row=11, column=4)
TShaped_plugbutton.grid(row=12, column=0)
Antique_vasebutton.grid(row=12, column=4)
Antique_teapotbutton.grid(row=13, column=0)
Silver_badgebutton.grid(row=13, column=4)
Clin_wiperbutton.grid(row=14, column=0)
Portable_defibrillatorbutton.grid(row=14, column=4)
Medical_bloodsetbutton.grid(row=15, column=0)
Ox_bleachbutton.grid(row=15, column=4)
Fivel_propane_tankbutton.grid(row=16, column=0)
Fuel_Conditionerbutton.grid(row=16, column=4)
Heat_exchange_alkali_surface_washerbutton.grid(row=17, column=0)
Rechargeable_batterybutton.grid(row=17, column=4)
Secure_flash_drivebutton.grid(row=18, column=0)
Fortysecond_signature_blend_english_teabutton.grid(row=18, column=4)
Golden_roosterbutton.grid(row=19, column=0)
Roler_submariner_gold_wrist_watchbutton.grid(row=19, column=4)
Battered_antique_bookbutton.grid(row=20, column=0)
Fireklean_gun_lubebutton.grid(row=20, column=4)
Old_firesteelbutton.grid(row=21, column=0)
Deadlyslobs_beard_oilbutton.grid(row=21, column=4)
Golden_1gphonebutton.grid(row=22, column=0)
sixsten140m_military_batterybutton.grid(row=22, column=4)
Ofz_30x160mm_shellbutton.grid(row=23, column=0)
KEKtape_duct_tapebutton.grid(row=23, column=4)
Raven_figurinebutton.grid(row=24, column=0)
Ripstop_clothbutton.grid(row=24, column=4)
Aramid_fiber_clothbutton.grid(row=25, column=0)
Fleece_clothbutton.grid(row=25, column=4)
Polyamide_fabric_Cordurabutton.grid(row=26, column=0)
Can_of_dr_lupos_coffee_beansbutton.grid(row=26, column=4)
Veritas_guitar_pickbutton.grid(row=27, column=0)

#Creating add buttons
ParacordbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(0))
Corrugated_HosebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(1))
Malboro_cigarettesbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(2))
Wilston_cigarettesbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(3))
Strike_cigarettesbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(4))
Horse_figurinebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(5))
Cat_figurinebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(6))
Bronze_LionbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(7))
Gas_analyzerbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(8))
Military_COFDM_wireless_signal_transmitterbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(9))
Uhf_RFID_readerbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(10))
VPX_flash_storage_modulebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(11))
Virtex_programmable_processorbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(12))
CapacitorsbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(13))
WiresbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(14))
Wd40_100mlbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(15))
Car_batterybuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(16))
Spark_plugbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(17))
Broken_gphonebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(18))
CPU_fanbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(19))
PC_CPUbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(20))
Printed_circuit_boardbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(21))
Graphics_cardbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(22))
PowercordbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(23))
TShaped_plugbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(24))
Antique_vasebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(25))
Antique_teapotbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(26))
Silver_badgebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(27))
Clin_wiperbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(28))
Portable_defibrillatorbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(29))
Medical_bloodsetbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(30))
Ox_bleachbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(31))
Fivel_propane_tankbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(32))
Fuel_ConditionerbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(33))
Heat_exchange_alkali_surface_washerbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(34))
Rechargeable_batterybuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(35))
Secure_flash_drivebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(36))
Fortysecond_signature_blend_english_teabuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(37))
Golden_roosterbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(38))
Roler_submariner_gold_wrist_watchbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(39))
Battered_antique_bookbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(40))
Fireklean_gun_lubebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(41))
Old_firesteelbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(42))
Deadlyslobs_beard_oilbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(43))
Golden_1gphonebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(44))
sixsten140m_military_batterybuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(45))
Ofz_30x160mm_shellbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(46))
KEKtape_duct_tapebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(47))
Raven_figurinebuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(48))
Ripstop_clothbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(49))
Aramid_fiber_clothbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(50))
Fleece_clothbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(51))
Polyamide_fabric_CordurabuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(52))
Can_of_dr_lupos_coffee_beansbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(53))
Veritas_guitar_pickbuttonAdd = Button(mainFrame, text="+", command=lambda:addtoclass(54))

#creating subract buttons
ParacordbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(0))
Corrugated_HosebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(1))
Malboro_cigarettesbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(2))
Wilston_cigarettesbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(3))
Strike_cigarettesbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(4))
Horse_figurinebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(5))
Cat_figurinebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(6))
Bronze_LionbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(7))
Gas_analyzerbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(8))
Military_COFDM_wireless_signal_transmitterbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(9))
Uhf_RFID_readerbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(10))
VPX_flash_storage_modulebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(11))
Virtex_programmable_processorbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(12))
CapacitorsbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(13))
WiresbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(14))
Wd40_100mlbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(15))
Car_batterybuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(16))
Spark_plugbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(17))
Broken_gphonebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(18))
CPU_fanbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(19))
PC_CPUbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(20))
Printed_circuit_boardbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(21))
Graphics_cardbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(22))
PowercordbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(23))
TShaped_plugbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(24))
Antique_vasebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(25))
Antique_teapotbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(26))
Silver_badgebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(27))
Clin_wiperbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(28))
Portable_defibrillatorbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(29))
Medical_bloodsetbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(30))
Ox_bleachbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(31))
Fivel_propane_tankbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(32))
Fuel_ConditionerbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(33))
Heat_exchange_alkali_surface_washerbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(34))
Rechargeable_batterybuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(35))
Secure_flash_drivebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(36))
Fortysecond_signature_blend_english_teabuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(37))
Golden_roosterbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(38))
Roler_submariner_gold_wrist_watchbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(39))
Battered_antique_bookbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(40))
Fireklean_gun_lubebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(41))
Old_firesteelbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(42))
Deadlyslobs_beard_oilbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(43))
Golden_1gphonebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(44))
sixsten140m_military_batterybuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(45))
Ofz_30x160mm_shellbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(46))
KEKtape_duct_tapebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(47))
Raven_figurinebuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(48))
Ripstop_clothbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(49))
Aramid_fiber_clothbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(50))
Fleece_clothbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(51))
Polyamide_fabric_CordurabuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(52))
Can_of_dr_lupos_coffee_beansbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(53))
Veritas_guitar_pickbuttonSubtract = Button(mainFrame, text="-", command=lambda:subtractfromclass(54))


#grid positions for subtract buttons
ParacordbuttonSubtract.grid(row=0, column=1)
Corrugated_HosebuttonSubtract.grid(row=0, column=5)
Malboro_cigarettesbuttonSubtract.grid(row=1, column=1)
Wilston_cigarettesbuttonSubtract.grid(row=1, column=5)
Strike_cigarettesbuttonSubtract.grid(row=2, column=1)
Horse_figurinebuttonSubtract.grid(row=2, column=5)
Cat_figurinebuttonSubtract.grid(row=3, column=1)
Bronze_LionbuttonSubtract.grid(row=3, column=5)
Gas_analyzerbuttonSubtract.grid(row=4, column=1)
Military_COFDM_wireless_signal_transmitterbuttonSubtract.grid(row=4, column=5)
Uhf_RFID_readerbuttonSubtract.grid(row=5, column=1)
VPX_flash_storage_modulebuttonSubtract.grid(row=5, column=5)
Virtex_programmable_processorbuttonSubtract.grid(row=6, column=1)
CapacitorsbuttonSubtract.grid(row=6, column=5)
WiresbuttonSubtract.grid(row=7, column=1)
Wd40_100mlbuttonSubtract.grid(row=7, column=5)
Car_batterybuttonSubtract.grid(row=8, column=1)
Spark_plugbuttonSubtract.grid(row=8, column=5)
Broken_gphonebuttonSubtract.grid(row=9, column=1)
CPU_fanbuttonSubtract.grid(row=9, column=5)
PC_CPUbuttonSubtract.grid(row=10, column=1)
Printed_circuit_boardbuttonSubtract.grid(row=10, column=5)
Graphics_cardbuttonSubtract.grid(row=11, column=1)
PowercordbuttonSubtract.grid(row=11, column=5)
TShaped_plugbuttonSubtract.grid(row=12, column=1)
Antique_vasebuttonSubtract.grid(row=12, column=5)
Antique_teapotbuttonSubtract.grid(row=13, column=1)
Silver_badgebuttonSubtract.grid(row=13, column=5)
Clin_wiperbuttonSubtract.grid(row=14, column=1)
Portable_defibrillatorbuttonSubtract.grid(row=14, column=5)
Medical_bloodsetbuttonSubtract.grid(row=15, column=1)
Ox_bleachbuttonSubtract.grid(row=15, column=5)
Fivel_propane_tankbuttonSubtract.grid(row=16, column=1)
Fuel_ConditionerbuttonSubtract.grid(row=16, column=5)
Heat_exchange_alkali_surface_washerbuttonSubtract.grid(row=17, column=1)
Rechargeable_batterybuttonSubtract.grid(row=17, column=5)
Secure_flash_drivebuttonSubtract.grid(row=18, column=1)
Fortysecond_signature_blend_english_teabuttonSubtract.grid(row=18, column=5)
Golden_roosterbuttonSubtract.grid(row=19, column=1)
Roler_submariner_gold_wrist_watchbuttonSubtract.grid(row=19, column=5)
Battered_antique_bookbuttonSubtract.grid(row=20, column=1)
Fireklean_gun_lubebuttonSubtract.grid(row=20, column=5)
Old_firesteelbuttonSubtract.grid(row=21, column=1)
Deadlyslobs_beard_oilbuttonSubtract.grid(row=21, column=5)
Golden_1gphonebuttonSubtract.grid(row=22, column=1)
sixsten140m_military_batterybuttonSubtract.grid(row=22, column=5)
Ofz_30x160mm_shellbuttonSubtract.grid(row=23, column=1)
KEKtape_duct_tapebuttonSubtract.grid(row=23, column=5)
Raven_figurinebuttonSubtract.grid(row=24, column=1)
Ripstop_clothbuttonSubtract.grid(row=24, column=5)
Aramid_fiber_clothbuttonSubtract.grid(row=25, column=1)
Fleece_clothbuttonSubtract.grid(row=25, column=5)
Polyamide_fabric_CordurabuttonSubtract.grid(row=26, column=1)
Can_of_dr_lupos_coffee_beansbuttonSubtract.grid(row=26, column=5)
Veritas_guitar_pickbuttonSubtract.grid(row=27, column=1)

#grid positions for add buttons
ParacordbuttonAdd.grid(row=0, column=3)
Corrugated_HosebuttonAdd.grid(row=0, column=7)
Malboro_cigarettesbuttonAdd.grid(row=1, column=3)
Wilston_cigarettesbuttonAdd.grid(row=1, column=7)
Strike_cigarettesbuttonAdd.grid(row=2, column=3)
Horse_figurinebuttonAdd.grid(row=2, column=7)
Cat_figurinebuttonAdd.grid(row=3, column=3)
Bronze_LionbuttonAdd.grid(row=3, column=7)
Gas_analyzerbuttonAdd.grid(row=4, column=3)
Military_COFDM_wireless_signal_transmitterbuttonAdd.grid(row=4, column=7)
Uhf_RFID_readerbuttonAdd.grid(row=5, column=3)
VPX_flash_storage_modulebuttonAdd.grid(row=5, column=7)
Virtex_programmable_processorbuttonAdd.grid(row=6, column=3)
CapacitorsbuttonAdd.grid(row=6, column=7)
WiresbuttonAdd.grid(row=7, column=3)
Wd40_100mlbuttonAdd.grid(row=7, column=7)
Car_batterybuttonAdd.grid(row=8, column=3)
Spark_plugbuttonAdd.grid(row=8, column=7)
Broken_gphonebuttonAdd.grid(row=9, column=3)
CPU_fanbuttonAdd.grid(row=9, column=7)
PC_CPUbuttonAdd.grid(row=10, column=3)
Printed_circuit_boardbuttonAdd.grid(row=10, column=7)
Graphics_cardbuttonAdd.grid(row=11, column=3)
PowercordbuttonAdd.grid(row=11, column=7)
TShaped_plugbuttonAdd.grid(row=12, column=3)
Antique_vasebuttonAdd.grid(row=12, column=7)
Antique_teapotbuttonAdd.grid(row=13, column=3)
Silver_badgebuttonAdd.grid(row=13, column=7)
Clin_wiperbuttonAdd.grid(row=14, column=3)
Portable_defibrillatorbuttonAdd.grid(row=14, column=7)
Medical_bloodsetbuttonAdd.grid(row=15, column=3)
Ox_bleachbuttonAdd.grid(row=15, column=7)
Fivel_propane_tankbuttonAdd.grid(row=16, column=3)
Fuel_ConditionerbuttonAdd.grid(row=16, column=7)
Heat_exchange_alkali_surface_washerbuttonAdd.grid(row=17, column=3)
Rechargeable_batterybuttonAdd.grid(row=17, column=7)
Secure_flash_drivebuttonAdd.grid(row=18, column=3)
Fortysecond_signature_blend_english_teabuttonAdd.grid(row=18, column=7)
Golden_roosterbuttonAdd.grid(row=19, column=3)
Roler_submariner_gold_wrist_watchbuttonAdd.grid(row=19, column=7)
Battered_antique_bookbuttonAdd.grid(row=20, column=3)
Fireklean_gun_lubebuttonAdd.grid(row=20, column=7)
Old_firesteelbuttonAdd.grid(row=21, column=3)
Deadlyslobs_beard_oilbuttonAdd.grid(row=21, column=7)
Golden_1gphonebuttonAdd.grid(row=22, column=3)
sixsten140m_military_batterybuttonAdd.grid(row=22, column=7)
Ofz_30x160mm_shellbuttonAdd.grid(row=23, column=3)
KEKtape_duct_tapebuttonAdd.grid(row=23, column=7)
Raven_figurinebuttonAdd.grid(row=24, column=3)
Ripstop_clothbuttonAdd.grid(row=24, column=7)
Aramid_fiber_clothbuttonAdd.grid(row=25, column=3)
Fleece_clothbuttonAdd.grid(row=25, column=7)
Polyamide_fabric_CordurabuttonAdd.grid(row=26, column=3)
Can_of_dr_lupos_coffee_beansbuttonAdd.grid(row=26, column=7)
Veritas_guitar_pickbuttonAdd.grid(row=27, column=3)

#Creating the main loop
root.mainloop()
