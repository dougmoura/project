
#CONSTANTS FOR ARINC429
HI_LEVEL = 3


class a429StateMachine():

    def __init__(self):

        self._outputData = ""
        self._thisState = 0
        self._nextState = 0
        self.clear = 0


    def goToNextState(self,voltageLevel):

        if (self.clear is 1) :

            self._thisState = 0

        else:

            self._thisState = self._nextState

        return self.procesStates(voltageLevel)

    def procesStates(self,voltageLevel):

        if (self._thisState is 0):

            if (int(voltageLevel) >= HI_LEVEL):

                self._outputData += "1"
                self._nextState = 1

            else:

                self._outputData += "0"
                self._nextState = 2


        if (self._thisState is 1):

            if (int(voltageLevel) >= HI_LEVEL):

                self._outputData += "1"
                self._nextState = 1

            else:

                self._outputData += "0"
                self._nextState = 2

        if (self._thisState is 2):

            if (int(voltageLevel) >= HI_LEVEL):

                self._outputData += "1"
                self._nextState = 1

            else:

                self._outputData += "0"
                self._nextState = 2


        return self._outputData
