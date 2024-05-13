#!/usr/bin/env python3

from typing import Optional
import re
import sys

def markdown_include(inputFile: str, outputFile: Optional[str] = None) -> None:
    # define default output filename
    if outputFile is None:
        indexPeriod = inputFile.rfind('.')

        if indexPeriod == -1:
            prefix = inputFile
            suffix = ''
        else:
            prefix = inputFile[:indexPeriod]
            suffix = inputFile[indexPeriod:]

        outputFile = prefix + '_mdincl_output' + suffix

    # fine the relative dir of the inputFile
    indexSlash = inputFile.rfind("/")
    if indexSlash == -1:
        directory = "./"
    else:
        directory = inputFile[:indexSlash+1]

    try:
        with open(inputFile, 'r') as file:
            content = file.read()
    except:
        print('Unexcepted Error: input file read error')
        sys.exit()

    includes = re.findall(r'<!-- include \((.*)\) -->', content)

    for include in includes:
        try:
            with open(directory + include, 'r') as file:
                includeContent = file.read()
        except:
            print('Unexcepted Error: included file cannot be found')
            sys.exit()

        content = content.replace(
            '<!-- include ({}) -->'.format(include),
            includeContent
        )

    with open(outputFile, 'w') as file:
        file.write(content)
