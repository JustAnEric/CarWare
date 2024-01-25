from memoryzero import mem0
from typing import Literal
memory_ = mem0()

def mkd_(dir):
    print(f"| MKDIR | {dir}")
    return os.mkdir(dir)

print("[0xc00] Loading temporary data into memory...")

import os
idx_install_path = memory_.mkobj("/etc/carware")

if (os.path.exists(idx_install_path)):
    print("CarWare has already been installed, skipping installation.")
    print("No more jobs, exiting.")
    exit(0)
    
if (os.path.exists('./build') and os.path.isdir('./build')):
    print("!~ CarWare builds have been previously made, removing previous builds and reinstalling/reinitializing them.")
    os.removedirs('./build')

print("Installing Carware (you may be prompted to enter root password)")
mkd_('./build')
mkd_('./build/dev')
mkd_('./build/pack')
mkd_('./build/dist')
mkd_('./build/deb')

print("Packing...")

print(f'ROOT $/> sudo mkdir -p {memory_.ldobj(idx_install_path)}')
os.system(f'sudo mkdir -p {memory_.ldobj(idx_install_path)}')

for i in [
    ( "carware-d.py"  ),
    ( "carware.py"    ),
    ( "memoryzero.py" )
]:
    print(f"| COPY | ./{i} ==> {memory_.ldobj(idx_install_path)}/{i}")
    os.system(f'sudo cp ./{i} {memory_.ldobj(idx_install_path)}/{i}')
    print(f"| COPY | Finished: ./{i} ==> {memory_.ldobj(idx_install_path)}/{i}")
    
print("[1xc00] Dumping temporary data from memory...")
memory_.clrmem()
print("[0xc001] set value rd at memory table 0xc010")
print("Finishing...")

# run the carware daemon

os.system('sudo systemctl enable carware-daemon')
os.system('sudo systemctl start carware-daemon')

print("Your CarWare Installation has successfully suceeded.")

print("---------------------------------CARWARE INSTALLATION---------------------------------")

s = input("What Wi-Fi connection do you want your CarWare to connect to when your car starts? ([o]ptional) ")
print("OK.")
if (s == '' or s == 'o'):
    print("Locally hosting CarWare server...")
    
else:
    sw = input("What is the Wi-Fi connection type ([W]PA, [w]PA2, [wP]A3, [o]pen, [We]P) ")
    if (sw != 'W' or sw != 'w' or sw.lower() != 'wp' or sw != 'o' or sw.lower() != 'we'):
        print("Not a valid Wi-Fi connection type. Cancelled setup.")
        print("~ Please try again by running carware-setup again.")
        
print("No more jobs, exiting.")