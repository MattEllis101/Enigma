ENIGMA

This project is a software simulation, implemented in Python 3, of the German enigma machine. The enigma machine was used during WW2 for secure communication.

The Python code consists of four Python modules and three text files.

The four Python modules are:
-- enigma.txt (This models the enigma machine)
-- inputs.py (The module to choose the rotors, their initial positions, and the reflector)
-- plugboard.py (The module to set the plugboard. That information is in plugboard.txt.)
-- reflector.py (modeling there various reflectors.)


The three text files are:
-- plain.txt (The plain text.)
-- cipher.txt (The cipher text.)
-- plugboard.txt (Contains all characters.)

The text files can be modified. For proper simulation, the plugboard.txt should contain all uppercase letters. Six of them are replaced by themselves. There are ten pairs of distinct components, which will be interchanged,


-- To excuse the code, simply run enigma.py. You will need to have the python, version 3.7.4 or later to run these files properly.This program was created by
Mathew Ellison and Frank Stomp.

If you have any questions please contact mathew.ellison@navajotech.edu
