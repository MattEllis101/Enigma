######################################################################
#         Authors: Mathew Ellison and Frank Stomp                    #
#  This module allows the user to select three distinct rotors,      #
#  initial turns, reflector, and option of encryption or decryption. # 
#                                                                    #
######################################################################

import rotors
import reflector

class Inputs:
    """
    class created to allow the user to choose the rotors, rotor settings, and the reflector
    """
        
    def rotorInputs(count, rotorList):
        """Method used to determine which rotors to use.
        The user provides the rotors from right to left.
        """

        i = count
        while count == i:
            if count == 0:
                rotorPosition = "right"
            elif count == 1:
                rotorPosition = "middle"
            else:
                rotorPosition = "left"
            
            rotor = input("Provide the " + rotorPosition + " rotor (1 through 5): ")
         
            if rotor in rotorList: #(A rotor can be chosen only once.)
                print("Rotor must be different from one another. Select another rotor.")
            elif not(len(rotor) == 1 and ord("1") <= ord(rotor) <= ord("5")):
                print("Only rotors 1 - 5 are admissible")
            else:
                count += 1
                rotorList.insert(0, rotor)
        return count
        
    def rotorSettings(count, rotorPositions):
        """ position of what character each rotor is set to is assigned here by the character.
        """

        i = count
        if count == 0:
            rotorPosition = "right"
        elif count == 1:
            rotorPosition = "middle"
        else:
            rotorPosition = "left"
            
        while count == i:
                ch = input("Give me the initial position of the " +  rotorPosition + " rotor (A through Z): ")
                if not (len(ch) == 1 and ch.isupper()):
                    print("Only 'A' through 'Z' are admissible. (Capital letters only.)")
                else:
                    rotorPositions.insert(0, ch)
                    count += 1
        return count

    def reflectorInput():
        """ the refector is selected by the user.
        """

        ch = input("Provide a reflector (A , B, or C): ")
        while not (len(ch) == 1 and ord("A") <= ord(ch) <= ord("C")):
            print("Only A, B, or C are admissible")
            ch = input("Give me a reflector (A , B, or C): ")
        return ch
