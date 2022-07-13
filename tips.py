import argparse
parser = argparse.ArgumentParser(description='Nickelback')
parser.add_argument('-a1','--a', help = ("popular song of popular band"), type = str, default = None)
parser.add_argument('-a2','--a_copy', help = ('now lyrics are changed'), type = str, default = None)
parser.add_argument('-n', '--name', help='a name to personalize motivational speech', type = input, required=True)
args =  parser.parse_args()

def CLI_function(a, a_copy, name):
    with open ('a.txt', 'r') as rhomework:
        with open ('a_copy.txt','w') as whomework:
            for line in rhomework:
                line = line.replace('o','0')
                line = line.replace('?', f'{name}?')
                whomework.write(line)

CLI_function (args.a, args.a_copy, args.name)