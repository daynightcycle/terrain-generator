
import ast
import os
from random import randrange


def main():
    while True:
        main_menu_selection()


def print_main_menu():
    print("\n", 27 * "-", "MAIN MENU", 27 * "-")
    print("A) Load Save")
    print("B) Create Save")
    print("C) Global Settings")
    print("D) Exit")
    print(66 * "-")


def main_menu_selection():
    while True:
        print_main_menu()
        selection = input("Enter selection: ")
        if selection in ("a", "A"):
            load_save()
        elif selection in ("b", "B"):
            create_save()
        elif selection in ("c", "C"):
            print("C has been selected.")
        elif selection in ("d", "D"):
            quit()
        else:
            print("That is an invalid selection. Try again.")


def create_save():
    save_file = input("\n" + "Enter a file path and name: ")
    if not os.path.exists(save_file):
        with open(save_file, 'w') as fp:
            fp.write("location: " + str([0, 0]) + "\n" + "q_range: " + str([0, 0]) + "\n" + "r_range: " + str([0, 0]) + "\n" + "seed_list: " + str([[gen_land_starter()]]))
        fp.close()
        print("\n" + "Your save has been created.")
    else:
        print("\n" + "This file already exists.")


def load_save():
    save_file = input("\n" + "Enter a file path: ")
    if os.path.exists(save_file):
        with open(save_file, 'r') as fp:
            contents = fp.readlines()
            fp.close()
            location = ast.literal_eval(contents[0][len('location: '):].strip("\n"))
            q_range = ast.literal_eval(contents[1][len('q_range: '):].strip("\n"))
            r_range = ast.literal_eval(contents[2][len('r_range: '):].strip("\n"))
            seed_list = ast.literal_eval(contents[3][len('seed_list: '):].strip("\n"))
            seed = seed_list[location[0]][location[1]]
            form_factor = int(seed[:3])
            seed = seed[3:]
            el_factor = int(seed[:3])
            seed = seed[3:]
            down_factor = int(seed[:3])
            seed = seed[3:]
            up_factor = int(seed[:3])
            seed = seed[3:]
            temp_factor = int(seed[:3])
            seed = seed[3:]
            wet_factor = int(seed[:3])
            seed = seed[3:]
            riv_bool = int(seed[:1])
            seed = seed[1:]
            riv_entry_factor = int(seed[:1])
            seed = seed[1:]
            riv_exit_factor = int(seed[:1])
            seed = seed[1:]
            hill_bool = int(seed[:1])
            seed = seed[1:]
            vol_factor = int(seed[:3])
            seed = seed[3:]
            karst_factor = int(seed[:3])
            seed = seed[3:]
            vary_factor = int(seed[:2])
            journey(location, q_range, r_range, seed_list, form_factor, el_factor, down_factor, up_factor, temp_factor, wet_factor, riv_bool, riv_entry_factor, riv_exit_factor, hill_bool, vol_factor, karst_factor, vary_factor)
    else:
        print("\n" + "This file does not exist.")


