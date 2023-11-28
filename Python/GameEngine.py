from Python.BinsGame import BinsGame
from Python.IStrategy import IStrategy

class GameEngine:
    
    def __init__(self, binsGame: BinsGame, times: int = 100000):
        self._times = times
        self._binsGame = binsGame
        self._pmf = None
        
    def setTimes(times: int):
        if times <= 0:
            raise ValueError("Illegal Argument: Number of times to simulate cannot be negative")
        self._times = times
    
    def simulateGames(self):
        n = self._binsGame.getGameSize()
        self._pmf = [0 for i in range(n + 1)]
        for i in range(self._times):
            turns = self._binsGame.play()
            self._pmf[turns] += 1/self._times
    
    def summary(self):
        n = self._binsGame.getGameSize()
        if self._pmf == None:
            self.simulateGames()
        cumulative = 0
        for i in range(n):
            if cumulative == 0 and cumulative + self._pmf[i] >= 0:
                print("Min.:\t", i)
            if cumulative < .25 and cumulative + self._pmf[i] >= .25:
                print("1st Qu.:", i)
            if cumulative < .5 and cumulative + self._pmf[i] >= .5:
                print("Median:", i)
                print("Mean\t:", "{:.2f}%".format(GameEngine.getMean(pmf)))
            if cumulative < .75 and cumulative + self._pmf[i] >= .75:
                print("3rd Qu.:", i)
            if cumulative < 1.0 and cumulative + self._pmf[i] == 1.0:
                print("Max:\t", i)
            cumulative += self._pmf[i]
       

    def getMean(pmf):
        if pmf == None:
            raise ValueError("Probability mass function not defined")
        return sum([i * pmf[i] for i in range(len(pdf))]) / len(pdf)
    
    def getStdrdError(pmf):
        if pmf == None:
            raise ValueError("Probability mass function not defined")
        mean = getMean(pmf)
        return math.sqrt(sum([(i - mean)**2 * pmf[i] for i in range(len(pdf))]) / (len(pdf) - 1))
                                                                
                      
                