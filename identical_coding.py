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

not_process = ['#', '"', '/', '*', 'import ', 'from ']

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
            
            accept_line = True
            for string in not_process:
                if line.lstrip().startswith(string):
                    accept_line = False
                    break

            if not accept_line:
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
            opt = input('\nRun code? (y): ')

            if len(opt) is 0 or opt is 'y':
                print('')
                if f.name.endswith('.py'):
                    os.system('python ' + f.name)
                elif f.name.endswith('.java'):
                    os.system(f'javac {f.name}')

                    dirname = os.path.dirname(f.name)
                    basename = os.path.basename(f.name)
                    filename = os.path.splitext(basename)[0]
                    os.system(f'java -cp {dirname} {filename}')
                    
                    os.system(f'rm {os.path.splitext(f.name)[0]}.class')
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nTraining finished')
