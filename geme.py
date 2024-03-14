import main.object as obj

class game:
    def start():
        res = False
        while res == False:
            post = int(input("ポケモンをやろうぜ"))
            condition = False
            if post == 0:
                res = True
            elif post == 1:
                pId = int(input("ポケモンの情報を入れてください"))
                pikatyuu = obj.pokemon(pId)
                pikatyuu.Detail()

gam = game
game.start()
