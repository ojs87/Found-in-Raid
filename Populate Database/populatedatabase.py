from tkinter import *
from Itemclass import Lootinfo
import sqlite3

loot = ["Paracord", "Corrugated Hose", "Malboro cigarettes", "Wilston cigarettes", "Strike cigarettes", "Horse figurine", "Cat figurine", "Bronze Lion",
        "Gas analyzer", "Military COFDM wireless signal transmitter", "Uhf RFID reader", "VPX flash storage module", "Virtex programmable processor",
        "Capacitors", "Wires", "Wd-40 100ml", "Car battery", "Spark plug", "Broken gphone", "CPU fan", "PC CPU", "Printed circuit board", "Graphics card",
        "Powercord", "T-Shaped plug", "Antique vase", "Antique teapot", "Silver badge", "Clin wiper", "Portable defibrillator", "Medical bloodset", "Ox bleach",
        "5l propane tank", "Fuel Conditioner", "Heat-exchange alkali surface washer", "Rechargeable battery", "Secure flash drive", "42nd signature blend english tea",
        "Golden rooster", "Roler submariner gold wrist watch", "Battered antique book", "Fireklean gun lube", "Old firesteel", "Deadlyslob's beard oil", "Golden 1gphone",
        "6-sten-140-m military battery", "Ofz 30x160mm shell", "KEKtape duct tape", "Raven figurine", "Ripstop cloth", "Aramid fiber cloth", "Fleece cloth",
        "Polyamide fabric Cordura", "Can of dr. lupo's coffee beans", "Veritas guitar pick" ]

