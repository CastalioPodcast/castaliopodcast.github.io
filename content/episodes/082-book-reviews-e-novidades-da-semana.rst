---
title: "Episódio 82: Book Review: 36 Books That Changed the World e The Martian Chronicles"
slug: episodio-82-book-review-36-books-that-changed-the-world-e-the-martian-chronicles
aliases:
- /episodio-82-book-review-36-books-that-changed-the-world-e-the-martian-chronicles.html
date: 2017-01-08
authors:
- Og Maciel
- Elyézer Rezende
- Bruno Rocha
category: Podcast
podcast: "https://archive.org/download/castalio-podcast-82/castalio-podcast-82.mp3"
tags:
- book review
- novidades da semana
- 36 books that changed the world
- the martian chronicles
- python 3.6
- typing
- kite
- grumpy
- golang
- mocket
- coloredlogs
- tkinter
- tcl
description: Hoje, trazemos mais um book review com os livros The Martian Chronicles
              e 36 books that changed the world. Também trazemos algumas novidades da
              semana com dica, pacotes e projetos interessantes.
image: /images/books-82.jpg
image-alt: 36 books that changed the world
---

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

No episódio de hoje temos um convidado, o Rafael Rosa Fu que aceitou nosso
convite e fez 2 book reviews, um falando sobre o livro "36 Books that Changed the World"
e outro sobre o "The Martian Chronicles".

A dica de Python da semana é sobre testes, mais especificamente sobre o uso
do ``subTest`` que é um context manager que foi adicionado ao módulo unittest do Python3.4
e que já estava disponível no 2.7. Usando o unittest e o ``subTest`` possibilita que
em um mesmo test case várias iterações de um loop sejam testadas tendo seu
resultado acumulado ao invés de sair na primeira falha. O Elyézer preparou o seguinte
exemplo::

    def par(n):
        """Verifica se o número é par"""
        return n % 2 == 0

    def test_todos_par(self):
        """Testa se todos os números da lista são pares"""
        for n in (0, 2, 3, -2, 4):
            with self.subTest(n=n):
                self.assertTrue(par(n))

Sem o uso do ``subTest`` o teste acima iria parar de ser executado na primeira falha, ou seja,
quando o ``n`` recebesse o valor ``3``, mas usando o ``subTest`` garantimos que todos os
números da lista serão testados e o caso de falha será informado apenas ao final quando
sair do contexto do ``subTest``.

Depois dessa pequena dica, falamos sobre as novidades da semana:

.. more

Projetos e Pacotes
------------------

- **Python 3.6.0**

  Foi lançada a versão final do `Python 3.6.0`_ contendo todas as novidades
  que já mencionamos no `episódio 76`_

- **typing**

  Já haviamos falado sobre o MyPy que traz a opção de tipagem e também sobre os annotations
  do Python 3.x, mas agora você pode também utilizar este recurso em versões anteriores
  instalando a bilbioteca `typing`_

- **Kite**

  Imagina fazer **pair programming** com uma inteligência articial? É isso que o `Kite`_
  oferece. Com plugins para os principais editores, o Kite utiliza de A.I para recomendar
  o que você deve fazer em seu código e mostra informações relevantes sobre o trecho digitado.
  Você digita ``import r`` e antes de completar o nome do módulo ele já te mostra uma lista
  de todos os pacotes mais populares iniciados com a letra ``r`` e exibe dicas sobre estes pacotes.

- **Grumpy**

  O pessoal do Google lançou um novo runtime para Python escrito em Go, o `Grumpy`_.
  Eles desenvolveram esta ferramenta para otimizar o YouTube que tem seu front-end e
  API escritos em Python e para melhorar seu desempenho, criando um runtime onde
  é possível executar código Python em cima de Go e a vantagem é que com isso você
  pode fazer ``from __go__ import qualquer_coisa`` e então aproveitar os recursos
  assíncronos da linguagem.

- **Python Mocket**

  Mock+Socket, `Python-Mocket`_ é uma biblioteca para fazer Mock de sockets e clients http.
  Por exemplo, quando você precisa testar o client de uma API mas não deseja efetuar chamadas reais,
  então você usa o **mocket** para gravar respostas padrão para URLs e Payloads específicos.

