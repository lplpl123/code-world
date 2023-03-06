from origins.origin import Origin


class OriginInstance(Origin):
    def __init__(self):
        super(OriginInstance, self).__init__()
        self.yang_nums = self.yang_nums[2]
        self.yin_nums = self.yin_nums[2]