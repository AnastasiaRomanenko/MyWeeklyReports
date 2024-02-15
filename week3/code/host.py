import os

hosts_file_path = "/etc/hosts"
redirect = "127.0.0.1"
domain_to_redirect = "usosweb.tu.kielce.pl"

with open(hosts_file_path, "a") as file:
    file.write(f"\n{redirect} {domain_to_redirect}\n")