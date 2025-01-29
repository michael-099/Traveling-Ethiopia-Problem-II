import heapq

class Cities:
    def __init__(self):
        self.cities={}


    def add_city(self,c1,c2,w):
        if c1 not in self.cities:
            self.cities[c1]=[c2,w]
        else :
            self.cities[c1].append([c2,w])
   

class UCS:
    def uniform_coast_search():
        pass





def main():
    print("hello")
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

    print(map.cities)
    print(len(map.cities))


if __name__ ==  "__main__":
    main()
 