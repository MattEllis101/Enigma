####################################################################
#         Authors: Mathew Ellison and Frank Stomp                  #
#                                                                  #
# The plugboard was supposed to add extra complexity.              #
# Ten pairs of characters were chosen. Components of the same pair #
# were permuted. (Each of the other six characters were treated as #
# the character itself.) The user can modify plugboard.txt.        #
####################################################################

class Plugboard:
   """ Ten pairs of characters are permuted.
       The remaining 6 characters of the alphabet are not permuted.
   """

   def __init__(self):
       """ The creation of a plugboard object
       """
       self.str = self.plugboard()
       
   def plugboard(self):
      """
      #F remove: The plugboard is provided in a file plugboard.txt
      #F add: A plugboard is provided in a file plugboard.txt
      """

      file = open("plugboard.txt", "r")
      line = file.readline()
      file.close()
      return line

