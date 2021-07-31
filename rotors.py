#############################################################
#         Authors: Mathew Ellison and Frank Stomp           #
#                                                           #
# The five rotors which could be used in the enigma machine #
# are described by strings.                                 #
# Three, different from one another were selected for       #
# encryption                                                #
# The rotors are numbered 1 through 5                       #
#############################################################

class Rotor():
    """
    Five rotors with 26 characters shuffled in a specific order.
    These rotors were taken from https://en.wikipedia.org/wiki/Enigma_rotor_details, where they are called
    Rotor I, Rotor II, Rotor III, Rotor IV, and Rotor V.
    """
    
    def rotor1(self):
        return "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        
    def rotor2(self):
        return "AJDKSIRUXBLHWTMCQGZNPYFVOE"

    def rotor3(self):
        return "BDFHJLCPRTXVZNYEIWGAKMUSQO"

    def rotor4(self):
        return "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    
    def rotor5(self):
        return "VZBRGITYUPSDNHLXAWMJQOFECK"

    def __init__(self, rotor):
        """
        This is used to create a rotor object and its notch.
        """
        
        if rotor == "1":
            self.str = self.rotor1()
            self.notch = ord("Q") - ord("A")
        elif rotor == "2":
            self.str = self.rotor2()
            self.notch = ord("E") - ord("A")
        elif rotor == "3":
            self.str = self.rotor3()
            self.notch = ord("V") - ord("A")
        elif rotor == "4":
            self.str = self.rotor4()
            self.notch = ord("J") - ord("A")
        elif rotor == "5":
            self.str = self.rotor5()
            self.notch = ord("Z") - ord("A")




     
    
