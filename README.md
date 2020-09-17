<img src="https://techcrunch.com/wp-content/uploads/2015/09/docker-dark.png?w=711">

A ideia é disponibilizar como conteinerizar um projeto e aproveitar todos os benefícios utilizando Docker. A ideia foi continuar a versão do repositório <a href="https://github.com/teixeirafabiano/pythonFlask">pythonFlask</a> com algumas alterações na estrutura e incremento de mais métodos no entrypoint.

<ul>
Serão necessários as seguintes instalações:
  <li><a href="https://docs.docker.com/engine/install/ubuntu/">Docker</a></li>
  <li><a href="https://virtualenv.pypa.io/en/stable/installation.html">Virtualenv</a></li>
</ul>


# docker


Com o terminal aberto:
<br>
#verificando a versão do python
<br>
python3 --version
<br>
#verificando versão pip3
pip3 --version
<br>
#verificando versão do virtualenv
<br>
virtualenv --version
<br>
#criando ambiente virtual
virtualenv -p python3 docker_flaskapi
<br>
#ativando o ambiente virtual
source docker_flaskapi/bin/activate
<br>
#instalando flask no ambiente virtual
<br>
pip3 install flask
<br>
#copiando para o arquivo requirements todas as dependencias
<br>
pip3 freeze > requirements.txt
