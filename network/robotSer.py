from socket import *
from conf import *


def process_move(direction):
    # do something here
    print 'Moving... %s' % direction


def main(robotSer):
    try:
        while True:
            print 'waiting for controller to connect...'
            robotCli, addr = robotSer.accept()
            print 'connected from: ', addr

            while True:
                direction = robotCli.recv(conf['BUFSIZ'])
                if direction == 'stop' or not direction:
                    robotCli.send('stop')
                    break

                if direction == 'close':
                    # termination
                    raise KeyboardInterrupt

                if direction not in DEFAULT_MOVE:
                    print 'invalid move.'
                    robotCli.send('Invalid move.')
                    continue

                process_move(direction)
                robotCli.send('[%s] move success.' % direction)
    except KeyboardInterrupt:
        print 'Finish Key hit, terminating process......'
        print 'closing robotCli.'
        try:
            robotCli.close()
        except:
            pass
        print 'closing robotSer.'
        robotSer.close()

if __name__ == '__main__':
    robotSer = socket(AF_INET, SOCK_STREAM)
    robotSer.bind(conf['ADDRESS'])
    robotSer.listen(5)

    main(robotSer)
