from socket import *
from conf import *


def main(cli):
    try:
        while True:
            direction = raw_input('> ')
            cli.send(direction)
            data = cli.recv(conf['BUFSIZ'])
            if data == 'stop' or not data:
                print 'Power off Controller.'
                break
            print 'Response: %s' % data
    except KeyboardInterrupt:
        print 'Terminating Controller.'
        cli.close()


if __name__ == '__main__':
    robotCli = socket(AF_INET, SOCK_STREAM)
    robotCli.connect(conf['ADDRESS'])

    main(robotCli)
