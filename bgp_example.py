from netmiko import ConnectHandler
# не показывать пароль при вводе в консоли. НЕ РАБОТАЕТ С РОДНЫМ ШЕЛОМ ПИТОНА!!!
import getpass

user = input('Username: ')
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password: ')
command = 'sh run | s bgp'
devices_ip = ['192.168.1.1', '192.168.1.2']

for ip in devices_ip:
    print('connection to device {}'.format(ip))
    device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': user,
        'password': password,
        'secret': enable_pass
    }

    with ConnectHandler(**device_params) as ssh:
        ssh.enable()
        '''примерный вывод
        router bgp 67890\n bgp log-neighbor-changes\n network X.X.X.X mask Y.Y.Y.Y\n network X.X.X.X mask Y.Y.Y.Y\n'''
        result = ssh.send_command(command)

    print(result)
    '''router bgp 67890
        bgp log-neighbor-changes
        network X.X.X.X mask Y.Y.Y.Y
        network X.X.X.X mask Y.Y.Y.Y'''