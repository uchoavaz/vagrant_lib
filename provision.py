
from up_vagrant import VMCreation

vm = VMCreation()
vm.vm_name('maquina_genomika')
vm.vm_cpu('2')
vm.vm_memory('2048')
vm.vm_path_image(
    (
        'https://cloud-images.ubuntu.com/vagrant/trusty/current'
        '/trusty-server-cloudimg-i386-vagrant-disk1.box'
    ))
vm.create()
