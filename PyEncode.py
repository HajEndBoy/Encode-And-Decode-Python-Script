import base64
import sys
print('EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam EndTeam')
fnameINPUT = input('File Name: ')
def main():
    fname = fnameINPUT
    with open(fname, 'rb') as f:
        data = f.read()

    with open(fname, 'wb') as f:
        f.write(base64.encodebytes(data))

if __name__ == '__main__':
    main()