<img src="https://techcrunch.com/wp-content/uploads/2015/09/docker-dark.png?w=711">

A ideia é disponibilizar como conteinerizar um projeto e aproveitar todos os benefícios de um Docker. Para tanto, segui na versão do repositório <a href="https://github.com/teixeirafabiano/pythonFlask">pythonFlask</a> com algumas alterações na estrutura e incremento de mais métodos no entrypoint.

<ul>
Serão necessários as seguintes instalações:
  <li><a href="https://docs.docker.com/engine/install/ubuntu/">Docker</a></li>
  <li><a href="https://virtualenv.pypa.io/en/stable/installation.html">Virtualenv</a></li>
</ul>

<table align=center border=0>
  <tr>
    <td colspan=2><b>Virtualenv</b></td>
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
    <td colspan=2><b>Docker</b></td>
  </tr>
  <tr>
    <td>#construindo a image</td>
    <td>docker build -t flaskapi .</td>
  </tr>
  <tr>
    <td>Nota: ao final de todas as tasks, tudo ok, mensagem de sucesso com id da imagem e tag</td>
    <td>Successfully built f5fbed860149<br>
        Successfully tagged flaskapi:latest
    </td>
  </tr>
  <tr>
    <td>#verificando as images criada</td>
    <td>docker images</td>
  </tr>
  <tr>
    <td>#instanciando o container a partir da imagem flaskapi</td>
    <td>docker run -it --name flask-container -p 3200:3200 flaskapi</td>
  </tr>
</table>

Dockerfile
==========
<br>
Para criar a imagem usei o arquivo Dockerfile que possui as instruções que são lidas do início ao fim e cada linha executada por vez. Mas afinal, o que criamos? Imagem ou container? Abstraindo, o container é a instância da classe imagem criada. A imagem é a abstração de somente leitura, de onde será instânciado o container. Com isso, a imagem jamais estará em execução!
<br>
Então segue descrição dos comandos que estão no Dockerfile linha a linha:
<br>
<b>FROM:</b> Informa qual imagem será usada como base.<br>
<b>LABEL:</b> Em alguns casos você pode querer usar algum argumento que será substituído pelo valor correto em tempo de criação da imagem.<br>
<b>WORKDIR:</b> Define o dirtório de trabalho para qualquer instrução: RUN, CMD, ENTRYPOINT, COPY e ADD. Se a instrução não existir, será criado mesmo se não for usado em nenhuma instrução subsequente no Dockerfile.<br>
<b>ADD:</b> A instrução permite copiar os arquivos dentro do sistema de arquivo da imagem.<br>
<b>VOLUME:</b> É o mecanismo preferencial para persistir os dados gerados e usados pelo container. Embora a montagem dependa da estrutura de diretório da máquina host docker, os volumes são totalmente gerenciados pelo docker.<br>
<b>RUN:</b> Informa quais comandos serão executados no ambiente para efetuar as mudanças necessárias na infraestrutura do sistema. São como comandos executados no shell do ambiente. E nesse caso, é executado a instalação de todas as dependências do sistema no arquivo requirements.txt.<br>
<b>ENV:</b> Variáveis de ambiente podem, pelo statement ENV, ser usadas em certas instruções como variáveis a ser interpretadas pelo Dockerfile.<br>
<b>CMD:</b> Informa qual comando é executado por padrão. No caso, o entrypoint app.py.<br>
<br>

Compilação Docker
=================
<br>
Agora podemos construir o container docker. Certifique-se de que está no diretório raiz do projeto (crie um diretório chamado flaskapi e copie toda pasta ws para dentro) e, em seguida, faça docker build -t flaskapi .
<br><br>
Isso diz ao Docker para construir um contêiner usando o projeto no diretório de trabalho atual (o . no final) e marcá-lo flaskapi(significa “tag”). O Docker puxará a imagem base do Docker Hub e, em seguida, copiará o código do nosso aplicativo para o contêiner.-t python:3.8.5-alpine
<br><br>
Importante: Cada vez que o código é alterado, é necessário construir o container novamente! Se o seu Dockerfile estiver organizado corretamente, a compilação deve levar apenas alguns segundos.
<br>
<br>

Docker run
==========
<br>
Agora estamos prontos para correr! Supondo que você tenha marcado o contêiner my_flask_appcomo eu fiz acima, execute-o com:
<br><br>
docker run -it --name flask-container -p 3200:3200 flaskapi
<br><br>
-p conecta a porta 3200 do container Docker à porta 3200 da máquina para que o HTTP possa funcionar.<br>
-it modo interativo. Mantém o STDIN aberto mesmo sem console anexado e aloca uma pseudo TTY.<br>
<br>
O aplicativo flask agora deve estar em execução - vá para o endereço IP do seu servidor no seu navegador.
<br><br>
Se você receber um erro como “endereço já em uso” ou “porta 3200 já em uso”:
<br><br>
Certifique-se de que seu aplicativo Flask ou outro aplicativo ainda não esteja em execução e usando a porta 3200. Às vezes, o docker não desassocia as portas após fechar os containers, então tente executar o container novamente: sudo service docker restart. Você pode matar o container com CTRL + C. Observe que se você acessar o IP do seu servidor no navegador, não há nada lá.

Executando Persistentemente
===========================
Provavelmente, existe a intenção que o aplicativo seja executado em segundo plano e reiniciado automaticamente se a máquina servidor for reiniciada. Então, vamos adicionar algumas coisas ao nosso comando:docker run<br>
<br>
docker run -d --restart=always -p 3200:32090 -t flaskapi
<br><br>
-d executa o contêiner do Docker como um daemon em segundo plano.<br>
--restart=always reinicia o contêiner se ele travar ou se o dock do sistema estiver em execução for reiniciado.<br>
