<img src="https://techcrunch.com/wp-content/uploads/2015/09/docker-dark.png?w=711">

A ideia é dispnibilizar como conteinerizar um projeto e aproveitar todos os benefícios utilizando Docker. A ideia foi continuar a versão do repositório <a href="https://github.com/teixeirafabiano/pythonFlask">pythonFlask</a> com algumas alterações na estrutura e incremento de mais métodos no entrypoint.

Será necessário instalação então segue <a href="https://docs.docker.com/engine/install/ubuntu/">link</a> do Docker...

# docker



#check python version
python3 --version

#check pip3 version
pip3 --version

#check virtualenv version
virtualenv --version

#create virtualenv
virtualenv -p python3 docker_flaskapi

#activate virtualenv
source docker_flaskapi/bin/activate

#install flask
pip3 install flask

#freeze all dependencies
pip3 freeze > requirements.txt
