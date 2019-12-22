_rank_c = 10
_rank_g = 20
_rank_d = 30
_rank_r = 40

class Maker:
    rank_c = _rank_c 

    def __new__(cls):
        print('new')
        print(Maker.rank_c)
        return super().__new__(cls)

    def __init__(self):
        print('init')
        print(Maker.rank_c)
        super().__init__()
        
    def make_c(self, num):
        Maker.rank_c = num

    def export_c(self):
        return Maker.rank_c

f = Maker()
print("Before:" + str(f.export_c()))
f.make_c(5)
print("After:" + str(f.export_c()))
