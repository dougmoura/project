from src.a429StateMachine import  *


class a429Decoder():

    def __init__(self):

        self._dataLenght = 32
        self._data = []
        self._label = []
        self._stateMachine = a429StateMachine()
        self._stateMachine.clearMachine()

    def getData(self):

        if (len(self._data) is 0):

            raise BufferError

        else:

            return self._data

    def setData(self,voltageLevel):

        if ((float(voltageLevel) < HI_LEVEL) and (float(voltageLevel) > LOW_LEVEL)):

            raise ValueError

        else:

            self._data = self._stateMachine.goToNextState(voltageLevel)

    def getLabel(self):

        self._label = self._data[:8]
        return list(reversed(self._label))

