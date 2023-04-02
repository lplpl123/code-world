from origins.yinyang.yang import Yang
from origins.yinyang.yin import Yin


class ShaoYin(Yang, Yin):

    def __init__(self):
        Yang.__init__(self)
        Yin.__init__(self)
        self.shaoyin = [self.yang_yao, self.yin_yao]
