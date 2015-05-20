import unittest
from src.a429Decoder import *

class test_a429Decoder (unittest.TestCase):

    def setUp(self):
         self.a429Decoder = a429Decoder()

    def test_receiveNoneData(self):

        with self.assertRaises(BufferError):

            self.assertEqual (self.a429Decoder.getData(),"")

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

    def tearDown(self):
        pass
