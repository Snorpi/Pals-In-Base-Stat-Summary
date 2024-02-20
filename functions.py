from pals import characters


def display_characters(selected_characters):
    sum_kindling = 0
    sum_planting = 0
    sum_handiwork = 0
    sum_lumbering = 0
    sum_medicine_production = 0
    sum_transporting = 0
    sum_watering = 0
    sum_generating_electricity = 0
    sum_gathering = 0
    sum_mining = 0
    sum_cooling = 0
    sum_farming = 0
    for character in selected_characters:
        print(f"{character.pal_name}: Kindling: {character.kindling}, Planting: {character.planting},"
              f" Handiwork: {character.handiwork}, Lumbering: {character.lumbering}, "
              f"Medicine Production: {character.medicine_production}, Transporting: {character.transporting}, "
              f"Watering: {character.watering}, Generating Electricity: {character.generating_electricity}, "
              f"Gathering: {character.gathering}, Mining: {character.mining}, Cooling: {character.cooling}, "
              f"Farming: {character.farming}")
        sum_kindling += character.kindling
        sum_planting += character.planting
        sum_handiwork += character.handiwork
        sum_lumbering += character.lumbering
        sum_medicine_production += character.medicine_production
        sum_transporting += character.transporting
        sum_watering += character.watering
        sum_generating_electricity += character.generating_electricity
        sum_gathering += character.gathering
        sum_mining += character.mining
        sum_cooling += character.cooling
        sum_farming += character.farming

    print(f"Sum: Kindling: {sum_kindling}, Planting: {sum_planting}, Handiwork: {sum_handiwork}, "
          f"Lumbering: {sum_lumbering}, Medicine Production: {sum_medicine_production},"
          f" Transporting: {sum_transporting}, Watering: {sum_watering}, "
          f" Generating Electricity: {sum_generating_electricity}, Mining: {sum_mining}, Cooling: {sum_cooling}, "
          f"Farming: {sum_farming}")


def select_characters():
    selected_characters = []
    while True:
        print("Select character by name (or 'done' to finish):")
        for i, character in enumerate(characters):
            print(f"{i + 1}. {character.pal_name}")

        choice = input("> ").lower()

        if choice == "done":
            break

        try:
            index = int(choice) - 1
            if 0 <= index < len(characters):
                selected_characters.append(characters[index])
            else:
                print("Invalid choice. Please choose a valid character number or 'done'.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    return selected_characters