def journey(location, q_range, r_range, seed_list, form_factor, el_factor, down_factor, up_factor, temp_factor, wet_factor, riv_bool, riv_entry_factor, riv_exit_factor, hill_bool, vol_factor, karst_factor, vary_factor):
    while True:
        print("\n" + "Biome: " + get_biome(temp_factor, wet_factor, form_factor, el_factor, down_factor, riv_bool, hill_bool))
        description_message = "\n"
        # Landform Description (form, elevation, uplift, hill bool)
        if el_factor <= 65:
            description_message += "The water is deep."
        elif el_factor <= 69:
            description_message += "The water is shallow."
        elif el_factor == 70:
            description_message += "Here is where the water meets the shore."
            if form_factor <= 35:
                description_message += " The land is flat."
                if up_factor <= 50:
                    pass
                elif up_factor <= 75:
                    pass
                elif up_factor <= 90:
                    description_message += " There are gentle waves in the earth."
                elif up_factor <= 95:
                    description_message += " There are a few short mounds."
                else:
                    description_message += " There are notable hills."
            elif form_factor <= 75:
                if hill_bool == 1:
                    description_message += " The land is hilly."
                    if up_factor <= 50:
                        description_message += " The hills are gentle and relatively flat."
                    elif up_factor <= 75:
                        pass
                    elif up_factor <= 90:
                        description_message += " The hills are large and relatively steep."
                    elif up_factor <= 95:
                        description_message += " The hills are huge and steep."
                    else:
                        description_message += " The hills are great and mountainous."
                else:
                    description_message += "The land is high and flat."
                    if up_factor <= 50:
                        pass
                    elif up_factor <= 75:
                        pass
                    elif up_factor <= 90:
                        description_message += " There are gentle waves in the earth."
                    elif up_factor <= 95:
                        description_message += " There are a few short mounds."
                    else:
                        description_message += " There are notable hills."
            else:
                description_message += " The land is mountainous."
                if up_factor <= 50:
                    pass
                elif up_factor <= 75:
                    pass
                elif up_factor <= 90:
                    description_message += " The mountains are particularly large and steep."
                elif up_factor <= 95:
                    description_message += " The mountains are gigantic. Climbing them may give you altitude sickness."
                else:
                    description_message += " The mountains unbelievably high and steep. Their peaks may be some of the highest in the world."
        else:
            if form_factor <= 35:
                description_message += "The land is flat."
                if up_factor <= 50:
                    pass
                elif up_factor <= 75:
                    pass
                elif up_factor <= 90:
                    description_message += " There are gentle waves in the earth."
                elif up_factor <= 95:
                    description_message += " There are a few short mounds."
                else:
                    description_message += " There are notable hills."
            elif form_factor <= 75:
                if hill_bool == 1:
                    description_message += "The land is hilly."
                    if up_factor <= 50:
                        description_message += " The hills are gentle and relatively flat."
                    elif up_factor <= 75:
                        pass
                    elif up_factor <= 90:
                        description_message += " The hills are large and relatively steep."
                    elif up_factor <= 95:
                        description_message += " The hills are huge and steep."
                    else:
                        description_message += " The hills are great and mountainous."
                else:
                    description_message += "The land is high and flat."
                    if up_factor <= 50:
                        pass
                    elif up_factor <= 75:
                        pass
                    elif up_factor <= 90:
                        description_message += " There are gentle waves in the earth."
                    elif up_factor <= 95:
                        description_message += " There are a few short mounds."
                    else:
                        description_message += " There are notable hills."
            else:
                description_message += "The land is mountainous."
                if up_factor <= 50:
                    pass
                elif up_factor <= 75:
                    pass
                elif up_factor <= 90:
                    description_message += " The mountains are particularly large and steep."
                elif up_factor <= 95:
                    description_message += " The mountains are gigantic. Climbing them may give you altitude sickness."
                else:
                    description_message += " The mountains unbelievably high and steep. Their peaks may be some of the highest in the world."
        # River Description (river bool, river entry, river exit)
        if riv_bool == 1:
            if riv_entry_factor == 1:
                description_message += " A river is flowing from the north to"
            elif riv_entry_factor == 2:
                description_message += " A river is flowing from the north-east to"
            elif riv_entry_factor == 3:
                description_message += " A river is flowing from the south-east to"
            elif riv_entry_factor == 4:
                description_message += " A river is flowing from the south to"
            elif riv_entry_factor == 5:
                description_message += " A river is flowing from the south-west to"
            elif riv_entry_factor == 6:
                description_message += " A river is flowing from the north-west to"
            else:
                description_message += " A river is flowing from its source to"
            if riv_exit_factor == 1:
                description_message += " the north."
            elif riv_exit_factor == 2:
                description_message += " the north-east."
            elif riv_exit_factor == 3:
                description_message += " the south-east."
            elif riv_exit_factor == 4:
                description_message += " the south."
            elif riv_exit_factor == 5:
                description_message += " the south-west."
            elif riv_exit_factor == 6:
                description_message += " the north-west."
            else:
                description_message += " its delta."
        else:
            pass
        # Volcanism Description
        if vol_factor == 1:
            description_message += " There are signs of volcanism."
        else:
            pass
        # Karst Description
        if karst_factor == 1:
            description_message += " There are signs of karst."
        else:
            pass
        print(description_message)
        direction = input("\n" + "Travel <n/ne/se/s/sw/nw>? ")


