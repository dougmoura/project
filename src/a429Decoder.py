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

        if ((int(voltageLevel) < HI_LEVEL) and (int(voltageLevel) > LOW_LEVEL)):

            raise ValueError

        else:

            self._data = self._stateMachine.goToNextState(voltageLevel)



        # if (self._thisState is 0):
        #
        #     if (int(voltageLevel) >= HI_LEVEL):
        #
        #         self._thisState = 1
        #         self._data += "1"
        #
        #     else:
        #
        #         self._thisState = 2
        #         self._data += "0"
        #
        # elif (self._thisState is 1):
        #
        #         if (int(voltageLevel) <= LOW_LEVEL):
        #             self._thisState = 0
        #             self._data +="0"
        #
        #         else:
        #
        #             self._thisState = 0
        #             self._data += "1"
        #
        # elif (self._thisState is 2):
        #
        #         if (int(voltageLevel) >= HI_LEVEL):
        #             self._thisState = 0
        #             self._data +="1"
        #
        #         else:
        #
        #             self._thisState = 0
        #             self._data += "0"



