# HAUS - EVERTON VASZELEWSKI COMPONENTE C 2 + BANCO DE DADOS
# MVP SPRINT 2 - Pós-Graduação em Engenharia de Software

Componente C 2 (Lista de Desejos - WISHLIST) do projeto HAUS: Um Sistema web de gerenciamento e catalogar coleções de objetos de Música


---
## Como executar 

Requisitos:
- Certificar de que o [Docker](https://docs.docker.com/engine/install/) está instalado em sua máquina e em execução.
- Para obter Contexto e utilizar uma interface Frontend, siga os passos deste repositório: [HAUS-Front](https://github.com/Vaszelewski/pucrio-mvp-sprint2-haus-component-a-b/).

![back c2](https://github.com/Vaszelewski/pucrio-mvp-sprint2-haus-component-c-2/assets/50892923/c1ce12c6-d524-4221-bf09-8ef3af953e97)

Etapas:


1 - Clonar o repositório e descompactar da pasta .zip.

2 - Ir ao diretório raiz, onde contém o Dockerfile, e executar como administrador o seguinte comando para construir a imagem Docker:
```
$ docker build -t rest-api .
```

3 - Após a criação da imagem, executar como adminitrador o seguinte comando para rodar o container:
```
$ docker run -p 8000:8000 rest-api
```

Após seguir todos os passos, abrir o link abaixo no bavegador para verificar o status da API em execução
- [http://localhost:8000/#/](http://localhost:8000/#/)

