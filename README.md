<img src="https://techcrunch.com/wp-content/uploads/2015/09/docker-dark.png?w=711">

A ideia é disponibilizar como conteinerizar um projeto e aproveitar todos os benefícios de um Docker. Para tanto, segui na versão do repositório <a href="https://github.com/teixeirafabiano/pythonFlask">pythonFlask</a> com algumas alterações na estrutura e incremento de mais métodos no entrypoint.

<ul>
Serão necessários as seguintes instalações:
  <li><a href="https://docs.docker.com/engine/install/ubuntu/">Docker</a></li>
  <li><a href="https://virtualenv.pypa.io/en/stable/installation.html">Virtualenv</a></li>
</ul>

<table align=center border=0>
  <tr>
    <td colspan=2>Virtualenv</td>
  </tr>
  <tr>
    <td>#verificando a versão do python</td>
    <td>python3 --version</td>
  </tr>
  <tr>
    <td>#verificando versão pip3</td>
    <td>pip3 --version</td>
  </tr>
  <tr>
    <td>#verificando versão do virtualenv</td>
    <td>virtualenv --version</td>
  </tr>
  <tr>
    <td>#criando ambiente virtual</td>
    <td>virtualenv -p python3 docker_flaskapi</td>
  </tr>
  <tr>
    <td>#ativando o ambiente virtual</td>
    <td>source docker_flaskapi/bin/activate</td>
  </tr>
  <tr>
    <td>#instalando flask no ambiente virtual</td>
    <td>pip install flask</td>
  </tr>
  <tr>
    <td>#copiando para o arquivo requirements todas as dependencias</td>
    <td>pip3 freeze > requirements.txt</td>
  </tr>
  <tr>
    <td colspan=2>Docker</td>
  </tr>
  <tr>
    <td>#construindo a image</td>
    <td>docker build -t flaskapi .</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td>Sending build context to Docker daemon  14.31MB
Step 1/9 : FROM python:3.8.5-alpine
 ---> 0f03316d4a27
Step 2/9 : LABEL author=fabiano
 ---> Running in f3aaaa3b2941
Removing intermediate container f3aaaa3b2941
 ---> 2aab6659c54b
Step 3/9 : LABEL description=development
 ---> Running in 562368d95180
Removing intermediate container 562368d95180
 ---> d04b1dd77acc
Step 4/9 : WORKDIR /app
 ---> Running in a616e49008ca
Removing intermediate container a616e49008ca
 ---> 0925fe43fdd9
Step 5/9 : ADD . /app
 ---> 772a7323e66c
Step 6/9 : VOLUME $pwd/ciclista/DAO/data/cyclist.db:/container/ciclista/DAO/data/cyclist.db
 ---> Running in 78375232c83d
Removing intermediate container 78375232c83d
 ---> 3156a7a0dbcb
Step 7/9 : RUN pip install -r requirements.txt
 ---> Running in a1976e0d5cc4
Collecting click==7.1.2
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting Flask==1.1.2
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting itsdangerous==1.1.0
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2==2.11.2
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe==1.1.1
  Downloading MarkupSafe-1.1.1.tar.gz (19 kB)
Collecting Werkzeug==1.0.1
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Building wheels for collected packages: MarkupSafe
  Building wheel for MarkupSafe (setup.py): started
  Building wheel for MarkupSafe (setup.py): finished with status 'done'
  Created wheel for MarkupSafe: filename=MarkupSafe-1.1.1-py3-none-any.whl size=12627 sha256=a57d6802818e373a8aab6f0a7601404876247aadf3ce2d3867a340d84aeffdc5
  Stored in directory: /root/.cache/pip/wheels/0c/61/d6/4db4f4c28254856e82305fdb1f752ed7f8482e54c384d8cb0e
Successfully built MarkupSafe
Installing collected packages: click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask
Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0
Removing intermediate container a1976e0d5cc4
 ---> 0f86c5072069
Step 8/9 : ENV NAME=fgteixeira
 ---> Running in de900feb1c31
Removing intermediate container de900feb1c31
 ---> 481c5c07b356
Step 9/9 : CMD ["python", "app.py"]
 ---> Running in 5cd629a5f580
Removing intermediate container 5cd629a5f580
 ---> f5fbed860149
Successfully built f5fbed860149
Successfully tagged flaskapi:latest
</td>
  </tr>
  <tr>
    <td>#verificando a image criada</td>
    <td>docker images</td>
  </tr>
  <tr>
    <td>#instanciando o container a partir da imagem flaskapi</td>
    <td>docker run -it --name flask-container -p 3200:3200 flaskapi</td>
  </tr>
</table>
