import netifaces

def list_network_interfaces():
    interfaces = netifaces.interfaces()

    network_interfaces = []
    for index, interface in enumerate(interfaces, 1):
        interface_data = {
            "idif": index,
            "name": interface,
            "ipv4": None,
            "ipv6": None
        }

        # Detalhes
        # IPv4
        try:
            if netifaces.AF_INET in netifaces.ifaddresses(interface):
                ip_info4 = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
                interface_data["ipv4"] = ip_info4.get('addr', 'None')
        except ValueError:
            interface_data["ipv4"] = "   No IPv4 address assigned"

        # IPv6
        try:
            if netifaces.AF_INET6 in netifaces.ifaddresses(interface):
                ip_info6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6][0]
                interface_data["ipv6"] = ip_info6.get('addr', 'None')
        except ValueError:
            interface_data["ipv6"] = "   No IPv6 address assigned"

        network_interfaces.append(interface_data)

    return network_interfaces



if __name__ == "__main__":
    list_network_interfaces()