---
title: "Episódio 55: Editor Vim"
slug: episodio-55-editor-vi
aliases:
- /episodio-55-editor-vim.html
date: "2014-11-23T18:44:00"
authors:
- Og Maciel
- Elyézer Rezende
podcast: "https://archive.org/download/castalio-podcast-55/castalio-podcast-55.mp3"
tags:
- github
- vim
image: /images/episodio-55-vim.png
image-alt: Editor Vim
---

Depois de um longo e tenebroso inverno, estamos de volta ao ar, desta
vez para ficar e com algumas novidades.Mas primeiramente, uma explicação
sobre o sumiço súbito.

O processo de planejamento, gravação e edição de um podcast requer
muitas horas e perseverança para poder correr atrás de assuntos (ou no
caso deste podcast, entrevistados), pesquisar para ter um bom
"background", e horas e horas editando arquivos de áudio para poder
fornecer algo de (espero) boa qualidade para vocês que nos honram com
sua presença e apoio. Devido a algumas mudanças no trabalho (algumas
promoções com mais responsabilidades e longas horas) e na vida pessoal
(o nascimento de minha terceira filha, Iza), eu senti que não teria mais
o tempo livre necessário para continuar o podcast sem que o mesmo não
perdesse a qualidade das entrevistas ou áudio. Foi muito difícil
simplesmente abandonar o projeto às moscas, sem sequer dar alguma
explicação a vocês que sempre acompanhou o podcast... por isso, quero
então pedir 1,000 desculpas e que perdoem esta minha falta de
profissionalismo.

Durante os muitos meses que o podcast ficou parado, foram muitos os
e-mails e comentários de amigos e ouvintes perguntando se o projeto
estava realmente morto ou se existia alguma chance de trazê-lo de volta
ao ar, e eu sempre respondi que estava sem tempo livre, nem mesmo para
editar o áudio, então a resposta era não.

.. more

Eis que nas últimas semanas, tendo participado como convidado do `Opencast`_
podcast, aquela vontade enorme que eu tive para começar o Castálio podcast
voltou com uma força total, e depois de bater um papo com meu amigo Evandro
Pastor, muso inspirador e responsável principal pela criação deste, decidi
voltar a fazer o podcast, porém com algumas mudanças:

1. Ao invés de somente fazer episódios de entrevistas (que realmente é
   mais complicado devido ao agendamento com convidados, etc), desta vez
   também farei episódios temáticos, onde discutiremos sobre algum
   aplicativo, tecnologia ou assunto que seja interessante ao ouvinte.
2. Notou que falei "discutiremos", no plural? Pois é, um dos grandes
   motivos para trazer o podcast de volta é a presença do Elyézer que
   aceitou formar uma parceria comigo e me ajudar a manter o projeto no
   ar. Com a presença dele, vocês terão a oportunidade de escutar uma
   pessoa super técnica e tarimbada em tudo quanto é assunto de
   tecnologia e programação. E tem mais, além de saber sobre um monte de
   assuntos, ele ainda acha tempo para cozinhar uns rangos pra lá de
   interessantes e até mesmo fazer sushi!
3. Quer mais novidade? Beleza! Estamos também considerando deixar o
   WordPress de lado e usar algo mais "programático" que utilize Github,
   Jekyll e outras tecnologias do gênero, já que somos para lá de
   inspirados sobre programação e automatização (que é onde ganhamos o
   nosso "pão de cada dia" aqui na Red Hat). Um dia desses vou mostrar
   como que as coisas estão...

Para finalizar, eu não estaria aqui, depois de ter passado um tempinho editando
um bate-papo que tive com o Elyézer esta última semana, se não fosse por vocês
que deixaram comentários aqui, no Twitter, pedindo pela volta do podcast...
e especialmente quero deixar aqui o meu agradecimento ao `Ivan Fuzzer`_
e `Evandro Pastor`_, pelo apoio e incentivo para voltar! Muito obrigado mesmo!

Então, para nosso primeiro episódio temático decidimos falar sobre o
editor Vim, aquele editor que vem instalado por padrão na maioria das
distribuições GNU/Linux e no Mac OS, mas que muitos não devem usar por
ser um pouco estranho e assustador para quem somente conhece editores
com interface gráfica.

