from sts_random import JavaRandom,RandomXS128,stsRandom



class MathUtils:
    def __init__(self):
        self.mathrandom=RandomXS128()


    def randomInt(self, range:int):
        return self.mathrandom.nextInt(range+1)

    def randomInt(self,start:int,end:int):
        return start + self.mathrandom.nextInt(end-start +1)

    def randomLong(self ,range:int):
        return int(self.mathrandom.nextDouble() * range)

    def randomLong(self,start:int,end:int):
        return start + int(self.mathrandom.nextDouble() * float(end - start))
