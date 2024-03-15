from DB.Repository import pokemonRepository as p

class pokemon:
    def __init__(self, code, domein=0):
        self.code = code
        poke = p.findPoke(self.code)
        if poke:
            self.name = poke['name']
            self.edit_name = poke['name']
            self.type_code = poke['type_code']
            self.type_name = poke['type_name']
            self.sub_type = poke['sub_type']
            self.waza = {}
            self.trainer = ''
            self.level = 1
            self.parameter = poke['parameter']
            print(self.parameter)
        else:
            raise ValueError("存在しないポケだよー")
        
    def Detail(self):
        print("名前：" + self.name + "\n属性：" + self.type_name + "、" + self.sub_type)

    def Damage(waza):
        waza
        
    def Attack(poke, waza_code):
        print(poke.waza)

class trainer:
    def __init__(self, id) -> None:
        self.id  = id
try:
    condition = True
except ValueError as e:
    print("does not exist")