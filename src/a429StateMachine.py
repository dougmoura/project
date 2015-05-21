
#CONSTANTS FOR ARINC429
HI_LEVEL = 3.0
LOW_LEVEL = -3.0


class a429StateMachine():

    def __init__(self):

        self._outputData = ""
        self._thisState = 0
        self._nextState = 0
        self._clear = 0

    def clearMachine(self):

        self._clear = 1

    def goToNextState(self,voltageLevel):

        floatVoltageLevel = float(voltageLevel)

        if (self._clear is 1):

            self._clear = 0
            self._thisState = 0

        else:

           self._thisState = self._nextState

        return self.procesStates(floatVoltageLevel)

    def procesStates(self,voltage):

        if (self._thisState is 0):

            if (voltage >= HI_LEVEL):

                self._outputData += "1"
                self._nextState = 1

            else:

                self._outputData += "0"
                self._nextState = 2


        if (self._thisState is 1):

            if (voltage >= HI_LEVEL):

                self._outputData += "1"
                self._nextState = 1

            else:

                self._outputData += "0"
                self._nextState = 2

        if (self._thisState is 2):

            if (voltage >= HI_LEVEL):

                self._outputData += "1"
                self._nextState = 1

            else:

                self._outputData += "0"
                self._nextState = 2


        return self._outputData