Neste episódio falamos um pouco sobre o que atrai as pessoas a usarem o
Vim como editor de texto e código, como sair dele (já que este deve ser
o primeiro problema que novos usuários encontram pela primeira vez) e
sobre formas de deixá-lo super configurado da forma mais fácil do mundo!

Mesmo que você não use o Vim (eu mesmo uso o Emacs!!!) ou já tenha
usado, mas não achou nada interessante para convencê-lo(a) a a converter
como usuário, algumas das ferramentas mencionadas aqui são super
interessantes e podem ser úteis para que você mesmo(a) possa desenvolver
algo para o seu editor ou aplicativo favorito!!!

Escute Agora
------------

{{< podcast castalio-podcast-55 >}}

Links
-----

-  `Editor Vim`_
-  `Github`_
-  `Gist`_
-  `Cygwin`_
-  Gerenciadores de plugins:

   -  `Vundle`_
   -  `NeoBundle`_ (versão melhorada do Vundle)

-  `Vim Bootstrap`_ (`vim-bootstrap`_ no Github, consulte para uma `lista de atalhos`_)
-  `oh-my-vim`_
-  `oh-my-zsh`_ (framework para o zsh)
-  `vim-solarized`_ (tema de cores)
-  `Syntastic`_ (plugin para verificação da sintaxe)
-  `vim-fugitive`_ (git wrapper para o vim)
-  `ctrlp plugin`_
-  `gist-vim plugin`_
-  `jedi-vim plugin`_
-  `Snippets plugin`_
-  `Pacote com vários plugins`_
-  `.vim Elyézer`_

Entrando e saindo do modo de edição no Vim
------------------------------------------

Durante o episódio foi comentado do modo de inserção (edição) porém
faltaram as teclas. Ao entrar no Vim, ao digitar "i", você entrará no
modo de inserção e poderá digitar textos livremente como em qualquer
outro editor.

Para retornar ao modo normal, basta pressionar "Esc". Lembre-se que
neste modo é onde você irá executar os comandos como ":q" para sair,
":w" para salvar o arquivo (ou ":w teste.txt" para salvar como
teste.txt), ":x" para salvar e sair, entre outros.

Seleções visuais são feitas no modo visual, que pode ser acessado a
partir do modo normal utilizando a tecla "v", desta forma você poderá
realizar a seleção caracter por caracter. "Shift+v" ("V") para entrar no
modo visual, mas selecionando linhas. Ao realizar uma seleção utilize
"y" para copiar e, no modo normal, "p" para colar.

.. class:: alert alert-info

        **Música**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
.. _Opencast: http://tecnologiaaberta.com.br/
.. _Ivan Fuzzer: http://www.castalio.info/ivan-brasil-fuzzer-ubuntero/
.. _Evandro Pastor: http://www.castalio.info/evandro-pastor-quarto-estudio/
.. _Editor Vim: http://www.vim.org/
.. _Github: http://github.com
.. _Gist: http://gist.github.com
.. _Cygwin: https://cygwin.com/
.. _Vundle: https://github.com/gmarik/Vundle.vim
.. _NeoBundle: https://github.com/Shougo/neobundle.vim
.. _Vim Bootstrap: http://vim-bootstrap.com/
.. _oh-my-vim: https://github.com/liangxianzhe/oh-my-vim
.. _oh-my-zsh: https://github.com/robbyrussell/oh-my-zsh
.. _vim-solarized: https://github.com/altercation/vim-colors-solarized
.. _Syntastic: https://github.com/scrooloose/syntastic
.. _vim-fugitive: https://github.com/tpope/vim-fugitive
.. _ctrlp plugin: https://github.com/kien/ctrlp.vim
.. _gist-vim plugin: https://github.com/mattn/gist-vim
.. _jedi-vim plugin: https://github.com/davidhalter/jedi-vim
.. _Snippets plugin: https://github.com/SirVer/ultisnips
.. _Pacote com vários plugins: https://github.com/honza/vim-snippets
.. _.vim Elyézer: https://github.com/elyezer/.vim
.. _vim-bootstrap: https://github.com/avelino/vim-bootstrap
.. _lista de atalhos: https://github.com/avelino/vim-bootstrap#commands
