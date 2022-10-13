---
title: "Episódio 89: Tech News e Review do livro Ready Player One"
slug: episodio-89-tech-news-e-review-do-livro-ready-player-one
aliases:
- /episodio-89-tech-news-e-review-do-livro-ready-player-one.html
date: 2017-02-27
authors:
- Og Maciel
- Elyézer Rezende
- Bruno Rocha
podcast: "https://archive.org/download/castalio-podcast-89/castalio-podcast-89.mp3"
tags:
- python 3
- NASA
- namedtuples
- namespace
- fuzzy
- console
- book review
- django
- ernest cline
- og maciel
- bruno rocha
- elyezer rezende
description: Neste episódio trazemos as novidades sobre Python e Linux e
              também um review do livro Ready Player One de Ernest Cline.
image: /images/episodio-89.png
image-alt: Tech news e book review...
---

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

Se você ainda não migrou os seus projetos para Python 3 é melhor começar agora.
Como já mencionamos aqui o Python 2.x está com os dias contados e alguns
frameworks importantes como o Django estão começando a remover o suporte ao
Python 2.

Além disso o Python 3 está trazendo novidades muito interessantes que não
estarão disponíveis no Python 2, então a hora de migrar é agora!

Conheça agora algumas notícias, novidades e dicas de softwares e truques para o
terminal Linux e no final do episódio um excelente Book Review!

<div class="clearfix"></div>

# Escute enquanto lê os show notes

{{< podcast castalio-podcast-89 >}}

<br />

## Novidades e Dicas de Python

