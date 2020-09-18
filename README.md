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
    <td>ao final de todas as tasks, tudo ok, mensagem de sucesso com id da imagem e tag</td>
    <td>Successfully built f5fbed860149<br>
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
