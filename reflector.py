############################################################
#         Authors: Mathew Ellison and Frank Stomp          #
#                                                          #
# There were three different reflectors. Each of them is   #
# described by a string.                                   #
# One reflector was chosen for encryption. The reflectors  #
# are numbered A through C                                 #
############################################################

class Reflector:
    """
    Models a 'reflector' in the Enigma machine.
    See https://en.wikipedia.org/wiki/Enigma_rotor_details#Ring_setting.
    """

    def reflectorA(self):
        return "EJMZALYXVBWFCRQUONTSPIKHGD"

    def reflectorB(self):
        return "YRUHQSLDPXNGOKMIEBFZCWVJAT"

    def reflectorC(self):
        return "FVPJIAOYEDRZXWGCTKUQSBNMHL"

    def __init__(self, char):
        """
        reflectors are assigned to a specific character for user input.
        """

        if char == "A":
            self.str = self.reflectorA()
        elif char == "B":
            self.str = self.reflectorB()
        elif char == "C":
            self.str = self.reflectorC()
                
