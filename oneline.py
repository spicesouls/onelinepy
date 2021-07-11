#!/bin/env python3

###########################
# spicesouls.github.io <3 #
###########################
###########################################
from colorama import init, Fore, Style, Back; init()
banner = fr'''{Style.BRIGHT}
              _ _                 
  ___ ___ ___| |_|___ ___{Fore.YELLOW} ___ _ _{Fore.RESET}
 | . |   | -_| | |   | -_{Fore.YELLOW}| . | | |{Fore.RESET}     {Fore.YELLOW}Python{Fore.RESET}
 |___|_|_|___|_|_|_|_|___{Fore.YELLOW}|  _|_  |{Fore.RESET}     {Fore.BLUE}Obfuscator{Fore.RESET}
                         {Fore.YELLOW}|_| |___|{Fore.RESET}
'''
import sys, json, base64, codecs, encoders
###########################################

print(banner)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m", help="obfuscating Method (i.e, -m /one_line/base64)")
parser.add_argument("-i", help="Iterations For obfuscation.", default=1, type=int)
parser.add_argument("--script", help="File path of Python file to obfuscate.")
parser.add_argument("--code", help="Python code to obfuscate.")
parser.add_argument("--list", help="List obfuscating Methods.", action="store_true")
parser.add_argument("--output", help="Output File.")

args = parser.parse_args()

if args.list:
    print('''
  obfuscators ( * = May cause Syntax Errors )
 -=============-''')
    json = encoders.getjsonlist()
    count = 0
    for a in json:
        for b in json[a]:
            print(' ' + str(count) + '\t/' + a + '/' + b)
            count += 1
    sys.exit()

outputflag = None
if not args.m:
    pass
else:
    if not args.output:
        outputflag = False
    else:
        outputflag = True
    if not args.script and not args.code:
        print(' Error: Please provide Code or a File Path for obfuscation!')
    elif not args.script:
        try:
            method = encoders.getjsonall()[args.m]
        except KeyError:
            try:
                method = encoders.getjsonall()[args.m + '*']
            except KeyError:
                print(' Error: Invalid obfuscation Method Given!')
                sys.exit()
        print('  --> Code To obfuscate:', args.code)
        funcline = 'encoders.' + method
        if args.m.startswith('/one_line/'):
                print('[-+-] Starting obfuscation, iterations:', args.i)
                result = args.code
                for i in range(args.i):
                        result = eval(funcline + '(result)')
        else:
                print('[-+-] Generating...')
                result = eval(funcline + '(args.code)')
        if outputflag == False:
                print('\n[---] RESULT :' + Fore.RED + Style.BRIGHT, result, Style.RESET_ALL)
    elif not args.code:
        try:
            method = encoders.getjsonall()[args.m]
        except KeyError:
            try:
                method = encoders.getjsonall()[args.m + '*']
            except KeyError:
                print(' Error: Invalid obfuscation Method Given!')
                sys.exit()
        print('  --> Opening File...')
        with open(args.script, 'r', encoding="utf8") as o:
            code = str(o.read())
            o.close()
#       print(code)
        print('  --> Contents Read.')
        funcline = 'encoders.' + method
        if args.m.startswith('/one_line/'):
                print('[-+-] Starting obfuscation, iterations:', args.i)
                result = code
                for i in range(args.i):
                        result = eval(funcline + '(result)')
        else:
                print('[-+-] Generating...')
                result = eval(funcline + '(code)')
        if outputflag == False:
                print('\n[---] RESULT :' + Fore.RED + Style.BRIGHT, result, Style.RESET_ALL)

if outputflag == False:
    sys.exit()
elif outputflag == True:
    print('\n  --> Writing to Output File...')
    with open(args.output, 'w') as o:
        o.write(result)
        o.close()
    print('  --> Done!')
    sys.exit()

print(' Use -h For Usage.')
