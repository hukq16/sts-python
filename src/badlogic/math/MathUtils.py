from sts_random import JavaRandom, RandomXS128, stsRandom


class MathUtils:
    mathrandom = RandomXS128()

    @classmethod
    def randomInt(cls, range: int, end: int = None):
        if end is None:
            return cls.mathrandom.nextInt(range + 1)
        else:
            return range + cls.mathrandom.nextInt(end - range + 1)

    @classmethod
    def randomLong(cls, range: int, end: int = None):
        if end is None:
            return int(cls.mathrandom.nextDouble() * range)
        else:
            return range + int(cls.mathrandom.nextDouble() * float(end - range))

    @classmethod
    def shuffle(cls, target_list, random):

        size = len(target_list)
        SHUFFLE_THRESHOLD = 5  # 假设的阈值，具体值根据Java代码确定

        if size < SHUFFLE_THRESHOLD or isinstance(target_list, list):
            for i in range(size, 1, -1):
                cls.swap(target_list, i - 1, random.nextInt(i))
        else:
            arr = target_list[:]  # 创建列表的副本

            # 打乱数组
            for i in range(size, 1, -1):
                cls.swap(arr, i - 1, random.nextInt(i))

            # 将数组元素回写到列表
            for i, item in enumerate(arr):
                target_list[i] = item

    @staticmethod
    def swap(target_list, i, j):
        """ 交换列表中的元素 """
        target_list[i], target_list[j] = target_list[j], target_list[i]
