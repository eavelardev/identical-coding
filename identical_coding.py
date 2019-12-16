import argparse
import os

cli = '>>> '
info = '-->'
tab = '    '

parser = argparse.ArgumentParser(description='Identical coding.')

parser.add_argument('-f', '--file',
    type=argparse.FileType('r'), 
    help='Input file.')

args = parser.parse_args()

f = args.file
lines = f.readlines()
f.close()

def input_line():
    read = input(cli)
    read.rstrip()
    read = read.replace('\t', tab)    
    return read

def main():
    while True:
        start_code = False
        ok = True
        os.system('clear')

        for line in lines:
            line = line.rstrip()

            if not len(line):
                if start_code:
                    print('')
                continue

            if line.startswith('#') or line.startswith('"""'):
                if start_code:
                    print(info, line)
                continue

            if start_code is False:
                start_code = True

            read = input_line()

            if read != line:
                print(info, 'Error!, practice the line. Enter to exit')
                print(info, line)

                while True:
                    read = input_line()

                    if not len(read):
                        break

                    if read != line:
                        print(info, 'Error! - Practice more')

                ok = False
                break
        
        if ok:
            opt = read = input('\nRun code? (y): ')

            if len(opt) is 0 or opt is 'y':
                print('')
                exec(open(f.name).read())

            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nTraining finished')