def gen_land_starter():
    form_factor, form_string = gen_landform_starter()
    el_factor, el_string = gen_land_elevation_starter()
    down_factor, down_string = gen_depression_starter()
    up_factor, up_string = gen_uplift_starter()
    temp_factor, temp_string = gen_temperature_starter()
    wet_factor, wet_string = gen_wetness_starter()
    riv_factor, riv_bool, riv_entry_factor, riv_entry_string, riv_exit_factor, riv_exit_string = gen_river_starter()
    hill_factor, hill_bool = gen_hill_starter()
    vol_factor, vol_bool = gen_volcanism_starter()
    karst_factor, karst_bool = gen_karst_starter()
    vary_factor = gen_land_variation_starter()
    return str(form_factor).zfill(3) + str(el_factor).zfill(3) + str(down_factor).zfill(3) + str(up_factor).zfill(3) + str(temp_factor).zfill(3) + str(wet_factor).zfill(3) + str(riv_bool) + str(riv_entry_factor) + str(riv_exit_factor) + str(hill_bool) + str(vol_factor).zfill(3) + str(karst_factor).zfill(3) + str(vary_factor).zfill(2)


def gen_landform_starter():
    roll = randrange(1, 101)
    if roll <= 35:
        return roll, "Plains"
    elif roll <= 75:
        return roll, "Other"
    else:
        return roll, "Mountains"


def gen_elevation_starter():
    roll = randrange(1, 101)
    if roll <= 29:
        return roll, "Abyssal Water"
    elif roll <= 59:
        return roll, "Deep Water"
    elif roll <= 65:
        return roll, "Near-Shallow Water"
    elif roll <= 69:
        return roll, "Shallow Water"
    elif roll == 70:
        return roll, "Sea Level"
    elif roll <= 80:
        return roll, "Coastal"
    elif roll <= 90:
        return roll, "Inland"
    else:
        return roll, "Deep Inland"


def gen_land_elevation_starter():
    roll = randrange(1, 32)
    if roll == 1:
        return roll + 69, "Sea Level"
    elif roll <= 12:
        return roll + 69, "Coastal"
    elif roll <= 22:
        return roll + 69, "Inland"
    else:
        return roll + 69, "Deep Inland"


def gen_depression_starter():
    roll = randrange(1, 101)
    if roll <= 5:
        return roll, "Great Depressions(s)"
    elif roll <= 10:
        return roll, "Deep Depressions(s)"
    elif roll <= 25:
        return roll, "Shallow Depression(s)"
    elif roll <= 50:
        return roll, "Slight Depression(s)"
    else:
        return roll, "No Notable Depressions"


def gen_uplift_starter():
    roll = randrange(1, 101)
    if roll <= 50:
        return roll, "No Notable Uplifts(s)"
    elif roll <= 75:
        return roll, "Slight Uplifts(s)"
    elif roll <= 90:
        return roll, "Gentle Uplifts(s)"
    elif roll <= 95:
        return roll, "Steep Uplifts(s)"
    else:
        return roll, "Great Uplifts(s)"


def gen_temperature_starter():
    roll = randrange(1, 101)
    if roll <= 10:
        return roll, "Very Cold"
    elif roll <= 40:
        return roll, "Cold"
    elif roll <= 60:
        return roll, "Temperate"
    elif roll <= 80:
        return roll, "Warm"
    else:
        return roll, "Very Warm"


def gen_wetness_starter():
    roll = randrange(1, 101)
    if roll <= 15:
        return roll, "Xeric"
    elif roll <= 30:
        return roll, "Semi-Xeric"
    elif roll <= 40:
        return roll, "Moist-Dry"
    elif roll <= 60:
        return roll, "Moist"
    elif roll <= 70:
        return roll, "Moist-Damp"
    elif roll <= 85:
        return roll, "Semi-Wet"
    else:
        return roll, "Wet"


