---
title: "Episódio 123: Ambiente de Desenvolvimento - Parte 2"
aliases:
- /episodio-123-ambiente-de-desenvolvimento-parte-2.html
date: 2017-10-23
authors:
- Og Maciel
- Elyézer Rezende
- Bruno Rocha
podcast: "https://archive.org/download/castalio-podcast-123/castalio-podcast-123.mp3"
tags:
- ambiente de desenvolvimento
- editor
- ide
- programação
- python
- shell
- vim
- vscode
- emacs
- direnv
- git
- magit
- orgmode
- vim-gitgutter
- vim-fugitive
- vim-ctrlp
- geany
- pycharm
- visual studio code
- nano
- dotfiles
- vimrc
- emacs.d
image: /images/episode-123.png
image-alt: Ambiente de Desenvolvimento - Parte 2
---

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!


Neste episódio continuamos a falar do nosso ambiente de desenvolvimento. Se
você ainda não ouviu na `primeira parte
<http://localhost:8000/episodio-120-ambiente-de-desenvolvimento-parte-1.html>`_
falamos sobre nosso shell, sistema operacional e algumas configurações de
nossos ambientes. Nesta parte vamos focar e falar sobre nossos editores de
texto, alguns plugins, configurações e recursos que usamos. Alem disso,
deixamos outras dicas como, por exemplo, se deve usar o `Git`_ com chave SSH ou
usuário e senha e também alguns atalhos úteis para quem utiliza o terminal.

.. more

.. raw:: html

    <div class="clearfix"></div>

{{< podcast id="castalio-podcast-123" heading="Escute enquanto lê os show notes!" >}}


Recados
=======

1) A temporada 2017 do Castálio vai até 30/10/2017 e então faremos uma pausa de
   2 meses até Janeiro de 2017, confira em nossa `agenda
   <http://castalio.info/agenda.html>`_.

2) Utilize o cupom de desconto **PRC_Castalio** e compre seu ingresso para a
   `RubyConf <http://eventos.locaweb.com.br/proximos-eventos/rubyconf-2017/>`_
   com 30% de desconto.

Tópicos abordados neste episódio
================================

* O Og comentou sobre seu editor, o `Emacs`_, e alguns dos plugins que ele
  utiliza como o `Magit`_ e `OrgMode`_.
* O Elyézer falou sobre o `Vim`_ e alguns do plugins que utiliza como o
  `vim-fugitive`_, `vim-gitgutter`_ e o `vim-ctrlp`_. Ele também comentou sobre
  o por que de um editor modal ser ate considerado bom em termos de ergonomia e
  como buscar e navegar na documentação do Vim.
* O Bruno mostrou que utiliza alguns editores como `Geany`_, `PyCharm`_,
  `nano`_ e `VSCode`_. Ele também utiliza o `direnv`_ para criar ambientes
  virtuais para cada um de seus projetos e a ativação e desativação desses
  ambientes acontece quando o diretório do projeto e acessado ou deixado
  respectivamente.
* Falamos também como acessamos um repositório Git no Github, se utilizamos
  uma chave SSH ou usuário e senha.
* No final foi comentado sobre alguns atalhos do terminal para facilitar a
  entrada de comandos:

  * ``Ctrl + a``: move o cursor para o inicio da linha
  * ``Ctrl + e``: move o cursos para o final da linha
  * ``Ctrl + k``: apaga desde a posição do cursor ate o final da linha
  * ``Ctrl + w``: apara a palavra anterior ao cursor
  * ``Ctrl + r``: pesquisa no histórico de comandos fazendo o match em qualquer
    parte do comando. ``Ctrl + p`` e ``Ctrl + n`` podem ser utilizados para ir
    para o comando encontrado anterior e posterior respectivamente.


Assista a gravação deste episódio
=================================

Este episódio foi gravado ao vivo em nosso `canal no YouTube
<http://youtube.com/castaliopodcast>`_ e você pode assistir a gravação e os
demos no video abaixo:

