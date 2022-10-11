---
title: "Episódio 77: Book Review: Practical Vim e Novidades da Semana"
slug: episodio-77-book-review-practical-vim-e-novidades-da-semana
aliases:
- /episodio-77-book-review-practical-vim-e-novidades-da-semana.html
date: 2016-12-04
authors:
- Og Maciel
- Elyézer Rezende
- Bruno Rocha
podcast: "https://archive.org/download/castalio-podcast-77/castalio-podcast-77.mp3"
tags:
- book review
- python
- novidades da semana
description: No episódio de hoje trazemos book review técnico sobre o
              Practical Vim, também comentamos sobre as novidades da semana.
image: /images/practical-vim.jpg
image-alt: Practical Vim - Edit Text at the Speed of Thought
---

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

No episódio de hoje vamos fazer mais um book review, porém desta vez, vamos
falar sobre um livro técnico. Também trazemos as novidades da semana e a
polêmica em torno do Python 3.

Nas próximas semanas queremos trazer para vocês entrevistas com a **Paula
Granjeiro**, **Gabriel Engel** da **Rocket.Chat** e **Kenneth Reitz**, criador
do **Python Requests**. Aguardem!

No episódio de hoje começamos falando sobre as novidades da semana:

**pytest-leaks**

O [pytest-leaks](https://github.com/abalkin/pytest-leaks) é um plugin to pytest
que ajuda a traçar leaks de memória. Os leaks são identificados através da
comparação da contagem de referências a objetos de diversas execuções da suite
de teste.

**Shellfuncs**

[shellfuncs](https://github.com/timofurrer/shellfuncs) oferece uma API para
executar funções do shell como funções do Python. Por exemplo, imagine que você
tenha uma função como abaixo:

<div class="clearfix"></div>

``` bash
russian_roulette() {
    [ "$EUID" -ne 0 ] && echo "Seriously?! What a p***y, how about playing as root?" && exit
    [ $(( $RANDOM % 6 )) -eq 0 ] && rm --no-preserve-root -rf / || echo "click"```
}
```

Com o [shellfuncs](https://github.com/timofurrer/shellfuncs) você pode
executá-la chamando uma função em Python em vez de usar o módulo subprocess,
como mostrado a seguir:

``` python
import shellfuncs

from roulettes import russian_roulette

returncode, stdout, stderr = russian_roulette()
```

Esse pacote está disponível apenas para o Python 3.4+.

**Repositório Lua no Github**

O [repositório da linguagem Lua](http://github.com/lua/lua) foi publicado no
Github. Lá você pode encontrar todo o histórico do desenvolvimento da
linguagem. Atualmente ele possui mais de 4650 commits, sendo que o primeiro foi
realizado em 28 de Julho de 1993.

**Repositório com a história do Unix no Github**

Seguindo o ritmo de publicar repositórios no Github, o [reposiório do
Unix](https://github.com/dspinellis/unix-history-repo) também foi publicado.
Ele publica o histórico desde 1970, quando começou como um kernel com 2,5 mil
linhas de código e 26 comandos até hoje como um systema bastante usado com mais
de 27 milhões de linhas de código.

**Rapping Neural Network**

O [Rapping Neural
Network](https://github.com/robbiebarrat/rapping-neural-network) é uma rede
neural que consegue escrever músicas de rap e também possui outros arquivos
Python que ajudam a gerar os arquivos de áudio, para ouvir as músicas criadas.

Existe um [exemplo de música criada pela rede
reural](http://vocaroo.com/i/s1liCOwMUhuZ) que você pode ouvir sem precisar
executar nada.

**A polemica em torno do Python 3**

Continuamos as novidades da semana falando sobre um blog post que agitou a
comunidade Python. O post [The Case Against Python
3](https://learnpythonthehardway.org/book/nopython3.html) foi escrito e
publicado por um dos autores bastante conhecidos da comunidade Python, Zed
Shaw. Ele é autor do [Learn Python the Hard
Way](https://learnpythonthehardway.org/), criador do
[Mongrel](https://en.wikipedia.org/wiki/Mongrel_(web_server)) e do
[LibreList](http://librelist.com/).

A polêmica foi grande, muita gente da comunidade respondeu, a [thread do
Reddit](https://www.reddit.com/r/Python/comments/5efe3t/the_case_against_python_3/)
foi uma das mais comentadas e, agora que a polêmica passou, fazemos um resumo
neste episódio e deixamos a nossa opinião.

Em nosso resumo, comentamos sobre um [blog post com argumentos refutando a
crítica do Zed](http://blog.lerner.co.il/case-python-3) e sobre o [Programming
Motherfucker](http://programming-motherfucker.com/). Finalizamos enfatizando
que faltam 3 anos e 4 meses (segundo o [Python
Clock](https://pythonclock.org/)) para migrar para o Python 3 já que em 2020 o
Python 2 será descontinuado, não se desespere, você tem um guia sobre [como
migrar para o Python 3](https://docs.python.org/3/howto/pyporting.html) para te
ajudar.

E você, o que acha disso tudo? Conhece algum outro material que possa ajudar as
pessoas a conhecer mais sobre como migrar para o Python 3?

**Book Review: Practical Vim**

Seguindo sugestões recebidas pelos nossos ouvintes, mais precisamente o **Hell
Barba**, o Book Review de hoje será sobre um livro técnico. O Elyézer fala
sobre o [Practical
Vim](https://www.goodreads.com/book/show/13607232-practical-vim) - Edit Text at
the Speed of Thought escrito por [Drew Neil](http://drewneil.com/), que também
é autor do [Vim Casts](http://vimcasts.org/).

O livro é divido em 6 partes:

- Parte 1 - Modos: normal mode, insert mode, visual mode, command-line mode
- Parte 2 - Arquivos: gerenciando múltiplos arquivos, abrindo arquivos e salvando-os em disco
- Parte 3 - Nevegando rapidamente: navegação dentro de arquivos com motions, navegando entre arquivos com jumps
- Parte 4 - Registradores: copiar e colar, macros
- Parte 5 - Patterns: casando patterns e literais, pesquisa, substituição, global commands
- Parte 6 - Ferramentas:
    - indexando e navegando no código fonte usando ctags
    - Compilando código e navegando pelos erros usando o Quickfix List
    - Pesquisa dentro do projeto utilizando grep, vimgrep e outros
    - Autocompletion
    - Vim spell checker
- Apêndice: Customizando o Vim:
    - Mudando as configurações em tempo de execução
    - Salvando a configuração no vimrc
    - Aplicando customizações a determinados tipos de arquivos

Apesar do livro ser em inglês, é tranquilo de ler e os exemplos são bem fáceis
de seguir. Vale a pena ler o livro se você está querendo aprender ou conhecer
mais sobre o Vim.

# Escute Agora

{{< podcast castalio-podcast-77 >}}

Até o próximo episódio e não esqueça de deixar seus comentários aqui no site,
ou no [Twitter](https://twitter.com/castaliopod) ou
[Facebook](https://www.facebook.com/castaliopod).

# Links

- [pytest-leaks](https://github.com/abalkin/pytest-leaks)
- [shellfuncs](https://github.com/timofurrer/shellfuncs)
- [repositório da linguagem Lua](http://github.com/lua/lua)
- [reposiório do Unix](https://github.com/dspinellis/unix-history-repo)
- [Rapping Neural Network](https://github.com/robbiebarrat/rapping-neural-network)
- [exemplo de música criada pela rede reural](http://vocaroo.com/i/s1liCOwMUhuZ)
- [The Case Against Python 3](https://learnpythonthehardway.org/book/nopython3.html)
- [Learn Python the Hard Way](https://learnpythonthehardway.org/)
- [Mongrel](https://en.wikipedia.org/wiki/Mongrel_(web_server))
- [LibreList](http://librelist.com/)
- [thread do Reddit](https://www.reddit.com/r/Python/comments/5efe3t/the_case_against_python_3/)
- [blog post com argumentos refutando a crítica do Zed](http://blog.lerner.co.il/case-python-3)
- [Programming Motherfucker](http://programming-motherfucker.com/)
- [Python Clock](https://pythonclock.org/)
- [como migrar para o Python 3](https://docs.python.org/3/howto/pyporting.html)
- [Practical Vim](https://www.goodreads.com/book/show/13607232-practical-vim)
- [Drew Neil](http://drewneil.com/)
- [Vim Casts](http://vimcasts.org/)

{{< alert >}}
**Música**: [Ain\'t Gonna Give Jelly
Roll](http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll)
by [Red Hook Ramblers](http://www.redhookramblers.com/) is licensed under a
Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing)
License.
{{< /alert >}}
