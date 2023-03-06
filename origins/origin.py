from origins.yang import Yang
from origins.yin import Yin


# 现在感觉这里只是一个混沌
class Origin(Yang, Yin):
    def __init__(self):
        Yang.__init__(self)
        Yin.__init__(self)