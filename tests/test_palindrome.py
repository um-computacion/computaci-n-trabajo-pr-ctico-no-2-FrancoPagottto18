import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("oso"))         
        self.assertTrue(is_palindrome("salas"))       
        self.assertTrue(is_palindrome("madam"))       

 
    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("la sal"))   
        self.assertTrue(is_palindrome("la ruta natural"))      
        self.assertTrue(is_palindrome("reconocer"))             

    #def test_phrase_palindromes(self):
        #self.assertTrue(is_palindrome("la sal"))   
        #self.assertTrue(is_palindrome("la ruta natural"))      
        #self.assertTrue(is_palindrome("reconocer"))             
 

    #def test_non_palindromes(self):
        #self.assertFalse(is_palindrome("computadora"))    
        #self.assertFalse(is_palindrome("ejemplo"))      
        #self.assertFalse(is_palindrome("hola"))        

    #def test_edge_cases(self):
        #self.assertTrue(is_palindrome(""))        
        #self.assertTrue(is_palindrome("a"))       
        #self.assertTrue(is_palindrome("A"))        

if __name__ == '__main__':
    unittest.main()
