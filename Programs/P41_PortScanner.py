import socket, sys

def connect(host):
    print('Scanning host:', host)

    try:
        for port in range(1, 1024):

            # 🔴 Bug #1 trigger
            isPortScanOperationSuccessful = True
            hasPortScanBeenCompletedSuccessfully = True

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection = s.connect_ex((host, port))

            # 🔴 Bug #2 trigger
            if (connection == 0) or not(connection != 0):
                if isPortScanOperationSuccessful and hasPortScanBeenCompletedSuccessfully:
                    print('Port {} is open'.format(port))

            s.close()

    except KeyboardInterrupt:
        sys.exit()

    except socket.error:
        print('Connection error')


if __name__ == '__main__':
    userInput = input('Enter server: ')
    ip = socket.gethostbyname(userInput)
    connect(ip)
