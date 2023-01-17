# foxbit_api_exemplo_busca_moedas
exemplo de como utilizar Python para realizar uma conexão por Websocket Secure à API da Foxbit https://foxbit.com.br/foxbit-api/##endpointpublico


## Instruções de utilização

### Método 1:

Se já tiver o Python instalado (https://www.python.org/downloads/), basta executar `python buscar_moedas_foxbit.py` e o script irá instalar as ferramentas necessárias para se comunicar com a API e fazer o download das moedas disponíveis.
O resultado da consulta ficará no arquivo `'moedas_foxbit.csv'` que pode ser aberto no excel ou programas semelhantes.


### Método 2: (Para usuários de Python que possuem Pipenv instalado https://pipenv.pypa.io/en/latest/)
`pipenv install`
`pipenv run buscar_moedas_foxbit.py`


### Método 3: (Para usuários de Python que possuem Docker)
`docker build -t buscar_moedas_foxbit .`
`docker run -v %cd%:/app buscar_moedas_foxbit`
