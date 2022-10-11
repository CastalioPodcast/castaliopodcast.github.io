---
title: "Episódio 116: Tech News"
slug: episodio-116-tech-news
aliases:
- /episodio-116-tech-news.html
date: 2017-09-04
authors:
- Og Maciel
- Elyézer Rezende
- Bruno Rocha
podcast: "https://archive.org/download/castalio-podcast-116/castalio-podcast-116.mp3"
tags:
- docker
- linux tips
- rust
- rustlang
- tmate
- setup.py
- kenneth reitz
- flit
- poet
- fisl
- sady
- fisl18
- opencast
- pexpect
- pipenv
- pipfile
- pip
- pypi
- pypa
- python
- python-guide
- flask
- fs2w
- grupy
- cursodepython
- flask simplelogin
- login
- canalrustbr
- telegram
- bot
- lua
- lualang
- mattata
- rubyconf
description: Hoje, trazemos mais um Tech News com algumas novidades sobre
              o mundo de desenvolvimento de software e dicas de novas
              bibliotecas para Python e Lua. Este episodio foi gravado ao vivo
              pelo YouTube, aproveitamos e convidamos você para assinar o Canal
              do YouTube do Castálio Podcast.
image: /images/episode-116.png
image-alt: Tech News
---

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

Hoje trazemos um Tech News com novidades do mundo de desenvolvimento de
software e também dicas de cursos, eventos e novas bibliotecas para as
linguagens Python e Lua.

<div class="clearfix"></div>

# Escute enquanto lê os show notes

{{< podcast castalio-podcast-116 >}}

## Tech News

