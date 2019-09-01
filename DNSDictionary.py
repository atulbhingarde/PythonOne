providers = ["Level3", "Verisign", "Google", "Quad9", "DNS.WATCH",
             "Comodo Secure DNS", "OpenDNS Home", "Norton ConnectSafe",
             "GreenTeamDNS", "SafeDNS", "OpenNIC", "SmartViper", "Dyn",
             "FreeDNS", "Alternate DNS", "Yandex.DNS", "UncensoredDNS",
             "Hurricane Electric", "puntCAT", "Neustar", "Cloudflare",
             "Fourth Estate"]

ips = ["209.244.0.3", "64.6.64.6", "8.8.8.8", "9.9.9.9", "84.200.69.80",
       "8.26.56.26", "208.67.222.222", "199.85.126.10", "81.218.119.11",
       "195.46.39.39", "69.195.152.204", "208.76.50.50", "216.146.35.35",
       "37.235.1.174", "198.101.242.72", "77.88.8.8", "91.239.100.100",
       "74.82.42.42", "109.69.8.51", "156.154.70.1", "1.1.1.1", "45.77.165.194"]


####################################
### Part 1 - Provider Dictionary ###
####################################
DNS_dictionary = {}

# Use a for loop to create a dictionary mapping the provider names to their IPs. expected output: {'Level3': '209.244.0.3', ...}
#<YOUR CODE HERE>
print(f'length of providers {len(providers)}')
LengthOfProviders=len(providers)
for Provider in range(LengthOfProviders):
       print(f'provider is at {Provider} {providers[Provider]} ips {ips[Provider]}')
       DNS_dictionary[providers[Provider]] = ips[Provider]

print("DNS Dictionary: ")
print(DNS_dictionary)
print("--------")

# Use the dictionary to print Hurricane Electric's IP
print("Hurricane Electric's IP is: |" + DNS_dictionary['Hurricane Electric']+"|")
print("--------")
print("--------")


##################################
### Part 2 - List of Providers ###
##################################
DNS_dictionaries = []
temp_dict = {}

# Use a for loop to create a list of dictionaries with the associated information. expected output: 
# [{'provider_name': 'Level3', 'primary_server': '209.244.0.3'}, ...]
#atul <YOUR CODE HERE>
for Provider in range(LengthOfProviders):
       temp_dict = {}
       temp_dict['provider_name'] = providers[Provider]
       temp_dict['primary_server'] = ips[Provider]
       print(f'{temp_dict}')
       DNS_dictionaries.append(temp_dict)
print("DNS Dictionaries: ")
print(DNS_dictionaries)

print("--------")

# Use the list to print the total number of providers
print("Number of providers: "+ str(len(DNS_dictionaries)))
print("--------")
print("--------")

