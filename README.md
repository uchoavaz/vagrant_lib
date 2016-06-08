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
  
  - IP : 192.168.33.10
    
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
  
        sudo python provision.py

 *Sua máquina será montada com as configurações apontadas acima e criará uma pasta ('machines') no diretório raiz do projeto, onde estará o VagrantFile da mesma. O tempo de execução deste processo pode variar pois vai depender da conexão.
 
  - Entrando na máquina via ssh : 
      
        ssh vagrant@192.168.33.10
  
  A senha de conexão é 'vagrant'


Resolução do Teste
------------

- Problema 1

  Neste problema, foi pedido pra se fazer um script que baixasse um .txt que esta contido em uma url, salva-lo na máquina local e por fim, salvar todos os dados em um banco de dados local.
  
  Normalizei todas as entidades do banco, criando duas tabelas(PhenoDbHpo e PhenoDbGene) que se relacionam com o tipo de N para N e configurei o script em python para que não houvesse repetições de dados em ambas as tabelas.
  
  Para rodar o script que "puxa" todas essas informações, vá para o diretório em que foi baixado o projeto.
  
      cd  /home/vagrant/estagio_genomika/estagio_genomika
  
  e rode o script :
  
      sudo python manage.py update_local
  
  o download do arquivo gerado('hpo_genes.txt') fica salvo no mesmo diretório do script('update_local.py'):
  
      cd /home/vagrant/estagio_genomika/estagio_genomika/problema_1
  
  *Lembrando que são quase 400 mil linhas de dados e o banco é o sqlite3 então, pode-se demorar várias horas para concluir a tarefa. O projeto já está populado, caso não queira esperar e passar para as próximas etapas.
  
  Agora, o pŕoximo passo é extrair as informações relacionadas a um determinado HPO_ID passado pelo usuário.Utilize o comando a seguir no diretório raiz do projeto('/home/vagrant/estagio_genomika/estagio_genomika') com um HPO_ID:
  
      sudo python manage.py phizz HPO_ID
  
  *Se tentar passar um HPO_ID incorreto ou não existente, o script retorna uma mensagem
  
  Após ter inserido o comando, as informações relativas a esse HPO_ID estarão disponíveis em um arquivo .json (EX:HP_00000002.json) no mesmo diretório do script('phizz.py'):
  
        cd /home/vagrant/estagio_genomika/estagio_genomika/problema_1

- Problema 2
  
  Neste problema foi pedido um script que fizesse um processo automatizado de backup do banco de dados em um diretorio escolhido pelo usuário
  
  No diretório raiz do projeto('cd /home/vagrant/estagio_genomika/estagio_genomika') execute o comando para rodar o scrip de backup passando um diretório como argumento(Ex:'/home/vagrant/backup_folder') :
      
        sudo python manage.py backup_local /home/vagrant/backup_folder

  Ele executará o script 'backup_local.py' localizado no diretório ('/home/vagrant/estagio_genomika/estagio_genomika/problema_2'). Este script cria a pasta 'backup_folder' no diretório '/home/vagrant', verifica se existem arquivos com 3 dias ou mais de criação, exclui os mesmos se a afirmação for verdadeira e insere nela um arquivo de backup do banco de dados (sqlite3) com o formato .bak e o nomeia com a sua data de execução(Ex: 'hpo_20160607.bak')
