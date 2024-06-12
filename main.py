import os
import subprocess
import platform

def ping_vm(ip_address):
    if platform.system().lower() == 'windows':
        command = ['ping', '-n', '1', ip_address]
    else:
        command = ['ping', '-c', '1', ip_address]
    
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def check_vms_status(vm_ip_list):
    status_dict = {}
    for ip in vm_ip_list:
        status_dict[ip] = 'active' if ping_vm(ip) else 'not active'
    return status_dict

if __name__ == "__main__":
    vm_ip_list = ['192.168.191.130','192.168.191.129']
    
    status = check_vms_status(vm_ip_list)
    
    for ip, stat in status.items():
        print("The VM " + ip + " is " + stat)
