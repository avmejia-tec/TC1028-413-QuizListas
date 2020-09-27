#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import combina_listas


class Testprueba (unittest.TestCase):

    def test_codificacion(self):
        self.assertEqual(combina_listas.combina([1 , 2 , 3] ,"Hola"),"Error tipo")
        self.assertEqual(combina_listas.combina([1 , 2 , 3] , ["Hola", "Examen"]),"Error longitud")
        self.assertEqual(combina_listas.combina([1 , 2 , 3] , ["Hola", "es" ,"Examen"]),[1 , "Hola" , 2, "es" , 3 , "Examen"])
        
if __name__ == '__main__':
    unittest.main()
