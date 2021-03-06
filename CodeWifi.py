# coding: utf-8
import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode('iso8859-1')


NameWifi = (re.findall("Profil Tous les utilisateurs    ÿ: (.*)\r",command_output))

wifi_list = list()

if len(NameWifi) != 0:
    for name in NameWifi:
        wifi_profile = dict()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode('iso8859-1')
        if re.search("Clé           : Absente", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],capture_output = True).stdout.decode('iso8859-1')
            password = re.search("Contenu de la cl            :(.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])

