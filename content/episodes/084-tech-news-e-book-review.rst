---
title: "Episódio 84: Tech News e Book Reviews por Hack and Cast"
slug: episodio-84-tech-news-e-book-reviews-por-hack-and-cas
aliases:
- /episodio-84-tech-news-e-book-reviews-por-hack-and-cast.html
date: 2017-01-22
authors:
- Og Maciel
- Elyézer Rezende
- Bruno Rocha
podcast: "https://archive.org/download/castalio-podcast-84/castalio-podcast-84.mp3"
tags:
- book review
- novidades da semana
- eu sou a lenda
- a última pergunta
- a última resposta
- isaac asimov
- richard matheson
- kivy
- restructured text
- markdown
- sanic
- flask
- shellcheck
- shell cript
- bash
- kalliope
- mention bot
- getcinnamon
- toml
- yaml
- ini
- config
description: Hoje, trazemos mais um book review com os livros Eu Sou A Lenda,
              A Última Pergunta e A Última Resposta feitos pelos nossos amigos
              do Hack and Cast e também trazemos algumas novidades da semana
              com dicas de Documentação, Python e Shell Script.
image: /images/books-84.jpg
image-alt: Isaac Asimov
---

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

No episódio de hoje temos como convidados Magnum, Jorge e Ricardo do `Hack and Cast`_
que fizeram os reviews dos livros **Eu Sou a Lenda** de Richard Matheson, **A Última Pergunta** e
**A Última resposta** de Issac Asimov.

A dica de Python da semana é sobre o framework `Kivy`_, e a sugestão foi do nosso
ouvinte **Hell Barba**. O **Kivy** é um framework para desenvolvimento de interfaces
orientadas a **multi-touch** especialmente voltado a tablets e dispositivos móveis, mas
que também serve para desenvolver **Desktop GUI** para aplicativos Python de maneira bastante
similar ao **Tkinter** que citamos no epiśodio 82.

.. more


Escute agora enquanto lê os show notes
--------------------------------------

{{< podcast castalio-podcast-84 >}}

.. raw:: html

    <br />


Estão disponíveis no YouTube vários videos a respeito do Kivy, e inclusive esta
série de tutoriais chamada `Kivy Crash Course`_.

Para criar um **Hello World** no Kivy é bastante fácil, veja o seguinte exemplo

.. figure:: /images/kivy.jpg
   :alt: Kivy Hello World

Outra coisa interessante é que é possível utilizar uma linguagem de template bem
parecida com XML para separar a parte de design de interface do código de lógica
do seu aplicativo.


Projetos e Pacotes
------------------


- **Restructured Text e Markdown**

  Para quem escreve README files e documentação de software, markdown e reST
  são linguagens essenciais e estes editores online ajudam bastante na hora
  de escrever com elas:

  - Online reStructuredText editor: `<http://rst.ninjs.org/>`_
  - StackEdit (editor de markdown): `<https://stackedit.io/editor>`_
  - MarkDown Table Generator: `<http://www.tablesgenerator.com/markdown_tables>`_


  E também tem opção para instalar no Desktop:

  - ReText: `<https://github.com/retext-project/retext>`_


  Mencionamos também que o Aaron Swartz foi um dos maiores contribuidores
  na especificação da `linguagem Markdown <https://daringfireball.net/projects/markdown/>`_ e o documentário
  `The Internet's Owns Boy <https://www.youtube.com/watch?v=sTt2n6wBUQg>`_
  está disponível no YouTube e conta a história do Aaron. Vale a pena assitir!

- **Sanic**

  O `Sanic`_ é um "clone" do Flask compatível apenas com Python 3.5+ e isso
  significa que as views do Sanic são todas assincronas utilizando o `async def`
  do Python 3.5+ e mantendo a mesma API de roteamendo e métodos do Flask.

  Veja um exemplo::

        from sanic import Sanic
        from sanic.response import json

        app = Sanic()

        @app.route("/")
        async def test(request):
            return json({"hello": "world"})

        if __name__ == "__main__":
            app.run(host="0.0.0.0", port=8000)

- **Shell Check**

  É uma ferramenta que permite verificar a sintaxe de código
  shell script, e além de poder ser utilizado online ainda oferece extensões
  para alguns editores e também pode ser integrado ao Travis CI.

  Para a verificação online basta acessar o `site do projeto <http://www.shellcheck.net>`_
  e colar seu código para ser validado.

  Para instalar no fedora::

      dnf install ShellCheck

  Para instalar no Mac::

      brew install shellcheck

  Para instalar em outros sistemas veja a `documentacao <https://github.com/koalaman/shellcheck#installing>`_.

  As sugestões são baseadas em boas práticas do Bash e possuem links para o wiki
  do projeto com mais informacões sobre o porque seguir a recomendacao sugerida.
  Por exemplo::

    SC2086 Double quote to prevent globbing and word splitting
    https://github.com/koalaman/shellcheck/wiki/SC2086.

  Além disso possui uma galeria de `“bad code” <https://github.com/koalaman/shellcheck#gallery-of-bad-code>`_

  Ele integra automaticamente com o `syntastic <https://github.com/vim-syntastic/syntastic>`_ no Vim caso instalado .
  No Emacs com o `FlyCheck <https://github.com/flycheck/flycheck>`_, entre outros editores como Atom, Sublime, e PyCharm.