Paracord = Lootinfo(TRUE, 3, 0, 0, 0)
Corrugated_Hose = Lootinfo(TRUE, 2, 2, 26, 0)
Malboro_cigarettes = Lootinfo(TRUE, 5, 0, 0, 0)
Wilston_cigarettes = Lootinfo(TRUE, 5, 0, 0, 0)
Strike_cigarettes = Lootinfo(TRUE, 5, 0, 0, 0)
Horse_figurine = Lootinfo(TRUE, 2, 0, 0, 0)
Cat_figurine = Lootinfo(TRUE, 1, 0, 0, 0)
Bronze_Lion = Lootinfo(TRUE, 2, 0, 4, 0)
Gas_analyzer = Lootinfo(TRUE, 2, 0, 3, 1)
Military_COFDM_wireless_signal_transmitter = Lootinfo(TRUE, 1, 0, 2, 0)
Uhf_RFID_reader = Lootinfo(TRUE, 1, 0, 0, 0)
VPX_flash_storage_module = Lootinfo(TRUE, 1, 0, 2, 0)
Virtex_programmable_processor = Lootinfo(TRUE, 2, 0, 0, 0)
Capacitors = Lootinfo(TRUE, 5, 0, 12, 0)
Wires = Lootinfo(TRUE, 5, 0, 53, 0)
Wd40_100ml = Lootinfo(TRUE, 1, 0, 4, 0)
Car_battery = Lootinfo(TRUE, 4, 0, 5, 0)
Spark_plug = Lootinfo(TRUE, 8, 0, 5, 0)
Broken_gphone = Lootinfo(TRUE, 3, 0, 0, 0)
CPU_fan = Lootinfo(TRUE, 8, 0, 50, 0)
PC_CPU = Lootinfo(TRUE, 3, 0, 0, 0)
Printed_circuit_board = Lootinfo(TRUE, 2, 3, 10, 0)
Graphics_card = Lootinfo(TRUE, 3, 0, 0, 0)
Powercord = Lootinfo(TRUE, 2, 0, 13, 0)
TShaped_plug = Lootinfo(TRUE, 4, 0, 0, 0)
Antique_vase = Lootinfo(TRUE, 2, 0, 0, 0)
Antique_teapot = Lootinfo(TRUE, 3, 0, 0, 0)
Silver_badge = Lootinfo(TRUE, 1, 0, 0, 0)
Clin_wiper = Lootinfo(TRUE, 2, 0, 0, 0)
Portable_defibrillator = Lootinfo(TRUE, 1, 0, 0, 0)
Medical_bloodset = Lootinfo(TRUE, 3, 0, 2, 0)
Ox_bleach = Lootinfo(TRUE, 3, 0, 0, 0)
Fivel_propane_tank = Lootinfo(TRUE, 2, 0, 0, 0)
Fuel_Conditioner = Lootinfo(TRUE, 4, 0, 0, 0)
Heat_exchange_alkali_surface_washer = Lootinfo(TRUE, 2, 0, 2, 0)
Rechargeable_battery = Lootinfo(TRUE, 3, 0, 0, 0)
Secure_flash_drive = Lootinfo(TRUE, 2, 3, 3, 0)
Fortysecond_signature_blend_english_tea = Lootinfo(TRUE, 1, 0, 0, 0)
Golden_rooster = Lootinfo(TRUE, 1, 0, 0, 0)
Roler_submariner_gold_wrist_watch = Lootinfo(TRUE, 1, 0, 4, 0)
Battered_antique_book = Lootinfo(TRUE, 1, 0, 0, 0)
Fireklean_gun_lube = Lootinfo(TRUE, 1, 0, 1, 0)
Old_firesteel = Lootinfo(TRUE, 1, 0, 0, 0)
Deadlyslobs_beard_oil = Lootinfo(TRUE, 1, 0, 0, 0)
Golden_1gphone = Lootinfo(TRUE, 1, 0, 0, 1)
Sixsten140m_military_battery = Lootinfo(TRUE, 1, 0, 0, 0)
Ofz_30x160mm_shell = Lootinfo(TRUE, 10, 0, 0, 0)
KEKtape_duct_tape = Lootinfo(TRUE, 5, 0, 0, 0)
Raven_figurine = Lootinfo(TRUE, 1, 0, 0, 0)
Ripstop_cloth = Lootinfo(TRUE, 10, 0, 0, 0)
Aramid_fiber_cloth = Lootinfo(TRUE, 5, 0, 0, 0)
Fleece_cloth = Lootinfo(TRUE, 10, 0, 0, 0)
Polyamide_fabric_Cordura = Lootinfo(TRUE, 10, 0, 0, 0)
Can_of_dr_lupos_coffee_beans = Lootinfo(TRUE, 1, 0, 0, 0)
Veritas_guitar_pick = Lootinfo(TRUE, 1, 0, 0, 0)
Morphine_injector = Lootinfo(TRUE, 4, 4, 0, 0)
Can_of_beef_stew = Lootinfo(TRUE, 15, 0, 0, 0)
Bars_A_2607_95x18 = Lootinfo(TRUE, 5, 0, 0, 0)
Lower_half_mask = Lootinfo(TRUE, 7, 0, 0, 0)
Respirator = Lootinfo(TRUE, 4, 0, 0, 0)
BlackRock_chest_rig = Lootinfo(TRUE, 2, 0, 0, 0)
Wartech_gear_rig = Lootinfo(TRUE, 2, 0, 0, 0)
Pilgrim_tourist_backpack = Lootinfo(TRUE, 1, 0, 0, 0)
TT_pistol_7_62x25_TT_Gold = Lootinfo(TRUE, 1, 0, 0, 0)
Maska_1Sch_helmet = Lootinfo(TRUE, 1, 0, 0, 0)
Shturman_key = Lootinfo(TRUE, 1, 0, 0, 0)
CMS_kit = Lootinfo(TRUE, 2, 0, 0, 0)
Jar_of_DevilDog_mayo = Lootinfo(TRUE, 1, 0, 0, 0)
Can_of_sprats = Lootinfo(TRUE, 1, 0, 0, 0)
Fake_mustache = Lootinfo(TRUE, 1, 0, 0, 0)
Kotton_beanie = Lootinfo(TRUE, 1, 0, 0, 0)
Pestily_plague_mask = Lootinfo(TRUE, 1, 0, 0, 0)
Shroud_half_mask = Lootinfo(TRUE, 1, 0, 0, 0)
Antique_axe = Lootinfo(TRUE, 1, 0, 0, 0)
MULE_stimulator = Lootinfo(TRUE, 1, 0, 0, 0)
Cocktail_obdolbos = Lootinfo(TRUE, 1, 0, 0, 0)
Meldonin = Lootinfo(TRUE, 1, 0, 0, 0)
AHF1_M = Lootinfo(TRUE, 1, 1, 0, 0)
P22 = Lootinfo(TRUE, 1, 0, 0, 0)
L1_Norepinephrine = Lootinfo(TRUE, 1, 0, 0, 0)
Three_b_TG = Lootinfo(TRUE, 1, 1, 0, 0)

"Morphine_injector", "Can_of_beef_stew", "Bars_A_2607_95x18", "Lower_half_mask", "Respirator", "BlackRock_chest_rig", "Wartech_gear_rig",
"Pilgrim_tourist_backpack", "TT_pistol_7_62x25_TT_Gold", "Maska_1Sch_helmet", "Shturman_key", "CMS_kit", "Jar_of_DevilDog_mayo",
"Can_of_sprats", "Fake_mustache", "Kotton_beanie", "Pestily_plague_mask", "Shroud_half_mask", "Antique_axe", "MULE_stimulator",
"Cocktail_obdolbos", "Meldonin", "AHF1_M", "P22", "L1_Norepinephrine", "three_b_TG"

