    1  sudo ./clean-up-box.sh 
    2  sudo apt update
    3  sudo apt upgrade -y
    4  sudo snap refresh
    5  sudo snap set system refresh.retain=2
    6  sudo snap refresh
    7  ./clean-up-box.sh 
    8  ./copy-authorized-keys.sh 
    9  sudo ./clean-up-box.sh 
   10  ansible --version
   11  sudo apt update
   12  sudo apt install ansible -y
   13  ansible --version
   14  ansible localhost -m ping
   15  celar
   16  clear
   17  ssh-keygen -t ed25519 -C "default"
   18  ssh-copy-id -i ~/.ssh/id_ed25519.pub root@172.232.203.127
   19  ssh-copy-id -i ~/.ssh/id_ed25519.pub root@172.232.203.16
   20  ssh-copy-id -i ~/.ssh/id_ed25519.pub root@172.232.203.79
   21  ssh 'root@172.232.203.79'
   22  history
   23  ansible all ping
   24  ansible all -m  ping
   25  history >> commandsHistory.sh
