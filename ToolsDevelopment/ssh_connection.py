from paramiko import SSHClient
import paramiko

ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="localhost", port=32768, username="root", password="root")
# ssh.load_system_host_keys()
# ssh.connect('user@server:path')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls /')
print("============stdout===============")
for i in ssh_stdout:
    print(i)
print("============stderr===============")
for i in ssh_stderr:
    print(i)
print("============complete===============")
#print(ssh_stdout)
ssh.close()



# import paramiko
# import sys
#
# nbytes = 4096
# hostname = 'slc05ale.us.oracle.com'
# port = 22
# username = 'gvidyara'
# password = 'Wabi4moth'
# command = 'pwd;hostname'
#
# client = paramiko.Transport((hostname, port))
# client.connect(username=username, password=password)
#
# stdout_data = []
# stderr_data = []
# session = client.open_channel(kind='session')
# session.exec_command(command)
# while True:
#     if session.recv_ready():
#         stdout_data.append(session.recv(nbytes))
#     if session.recv_stderr_ready():
#         stderr_data.append(session.recv_stderr(nbytes))
#     if session.exit_status_ready():
#         break
#
# print('exit status: ', session.recv_exit_status())
# print(session.recv(nbytes))
# #print(''.join(stdout_data))
# #print(''.join(stderr_data))
#
# session.close()
# client.close()