{{< youtube 4m_6Q8wQmm8 >}}

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
        <div class="col-md-4">
            <p>
            <div class="media">
            <div class="media-left">
                <img class="media-object rounded-circle img-thumbnail" src="https://avatars1.githubusercontent.com/u/458654?v=3&s=240" alt="Bruno Rocha" width="200px">
            </div>
            <div class="media-body">
                <h4 class="media-heading">Bruno Rocha</h4>
                <ul class="list-unstyled">
                    <li><i class="bi bi-twitter"></i> <a href="https://www.twitter.com/rochacbruno">Twitter</a></li>
                    <li><i class="bi bi-github"></i> <a href="https://github.com/rochacbruno">Github</a></li>
                    <li><i class="bi bi-link"></i> <a href="http://brunorocha.org">Site</a></li>
                </ul>
            </div>
            </div>
            </p>
        </div>

        <div class="col-md-4">
            <p>
            <div class="media">
            <div class="media-left">
                <img class="media-object rounded-circle img-thumbnail" src="https://avatars2.githubusercontent.com/u/48132?v=3&s=240" alt="Elyézer Rezende" width="200px">
            </div>
            <div class="media-body">
                <h4 class="media-heading">Elyézer Rezende</h4>
                <ul class="list-unstyled">
                    <li><i class="bi bi-twitter"></i> <a href="https://www.twitter.com/elyezer">Twitter</a></li>
                    <li><i class="bi bi-github"></i> <a href="https://github.com/elyezer">Github</a></li>
                    <li><i class="bi bi-link"></i> <a href="http://elyezer.com/">Site</a></li>
                </ul>
            </div>
            </div>
            </p>
        </div>

        <div class="col-md-4">
            <p>
            <div class="media">
            <div class="media-left">
                <img class="media-object rounded-circle img-thumbnail" src="https://avatars0.githubusercontent.com/u/53362?s=400&v=4" alt="Og Maciel" width="200px">
            </div>
            <div class="media-body">
                <h4 class="media-heading">Og Maciel</h4>
                <ul class="list-unstyled">
                    <li><i class="bi bi-twitter"></i> <a href="https://twitter.com/ogmaciel">Twitter</a></li>
                    <li><i class="bi bi-github"></i> <a href="https://github.com/omaciel">Github</a></li>
                    <li><i class="bi bi-link"></i> <a href="https://omaciel.github.io/">Site</a></li>
                </ul>
            </div>
            </div>
            </p>
        </div>
    </div>

{{< podcast id="castalio-podcast-123" heading="Escute Agora" >}}


Links
=====

* `Git`_
* `Emacs`_
* `Magit`_
* `OrgMode`_
* `Vim`_
* `vim-fugitive`_
* `vim-gitgutter`_
* `vim-ctrlp`_
* `Geany`_
* `PyCharm`_
* `VScode`_
* `nano`_
* `direnv`_
* `vimrc do Elyézer`_
* `dotfiles do Og`_
* `emacs.d do Og`_

.. class:: alert alert-info

    **Music (Música)**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Mentioned
.. _Git: https://git-scm.com/
.. _Emacs: https://www.gnu.org/software/emacs/
.. _Magit: https://magit.vc/
.. _OrgMode: http://orgmode.org/
.. _Vim: http://www.vim.org/
.. _vim-fugitive: https://github.com/tpope/vim-fugitive
.. _vim-gitgutter: https://github.com/airblade/vim-gitgutter
.. _vim-ctrlp: https://github.com/kien/ctrlp.vim
.. _Geany: https://www.geany.org/
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _VScode: https://code.visualstudio.com/
.. _nano: https://www.nano-editor.org/
.. _direnv: https://direnv.net/
.. _vimrc do Elyézer: https://github.com/elyezer/.vim
.. _dotfiles do Og: https://github.com/omaciel/dotfiles
.. _emacs.d do Og: https://github.com/omaciel/super-emacs

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