- **Kalliope**

  O `Kalliope Project <https://github.com/kalliope-project>`_ é assistente
  pessoal com reconhecimento de voz projetado para automação residencial e
  que podem também ser usado para automatizar a execução de programas através
  de comandos de voz.

  Os comandos do Kalliope são programados através de plugins chamados **Neurons**
  e seu código é escrito em Python e a configuração feita com YAML, veja o exemplo
  da chamada a uma função chamda `say` recebendo o argumento `message` sempre
  que o Kalliope identificar **say hello** sendo falado no microfone::

        - name: "Hello-world"
          signals:
            - order: "say hello"
          neurons:
            - say:
                message: "Hello world!"

- **Mention Bot**

  O `Mention Bot <https://github.com/facebook/mention-bot>`_ é um bot
  desenvolvido pelo Facebook que via github web hooks é disparado toda vez
  que um novo Pull Request é enviado no seu repositório, então o Mention Bot
  analisa as linhas de código do PR e sugere os melhores contribuidores para
  serem os reviewers daquele PR.

- **Cinnamon**

  O `Cinnamon <https://www.getcinnamon.io/>`_ segue a mesma linha do Mention Bot,
  mas o foco dele são as issues, cada vez que alguém abre uma nova issue no seu
  repositório o Cinnabot analisa o conteúdo daquela issue e então analisa todo
  o histórico de issues do repositório e inclui um comentário citando as issues
  relacionadas e sugerindo o nome de um colaborador que possa ser o responsável
  por aquela issue. Este projeto é desenvolvido por nossos amigos da
  `Vinta Software <http://www.vinta.com.br/>`_ em Recife - Brasil, e é um projeto
  bastante útil e muito promissor!


- **TOML**

  Configurações de software em arquivos **.ini** são fáceis de ler em Python
  usando a biblioteca ConfigParser, porém as vezes o formato não oferece
  os tipos de dados mais complexos como listas e dicionários.

  Neste caso a resposta mais fácil parece ser o uso de YAML porém sabemos que
  o parsing de YAML pode ter um overhead desnecessário quando as configurações
  são simples.

  Para isso existe a  `Tom's Obvious, Minimal Language <https://github.com/toml-lang/toml>`_
  que mantém a simplicidade e performance do **.ini** mas oferece alguns tipos de
  dados mais complexos.

Book Review
-----------

Para este episódio trouxemos como convidados o Magnum, o Jorge e o Ricardo do
`Hack and Cast`_ que trouxeram reviews de 3 livros.

O Magnum falou um pouco sobre `Eu Sou A lenda`_ um livro que é uma mistura de
ficção científica com horror e o Magnum ressalta que o livro é muito melhor
que a adaptação para o cinema.

O Jorge falou sobre o conto `A Última Pergunta`_ de Issav Asimov, ele explicou
que este é um conto bastante curto que se passa em várias linhas temporais
comentando sobre a evolução da humanidade desde 1960, e aborda assuntos como
por exemplo a captação de energia solar e o salto evolutivo da
humanidade a partir disso e a questão cientifico-filosófica da
entropia termodinâmica.

E o Ricardo falou sobre o livro `A Última Resposta`_ que é também um conto do
Isaac Asimov bem curto, que não está diretamente relacionado com o anterior,
e que conta a história de um cientista que morre logo no inicio do conto
e que apesar de ser um cientista cético e ateu começa a analisar a situação
da morte e de forma bastante sarcástica questiona o momento da morte
conversando com a "Voz" que seria a figura do criador e este diálogo traz
reflexões cientificas, filosóficas e religiosas.

Ouça os book reviews no final deste episódio para saber mais detalhes!


Ainda não ouviu? escute agora!
------------------------------

{{< podcast castalio-podcast-84 >}}


.. class:: alert alert-info

    **Music (Música)**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Mentioned
.. _hack and cast: http://hackncast.org/
.. _kivy: http://kivy.org
.. _kivy crash course: https://www.youtube.com/playlist?list=SPdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq
.. _sanic: https://github.com/channelcat/sanic
.. _Eu Sou A lenda: https://www.goodreads.com/book/show/30192639-eu-sou-a-lenda
.. _A Última Pergunta: https://www.goodreads.com/book/show/4808763-the-last-question
.. _A Última Resposta: https://www.goodreads.com/book/show/15755066-the-last-answer

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
