class Cities:
    def __init__(self):
        self.cities = {}  
        self.heuristic = {}  

    def add_city(self, c1, c2, w):
        if c1 not in self.cities:
            self.cities[c1] = []
        self.cities[c1].append((c2, w))

    def set_city_heuristic(self, city, h):
        self.heuristic[city] = h
   


def build_map():
    map=Cities()
    map.add_city ("Kartum", "Humera", 21)
    map.add_city ("Kartum", "Metema", 19)
    map.add_city ("Metema", "Gondar", 7)
    map.add_city ("Humera", "Shire", 8)
    map.add_city ("Humera", "Gondar", 9)
    map.add_city ("Shire", "Axum", 2)
    map.add_city ("Shire", "Debarke", 9)
    map.add_city ("Debarke", "Gondar", 4)
    map.add_city ("Axum", "Adwa", 1)
    map.add_city ("Axum", "Asmera", 5)
    map.add_city ("Adwa", "Adigrat", 4)
    map.add_city ("Adwa", "Mekelle", 7)
    map.add_city ("Adigrat", "Mekelle", 4)
    map.add_city ("Adigrat", "Asmera", 4)
    map.add_city ("Mekelle", "Sekota", 9)
    map.add_city ("Mekelle", "Alamata", 5)
    map.add_city ("Sekota", "Alamata", 6)
    map.add_city ("Sekota", "Lalibela", 9)
    map.add_city ("Lalibela", "Debre Tabor", 8)
    map.add_city ("Lalibela", "Woldia", 7)
    map.add_city ("Alamata", "Woldia", 3)
    map.add_city ("Alamata", "Samara", 11)
    map.add_city ("Samara", "Woldia", 8)
    map.add_city ("Samara", "Fanti Rasu", 7)
    map.add_city ("Fanti Rasu", "Kilbet Rasu", 6)
    map.add_city ("Debre Tabor", "Bahir Dar", 4)
    map.add_city ("Bahir Dar", "Azezo", 7)
    map.add_city ("Azezo", "Metema", 7)
    map.add_city ("Gondar", "Azezo", 1)
    map.add_city ("Bahir Dar", "Finote Selam", 6)
    map.add_city ("Bahir Dar", "Injibara", 4)
    map.add_city ("Bahir Dar", "Metekel", 11)
    map.add_city ("Injibara", "Finote Selam", 2)
    map.add_city ("Finote Selam", "Debre Markos", 3)
    map.add_city ("Debre Markos", "Debre Sina", 17)
    map.add_city ("Debre Sina", "Debre Birhan", 2)
    map.add_city ("Debre Sina", "Kemise", 6)
    map.add_city ("Kemise", "Dessie", 4)
    map.add_city ("Dessie", "Woldia", 6)
    map.add_city ("Debre Birhan", "Addis Ababa", 5)
    map.add_city ("Addis Ababa", "Ambo", 5)
    map.add_city ("Addis Ababa", "Adama", 3)
    map.add_city ("Adama", "Matahara", 3)
    map.add_city ("Matahara", "Awash", 1)
    map.add_city ("Awash", "Gabi Rasu", 5)
    map.add_city ("Awash", "Chiro", 4)
    map.add_city ("Gabi Rasu", "Samara", 9)
    map.add_city ("Chiro", "Dire Dawa", 8)
    map.add_city ("Dire Dawa", "Harar", 4)
    map.add_city ("Harar", "Babile", 2)
    map.add_city ("Babile", "Jigjiga", 3)
    map.add_city ("Jigjiga", "Dega Habur", 5)
    map.add_city ("Dega Habur", "Kebri Dehar", 6)
    map.add_city ("Kebri Dehar", "Werder", 6)
    map.add_city ("Babile", "Goba", 28)
    map.add_city ("Goba", "Sof Oumer", 6)
    map.add_city ("Goba", "Bale", 18)
    map.add_city ("Sof Oumer", "Bale", 23)
    map.add_city ("Bale", "Liben", 11)
    map.add_city ("Bale", "Dodolla", 13)
    map.add_city ("Sof Oumer", "Goder", 23)
    map.add_city ("Kebri Dehar", "Goder", 5)
    map.add_city ("Gode", "Dollo", 17)
    map.add_city ("Gode", "Mokadisho", 22)
    map.add_city ("Dodolla", "Shashemene", 3)
    map.add_city ("Shashemene", "Hawassa", 1)
    map.add_city ("Hawassa", "Dilla", 3)
    map.add_city ("Dilla", "Bule Hora", 4)
    map.add_city ("Bule Hora", "Yabello", 3)
    map.add_city ("Yabello", "Konso", 3)
    map.add_city ("Konso", "Arba Minch", 4)
    map.add_city ("Arba Minch", "Wolaita Sodo", 4)
    map.add_city ("Wolaita Sodo", "Hossana", 4)
    map.add_city ("Hossana", "Shashemene", 7)
    map.add_city ("Yabello", "Moyale", 6)
    map.add_city ("Moyale", "Nairobi", 22)
    map.add_city ("Arba Minch", "Basketo", 10)
    map.add_city ("Basketo", "Bench Maji", 5)
    map.add_city ("Bench Maji", "Juba", 22)
    map.add_city ("Wolaita Sodo", "Dawaro", 6)
    map.add_city ("Dawaro", "Bonga", 10)
    map.add_city ("Bonga", "Jimma", 4)
    map.add_city ("Bonga", "Mezan Teferi", 4)
    map.add_city ("Bonga", "Tepi", 8)
    map.add_city ("Tepi", "Mezan Teferi", 4)
    map.add_city ("Jimma", "Bedelle", 7)
    map.add_city ("Bedelle", "Nekemte", 4)
    map.add_city ("Nekemte", "Gimbi", 4)
    map.add_city ("Nekemte", "Ambo", 9)
    map.add_city ("Gimbi", "Dembi Dolo", 6)
    map.add_city ("Dembi Dolo", "Assosa", 12)
    map.add_city ("Dembi Dolo", "Gambella", 4)
    map.add_city ("Gambella", "Gore", 5)
    map.add_city ("Gore", "Tepi", 9)
    map.add_city ("Gore", "Bedelle", 6)
    map.add_city ("Jimma", "Wolkite", 8)
    map.add_city ("Wolkite", "Ambo", 6)
    map.add_city ("Wolkite", "Worabe", 5)
    map.add_city ("Hossana", "Worabe", 2)
    map.add_city ("Worabe", "Buta Jirra", 2)
    map.add_city ("Buta Jirra", "Batu", 2)
    map.add_city ("Batu", "Shashemene", 3)
    map.add_city ("Batu", "Adama", 4)
    map.add_city ("Adama", "Assella", 4)
    map.add_city ("Dodolla", "Assasa", 1)
    
    return map

