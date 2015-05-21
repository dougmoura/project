from src.a429StateMachine import  *


class a429Decoder():

    def __init__(self):

        self._data = ""
        self._stateMachine = a429StateMachine()
        self._stateMachine.clearMachine()

    def getData(self):

        if (self._data is ""):

            raise BufferError

        else:

            return self._data

    def setData(self,voltageLevel):

        if ((float(voltageLevel) < HI_LEVEL) and (float(voltageLevel) > LOW_LEVEL)):

            raise ValueError

        else:

            self._data = self._stateMachine.goToNextState(voltageLevel)



