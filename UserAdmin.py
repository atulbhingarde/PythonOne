# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below

def getCreds():
    retDict = dict()
    #{"username": "", "password": ""}
    yourUserId = ""
    while ( len(yourUserId) == 0 ):
        yourUserId = input(f' Please key in your userid ')
    yourPassword = input(f' Hi {yourUserId} ! please key in your password ')
    retDict  = dict(username=yourUserId, password=yourPassword)
    return retDict
    
def checkLogin(adminList1,UserInfo):
    athandUser=UserInfo.get("username")
    athandPass=UserInfo.get("password")
    found = False
    for i in adminList1:
        user=i.get("username")
        pass1=i.get("password")
        #print(f'{user} and {pass1}')
        if ( not found ):
            found = ( ( athandPass == pass1 ) and ( athandUser == user ) )
            #print(f'{found} {user}')
    return found
    print(f'{UserInfo}')
    print(f'{adminList1}')
    #for 

hh = checkLogin(adminList,getCreds())
print(f'{hh}')