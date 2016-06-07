
import os
import socket

COMMANDS = {
    'configinit': 'Vagrant.configure(2) do |config|\n',
    'vmname': '  config.vm.box = "{0}"\n',
    'vmip': '  config.vm.network "private_network", ip: "192.168.33.10"\n',
    'configmachine': '  config.vm.provider "virtualbox" do |v|\n',
    'vname': '    v.name = "{0}"\n',
    'vmcpu': '    v.cpus = {0}\n',
    'vmmemory': '    v.memory = {0}\n',
    'endconfigmachine': '  end\n',
    'vmprovision': '  config.vm.provision "shell", inline: <<-SHELL\n',
    'vmupdate': '    sudo apt-get update\n',
    'vmpip': '    sudo apt-get -y install python-pip\n',
    'vmgit': (
        '    sudo apt-get install git-all <<EOF\n'
        'Y\n'
        '    EOF\n'
    ),
    'vmproject': '    sudo git clone https://github.com/uchoavaz/estagio_genomika.git\n',
    'vmdjango': '    sudo pip install django==1.9.7\n',
    'vmsqlite': '    sudo apt-get install sqlite3 libsqlite3-dev\n',
    'vmprovisionend': '  SHELL\n'

}


class VMCreation():
    name = None
    image = None
    initial_path = None

    commands = {
        'configinit': COMMANDS['configinit'],
        'endconfigmachine': COMMANDS['endconfigmachine'],
        'vmip': COMMANDS['vmip'],
        'configmachine': COMMANDS['configmachine'],
        'vmprovision': COMMANDS['vmprovision'],
        'vmupdate': COMMANDS['vmupdate'],
        'vmpip': COMMANDS['vmpip'],
        'vmgit': COMMANDS['vmgit'],
        'vmproject': COMMANDS['vmproject'],
        'vmdjango': COMMANDS['vmdjango'],
        'vmsqlite': COMMANDS['vmsqlite'],
        'vmprovisionend': COMMANDS['vmprovisionend'],
    }

    VARIABLES_ORDER = [
        'configinit',
        'vmname',
        'vmip',
        'configmachine',
        'vname',
        'vmcpu',
        'vmmemory',
        'endconfigmachine',
        'vmprovision',
        'vmupdate',
        'vmpip',
        'vmdjango',
        'vmsqlite',
        'vmprovisionend',
        'vmprovision',
        'vmgit',
        'vmprovisionend',
        'vmprovision',
        'vmproject',
        'vmprovisionend',
    ]

    def vm_name(self, name):
        self.commands['vmname'] = COMMANDS['vmname'].format(name)
        self.commands['vname'] = COMMANDS['vname'].format(name)
        self.name = name

    def vm_cpu(self, cpu):
        self.commands['vmcpu'] = COMMANDS['vmcpu'].format(cpu)

    def vm_memory(self, memory):
        self.commands['vmmemory'] = COMMANDS['vmmemory'].format(memory)

    def vm_path_image(self, image):
        self.image = image

    def create(self):
        remove_host_ssh = (
            "ssh-keygen -f '/home/{0}/.ssh/known_hosts'"
            " -R {1}".format(socket.gethostname(), '192.168.33.10'))
        os.system(remove_host_ssh)
        self.initial_path = os.getcwd()
        self.create_folder(self.name)
        self.create_vm()
        self.create_vagrantfile()
        os.chdir(self.initial_path)

    def create_folder(self, folder_name):
        if not os.path.isdir("machines"):
            os.system("mkdir machines")
        os.chdir(os.getcwd() + "/machines")
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        folder = os.getcwd() + "/" + folder_name
        os.chdir(folder)

    def create_vm(self):
        command = "vagrant box add {0} {1}".format(self.name, self.image)
        os.system(command)

    def create_vagrantfile(self):
        os.system("vagrant init")
        vagrantfile = open("Vagrantfile", "w")

        for var in self.VARIABLES_ORDER:
            vagrantfile.write(self.commands[var])
        vagrantfile.write('end')
        vagrantfile.close()
        os.system("vagrant up")
