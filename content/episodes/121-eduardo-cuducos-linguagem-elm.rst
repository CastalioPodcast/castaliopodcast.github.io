=============================================
Episódio 121: Eduardo Cuducos - Linguagem Elm
=============================================

:date: 2017-10-09
:authors: Og Maciel, Elyézer Rezende, Bruno Rocha
:podcast: https://archive.org/download/castalio-podcast-121/castalio-podcast-121.mp3
:tags: eduardo cuducos, elm, elm lang, operação serenata de amor, expedição
       liberdade, mútuo, internet sem limites, node.js, vue.js, react, redux,
       elm guide, elm in action, vamos aprender elm, ellie, demo, bob dylan -
       hurricane, dançando no escuro, big fish, a vida é bela, musashi, alan
       watts
:image: images/eduardo-cuducos.jpg
:image-alt: Eduardo Cuducos - Linguagem Elm

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

O nosso convidado de hoje é estudante de PhD em Sociologia, gosta de hackear
culturas e estilos de vida, está envolvido em projetos como a `Operação
Serenata de Amor`_, `Expedição Liberdade`_, `Mútuo`_, `Internet sem Limites`_.
Ele também contribui com projetos Open Source e, além de tudo isso, ele
desenvolve utilizando a linguagem `Elm`_, que será o foco deste episódio.
Eduardo Cuducos, seja bem vindo ao Castálio Podcast.

.. more

.. raw:: html

    <div class="clearfix"></div>

.. podcast:: castalio-podcast-121
    :heading: Escute enquanto lê os show notes!


Recados
=======

1) A `Python Brasil 13 <http://2017.pythonbrasil.org.br/>`_ está acontecendo
   desde o dia 6 e vai até o 11 de outubro em Belo Horizonte. No próximo
   episódio nos vamos contar todos os detalhes sobre o evento.
2) Já sorteamos os 10 ingressos para a `RubyConf
   <http://eventos.locaweb.com.br/proximos-eventos/rubyconf-2017/>`_. Quem não
   foi sorteado ainda pode usar o cupom **PRC_Castalio** para ter 30% de
   desconto na compra do ingresso.

Tópicos abordados neste episódio
================================

* Como que o Cuducos se interessou e iniciou na area de desenvolvimento.
* Como ele descobriu o Elm.
* O que é programação funcional.
* Empresas e projetos utilizando o Elm.
* Como que o Elm garante no runtime exceptions.
* É possível utilizar o Elm para compilar código que pode ser rodado no
  `Node.js`_?
* Desvantagens do Elm e onde não se recomenda utilizá-lo.
* Material recomendado para aprender a linguagem.
* Frameworks e o ecossistema da linguagem.
* Como está o mercado de trabalho para quem quer trabalhar com Elm.

Assista a gravação deste episódio
=================================

Este episódio foi gravado ao vivo em nosso `canal no YouTube
<http://youtube.com/castaliopodcast>`_ e você pode assistir a gravação e os
demos no vídeo abaixo:

.. youtube:: rq37oZvUuNw

Gostaríamos de agradecer a todos que ouviram e participaram ao vivo no Youtube
e se você tem algum comentário ou sugestão por favor comente em nossas redes
sociais no `Twitter <https://twitter.com/castaliopod>`_ ou no `Facebook
<https://www.facebook.com/castaliopod>`_. E também siga nossa `Spotify Playlist
<https://open.spotify.com/user/elyezermr/playlist/0PDXXZRXbJNTPVSnopiMXg>`_ e e
não se esqueça de inscrever-se no `Canal no YouTube
<http://youtube.com/castaliopodcast>`_.

Até o próximo episódio!

Contatos
========

.. raw:: html

    <div class="row">
        <div class="col-md-6">
            <p>
            <div class="media">
            <div class="media-left">
                <img class="media-object img-circle img-thumbnail" src="/images/eduardo-cuducos.jpg" alt="Eduardo Cuducos" width="200px">
            </div>
            <div class="media-body">
                <h4 class="media-heading">Eduardo Cuducos</h4>
                <ul class="list-unstyled">
                    <li><i class="fa fa-github"></i> <a href="https://github.com/cuducos">Github</a></li>
                    <li><i class="fa fa-link"></i> <a href="https://cuducos.me/">Site</a></li>
                    <li><i class="fa fa-twitter"></i> <a href="https://twitter.com/cuducos/">Twitter</a></li>
                    <li><i class="fa fa-youtube"></i> <a href="https://www.youtube.com/user/cuducos">YouTube</a></li>
                </ul>
            </div>
            </div>
            </p>
        </div>
    </div>

.. podcast:: castalio-podcast-121
    :heading: Escute Agora

Top 5
=====

* **Música**: `Hurricane`_ by `Bob Dylan`_
* **Música**: Stampede
* **Filme**: `Dançando no Escuro`_
* **Filme**: `Big Fish`_
* **Filme**: `A Vida é Bela`_
* **Livro**: `Musashi`_
* **Livro**: `Alan Watts`_

Links
=====

* `Operação Serenata de Amor`_
* `Expedição Liberdade`_
* `Mútuo`_
* `Internet sem Limites`_
* `Elm`_
* `Node.js`_
* `Vue.js`_
* `React`_
* `Redux`_
* `Elm Guide`_
* `Elm in Action`_
* `Vamos Aprender Elm!`_
* `Elm Brasil no Telegram`_
* `Ellie`_
* `Código fonte do demo`_

.. class:: panel-body bg-info

    **Music (Música)**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Mentioned
.. _Operação Serenata de Amor: https://serenatadeamor.org/
.. _Expedição Liberdade: http://www.expedicaoliberdade.com.br/
.. _Mútuo: https://vimeo.com/72760145
.. _Internet sem Limites: https://github.com/InternetSemLimites
.. _Elm: http://elm-lang.org/
.. _Node.js: https://nodejs.org/
.. _Vue.js: https://vuejs.org/
.. _React: https://reactjs.org/
.. _Redux: http://redux.js.org/
.. _Elm Guide: https://guide.elm-lang.org/
.. _Elm in Action: https://www.goodreads.com/book/show/31441704-elm-in-action
.. _Vamos Aprender Elm!: https://www.youtube.com/playlist?list=PLUj8WMX6gr4_Rqt7HSUaINnVZ6zURwrKu
.. _Elm Brasil no Telegram: https://t.me/elmbrasil
.. _Ellie: https://ellie-app.com
.. _Código fonte do demo: https://ellie-app.com/TQYv4QNxa1/0

.. _Bob Dylan: https://www.last.fm/music/Bob+Dylan
.. _Hurricane: https://www.last.fm/music/Bob+Dylan/_/Hurricane
.. _Dançando no Escuro: http://www.imdb.com/title/tt0168629/
.. _Big Fish: http://www.imdb.com/title/tt0319061/
.. _A Vida é Bela: http://www.imdb.com/title/tt0118799/
.. _Musashi: https://www.goodreads.com/book/show/102030.Musashi
.. _Alan Watts: https://www.goodreads.com/author/show/1501668.Alan_W_Watts

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
