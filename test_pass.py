# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getNextLenght(self):
        self.assertEqual(len(pwd.getNext("az")),2)
        self.assertEqual(len(pwd.getNext("aaaaz")),5)

    def test_getNextRaiseError(self):
        with self.assertRaises(ValueError):
            pwd.getNext('zzz')
            pwd.getNext('zzzzz')

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")


# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
