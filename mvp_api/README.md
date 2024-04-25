# Movimentos API

Este aplicativo visa oferecer uma ajuda para as pessoas que praticam exercícios físicos para se manter em forma.

A ideia é disponibilizar pequenos vídeos mostranto cada movimento junto com algumas características tais como: o tipo de trabalho muscular, a parte do corpo que é trabalhada, assim como um texto explicativo.

Trata-se da segunda versão de um MVP cujo objetivo é mostrar o resultado do aprendizado da disciplina.
**Desenvolvimento Full Stack Básico** 
---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