def gen_river_starter():
    roll = randrange(1, 101)
    if roll <= 90:
        return roll, 0, 0, None, 0, None
    else:
        riv_entry_roll = randrange(1, 7)
        if riv_entry_roll == 1:
            riv_entry = "North"
        elif riv_entry_roll == 2:
            riv_entry = "North-East"
        elif riv_entry_roll == 3:
            riv_entry = "South-East"
        elif riv_entry_roll == 4:
            riv_entry = "South"
        elif riv_entry_roll == 5:
            riv_entry = "South-West"
        else:
            riv_entry = "North-West"
        while True:
            riv_exit_roll = randrange(1, 7)
            if not riv_exit_roll == riv_entry_roll:
                if riv_exit_roll == 1:
                    riv_exit = "North"
                    break
                elif riv_exit_roll == 2:
                    riv_exit = "North-East"
                    break
                elif riv_exit_roll == 3:
                    riv_exit = "South-East"
                    break
                elif riv_exit_roll == 4:
                    riv_exit = "South"
                    break
                elif riv_exit_roll == 5:
                    riv_exit = "South-West"
                    break
                else:
                    riv_exit = "North-West"
                    break
        return roll, 1, riv_entry_roll, riv_entry, riv_exit_roll, riv_exit


def gen_hill_starter():
    roll = randrange(1, 101)
    if roll <= 75:
        return roll, 0
    else:
        return roll, 1


def gen_volcanism_starter():
    roll = randrange(1, 101)
    if roll <= 90:
        return roll, 0
    else:
        return roll, 1


def gen_karst_starter():
    roll = randrange(1, 101)
    if roll <= 80:
        return roll, 0
    else:
        return roll, 1


def gen_land_variation_starter():
    roll = randrange(1, 21)
    return roll


