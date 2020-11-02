import os
import socket


#1. test gateway connectivity
def get_default_gateway():
    gateway = os.system('ip r | grep default | awk {"print $3"}')
    # print(f'Your default gateway is {gateway}')
    print("Your default gateway is " + gateway)

#2. test remote IP connection (129.21.3.17)
def remote_ip_connect():
    hostname = socket.gethostname()
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        print(f'Remote Connection SUCCEEDED')
    else:
        print(f'Remote Connection FAILED')


#3. test hostname connectivity to validate DNS (www.google.com)

def validate_dns():
    hostname = 'www.google.com'
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        print(f'Remote Connection SUCCEEDED')
    else:
        print(f'Remote Connection FAILED')


if __name__ == '__main__':
    print('*** Beginning Test ***')
    for i in reversed(range(5)):
        print(i)

    get_default_gateway()
    remote_ip_connect()
    validate_dns()
    print('*** Test Complete. ***')


