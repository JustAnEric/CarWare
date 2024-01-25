from memoryzero import mem0
from typing import Literal
memory_ = mem0()

def mkd_(dir):
    print(f"| MKDIR | {dir}")
    return os.mkdir(dir)
    

print("[0xc00] Loading temporary data into memory...")

import os
idx_install_path = memory_.mkobj(Literal["/etc/carware"])

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
    print(f"| COPY | ./{i[0]} ==> {memory_.ldobj(idx_install_path)}/{i[0]}")
    os.system(f'sudo cp ./{i[0]} {memory_.ldobj(idx_install_path)}/{i[0]}')
    print(f"| COPY | Finished: ./{i[0]} ==> {memory_.ldobj(idx_install_path)}/{i[0]}")
    
print("[1xc00] Dumping temporary data from memory...")
memory_.clrmem()
print("[0xc001] set value rd at memory table 0xc010")
print("Finishing...")

# run the carware daemon

os.system('sudo systemctl enable carware-daemon')
os.system('sudo systemctl start carware-daemon')

print("Your CarWare Installation has successfully suceeded.")
