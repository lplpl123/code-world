from origins.yinyang.yang import Yang
from origins.yinyang.yin import Yin


class ShaoYang(Yang, Yin):

    def __init__(self):
        Yang.__init__(self)
        Yin.__init__(self)
        self.shaoyang = [self.yin_yao, self.yang_yao]

shaoyang = ShaoYang()
print(shaoyang.shaoyang)