def get_biome(temp_factor, wet_factor, form_factor, el_factor, down_factor, riv_bool, hill_bool):
    if temp_factor <= 10:
        if wet_factor <= 15:
            if (35 < form_factor <= 75 and hill_bool is False) or (form_factor < 75 and down_factor <= 10):
                return "Ice Fields"
            else:
                return "Ice Sheets"
        elif wet_factor <= 30:
            if form_factor > 75:
                return "Ice Sheets"
            else:
                return "Rockyland"
        elif wet_factor <= 40:
            if form_factor > 75:
                return "Rockyland"
            else:
                return "Mossy Rockyland"
        elif wet_factor <= 60:
            if form_factor > 75:
                return "Mossy Rockyland"
            else:
                return "Mossy Tundra Grassland"
        elif wet_factor <= 70:
            if form_factor > 75:
                return "Mossy Tundra Grassland"
            else:
                return "Tundra Grassland"
        elif wet_factor <= 85:  # FIX THIS SHIT AHHH
            if form_factor > 75:
                return "Tundra Grassland"
            else:
                if down_factor > 50 and el_factor > 90:
                    return "Shrubby Tundra Bog"
                elif down_factor <= 25 and 80 < el_factor <= 90 and form_factor <= 35:
                    return "Shrubby Tundra Fen"
                elif down_factor <= 25 and form_factor <= 35 and 70 <= el_factor <= 80:
                    return "Shrubby Coastal Marsh"
                else:
                    return "Shrubby Tundra Grassland"
        else:
            if form_factor > 75:
                return "Shrubby Tundra Grassland"
            else:
                if down_factor > 50 and el_factor > 90:
                    return "Scrubby Tundra Bog"
                elif down_factor <= 25 and 80 < el_factor <= 90 and form_factor <= 35:
                    return "Scrubby Tundra Fen"
                elif down_factor <= 25 and form_factor <= 35 and 70 <= el_factor <= 80:
                    return "Scrubby Coastal Marsh"
                else:
                    return "Scrubby Tundra Grassland"
    elif temp_factor <= 40:
        if wet_factor <= 15:
            if form_factor > 75:
                return "Rockyland"
            else:
                return "Sparse Shrubland"
        elif wet_factor <= 30:
            if form_factor > 75:
                return "Sparse Shrubland"
            else:
                return "Cold Shrubland"
        elif wet_factor <= 40:
            if form_factor > 75:
                return "Cold Shrubland"
            else:
                return "Cold Scrubland"
        elif wet_factor <= 60:
            if form_factor > 75:
                return "Cold Scrubland"
            else:
                return "Short Grassland"
        elif wet_factor <= 70:
            if form_factor > 75:
                return "Short Grassland"
            else:
                return "Coniferous Parkland"
        elif wet_factor <= 85:
            if form_factor > 75:
                return "Coniferous Parkland"
            else:
                return "Coniferous Woodland"
        else:
            if form_factor > 75:
                return "Coniferous Woodland"
            else:
                return "Coniferous Forest"
    elif temp_factor <= 60:
        if wet_factor <= 15:
            if form_factor > 75:
                return "Shrubby Tundra Grassland"
            else:
                return "Cold Desert"
        elif wet_factor <= 30:
            if form_factor > 75:
                return "Cold Desert"
            else:
                return "Temperate Shrubland"
        elif wet_factor <= 40:
            if form_factor > 75:
                return "Temperate Shrubland"
            else:
                return "Temperate Scrubland"
        elif wet_factor <= 60:
            if riv_bool == 1 and form_factor <= 35 and down_factor <= 25:
                return "Mixedgrass Floodplain"
            elif form_factor > 75:
                return "Temperate Scrubland"
            else:
                return "Mixed Grassland"
        elif wet_factor <= 70:
            if riv_bool == 1 and form_factor <= 35 and down_factor <= 25:
                return "Mixed-Tree Floodplain"
            elif form_factor > 75:
                return "Mixed Grassland"
            else:
                return "Mixed-Tree Parkland"
        elif wet_factor <= 85:
            if form_factor > 75:
                return "Coniferous Parkland"
            else:
                return "Mixed-Tree Woodland"
        else:
            if form_factor > 75:
                return "Coniferous Woodland"
            else:
                return "Mixed-Tree Forest"
    elif temp_factor <= 80:
        if wet_factor <= 15:
            if form_factor > 75:
                return "Temperate Shrubland"
            else:
                return "Hot Desert"
        elif wet_factor <= 30:
            if form_factor > 75:
                return "Temperate Scrubland"
            else:
                return "Warm Shrubland"
        elif wet_factor <= 40:
            return "Warm Scrubland"
        elif wet_factor <= 60:
            if riv_bool == 1 and form_factor <= 35 and down_factor <= 25:
                return "Tallgrass Floodplain"
            else:
                return "Tall Grassland"
        elif wet_factor <= 70:
            if riv_bool == 1 and form_factor <= 35 and down_factor <= 25:
                return "Broadleaved Floodplain"
            elif form_factor > 75:
                return "Mixed-Tree Parkland"
            else:
                return "Broadleaved Parkland"
        elif wet_factor <= 85:
            if form_factor > 75:
                return "Mixed-Tree Woodland"
            else:
                return "Broadleaved Woodland"
        else:
            if form_factor > 75:
                return "Broadleaved Forest"
            else:
                return "Seasonal Rainforest"
    else:
        if wet_factor <= 15:
            return "Wasteland"
        elif wet_factor <= 30:
            if form_factor > 75:
                return "Warm Shrubland"
            else:
                return "Hot Shrubland"
        elif wet_factor <= 40:
            if form_factor > 75:
                return "Warm Scrubland"
            else:
                return "Hot Scrubland"
        elif wet_factor <= 60:
            if riv_bool == 1 and form_factor <= 35 and down_factor <= 25:
                return "Coarse Grass Floodplain"
            else:
                return "Coarse Grassland"
        elif wet_factor <= 70:
            if riv_bool == 1 and form_factor <= 35 and down_factor <= 25:
                return "Wet Floodplain"
            else:
                return "Wet Parkland"
        elif wet_factor <= 85:
            if form_factor > 75:
                return "Moss Forest"
            else:
                return "Wet Woodland"
        else:
            if form_factor > 75:
                return "Cloud Forest"
            else:
                return "Evergreen Rainforest"


main()










