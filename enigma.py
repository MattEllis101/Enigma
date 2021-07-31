#############################################################
#         Authors: Mathew Ellison and Frank Stomp           #
#  The Enigma Machine program uses 7 other files to run     #
#  the encryption process. Four of the files are imports    #
#  the remaining 3 files are text files. The Enimga program # 
#  takes plain text and encypts the message.                # 
#############################################################

import rotors
import reflector
import inputs
import plugboard

class Enigma:
    def __init__(self, rotorList, initialPositionRotors, reflectorType):
        """
        The enigma machine is created here, by
        initializing the right, middle, and left rotors
        as well as the initial positions of each of the rotors.
        """
        
        self.rightRotor = rotors.Rotor(rotorList[2])
        self.middleRotor = rotors.Rotor(rotorList[1])
        self.leftRotor = rotors.Rotor(rotorList[0])
        self.rightOffset = ord(initialPositionRotors[2]) - ord("A")
        self.middleOffset = ord(initialPositionRotors[1]) - ord("A")
        self.leftOffset = ord(initialPositionRotors[0]) - ord("A")
        self.reflector = reflector.Reflector(reflectorType)
        self.plugboard = plugboard.Plugboard()

    def shift(self):
        """
        Rotates the rotors by one position. In some occasions there is a double shift.
        """

        if self.middleOffset == self.middleRotor.notch:
            self.middleOffset = (self.middleOffset + 1) % 26
            self.leftOffset = (self.leftOffset + 1) % 26
        else:
            if self.rightOffset == self.rightRotor.notch:
                self.middleOffset = (self.middleOffset + 1) % 26
        self.rightOffset = (self.rightOffset + 1) % 26
        
    def encrypt_forward(self, rotor, offset, char):
        """ Encrypts a character right to left and each rotor encrypts the character further.
        """

        i = (ord(char) - ord("A") + offset) % 26
        new_char = rotor.str[i]
        return chr(ord(new_char) - (offset % 26))

    def encrypt_backward(self, rotor, offset, char):
        """ Encrypts the character back through the rotors after it passes through the relector.
        No rotations of the rotors take place here.
        """

        i = ord(char) - ord("A") + offset
        new_char = chr(ord("A") + i % 26)
        i = rotor.str.find(new_char)
        return chr(ord("A") + (i - offset) % 26)

    def encrypt_next_char(self, new_char):
        """
        A character is encrypted using the functions encrypt_forward, permute, encrypt_backward, and plugboard.
        It then returns the final encyrpted character after passing through the plugboard.
        """

        enigma.shift()
        new_char = self.plugboard.str[ord(new_char) - ord("A")]
        new_char = self.encrypt_forward(self.rightRotor, self.rightOffset, new_char)
        new_char = self.encrypt_forward(self.middleRotor, self.middleOffset, new_char)
        new_char = self.encrypt_forward(self.leftRotor, self.leftOffset, new_char)
        new_char = self.permute(new_char)
        new_char = self.encrypt_backward(self.leftRotor, self.leftOffset, new_char)
        new_char = self.encrypt_backward(self.middleRotor, self.middleOffset, new_char)
        new_char = self.encrypt_backward(self.rightRotor, self.rightOffset, new_char)
        new_char = self.plugboard.str[ord(new_char) - ord("A")]
        return new_char
    
    def permute(self, char):
        """
        Permutation of a character using the reflector in module 'reflector'
        """
        i = ord(char) - ord("A")
        return self.reflector.str[i]

    def encrypt_text(self, inputFile, outputFile):
        """
        text from the inputFile are encrypted and saved to the outputFile.
        """

        new_char = " "
        while new_char:
            new_char = inputFile.read(1)
            if len(new_char) == 1 and new_char.isupper():
               new_char = enigma.encrypt_next_char(new_char)
            outputFile.write(new_char)
        
if __name__ == "__main__": 
    count = 0
    rotorList = [] 
    while count < 3:
        #rotors are selected here
        count = inputs.Inputs.rotorInputs(count, rotorList)
                                          
    count = 0
    initialPositionRotors = []
    while count < 3:
        #rotor positions are selected here
        count = inputs.Inputs.rotorSettings(count, initialPositionRotors)
        
 
    reflectorType = inputs.Inputs.reflectorInput()
    #reflector is selected here
    enigma = Enigma(rotorList, initialPositionRotors, reflectorType)
    prompt = "Do you want to encrypt or decrypt? " + "'e' for encrypt / 'd' for decrypt: "
    encrypt_or_decrypt = input(prompt)
    #plain.txt and cipher.txt are modifed here
    if encrypt_or_decrypt == "e":
        input_file = open("plain.txt", "r+")
        output_file = open("cipher.txt", "r+")
    else:
        input_file = open("cipher.txt", "r+")
        output_file = open("plain.txt", "r+")

    enigma.encrypt_text(input_file, output_file)
    
    input_file.close()
    output_file.close()