- **Django agora só em Python 3:** O Framework **Django**, um dos mais
    importantes do ecossistema Python lançará a versão 1.11 em breve e será a
    última a suportar Python 2.x. Na próxima major version do Django, a 2.0.0 o
    framework irá dar suporte apenas a Python 3 e dada a importância deste
    framework isto com certeza será um grande empurrão para a comunidade fazer
    logo a migração.

    O anúncio foi feito no [site
    oficial](https://docs.djangoproject.com/en/dev/releases/1.11/):

    > \"The Django 1.11.x series is the last to support Python 2. The next
    > major release, Django 2.0, will only support Python 3.5+\"

- **Namespaces**: Uma dica de **Python 3** que trazemos é a nova
    classe **SimpleNamespace** disponível no módulo **types** da biblioteca
    padrão do Python 3.3+. É muito comum criarmos classes que não possuem
    métodos e servem apenas para armazenar valores. Também usamos muitas vezes
    dicionários e arquivos de constantes para este fim. Essa necessidade é
    bastante antiga no Python e a idéia surgiu em [2012 na lista oficial da
    linguagem](https://mail.python.org/pipermail/python-ideas/2012-May/015232.html)
    mas só agora passou a fazer parte da biblioteca padrão:

    ```python
    >>> from types import SimpleNamespace
    >>> podcast = SimpleNamespace(name='Castálio')
    >>> podcast.site = 'http://castalio.info'
    >>> print(obj)
    namespace(name='Castálio', site='http://castalio.info')
    >>> hasattr(obj, 'site')
    True
    ```

- **Named Tuples**: E também existe o **namedtuple** que é uma outra
    maneira de armazenar valores em um namespace mas utilizando uma estrutura
    de tupla, que pode tanto ser acessada via índice ou via atributo.
    **namedtuple** está disponível também no Python 2, veja um exemplo:

    ```python
    >>> from collections import namedtuple
    >>> Podcast = namedtuple('Podcast', 'name site')
    >>> castalio = Podcast('Castálio', 'http://castalio.info')
    >>> castalio.site
    http://castalio.info
    ```

    E também é possivel acessar os atributos através dos índices:

    ```python
    >>> castalio[0]
    'Castálio'
    >>> castalio[1]
    'http://castalio.info'
    ```

    Uma outra caracteristica interessante, é que tanto **namedtuple**
    quanto **SimpleNamespace** podem ser usados como classe base, veja:

    ```python
    class SuperPodcast(Podcast):
        def play(self):
            print("I won't gonna give you none of my Jelly Rolls...")

    >>> castalio = SuperPodcast('Castálio', 'http://castalio.info')
    >>> castalio.play()
    I won't gonna give you none of my Jelly Rolls...
    ```

- **Dicas para o console do Linux**: O **Adventures in /usr/bin and the likes** :
    é um [blog
    post](http://ablagoev.github.io/linux/adventures/commands/2017/02/19/adventures-in-usr-bin.html)
    que traz uma coleção de dicas e truques para usar no seu terminal.

    A lista traz 30 comandos ou pacotes que podem ajudar a agilizar sua vida ao
    executar tarefas no console do seu Linux. Os destaques são:

    **Watch**:

    ```bash
    watch -n 1 -d date
    ```

    O comando acima executa o comando [date]{.title-ref} a cada 1 segundo e o
    [-d]{.title-ref} informa o watch para destacar as diferenças entre as
    execuções.

    Portanto o [watch]{.title-ref} é muito útil para quando você precisa
    executar repetidamente um comando e inspecionar a sua saída em busca de
    diferenças.

    **Tac**

    O [tac]{.title-ref} é o [cat]{.title-ref} reverso, e exibe o conteúdo de um
    arquivo invertendo a ordem das linhas, veja um exemplo:

    ```bash
    $ cat data.txt
    1
    2
    3

    $ tac data.txt
    3
    2
    1
    ```

- **O Bootstrap do Tkinter?**: E quem gostou das nossas dicas de
    **Tkinter** vai gostar também do [AppJar](http://appjar.info/).

    Um wrapper para o **Tkinter** que traz algumas facilidades e uma coisa bem
    interessante que é um sistema de **grid** bastante parecido com os sistemas
    de grid dos frameworks **css**.

    ![](/images/appjar-grid.png)

    Código:

    ```python
    from appJar import gui

    app=gui()
    app.setFont(20)
    app.addGrid("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]]
    )
    app.go()
    ```

    Existem outros exemplos na coleção de widgets do AppJar
    <http://appjar.info/pythonWidgets>

- **Sofwares para usar no Linux**: A **Awesome Linux Software** é uma
    lista colaborativa disponível no github
    <https://github.com/VoLuong/Awesome-Linux-Software> que traz uma boa
    seleção de softwares para Linux separados em diversas categorias.

    A parte mais legal dessas listas é que você pode contribuir enviando
    um Pull Request e adicionando os softwares que você mais usa no
    Linux.

- **Fuzzy Finder no terminal**: O **FZF** é um software de Fuzzy
    Finder para terminal, e ajuda muito na hora de encontrar comandos,
    diretórios e arquivos digitando apenas uma parte do nome ou do
    caminho. A instalação é bem simples e as instruções estão no github
    <https://github.com/junegunn/fzf>

- **Publique seus Notebooks**: O **Binder** cria uma coleção
    interativa contendo todos os **JuPyter Notebooks** encontrados em
    seu repositório no github. Você informa o caminho do repositório e
    ele cria um ambiente virtual onde os seus notebooks podem ser
    executados e então você pode adicionar uma **badge** no README de
    seu projeto. Veja mais em <http://mybinder.org/>

## Book Review

Hoje temos um convidado especial, o **Thiago Perrotta** que já foi entrevistado
aqui no [episódio
66](http://castalio.info/episodio-66-thiago-perrotta-leitura-e-tecnologia.html)
fez o review do livro [Ready Player
One](http://www.goodreads.com/book/show/9969571-ready-player-one) que foi o
primeiro livro escrito por Ernest Cline. O livro é um romance com uma temática
futurista. Foi lançado originalmente em 16 de agosto de 2011.

A história se passa no ano de 2044. O mundo passa por uma grande crise
energética, onde destruição e pobreza são os cenários mais comuns. A única
escapatória é o OASIS, uma realidade virtual onde a maioria das pessoas passa
grande parte do seu tempo. No OASIS as pessoas estudam, trabalham, jogam e
interagem umas com as outras, e assim economizam combustível (recurso escasso),
evitam ficar muito tempo em contato com a poluição e tem mais acesso a cultura
e informações.

# Ainda não ouviu? escute agora!

{{< podcast castalio-podcast-89 >}}

{{< alert >}}
**Music (Música)**: [Ain\'t Gonna Give Jelly
Roll](http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll)
by [Red Hook Ramblers](http://www.redhookramblers.com/) is licensed under a
Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing)
License.
{{< /alert >}}
