'''
@author: Kartikei Mittal
connect_n.py file
Contains main module of this repositry.
https://github.com/Kartikei-12/Connect-N
'''

def getVersion(file):
    # Returns version after reading from given file.
    try: # Integrating file number.
        with open(file, 'r') as f:
            temp = f.read()
            f.close()
            return temp
    except FileNotFoundError:
        return ''
