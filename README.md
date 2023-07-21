# Teste Framework - Marco Machado

Teste de Marco Machado referente à vaga Desenvolvedor(a) Python Sênior

### Comandos para subir o ambiente

Clone o repositório
```shell
git clone https://github.com/marcoaureliodev/framework_teste.git
```

Entre na pasta clonada
```shell
cd framework_teste
```

Suba o docker
```shell
docker-compose up --build
```

#### Grupo de comandos
```shell
git clone https://github.com/marcoaureliodev/framework_teste.git
cd framework_teste
docker-compose up --build
```


### Comandos para rodar os testes de ambiente

Primeiro é necessário localizar o nome do container que está rodando, use o comando:

```shell
docker ps
```

Após localizar o nome do container que está rodando, é preciso acessar o container com o comando abaixo:

Obs.: Provavelmente o nome será: **framework_teste_web_1**

```shell
docker exec -it <container-name> /bin/bash
```

Após acessar o container, basta rodar o teste:

```shell
pytest
```

#### Grupo de comandos
```shell
docker exec -it framework_teste_web_1 /bin/bash
pytest
```

### Comandos para leitura de log
Observação: Os logs são sempre lançados no arquivo access_logging.log


Primeiro é necessário localizar o nome do container que está rodando, use o comando:
Obs.: Provavelmente o nome será: **framework_teste_web_1**

```shell
docker ps
```

Após localizar o nome do container que está rodando, é preciso acessar o container com o comando abaixo:

```shell
docker exec -it <container-name> /bin/bash
```

Após acessar o container, basta rodar o teste:

```shell
tail -f access_logging.log
```


#### Grupo de comandos
```shell
docker exec -it framework_teste_web_1 /bin/bash
tail -f access_logging.log
```


## Postman

```shell
https://api.postman.com/collections/27899537-4c26a6fe-47c5-4f1d-8125-c77b37f77f66?access_key=PMAT-01H5WXVRT8GAEATN52BVGKJBZ8
```


## Agradeço a oportunidade e fico no aguardo do retorno.
