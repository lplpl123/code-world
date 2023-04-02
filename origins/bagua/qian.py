from origins.yinyang.yang import Yang
from origins.sixiang.taiyang import TaiYang


class Qian(TaiYang, Yang):

    def __init__(self):
        TaiYang.__init__(self)
        Yang.__init__(self)
        self.qian = self.taiyang.append(self.yang_yao)