- O Jeferson do canal [Linux Tips](http://youtube.com/linuxtipscanal)
    (que foi nosso entrevistado no [episódio
    109](http://castalio.info/episodio-109-jeferson-noronha-canal-linuxtips.html))
    está publicando gratuitamente o [Curso Descomplicando Docker]().
- O grupo [Rust Lang Brasil no Telegram](https://t.me/rustlangbr)
    iniciou há algumas semanas as lives no Youtube que acontecem todas as
    terça-feiras às 22h no [Canal Rust BR](http://bit.ly/canalrustbr). Todos
    interessados em aprender [Rust](https://www.rust-lang.org/) estão
    convidados a participar via Youtube e também colocar a mão na massa nos
    exercicios do [exercism](http://exercism.io), que são resolvidos via
    [tmate](http://tmate.io) durante a transmissão.
- [Kenneth Reitz](https://www.kennethreitz.org/), o desenvolvedor da
    conhecida bibliteca [requests](https://github.com/requests/requests),
    lançou um novo projeto chamado
    [setup.py](https://github.com/kennethreitz/setup.py) com a intenção de ser
    um exemplo prático e bem escrito de configuração para distribuição de
    pacotes em Python.
- Também relacionado com a publicação de bibliotecas Python, falamos
    sobre o [Flit](https://github.com/takluyver/flit), que também foi tema de
    um [Artigo publicado no blog do Bruno
    Rocha](http://brunorocha.org/python/publish-your-python-packages-easily-using-flit.html),
    e que é uma ferramenta para simplificar a distribuição de pacotes Python
    sem a necessidade de um arquivo
    [setup.py](https://github.com/kennethreitz/setup.py).
- O [Elyézer](http://twitter.com/elyezer) participou de um [episódio
    do opencast](http://tecnologiaaberta.com.br/2017/08/opencast-80-fisl-18/)
    sobre o FISL 18 que foi adiado e acontecerá somente no ano que vem. Neste
    episódio também esteve presente o
    [Sady](http://softwarelivre.org/profile/sady) que é um dos organizadores do
    evento.
- O [Pexpect](http://pexpect.readthedocs.io/en/stable/) é uma
    biblioteca escrita em Python que ajuda a rodar e controlar comandos de
    console. Ela permite responder a padrões esperados nas saídas dos comandos
    (utilizando RegExp) permitindo a automatização da interação com aplicativos
    de linha de comando.
- Mais um projeto interessante do [Kenneth
    Reitz](https://www.kennethreitz.org/) é o
    [pipenv](http://docs.pipenv.org/en/latest/index.html), que é descrito no
    próprio repositório como o casamento sagrado entre
    [Pipfile](https://github.com/pypa/pipfile),
    [Pip](https://github.com/pypa/pip) e
    [Virtualenv](https://github.com/pypa/virtualenv). Este projeto utiliza o
    [Pipfile](https://github.com/pypa/pipfile), um formato alternativo ao
    requirements.txt e que tem um maior controle na gestão de dependências.
    Entre as features do [pipenv](http://docs.pipenv.org/en/latest/index.html)
    estão, a criação automática de um ambiente virtual, a criação automática de
    um arquivo de dependências assim que novos pacotes são instalados e a
    criação de um arquivo determinístico com o [lock]{.title-ref} das versões
    das dependências que também tem suporte a verificação de hashes.
- Aconteceu em SP o [Workshop de
    Flask](https://github.com/cursodepythonoficial/flask_workshop) do
    [Grupy-SP](https://www.meetup.com/Grupy-SP/). Neste workshop o material
    utilizado no treinamento de [Flask](http://FLASK.wtf) do
    [CursoDePython.com.br](http://Youtube.com/CursoDePython) foi apresentado
    aos participantes e o código fonte disponibilizado no github do [Workshop
    de Flask](https://github.com/cursodepythonoficial/flask_workshop).
- Do [Workshop de
    Flask](https://github.com/cursodepythonoficial/flask_workshop) surgiu o
    desenvolvimento de uma nova extensão para o [Flask](http://FLASK.wtf), o
    [Flask Simple Login](https://github.com/rochacbruno/flask_simplelogin), que
    traz uma forma bem fácil de inserir controle de acesso com usuário e senha
    a sites feitos em Flask.
- O [Telegram Bot Lua](https://github.com/wrxck/telegram-bot-lua) é um
    framework para desenvolvimento de bots para Telegram. Basta executar o
    webserver integrado em um servidor, configurar as chaves da API do Telegram
    e o bot estará em funcionamento. Por ser desenvolvido com a [Linguagem
    Lua](http://castalio.info/tag/lua.html), o bot é bem fácil de ser
    customizado com novas ações. O [Mattata](https://github.com/wrxck/mattata)
    é um bot que já possui diversas funcionalidades e foi escrito usando este
    framework.

## Sorteio de Ingressos para a RubyConf

A [RubyConf](http://eventos.locaweb.com.br/proximos-eventos/rubyconf-2017/),
maior conferência brasileira de Ruby acontecerá na Fecomercio em São Paulo nos
dias 17 e 18 de Novembro, os ingressos já estão à venda e nós sorteamos 2
ingressos neste episódio e também disponibilizamos o cupom **PRC_Castalio** que
concede 30% de desconto na compra do ingresso, à partir do segundo lote.

Já sorteamos 6 ingressos e ainda sortearemos mais 4 e para concorrer basta
preencher o [formulário](http://bit.ly/CastalioRubyConf) e estar inscrito no
[canal do YouTube](http://www.youtube.com/c/CastalioPodcast).

Pessoas que já foram sorteadas:

- Carlos HB
- Matheus Pellegrini Fernandes
- Marcos André de Souza
- Josué Carvalho Rodrigues
- Paulo Henrique Pinheiro
- Thiago Lopes

[Link do último sorteio](https://sorteador.com.br/sorteador/resultado/916689)

## Assista a gravação deste episódio

Como sempre, nossa entrevista foi gravada ao vivo no nossa canal no [Canal do
YouTube do Castálio Podcast](http://youtube.com/c/CastalioPodcast) e para ver a
gravação deste episódio confira o vídeo abaixo:

{{< youtube zlkbqSP-X_A >}}

Antes de finalizar o post, não podemos deixar de agradecer a todos que nos
deixaram comentários. Se você tem algo a nos dizer, você pode deixar seus
comentários aqui no site, ou no [Twitter](https://twitter.com/castaliopod) ou
no [Facebook](https://www.facebook.com/castaliopod). Também não esqueça de
seguir a [Playlist do Castálio
Podcast](https://open.spotify.com/user/elyezermr/playlist/0PDXXZRXbJNTPVSnopiMXg)
e inscrever-se no o [Canal do YouTube do Castálio
Podcast](http://youtube.com/c/CastalioPodcast).

Até o próximo episódio!

# Escute agora

{{< podcast castalio-podcast-116 >}}

# Links

- [Canal do YouTube do Castálio Podcast](http://youtube.com/c/CastalioPodcast)
- [Linux Tips](http://youtube.com/linuxtipscanal)
- [episódio 109](http://castalio.info/episodio-109-jeferson-noronha-canal-linuxtips.html)
- [Curso Descomplicando Docker]()
- [Rust Lang Brasil no Telegram](https://t.me/rustlangbr)
- [Canal Rust BR](http://bit.ly/canalrustbr)
- [Rust](https://www.rust-lang.org/)
- [exercism](http://exercism.io)
- [tmate](http://tmate.io)
- [Kenneth Reitz](https://www.kennethreitz.org/)
- [requests](https://github.com/requests/requests)
- [setup.py](https://github.com/kennethreitz/setup.py)
- [Flit](https://github.com/takluyver/flit)
- [Artigo publicado no blog do Bruno Rocha](http://brunorocha.org/python/publish-your-python-packages-easily-using-flit.html)
- [Elyézer](http://twitter.com/elyezer)
- [episódio do opencast](http://tecnologiaaberta.com.br/2017/08/opencast-80-fisl-18/)
- [Sady](http://softwarelivre.org/profile/sady)
- [Pexpect](http://pexpect.readthedocs.io/en/stable/)
- [pipenv](http://docs.pipenv.org/en/latest/index.html)
- [Pipfile](https://github.com/pypa/pipfile)
- [Pip](https://github.com/pypa/pip)
- [Virtualenv](https://github.com/pypa/virtualenv)
- [Workshop de Flask](https://github.com/cursodepythonoficial/flask_workshop)
- [Grupy-SP](https://www.meetup.com/Grupy-SP/)
- [Flask](http://FLASK.wtf)
- [CursoDePython.com.br](http://Youtube.com/CursoDePython)
- [Flask Simple Login](https://github.com/rochacbruno/flask_simplelogin)
- [Telegram Bot Lua](https://github.com/wrxck/telegram-bot-lua)
- [Linguagem Lua](http://castalio.info/tag/lua.html)
- [Mattata](https://github.com/wrxck/mattata)

{{< alert >}}
**Music (Música)**: [Ain\'t Gonna Give Jelly
Roll](http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll)
by [Red Hook Ramblers](http://www.redhookramblers.com/) is licensed under a
Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing)
License.
{{< /alert >}}
