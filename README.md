# Teste Framework - Marco Machado

Teste de Marco Machado referente à vaga Desenvolvedor(a) Python Sênior

### Comandos para subir o ambiente

```shell
docker-compose up --build
```

### Comandos para rodar os testes de ambiente

Primeiro é necessário localizar o nome do container que está rodando, use o comando:

```shell
docker ps
```

Após localizar o nome do container que está rodando, é preciso acessar o container com o comando abaixo:

```shell
docker exec -it <container-name> /bin/bash
```

Após acessar o container, basta rodar o teste:

```shell
pytest
```


### Comandos para leitura de log
Observação: Os logs são sempre lançados no arquivo access_logging.log


Primeiro é necessário localizar o nome do container que está rodando, use o comando:

```shell
docker ps
```

Após localizar o nome do container que está rodando, é preciso acessar o container com o comando abaixo:

```shell
docker exec -it <container-name> /bin/bash
```

Após acessar o container, basta rodar o teste:

```shell
pytest
```
