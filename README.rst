=======
Avisos!
=======

* Nenhum aviso!


==============
Compiladores 1
==============

Este é o Git da disciplina Fundamentos de Compiladores. Aqui ficará o material produzido em sala de aula 
assim como tarefas, wiki e discussões. Este arquivo contêm informações básicas sobre a disciplina e o 
plano de ensino do semestre.


Informações básicas
===================

Curso: 
    Engenharia de Software
Professor: 
    Fábio Macêdo Mendes
Disciplina: 
    Compiladores 1
Semestre/ano: 
    01/2020
Carga horária: 
    60 h
Créditos: 
    04


Ementa
======

* Introdução
* Autômatos
* Organização e estrutura de compiladores e interpretadores.
* Análise léxica.
* Expressões Regulares
* Análise sintática.
* Gramáticas Regulares e Livres de Contexto
* Estruturas de Dados e representação interna de código-fonte.
* Análise semântica.
* Geração de código.
* Máquinas abstratas e ambientes de tempo de execução.
* Projeto de Compiladores.
* Compiladores, Interpretadores e Parsers na Engenharia de Software.


Horário das aulas e atendimento
===============================

Aulas teóricas e de exercícios: segundas e sextas-feiras às 14h
Atendimento: realizado de forma assíncrona no grupo de Telegram da disciplina


Informações importantes
========================

Este curso utiliza Telegram + GitHub + Microsoft Teams para gerenciar o curso. A comunicação com a 
turma é feita através do Telegram e os encontros presenciais no Microsoft Teams. Habilite a funcionalidade 
"Watch" no repositório para receber notificações sobre atualizações.

Github:
    https://github.com/compiladores-fga/2020-1
Telegram:
    (oculto, enviado por e-mail)
Teams:
    (oculto, disponível no grupo de Telegram)


Critérios de avaliação
======================

A avaliação será feita usando um critério de avaliação baseado em capacidades e competências complementada por um 
mecanismo de avaliação competitiva. 


Avaliação por capacidades e competências
----------------------------------------

Na avaliação por capacidades e competências, cada aluno deve demonstrar competência nas habilidades básicas 
desenvolvidas durante o curso. O critério para demonstrar competência normalmente é baseado no resultado de pequenas 
avaliações, mas pode ser realizado de outras maneiras também (ex.: um projeto de programação, criação de um conteúdo 
didático e outros). Note que **não** existem provas agendadas ao longo do semestre. O aluno que falhar em alguma avaliação ainda 
pode fazê-la posteriormente assim que se sentir habilitado. Uma única prova final/substitutiva será realizada ao
fim do semestre com o conteúdo completo da disciplina, onde o aluno poderá testar as competências que ainda não foram
confirmadas.

É necessário, ao final do semestre, traduzir o mapa de competências em uma categoria de menções. A tradução
é feita segundo as regras abaixo:

* **SR:** Reprovação por faltas 
* **II:** Comprovou menos de 16 competências básicas.
* **MI:** Comprovou entre 16 e 27 das competências básicas.
* **MM:** Comprovou pelo menos 28 das competências básicas.
* **MS:** Comprovou todas 37 competências básicas.
* **SS:** Comprovou todas competências básicas e 7 competências avançadas.


Código de ética e conduta
-------------------------

Algumas avaliações serão realizadas com auxílio do computador no laboratório de informática. Todas as submissões 
serão processadas por um programa de detecção de plágio. Qualquer atividade onde for detectada a presença de 
plágio será anulada sem a possibilidade de substituição. Não será feita qualquer distinção entre o aluno que 
forneceu a resposta para cópia e o aluno que obteve a mesma.

As mesmas considerações também se aplicam às provas teóricas e atividades entregues no papel.


Prepare-se
==========

O curso utiliza alguns pacotes e ferramentas para os quais cada estudante deverá providenciar a instalação o mais 
cedo o possível. O curso requer Python 3.6+ com alguns pacotes instalados:

* Pip: Gerenciador de pacotes do Python (sudo apt-get install python3-pip)
* Jupyter notebook/nteract/Google colab: Ambiente de programação científica (https://nteract.io)
* Lark (pip3 install lark-parser --user): Biblioteca de parsing para Python. (note a **ausência** do sudo no comando!)
* Docker: cria ambientes completamente isolados para teste e validação (sudo apt-get install docker.io)

Já que vamos utilizar o Python, vale a pena instalar as seguintes ferramentas:

* virtualenvwrapper: isola ambientes de desenvolvimento
* flake8: busca erros de estilo e programação no seu código
* black: formatador de código de acordo com o guia de estilo do Python
* pytest, pytest-cov: criação de testes unitários
* Editores de código/IDE: Utilize o seu favorito. Caso precise de uma recomendação, seguem algumas:
 * PyCharm Educacional - IDE com ótimos recursos de introspecção e refatoração, mas adora memória RAM. Possui uma versão livre e uma versão profissional paga, mas que é gratuita para estudantes.
 * VSCode - um bom meio termo entre uma IDE e um editor de código leve. Criado para Javascript, mas possui bons plugins para Python e várias outras linguagens.
 * Vi/Vim - herança dos anos 70 que nunca morre ;) Instale os plugins para Python.

DICA: em todos os casos, prefira instalar os pacotes Python utilizando o apt-get ou o mecanismo que sua 
distribuição fornece e, somente se o pacote não existir, instale-o utilizando o pip. Se utilizar o pip, 
faça a instalação de usuário utilizando o comando ``pip3 install <pacote> --user`` (NUNCA utilize o sudo 
junto com --user e evite instalar globalmente para evitar problemas futuros com o APT). Melhor ainda: isole
o ambiente utilizado em cada disciplina com uma ferramenta como o Virtualenv ou o [Poetry](https://poetry.eustace.io).


Linux e Docker
--------------

Os comandos de instalação acima assumem uma distribuição de Linux baseada em Debian. Não é necessário instalar 
uma distribuição deste tipo e você pode adaptar os comandos para o gerenciador de pacotes da sua 
distribuição (ou o Brew, no caso do OS X). Apesar do Linux não ser necessário para executar a maior parte 
das tarefas, é altamente recomendável que todos instalem o Docker para compartilharmos ambientes de 
desenvolvimento previsíveis (por exemplo, eu testarei as submissões em containers específicos que serão 
compartilhados com a turma). É possível executar o Docker em ambientes não-Linux utilizando o 
Docker Machine ou o Vagrant. Deste modo, cada aluno deve providenciar a instalação do Docker e 
Docker Compose na sua máquina.


Bibliografia principal
----------------------

**Dragon Book:** Compilers: Principles, Techniques, and Tools, Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman, Pearson, 2006.
**SICP:** Structure and Interpretation of Computer Programs, Gerald Jay Sussman and Hal Abelson, MIT Press. (https://web.mit.edu/alexmv/6.037/sicp.pdf)


Cronograma de atividades
========================

Consultar `cronograma <cronograma.rst>`_.

Obs.: O cronograma está sujeito a alterações.