loot2 = ["Paracord",
"Corrugated_Hose",
"Malboro_cigarettes",
"Wilston_cigarettes",
"Strike_cigarettes",
"Horse_figurine",
"Cat_figurine",
"Bronze_Lion",
"Gas_analyzer",
"Military_COFDM_wireless_signal_transmitter",
"Uhf_RFID_reader",
"VPX_flash_storage_module",
"Virtex_programmable_processor",
"Capacitors",
"Wires",
"Wd40_100ml",
"Car_battery",
"Spark_plug",
"Broken_gphone",
"CPU_fan",
"PC_CPU",
"Printed_circuit_board",
"Graphics_card",
"Powercord",
"TShaped_plug",
"Antique_vase",
"Antique_teapot",
"Silver_badge",
"Clin_wiper",
"Portable_defibrillator",
"Medical_bloodset",
"Ox_bleach",
"Fivel_propane_tank",
"Fuel_Conditioner",
"Heat_exchange_alkali_surface_washer",
"Rechargeable_battery",
"Secure_flash_drive",
"Fortysecond_signature_blend_english_tea",
"Golden_rooster",
"Roler_submariner_gold_wrist_watch",
"Battered_antique_book",
"Fireklean_gun_lube",
"Old_firesteel",
"Deadlyslobs_beard_oil",
"Golden_1gphone",
"Sixsten140m_military_battery",
"Ofz_30x160mm_shell",
"KEKtape_duct_tape",
"Raven_figurine",
"Ripstop_cloth",
"Aramid_fiber_cloth",
"Fleece_cloth",
"Polyamide_fabric_Cordura",
"Can_of_dr_lupos_coffee_beans",
"Veritas_guitar_pick",]



loot3 = ['Three_b_TG', 'Fortysecond_signature_blend_english_tea', 'Fivel_propane_tank', 'Sixsten140m_military_battery', 'AHF1_M', 'Antique_axe', 'Antique_teapot', 'Antique_vase', 'Aramid_fiber_cloth', 'Bars_A_2607_95x18', 'Battered_antique_book', 'BlackRock_chest_rig', 'Broken_gphone', 'Bronze_Lion', 'CMS_kit', 'CPU_fan', 'Can_of_beef_stew', 'Can_of_dr_lupos_coffee_beans', 'Can_of_sprats', 'Capacitors', 'Car_battery', 'Cat_figurine', 'Clin_wiper', 'Cocktail_obdolbos', 'Corrugated_Hose', 'Deadlyslobs_beard_oil', 'Fake_mustache', 'Fireklean_gun_lube', 'Fleece_cloth', 'Fuel_Conditioner', 'Gas_analyzer', 'Golden_1gphone', 'Golden_rooster', 'Graphics_card', 'Heat_exchange_alkali_surface_washer', 'Horse_figurine', 'Jar_of_DevilDog_mayo', 'KEKtape_duct_tape', 'Kotton_beanie', 'L1_Norepinephrine', 'Lower_half_mask', 'MULE_stimulator', 'Malboro_cigarettes', 'Maska_1Sch_helmet', 'Medical_bloodset', 'Meldonin', 'Military_COFDM_wireless_signal_transmitter', 'Morphine_injector', 'Ofz_30x160mm_shell', 'Old_firesteel', 'Ox_bleach', 'P22', 'PC_CPU', 'Paracord', 'Pestily_plague_mask', 'Pilgrim_tourist_backpack', 'Polyamide_fabric_Cordura', 'Portable_defibrillator', 'Powercord', 'Printed_circuit_board', 'Raven_figurine', 'Rechargeable_battery', 'Respirator', 'Ripstop_cloth', 'Roler_submariner_gold_wrist_watch', 'Secure_flash_drive', 'Shroud_half_mask', 'Shturman_key', 'Silver_badge', 'Spark_plug', 'Strike_cigarettes', 'TShaped_plug', 'TT_pistol_7_62x25_TT_Gold', 'Uhf_RFID_reader', 'VPX_flash_storage_module', 'Veritas_guitar_pick', 'Virtex_programmable_processor', 'Wartech_gear_rig', 'Wd40_100ml', 'Wilston_cigarettes', 'Wires']

#Create a database or connect to one
conn = sqlite3.connect('item_book2.db')

#create cursor
c = conn.cursor()
x=0
#populate the database
def populateDatabase():
    x=0
    while x < len(loot3):
        testname = loot3[x]
        c.execute("INSERT INTO fir_items VALUES(:name, :fir_status, :quest1, :quest2, :hideout, :mycount)",
         {
                'name': loot3[x],
                'fir_status': eval(loot3[x]).fir_status,
                'quest1' : eval(loot3[x]).quest1,
                'quest2' : eval(loot3[x]).quest2,
                'hideout' : eval(loot3[x]).hideout,
                'mycount' : eval(loot3[x]).mycount
        })
        x += 1

#Create the database tables
def createDatabase():

    c.execute("""CREATE TABLE fir_items (
            name text,
            fir_status boolean,
            quest1 integer,
            quest2 integer,
            hideout integer,
            mycount integer
    )""")

#run the code, either popluate or create
#createDatabase()
populateDatabase()

#check the database
c.execute("SELECT *, oid FROM fir_items")
records = c.fetchall()
print(records)
#commit changes
conn.commit()
#close connection
conn.close()
