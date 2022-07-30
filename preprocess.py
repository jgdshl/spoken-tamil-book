#!/home/jiggy/miniconda3/bin/python

import sys
import os

def main ():
    error, inputfile, outputfile = validate_args ()

    if error:
        raise Exception()
    
    print (inputfile, outputfile)

def validate_args ():
    '''
    validates required arguments and returns error if input file is missing
    '''
    arg_length = len (sys.argv)

    return_obj = {
        error: False,
        error_str: '',
        inputfile: None,
        outputfile: None,
    }

    if arg_length == 1:
        return_obj.error_str = 'Missing input file'
        return_obj.error = True

    elif arg_length == 2:
        _, inputfile = sys.argv
    
    elif arg_length == 3:
        _, inputfile, outputfile = sys.argv
    
    else:
        print ('Invalid number of arguments')
        error = True

    if outputfile == None:
        outputfile = os.path.join(
            '.',
            'preprocessed',
            os.path.basename(inputfile),
        )

    return (error, inputfile, outputfile)


def preprocess (line):
    trans_on = False
    symbols = {
        'E': 'ê',
        'O': 'ô',
        'U': 'ù',
        'N': 'ɳ',
        'L': 'ɭ',
        'z': 'ʐ',
    }

if __name__ == '__main__':
    main()