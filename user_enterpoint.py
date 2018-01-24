#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import getpass
import subprocess
from django.contrib.auth import authenticate

class UserPortal(object):

    def __init__(self):
        self.user = '123'

    def user_auth(self):
        retry_count = 0
        while retry_count <= 3:
            username = input('Username:')
            if len(username) == 0: continue
            password = getpass.getpass("Password:").strip()
            if len(password) == 0:
                print("Password cannot be null.")
                continue

            user = authenticate(username=username, password=password)
            if user:
                self.user = user
                return
            else:
                print("Invalid username or password!")
            retry_count += 1

    def interactive(self):
        self.user_auth()
        if self.user:

            exit_flag = False
            while not exit_flag:

                for index,host_group in enumerate(self.user.host_groups.all()):
                    print('%s. %s [%s]'%(index,host_group.name,host_group.bind_hosts.all().count()))

                print('%s. Ungrouped Hosts [%s]'%(index+1,self.user.bind_hosts.all().count()))

                user_input = input("Choose Group:").strip()
                if len(user_input) == 0: continue
                if user_input.isdigit():
                    user_input = int(user_input)
                    if user_input >= 0 and user_input < self.user.host_groups.all().count():
                        selected_hostgroup = self.user.host_groups.all()[user_input]
                    elif user_input == self.user.host_groups.all().count():
                        selected_hostgroup = self.user
                    else:
                        print("invalid host group")
                        continue

                    while True:

                        for index, bind_host in enumerate(selected_hostgroup.bind_hosts.all()):

                            print("%s. %s(%s user:%s)" % (index,
                                                          bind_host.host.hostname,
                                                          bind_host.host.ip_addr,
                                                          bind_host.host_user.username))

                        user_input2 = input("Choose Host:").strip()
                        if len(user_input2) == 0: continue
                        if user_input2.isdigit():
                            user_input = int(user_input2)
                            if user_input >= 0 and user_input < selected_hostgroup.bind_hosts.all().count():
                                select_host = selected_hostgroup.bind_hosts.all()[user_input]
                                print('Connecting ...........',select_host)
                                cmd_inp = 'sshpass -p {password} ssh {user}@{ip_addr} -o "StrictHostKeyChecking no"'.format(password=select_host.host_user.password,
                                                                                                                            user = select_host.host_user.username,
                                                                                                                            ip_addr = select_host.host.ip_addr)
                                subprocess.run(cmd_inp,shell=True)
                                print('Logout .......... ')
                        if user_input2 == "b":
                            break

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrazyAG.settings")
    import django
    django.setup()

    from audit import models

    portal = UserPortal()
    portal.interactive()