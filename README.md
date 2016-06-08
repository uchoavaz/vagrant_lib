=================
Biblioteca Vagrant
=================

Este repositório contem uma biblioteca, escrita em Python, que automatiza a criação de uma máquina virtual pelo Vagrant

Configurações da Máquina Virtual
------------

  - Memória: 1024 MB

  - CPU: 2 core

  - HD : 40GB (Dinâmico)
  
  - S.O : Ubuntu 14.04 (Trusty)
  
  - Ip : 192.168.33.10
    
Dependências instaladas
------------
  - git
  
  - Django 1.9.7
  
  - pip(python 2.7)
  
  - Projeto da resolução do teste de seleção da Genomika
  

Preparando a Máquina
------------
*Este projeto foi testado em uma máquina Ubuntu 14.04 x64

  - Baixar o executável do Vagrant 1.8.1 para o seu S.O(Debian) :
  
      https://www.vagrantup.com/downloads.html

  , entrar pelo terminal no diretório onde este arquivo foi baixado e executar o comando de instalação(colocar o nome do arquivo baixado):
  
      sudo dpkg -i nome_do_arquivo.deb
  
  - Baixar o VirtualBox 5.0 para algum sistema Debian, neste caso foi para o Ubuntu 14.04 x64:
  
      https://www.virtualbox.org/wiki/Linux_Downloads

    , entrar pelo terminal no diretório onde este arquivo foi baixado e executar o comando de instalação(colocar o nome do arquivo baixado):
    
        sudo dpkg -i nome_do_arquivo.deb

Executando o projeto
------------

  - Baixe o repositório do projeto em um diretório:
  
        sudo git clone https://github.com/uchoavaz/vagrant_lib.git

   e entre na pasta do projeto :
   
        cd vagrant_lib

  - Execute o comando :
  
        sudo python manage.py provision.py

 *Sua máquina será montada com as configurações apontadas acima e criará uma pasta ('machines') no diretório raiz do projeto, onde estará o VagrantFile da mesma. O tempo de execução deste processo pode variar pois vai depender da conexão.
 
  - Entrando na máquina via ssh : 
      
        ssh vagrant@192.168.33.10
  
  A senha de conexão é 'Vagrant'

Executando scripts do Teste da Genomika
------------
