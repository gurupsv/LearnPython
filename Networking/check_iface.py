# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import netifaces
import psutil
import socket
import subprocess


def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr


def run_command(command_full):
    command_op = subprocess.run([command_full], stdout=subprocess.PIPE, text=True, input="args")
    return command_op


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(is_interface_up('en0'))
    print(run_command('ifconfig').stdout)


