import subprocess
import optparse
import re


class MacChanger:

    def __init__(self):
        pass

    @staticmethod
    def get_arguments():
        parser = optparse.OptionParser()
        parser.add_option("-i", "--interface", dest="interface", help="interface to change mac_address")
        parser.add_option("-m", "--mac", dest="new_mac", help="Mac address")
        (values, arguments) = parser.parse_args()
        if not values.interface:
            parser.error("[-] Please specify an interface, --help for more info")
        elif not values.new_mac:
            parser.error("[-] Please specify an new mac, --help for more info")
        return values

    @staticmethod
    def mac_change(interface, new_mac):
        print("[*] Changing mac values of " + interface + " with mac address " + new_mac)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])

    @staticmethod
    def get_current_mac(interface):
        ifconfig_result = subprocess.check_output(["ifconfig", interface])
        mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if mac_search_result:
            return mac_search_result.group(0)
        else:
            print("[-] Could not find a mac address")

    def execute_mac_changer(self):
        values = self.get_arguments()
        current_mac = self.get_current_mac(values.interface)
        print("Current Mac >> " + str(current_mac))
        self.mac_change(values.interface, values.new_mac)
        new_mac_add = self.get_current_mac(values.interface)
        if current_mac == values.new_mac:
            print("[+] MAC address successfully changed to " + new_mac_add)
        else:
            print("[-] MAC address did not change")


mac_changer_obj = MacChanger()
mac_changer_obj.execute_mac_changer()

