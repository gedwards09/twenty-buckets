import math
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
        maxturns = 0
        for i in range(len(self._pmf)):
            if cumulative == 0 and cumulative + self._pmf[i] > 0:
                print("Min.:   ", i)
            if cumulative < .25 and cumulative + self._pmf[i] >= .25:
                print("1st Qu.:", i)
            if cumulative < .5 and cumulative + self._pmf[i] >= .5:
                print("Median: ", i)
                print("Mean:   ", "{:.4f}".format(self.mean()), "(sterr:", "{:.4f})".format(self.standardError()))
            if cumulative < .75 and cumulative + self._pmf[i] >= .75:
                print("3rd Qu.:", i)
            if self._pmf[i] > 0 and i > maxturns:
                maxturns = i
            cumulative += self._pmf[i]
        print("Max:    ", maxturns)
        print("")
        print("Win20 Probability:", "1 in {:0f}".format(1/self._pmf[i]))

    def mean(self):
        return self._times * sum([i * self._pmf[i] for i in range(len(self._pmf))]) / self._times
    
    def standardDeviation(self):
        mean = self.mean()
        return math.sqrt( sum([(i - mean)**2 * self._times * self._pmf[i] for i in range(len(self._pmf))]) / (self._times - 1) )
    
    def standardError(self):
        return self.standardDeviation() / math.sqrt(self._times)
        
                                                                
                      
                