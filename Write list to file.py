loot = ["Paracord", "Corrugated Hose", "Malboro cigarettes", "Wilston cigarettes", "Strike cigarettes", "Horse figurine", "Cat figurine", "Bronze Lion", 
        "Gas analyzer", "Military COFDM wireless signal transmitter", "Uhf RFID reader", "VPX flash storage module", "Virtex programmable processor", 
        "Capacitors", "Wires", "Wd-40 100ml", "Car battery", "Spark plug", "Broken gphone", "CPU fan", "PC CPU", "Printed circuit board", "Graphics card", 
        "Powercord", "T-Shaped plug", "Antique vase", "Antique teapot", "Silver badge", "Clin wiper", "Portable defibrillator", "Medical bloodset", "Ox bleach", 
        "5l propane tank", "Fuel Conditioner", "Heat-exchange alkali surface washer", "Rechargeable battery", "Secure flash drive", "42nd signature blend english tea", 
        "Golden rooster", "Roler submariner gold wrist watch", "Battered antique book", "Fireklean gun lube", "Old firesteel", "Deadlyslob's beard oil", "Golden 1gphone", 
        "6-sten-140-m military battery", "Ofz 30x160mm shell", "KEKtape duct tape", "Raven figurine", "Ripstop cloth", "Aramid fiber cloth", "Fleece cloth", 
        "Polyamide fabric Cordura", "Can of dr. lupo's coffee beans", "Veritas guitar pick" ]

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
"sixsten140m_military_battery",
"Ofz_30x160mm_shell",
"KEKtape_duct_tape",
"Raven_figurine",
"Ripstop_cloth",
"Aramid_fiber_cloth",
"Fleece_cloth",
"Polyamide_fabric_Cordura",
"Can_of_dr_lupos_coffee_beans",
"Veritas_guitar_pick",]

items_file = open("Items.txt", "a")
x=0

#writing the grid positions for the button widgets below
#while x < len(loot)-1:
#    items_file.write(loot2[x] + 'button.grid(row=' + str(int(x/2)) + ', column=0)\n')
#    x += 1
#    items_file.write(loot2[x] + 'button.grid(row=' + str(int((x-1)/2)) + ', column=1)\n')
#    x += 1

#writing the button widgets to Items.txt
while x < len(loot)-1:
    items_file.write(loot2[x] + 'button = Button(mainFrame, text="' + loot[x] + '", width=35, padx=5, command=lambda:newwindow(' + loot2[x] + '))\n')
    x += 1

items_file.close()