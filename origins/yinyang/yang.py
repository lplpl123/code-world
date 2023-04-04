class Yang:
    def __init__(self):
        self.approch_target = True  # todo 以后改为类的属性，现在是实例的属性，因为阴阳是不可能实例化的
        self.yang_nums = [1, 3, 5, 7, 9]
        self.xiangs = ['初生', '上升加速', '上升最快', '上升减速', '极致']
        self.yang_yao = "++"

    def create_yang_steps(self):
        self.yang_steps = {}
        for yang_num, xiang in zip(self.yang_nums, self.xiangs):
            self.yang_steps[yang_num] = xiang


# test
yang = Yang()
yang.create_yang_steps()
print(yang.yang_steps)