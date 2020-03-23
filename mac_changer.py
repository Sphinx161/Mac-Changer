import subprocess

interface = input("interface >>")
mac_add = (input("mac >>"))

print("[*] Changing mac values of " + interface + " with mac address " + mac_add)
# subprocess.call("sudo ifconfig " + interface + " down", shell=True)
# subprocess.call("sudo ifconfig " + interface + " hw ether " + mac_add, shell=True)
# subprocess.call("sudo ifconfig " + interface + " up", shell=True)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_add])
subprocess.call(["ifconfig", interface, "up"])

