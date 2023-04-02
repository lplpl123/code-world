from origins.yinyang.yin import Yin


class TaiYin(Yin):

    def __init__(self):
        Yin.__init__(self)
        self.taiyang = [self.yin_yao, self.yin_yao]