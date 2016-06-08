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
    
Dependências instaladas
------------
  - git
  
  - Django 1.9.7
  
  - pip(python 2.7)
  
  - Projeto da resolução do teste de seleção da Genomika
  

Preparando a Máquina
------------

  - Baixar o executável do Vagrant 1.8.1 para Debian(x64) :
  
      https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
    
  ou para Debian(x86):
      
      https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_i686.deb

  , entrar pelo terminal no diretório onde este arquivo foi baixado e executar o comando de instalação(colocar o nome do arquivo):
  
      sudo dpkg -i nome_do_arquivo.deb
  
  - Baixar o VirtualBox 5.0 para algum sistema Debian, neste caso foi para o Ubuntu 14.04 x64:
  
        https://www.virtualbox.org/wiki/Linux_Downloads

    , entrar pelo terminal no diretório onde este arquivo foi baixado e executar o comando de instalação(colocar o nome do arquivo):
    
        sudo dpkg -i nome_do_arquivo.deb

Executando o projeto
------------

  - Baixe o repositório do projeto :
    
