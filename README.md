# reciclagem-perto-de-casa
Trabalho em grupo da matéria de Introdução a Linguagem Estruturada pela UNIP de Campinas.

O objetivo do aplicativo é mostrar para o usuário os pontos de coleta de lixo recíclaveis mais próximos da localização fornecida.

Documentação: O usuário recebe quatro opções quando o programa rodar, tanto pelo terminal, quanto pelo navegador:

1. Ponto de coleta mais próximo
2. Todos pontos de coleta
3. Sobre nós
4. Sair

 Mas antes de rodar o código é necessário seguir os seguintes comandos no terminal (se estiver utilizando nativamente python 3.7.4, isto é.):

	pip install geopy

	python main.py

Para conseguir visualizar o projeto no seu próprio navegador você pode seguir o seguinte link:

	https://gitpod.io/#https://github.com/wilfelipe/reciclagem-perto-de-casa
	
É só clicar o link acima que ele vai baixar para você a extensão no navegador necessária para rodar o projeto sem ter que baixar nenhuma arquivo. Seguindo o link vai permitir que você tenha certeza que você tem a extensão do gitpod, em seguida abrirá o projeto.

Digite os seguintes comandos individualmente separados por um enter no terminal do gitpod:

	pip3 install geopy

	python3 main.py
	
Feito uma das duas alternativas para conseguir rodar o código, o usuário recebe o menu:

-------------------- Reciclagem Perto de Casa --------------------

1. Ponto de coleta mais próximo
2. Todos pontos de coleta
3. Sobre nós
4. Sair


Quando o usuário digitar 1 e, em seguida enter, o terminal limpa todas as opções da tela e novas opções surgem perguntando o usuário qual o tipo do material que o usuário gostaria de reciclar:
	
-------------------- O que você deseja reciclar? --------------------

1. Vidros
2. Metais
3. Plásticos
4. Pneus
5. Papéis 


Ao ser selecionada a opção do usuário, a localização do usuário é pedida como demonstrado abaixo:



-------------------- Qual o seu endereço? --------------------

Cidade: Campinas
Estado: São Paulo
Endereço: Norte Sul

E como resultado:

Região Central


Distância:  2.23 Km


Enderço:  Rua Francisco Theodoro, 1050 . Campinas


Tipos de residuos:  Vidros,Metais,Plásticos,Papéis


---------------------------





Voltando para o menu, temos as seguintes opções:



2. Todos pontos de coleta

Essa opção mostra todos os pontos de coleta armazenado no arquivo .csv do projeto.


já a opção 3 mostra os nomes do colaboradores do código e seus repectivos RA's:


3. Sobre nós

E por fim, na opção 4 o usuário consegue fechar o aplicativo.


4. Sair


Final da Documentação: No final das contas ficamos muito feliz com o resultado, acreditamos que conseguimos atingir todos os objetivos e desafios da APS.
