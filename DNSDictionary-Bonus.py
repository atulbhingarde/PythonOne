import pprint
def GetList(ThisList,thisProvider):
    yy=thisProvider.split(",")
    buildStruct = []
    for MyIndex in range(len(yy)):
        found = False
        #print(f'{yy[MyIndex]}')
    
        return_ip=""
        for thisPrimary in ThisList:
            if ( not found ) :
                # print(f'{thisPrimary}')
                found = yy[MyIndex] in thisPrimary["provider_name"]
                if ( found ): 
                    buildStruct.append(thisPrimary)
                    #print(f' this is it {buildStruct}')

    return(buildStruct)    
def GetTot(ThisList,thisProvider):
    
    found = False
    return_ip=""
    for thisPrimary in ThisList:
        if ( not found ) :
            # print(f'{thisPrimary["provider"]}')
            found = thisProvider in thisPrimary["provider_name"]
            if ( found ): return_ip= thisPrimary
    return(return_ip)    
def GetSecondaryIP(ThisList,thisProvider):
    
    found = False
    return_ip=""
    for thisPrimary in ThisList:
        if ( not found ) :
            # print(f'{thisPrimary["provider"]}')
            found = thisProvider in thisPrimary["provider"]
            if ( found ): return_ip= thisPrimary["ip"]
    return(return_ip)    

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

# Use a for loop to create a dictionary mapping the provider names to their IPs


# Use the dictionary to print Hurricane Electric's IP


##################################
### Part 2 - List of Providers ###
##################################

# Use a for loop to create a list of dictionaries with the associated information


# Use the list to print the total number of providers


#############################################################
### Part 3 (Bonus) - Adding Secondaries to the Dictionary ###
#############################################################
secondary_ips = [
    {"provider": "Level3", "ip": "209.244.0.4"},
    {"provider": "Verisign", "ip": "64.6.65.6"},
    {"provider": "Google", "ip": "8.8.4.4"},
    {"provider": "Quad9", "ip": "149.112.112.112"},
    {"provider": "DNS.WATCH", "ip": "84.200.70.40"},
    {"provider": "Comodo Secure DNS", "ip": "8.20.247.20"},
    {"provider": "OpenDNS Home", "ip": "208.67.220.220"},
    {"provider": "Norton ConnectSafe", "ip": "199.85.127.10"},
    {"provider": "GreenTeamDNS", "ip": "209.88.198.133"},
    {"provider": "SafeDNS", "ip": "195.46.39.40"},
    {"provider": "OpenNIC", "ip": "23.94.60.240"},
    {"provider": "SmartViper", "ip": "208.76.51.51"},
    {"provider": "Dyn", "ip": "216.146.36.36"},
    {"provider": "FreeDNS", "ip": "37.235.1.177"},
    {"provider": "Alternate DNS", "ip": "23.253.163.53"},
    {"provider": "Yandex.DNS", "ip": "77.88.8.1"},
    {"provider": "UncensoredDNS", "ip": "89.233.43.71"},
    {"provider": "Neustar", "ip": "156.154.71.1"},
    {"provider": "Cloudflare", "ip": "1.0.0.1"}
]


####################################
### Part 1 - Provider Dictionary ###
####################################
DNS_dictionary = {}

# Use a for loop to create a dictionary mapping the provider names to their IPs. expected output: {'Level3': '209.244.0.3', ...}
#<YOUR CODE HERE>
temp_dict = {}
#temp = [] 
#print(f' this secondary {secondary_ips}')
ttyl = [] 
# ind=1
for value in secondary_ips:
    temp_dict = value
    
    ttytemp=temp_dict['ip']
    
    
    # ind = ind + 1 
    ttyl.extend({ttytemp})
    
print(f'{ttyl[1]}')
print(f'length of providers {len(providers)}')
print(f'length of secondary {len(ttyl)}')
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

ry = len(ttyl)

print(f'one moe {secondary_ips[1].values()}')

print(f'secondary_type is of {type(secondary_ips)}')
for Provider in range(LengthOfProviders):
       temp_dict = {}
       temp_dict['provider_name'] = providers[Provider]
       temp_dict['primary_server'] = ips[Provider]
       tp=providers[Provider]

       print(f'here {tp}')
       print(len(secondary_ips))
       LocSecIp=GetSecondaryIP(secondary_ips,providers[Provider])
       print(LocSecIp)
       if ( LocSecIp != ""  ): 
           temp_dict['secondary_server'] = LocSecIp
           print(f'after addig {temp_dict}')
        
    
       DNS_dictionaries.append(temp_dict)
print("DNS Dictionaries: ")
print(DNS_dictionaries)

print("--------")

# Use the list to print the total number of providers
print("Number of providers: "+ str(len(DNS_dictionaries)))
print("--------")
print("--------")
# Use a for loop to update your dictionary from part 1 with the new IPs

    # set provider value in dictionary to array of IPs (new and old)

# Use the dictionary to print Hurricane Electric's IPs

#######################################################
### Part 4 (Bonus) - Adding Secondaries to the List ###
#######################################################

# Use nested for loops to update the list from part 2 with a "secondary_server" key.
#print(f'secondary array {len(ttyl) original arraay '{len(DNS_dictionaries)}')
yy = GetTot(DNS_dictionaries,"Google")
print(yy)
mylist="Level3,Verisign"
yy = GetList(DNS_dictionaries,mylist)
#print(f'{yy}')
pprint.pprint(yy)
