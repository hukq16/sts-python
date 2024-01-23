from sts_random import JavaRandom,RandomXS128,stsRandom



class MathUtils:
    def __init__(self):
        self.mathrandom=RandomXS128()


    def randomInt(self, range:int,end:int = None):
        if end is None:
            return self.mathrandom.nextInt(range+1)
        else:
            return range + self.mathrandom.nextInt(end - range + 1)

    def randomLong(self ,range:int,end:int = None):
        if end is None:
            return int(self.mathrandom.nextDouble() * range)
        else:
            return range + int(self.mathrandom.nextDouble() * float(end - range))