- **Colored Logs**

  Muito simples, instale o `coloredlogs`_ e rode ``coloredlogs.install()`` e tenha
  suas mensagens de log coloridas no terminal.

- **Tkinter**

  O `Tkinter`_ é uma extensão para usar a linguagem Tcl em Python. Ela serve para
  criar interfaces gráficas simples que usam o mesmo look and feel do seu sistema
  operacional. Neste episódio fazemos um convite para participar do `Castálio Playground`_
  e aprender ou exercitar seus conhecimentos em Python usando o nosso exemplo em Tkinter.


Book Review
-----------

O `Rafael Rosa Fu`_ é o nosso convidado neste episódio falando sobre estes
2 livros.

- `36 Books that Changed the World`_

    Desde o desenvolvimento da linguagem escrita, os livros têm desempenhado um papel central em nossa cultura.
    Divertindo, Instruindo e Inspirando. Mas um livro pode realmente mudar o curso da história?
    A resposta é, sim. **36 Livros Que Mudaram o Mundo** é uma fascinante coleção de Grandes Cursos
    elaborada a partir de uma extensa seleção de livros. É um tour intelectual de milhares de anos
    de história e de civilizações ao redor do globo.

- `The Martian Chronicles`_

   É um livro de contos de ficção científica de 1950, de autoria do escritor estadunidense Ray Bradbury,
   cujo tema recorrente é a colonização de Marte por humanos com problemas e eventualmente vindos de uma Terra
   sob a iminência de ser devastada pela Guerra Atômica. O livro mostra todo o processo da colonização do planeta vermelho com a chegada dos primeiros humanos, até o período onde devido ao descuido e abuso de seus recursos naturais, o planeta começa a entrar em decadencia. Composto de várias histórias, o livro é simplemente fantástico e Ray Bradbury mostra todo o seu gênio trazendo momentos variados como a comêdia, horror e saudozismo para ilustrar como o ser humano destroi mais um planeta.


Escute Agora
------------

{{< podcast castalio-podcast-82 >}}

Sorteio da Caneca do Castálio
+++++++++++++++++++++++++++++

.. figure:: /images/caneca.png
   :alt: Caneca do Castálio
   :figclass: clear

A nova caneca do Castálio teve sua arte desenvolvida gentilmente pela Karla que
faz aquarelas no `Emporium Karela`_ e conforme prometido sorteamos uma das canecas
entre os ouvintes que comentaram no `episódio 81`_.

Para o sorteio ordenamos os comentários por ordem de data crescente e então usamos
o site **Sorteador** para escolher um número aleatoriamente, e o grande vencedor foi
o nosso ouvinte **Nuno**.

O resultado do sorteio está registrado no seguite link  `<http://sorteador.com.br/sorteador/resultado/446325>`_

Parabéns **Nuno**, muito obrigado pela sua participação!!!

Escute nossos próximos episódios para saber como adquirir (ou quem sabe ganhar) uma das
canecas do Castálio!


.. class:: alert alert-info

    **Music (Música)**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Mentioned
.. _Python 3.6.0: https://www.python.org/downloads/release/python-360/
.. _episódio 76: /episodio-76-book-review-e-python-packages.html
.. _typing: https://pypi.python.org/pypi/typing
.. _Kite: https://kite.com/
.. _Grumpy: https://opensource.googleblog.com/2017/01/grumpy-go-running-python.html
.. _Python-Mocket: https://github.com/mindflayer/python-mocket
.. _coloredlogs: https://pypi.python.org/pypi/coloredlogs
.. _tkinter: https://docs.python.org/3.3/library/tk.html
.. _Castálio Playground: https://github.com/CastalioPodcast/playground
.. _Rafael Rosa Fu: http://castalio.info/carlos-brando-e-rafael-rosa-fu-grokpodcast-part-1.html
.. _36 Books that Changed the World: http://www.thegreatcourses.com/courses/36-books-that-changed-the-world.html
.. _The Martian Chronicles: https://www.goodreads.com/book/show/76778.The_Martian_Chronicles
.. _Emporium Karela: https://www.etsy.com/pt/shop/EmporiumKarela
.. _episódio 81: /episodio-81-book-review-as-vinhas-da-ira-e-novidades-da-semana.html

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
