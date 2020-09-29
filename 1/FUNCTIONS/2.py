def how_many_planets_in_list(planets_list, needed_planet):
    count = 0
    for planet in planets_list:
        if planet == needed_planet:
            count += 1
    return count


planets_list = ['Земля', "Марс", "Земля", "Юпитер", "Касич", "Марс", "Земля"]
count = how_many_planets_in_list(planets_list, 'Земля')
print(count)
