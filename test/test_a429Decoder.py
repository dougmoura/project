import unittest
from src.a429Decoder import *

class test_a429Decoder (unittest.TestCase):

    def setUp(self):

         self.a429Decoder = a429Decoder()

    def test_receiveNoneData(self):

        with self.assertRaises(BufferError):

            self.assertEquals(self.a429Decoder.getData(),"")

######################################################################
# TESTING SIMPLE TRANSITIONS OF INPUT RECEIVED FROM ANALOG BUS READER
######################################################################

    def test_hiToLowTransition(self):

        self.a429Decoder.setData("4")
        self.a429Decoder.setData("-4")
        self.assertEquals("10",self.a429Decoder._data)

    def test_lowToHiTransition(self):

        self.a429Decoder = a429Decoder()
        self.a429Decoder.setData("-4")
        self.a429Decoder.setData("4")
        self.assertEquals("01",self.a429Decoder._data)

    def test_twoHiTransitions(self):

        self.a429Decoder.setData("4")
        self.a429Decoder.setData("4")
        self.assertEquals("11",self.a429Decoder._data)

    def test_twoLowTransitions(self):

        self.a429Decoder.setData("-4")
        self.a429Decoder.setData("-4")
        self.assertEquals("00",self.a429Decoder._data)

    def test_treeHiTransitions(self):

        self.a429Decoder.setData("4")
        self.a429Decoder.setData("4")
        self.a429Decoder.setData("4")
        self.assertEquals("111",self.a429Decoder._data)

    def test_treeLowTransitions(self):

        self.a429Decoder.setData("-4")
        self.a429Decoder.setData("-4")
        self.a429Decoder.setData("-4")
        self.assertEquals("000",self.a429Decoder._data)

    def test_doubleLowTransitions(self):

        self.a429Decoder.setData("-4")
        self.a429Decoder.setData("4")
        self.a429Decoder.setData("-4")
        self.assertEquals("010",self.a429Decoder._data)

    def test_doubleHiTransitions(self):

        self.a429Decoder.setData("4")
        self.a429Decoder.setData("-4")
        self.a429Decoder.setData("4")
        self.assertEquals("101",self.a429Decoder._data)

######################################################################
#TESTING SPECIFICATION OF A429 BUS
######################################################################

    def test_voltageHiBelowThreshold(self):

        with self.assertRaises(ValueError):

            self.a429Decoder.setData("2.99")

    def test_voltageLowBelowThreshold(self):

        with self.assertRaises(ValueError):

            self.a429Decoder.setData("-2.99")

    def test_equalUpperLevel(self):

        self.a429Decoder.setData("3.00001")
        self.assertEquals("1",self.a429Decoder._data)

    def test_equalLowerLevel(self):

        self.a429Decoder.setData("-3.00001")
        self.assertEquals("0",self.a429Decoder._data)

    def tearDown(self):
        pass
