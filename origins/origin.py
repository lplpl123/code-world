from origins.yinyang.yang import Yang
from origins.yinyang.yin import Yin


# 现在感觉这里只是一个混沌
class Origin(Yang, Yin):
    def __init__(self):
        Yang.__init__(self)
        Yin.__init__(self)