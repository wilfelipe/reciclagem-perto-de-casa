# reciclagem-perto-de-casa
Trabalho em grupo da matéria de Introdução à Linguagem Estruturada, pela UNIP de Campinas.

O objetivo do aplicativo é apresentar para o usuário os pontos de coleta de lixo recíclaveis mais próximos da localização fornecida.

Documentação: 

Quando o programa rodar, tanto pelo terminal, quanto pelo navegador, o usuário é introduzido ao menu:

	1. Ponto de coleta mais próximo
	2. Todos pontos de coleta
	3. Sobre nós
	4. Sair

 Antes de rodar o código é necessário seguir os seguintes comandos no terminal (se estiver utilizando nativamente python 3.7.4, isto é.):

	pip install geopy

	python main.py

Alterinativamente, para conseguir visualizar e rodar o projeto no seu próprio navegador, tanto desktop, quanto mobile, você pode seguir o seguinte link:

	https://gitpod.io/#https://github.com/wilfelipe/reciclagem-perto-de-casa
	
Clicando no link acima: Será baixado, caso já não tenha, a extensão necessária para rodar o projeto no navegador, sem ter que baixar nenhum arquivo, nem se quer python. Seguindo o link vai permitir que você tenha certeza que você tem a extensão do gitpod. Devemos resaltar que recomendamos o uso do gitpod em qualquer repositório do github. 


Em seguida abrirá o projeto.



Agora, digite os seguintes comandos individualmente separados por um enter no terminal do gitpod:

	pip3 install geopy

	python3 main.py
	
Baixando suas dependência, com uma das duas alternativas apresentadas, o usuário estará pronto para rodar o arquivo main.py, que por sua vez cumpre seu objetivo:

	-------------------- Reciclagem Perto de Casa --------------------

	1. Ponto de coleta mais próximo
	2. Todos pontos de coleta
	3. Sobre nós
	4. Sair


Quando o usuário digitar 1 e, em seguida enter, o terminal limpa todas as opções da tela e novas opções surgem, perguntando ao usuário qual o tipo do material que o usuário gostaria de reciclar:
	
	-------------------- O que você deseja reciclar? --------------------

	1. Vidros
	2. Metais
	3. Plásticos
	4. Pneus
	5. Papéis 


Ao ser selecionada a opção do usuário, a localização do usuário é requesitada como demonstrado abaixo:



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

Essa opção mostra todos os pontos de coleta armazenados no arquivo .csv do projeto.


já a opção 3 mostra os nomes do colaboradores do código e seus repectivos RA's:


	3. Sobre nós

E por fim, na opção 4 o usuário consegue fechar o aplicativo.


	4. Sair


Final da Documentação: No final das contas ficamos muito felizes com o resultado, acreditamos que conseguimos atingir todos os objetivos e desafios da APS.
