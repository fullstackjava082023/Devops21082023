# install ansible
sudo apt update
sudo apt install ansible -y


# print ansible version
ansible --version

ansible localhost -m ping
ansible localhost -m shell -a "echo hello world"