def build_map_heuristic():
    map=Cities()
    
    map.add_city("Kartum", "Humera", 21)
    map.add_city("Kartum", "Metema", 19)
    map.add_city("Metema", "Gondar", 7)
    map.add_city("Humera", "Shire", 8)
    map.add_city("Humera", "Gondar", 9)
    map.add_city("Shire", "Axum", 2)
    map.add_city("Shire", "Debarke", 9)
    map.add_city("Debarke", "Gondar", 4)
    map.add_city("Axum", "Adwa", 1)
    map.add_city("Axum", "Asmera", 5)
    map.add_city("Adwa", "Adigrat", 4)
    map.add_city("Adwa", "Mekelle", 7)
    map.add_city("Adigrat", "Mekelle", 4)
    map.add_city("Adigrat", "Asmera", 4)
    map.add_city("Mekelle", "Sekota", 9)
    map.add_city("Mekelle", "Alamata", 5)
    map.add_city("Sekota", "Alamata", 6)
    map.add_city("Sekota", "Lalibela", 9)
    map.add_city("Lalibela", "Debre Tabor", 8)
    map.add_city("Lalibela", "Woldia", 7)
    map.add_city("Alamata", "Woldia", 3)
    map.add_city("Alamata", "Samara", 11)
    map.add_city("Samara", "Woldia", 8)
    map.add_city("Samara", "Fanti Rasu", 7)
    map.add_city("Fanti Rasu", "Kilbet Rasu", 6)
    map.add_city("Debre Tabor", "Bahir Dar", 4)
    map.add_city("Bahir Dar", "Azezo", 7)
    map.add_city("Azezo", "Metema", 7)
    map.add_city("Gondar", "Azezo", 1)
    map.add_city("Gondar", "Debre Tabor", 6)
    map.add_city("Bahir Dar", "Finote Selam", 6)
    map.add_city("Bahir Dar", "Injibara", 4)
    map.add_city("Bahir Dar", "Metekel", 11)
    map.add_city("Injibara", "Finote Selam", 2)
    map.add_city("Finote Selam", "Debre Markos", 3)
    map.add_city("Debre Markos", "Debre Sina", 17)
    map.add_city("Debre Sina", "Debre Birhan", 2)
    map.add_city("Debre Sina", "Kemise", 7)
    map.add_city("Kemise", "Dessie", 4)
    map.add_city("Dessie", "Woldia", 6)
    map.add_city("Debre Markos", "Addis Ababa", 13)
    map.add_city("Debre Birhan", "Addis Ababa", 5)
    map.add_city("Addis Ababa", "Ambo", 5)
    map.add_city("Addis Ababa", "Adama", 3)
    map.add_city("Adama", "Matahara", 3)
    map.add_city("Matahara", "Awash", 1)
    map.add_city("Awash", "Gabi Rasu", 5)
    map.add_city("Awash", "Chiro", 4)
    map.add_city("Gabi Rasu", "Samara", 9)
    map.add_city("Chiro", "Dire Dawa", 8)
    map.add_city("Dire Dawa", "Harar", 4)
    map.add_city("Harar", "Babile", 2)
    map.add_city("Babile", "Jigjiga", 3)
    map.add_city("Jigjiga", "Dega Habur", 5)
    map.add_city("Dega Habur", "Kebri Dehar", 6)
    map.add_city("Kebri Dehar", "Werder", 6)
    map.add_city("Babile", "Goba", 28)
    map.add_city("Goba", "Sof Oumer", 6)
    map.add_city("Goba", "Robe", 18)
    map.add_city("Sof Oumer", "Robe", 23)
    map.add_city("Robe", "Liben", 11)
    map.add_city("Robe", "Dodolla", 13)
    map.add_city("Sof Oumer", "Gode", 23)
    map.add_city("Kebri Dehar", "Gode", 5)
    map.add_city("Gode", "Dollo", 17)
    map.add_city("Gode", "Mokadisho", 22)
    map.add_city("Dodolla", "Shashemene", 3)
    map.add_city("Shashemene", "Hawassa", 1)
    map.add_city("Hawassa", "Dilla", 3)
    map.add_city("Dilla", "Bule Hora", 4)
    map.add_city("Bule Hora", "Yabello", 2)
    map.add_city("Yabello", "Konso", 3)
    map.add_city("Konso", "Arba Minch", 4)
    map.add_city("Arba Minch", "Wolaita Sodo", 4)
    map.add_city("Wolaita Sodo", "Hossana", 4)
    map.add_city("Hossana", "Shashemene", 7)
    map.add_city("Yabello", "Moyale", 6)
    map.add_city("Liben", "Moyale", 11)
    map.add_city("Dollo", "Moyale", 18)
    map.add_city("Mokadisho", "Moyale", 40)
    map.add_city("Moyale", "Nairobi", 22)
    map.add_city("Arba Minch", "Basketo", 10)
    map.add_city("Basketo", "Bench Maji", 5)
    map.add_city("Bench Maji", "Juba", 22)
    map.add_city("Wolaita Sodo", "Dawaro", 6)
    map.add_city("Dawaro", "Bonga", 10)
    map.add_city("Bonga", "Jimma", 4)
    map.add_city("Bonga", "Mezan Teferi", 4)
    map.add_city("Bonga", "Tepi", 8)
    map.add_city("Tepi", "Mezan Teferi", 4)
    map.add_city("Jimma", "Bedelle", 7)
    map.add_city("Bedelle", "Nekemte", 4)
    map.add_city("Nekemte", "Gimbi", 4)
    map.add_city("Nekemte", "Ambo", 9)
    map.add_city("Gimbi", "Dembi Dolo", 6)
    map.add_city("Gimbi", "Assosa", 8)
    map.add_city("Dembi Dolo", "Assosa", 12)
    map.add_city("Dembi Dolo", "Gambella", 4)
    map.add_city("Gambella", "Gore", 5)
    map.add_city("Gore", "Tepi", 9)
    map.add_city("Gore", "Bedelle", 6)
    map.add_city("Jimma", "Wolkite", 8)
    map.add_city("Wolkite", "Ambo", 6)
    map.add_city("Wolkite", "Worabe", 5)
    map.add_city("Wolkite", "Buta Jirra", 4)
    map.add_city("Hossana", "Worabe", 2)
    map.add_city("Worabe", "Buta Jirra", 2)
    map.add_city("Buta Jirra", "Batu", 2)
    map.add_city("Batu", "Shashemene", 3)
    map.add_city("Batu", "Adama", 4)
    map.add_city("Adama", "Assella", 4)
    map.add_city("Dodolla", "Assasa",1)


    map.set_city_heuristic("Kartum", 81)
    map.set_city_heuristic("Humera", 65)
    map.set_city_heuristic("Shire", 67)
    map.set_city_heuristic("Axum", 66)
    map.set_city_heuristic("Adwa", 65)
    map.set_city_heuristic("Adigrat", 62)
    map.set_city_heuristic("Mekelle", 58)
    map.set_city_heuristic("Sekota", 59)
    map.set_city_heuristic("Lalibela", 57)
    map.set_city_heuristic("Debre Tabor", 52)
    map.set_city_heuristic("Bahir Dar", 48)
    map.set_city_heuristic("Azezo", 55)
    map.set_city_heuristic("Metema", 62)
    map.set_city_heuristic("Gondar", 56)
    map.set_city_heuristic("Debarke", 60)
    map.set_city_heuristic("Asmera", 68)
    map.set_city_heuristic("Alamata", 59)
    map.set_city_heuristic("Woldia", 50)
    map.set_city_heuristic("Dessie", 44)
    map.set_city_heuristic("Kemise", 40)
    map.set_city_heuristic("Debre Markos", 39)
    map.set_city_heuristic("Finote Selam", 42)
    map.set_city_heuristic("Injibara", 44)
    map.set_city_heuristic("Metekel", 59)
    map.set_city_heuristic("Assosa", 51)
    map.set_city_heuristic("Gambella", 51)
    map.set_city_heuristic("Tepi", 41)
    map.set_city_heuristic("Bonga", 33)
    map.set_city_heuristic("Jimma", 33)
    map.set_city_heuristic("Bedele", 40)
    map.set_city_heuristic("Nekemte", 39)
    map.set_city_heuristic("Gimbi", 43)
    map.set_city_heuristic("Ambo", 31)
    map.set_city_heuristic("Addis Ababa", 26)
    map.set_city_heuristic("Debre Birhan", 31)
    map.set_city_heuristic("Fanti Rasu", 49)
    map.set_city_heuristic("Kilbet Rasu", 55)
    map.set_city_heuristic("Samarra", 42)
    map.set_city_heuristic("Adama", 23)
    map.set_city_heuristic("Matahara", 23)
    map.set_city_heuristic("Awash", 21)
    map.set_city_heuristic("Chiro", 31)
    map.set_city_heuristic("Dire Dawa", 31)
    map.set_city_heuristic("Harar", 35)
    map.set_city_heuristic("Babile", 37)
    map.set_city_heuristic("Jigjiga", 40)
    map.set_city_heuristic("Dega Habur", 45)
    map.set_city_heuristic("Kebri Dehar", 40)
    map.set_city_heuristic("Gode", 35)
    map.set_city_heuristic("Dollo", 18)
    map.set_city_heuristic("Moyale", 0)
    map.set_city_heuristic("Worabe", 22)
    map.set_city_heuristic("Buta Jirra", 21)
    map.set_city_heuristic("Batu", 19)
    map.set_city_heuristic("Assella", 22)
    map.set_city_heuristic("Assasa", 18)
    map.set_city_heuristic("Dodolla", 19)
    map.set_city_heuristic("Goba", 40)
    map.set_city_heuristic("Sof Oumer", 45)
    map.set_city_heuristic("Liben", 40)
    map.set_city_heuristic("Dilla", 12)
    map.set_city_heuristic("Bule Hora", 8)
    map.set_city_heuristic("Yabello", 6)
    map.set_city_heuristic("Konso", 9)
    map.set_city_heuristic("Arba Minch", 13)
    map.set_city_heuristic("Wolaita Sodo", 17)
    map.set_city_heuristic("Hossana", 21)
    map.set_city_heuristic("Shashemene", 16)
    map.set_city_heuristic("Hawassa", 15)
    map.set_city_heuristic("Dawro", 23)
    map.set_city_heuristic("Bench Maji", 28)
    map.set_city_heuristic("Basketo", 23)
    map.set_city_heuristic("Gore", 46)
    map.set_city_heuristic("Mezan Teferi", 37)
    map.set_city_heuristic("Mokadisho", 40)
    map.set_city_heuristic("Debre Sina", 33)
    map.set_city_heuristic("Gabi Rasu", 32)
    map.set_city_heuristic("Dembi Dolo", 49)
    map.set_city_heuristic("Werder", 46)
    map.set_city_heuristic("Juba", 50)
    map.set_city_heuristic("Nairobi", 22)
    map.set_city_heuristic("Wolkite", 25)
    map.set_city_heuristic("Bedelle", 40)
    map.set_city_heuristic("Dawaro", 23)
    map.set_city_heuristic("Samara", 42)
    map.set_city_heuristic("Robe", 22)

    return map



