Episódio 99: Tech News e Book Review
####################################
:date: 2017-05-08
:authors: Og Maciel, Elyézer Rezende, Bruno Rocha
:category: Podcast
:podcast: https://archive.org/download/castalio-podcast-99/castalio-podcast-99.mp3
:tags: tech news, book review, complô contra a américa, philip roth, red hat,
       satellite 6, ansible, fauxfactory, pyup, openshift.io, bpython, tarek
       ziade, ipython, python, dan bader, faas, mstream, what the flask,
       pythonclub, tdd, api, rest, restful, django, django apps checklist,
       localstack, facebook, dev na estrada, hack'n'cast, opencast, priscila
       mayumi, caipyra, python brasil 13, python brasil, renzo nuccitelli,
       bruno rocha, og maciel, elyézer rezende, docker, prometheus, empreender
       e programar, flask, jupyter notebooks, py.test, travis, codecov
:description: Hoje, trazemos mais um Tech News e para quebrar o gelo um Book
              Review sobre o livro Complô Contra a América de Philip Roth.
              Este episodio foi gravado ao vivo pelo YouTube, aproveitamos e
              convidamos você para assinar o `Canal do YouTube do Castálio
              Podcast`_.
:image: images/tech-news.png
:image-alt: Tech News e Book Review

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

Hoje trazemos um Tech News com notícias, sugestões e dicas. Também fazemos um
Book Review do livro Complô Contra a América de Philip Roth. Além disso, temos
uma novidade, o Castálio agora tem um canal no YouTube e este episódio foi
gravado ao vivo por lá. Se você quer receber as novidades das próximas
gravações ao vivo e outros conteúdos que estaremos publicando por lá, assine o
`Canal do YouTube do Castálio Podcast`_.

.. more

Escute enquanto lê os show notes
--------------------------------

.. podcast:: castalio-podcast-99

.. raw:: html

    <br />

Tech News
=========

* `FauxFactory dropped support for Python 2 <https://github.com/omaciel/fauxfactory>`_

  * Usado pelas equipes da Red Hat Satellite 6 e Ansible, dentre outros.
  * Geradores de dados foram mudados para módulos próprios (mais fácil de
    manter)
  * `100% de cobertura de código <https://codecov.io/gh/omaciel/fauxfactory>`_
  * Testes são rodados no Travis usando py.test e novos testes foram
    adicionados (193 para 242).
  * Instale utilizando o pip: ``pip install fauxfactory``

* `pyup.io <https://pyup.io/>`_

  * Receba notificações de quando uma dependência do seu projeto foi atualizada
    ou tem alguma vulnerabilidade.

* `Vídeo de apresentação do OpenShift.io <https://www.youtube.com/watch?v=X-rAAF_7nSQ>`_

* `pyfora <http://docs.pyfora.com>`_ biblioteca para dividir o processamento em
  varias máquinas.

* `bpython <http://freecode.com/projects/bpython>`_

  * B de Better Python mas na verdade o B é de Bob Farrel, o criador do projeto
  * Interpretador Python interativo baseado na biblioteca curses
  * O `Tarek Ziade
    <http://castalio.info/episodio-83-tarek-ziade-mozilla.html>`_ é um dos
    contribuidores :)
  * Alguns dos recursos:

    * In-line syntax highlighting
    * Readline-like autocomplete with suggestions displayed as you type.
    * Expected parameter list for any Python function.
    * "Rewind" function to pop the last line of code from memory and re-evaluate.
    * Send the code you've entered off to a pastebin.
    * Save the code you've entered to a file.
    * Auto-indentation.
    * Python 3 support.

  * Diferenças com IPython

    * Não existe acesso aos comandos do seu shell
    * Não tem como fazer um reload em módulos importados
    * Não tem notebooks (aka ipython notebooks aka Jupyter)

  * ``pip install bpython``
  * `A better Python REPL – bpython vs python
    <https://www.youtube.com/watch?v=QITlSgYf8mc>`_ vídeo por `Dan Bader
    <https://dbader.org/>`_

* `FAAS (Function as a Service) <https://github.com/alexellis/faas>`_:
  Serverless Platform based on Docker and Prometheus

* `Mstream <https://github.com/IrosTheBeggar/mStream>`: crie seu próprio Spotify

* `What the Flask? parte 4 - Extensões para o Flask
  <http://pythonclub.com.br/what-the-flask-pt-4-extensoes-para-o-flask.html>`_
  foi lançado.

* `Test Driven Development of a Django RESTful API <https://realpython.com/blog/python/test-driven-development-of-a-django-restful-api/>`_

  * Artigo que mostra como criar um aplicativo Django com interface REST usando
    a metodologia TDD.
  * Mencionado sobre o `Django Apps Checklist
    <http://djangoappschecklist.com/>`_ e o episódio `Empreender e Programar
    <http://castalio.info/episodio-90-empreender-e-programar-parte-1.html>`_.

* `LocalStack <https://github.com/atlassian/localstack>`_ infraestrutura fake
  da Amazon para usar em testes e desenvolvimento.

* Caso do Facebook sobre o preconceito com as mulheres: `According to The Wall
  Street Journal
  <https://www.wsj.com/articles/facebooks-female-engineers-claim-gender-bias-1493737116>`_,
  female engineers who work at Facebook may face gender bias `that prevents
  their code from being accepted at the same rate as male counterparts
  <https://www.theverge.com/2017/5/2/15517302/facebook-female-engineers-gender-bias-studies-report>`_.
  "For Facebook, these revelations call into question the company's ongoing
  diversity efforts and its goal to build overarching online systems for people
  around the globe," reports The Verge.  "The company's `workforce is just 33
  percent female
  <http://www.businessinsider.com/uber-diversity-report-comparison-google-apple-facebook-microsoft-twitter-2017-3>`_,
  with women holding just 17 percent of technical roles and 27 percent of
  leadership positions."

Assista a gravação do episódio:

.. youtube:: F30Jp73PKXo

Book Review
-----------

Hoje trazemos o book review do livro `Complô Contra a América
<https://en.wikipedia.org/wiki/The_Plot_Against_America>`_ de Philip Roth.
Confira alguns pontos que foram mencionados:

* Ficção histórica (1940)
* Historiá contada do ponto de vista de um garoto da cidade de Newark, NJ.
* Franklin Delano Roosevelt (FDR) tenta se eleger pela terceira vez para a
  presidência, mas perde para o aviador Charles Lindbergh, que e famoso por ter
  feito um voo direto (sem parar) de NY até Paris.
* Charles Lindbergh diz em sua campanha não se envolver com a guerra e faz
  comentários elogiando Hitler.
* Charles Lindbergh diz que um voto para FDR significaria um voto a favor da
  guerra (America First)
* FDR pretende entrar na guerra e lutar contra Hitler
* Charles Lindbergh ganha a eleição, mostrando que muitas pessoas preferem não
  entrar na guerra, mesmo que isso signifique virar as costas ou fechar os
  olhos e ignorar o que está acontecendo com os Judeus e minorias na Europa.
* Uma vez eleito, o novo presidente assina um acordo de cooperação com Hitler,
  dizendo que os EUA não iriam participar ou se intrometer com a guerra e/ou
  decisões de Hitler.
* Nos EUA, todas as pessoas que já tinham noções anti semitistas se sentem mais
  com liberdade para se expressar em público todo seu preconceito.
* O livro então nos conta, do ponto de vista do personagem principal, como que
  pouco a pouco o governo começa de forma bem sutil a identificar e separar os
  Judeus dentre a população Americana.

  * Propaganda forte dizendo que Judeus não são Americanos, independente de
    quantas gerações já existam no pais
  * Preconceito e racismo extremo contra Judeus
  * Formação de um movimento igual os Nazistas fizeram onde crianças são
    convidadas a participar de campos de treinamento

    * Denunciar qualquer pessoa que seja contra o governo, mesmo se forem seus
      próprios pais
    * Lavagem cerebral para aceitar que Judeus são sinónimo de pessoas que amam
      a guerra, não americanos

* O final do livro acontece de forma muito rápida, e na minha opinião deixa a
  desejar por terminar assim
* Semelhanças com os USA depois do Trump

  * America First
  * Rússia e EUA (Putin & Trump)

* Semelhanças com o autor

  * Família chama-se Roth
  * Narrador chama-se Philip
  * Cenário é Newark

O livro possui adaptações para o cinema:

* `Pastoral Americana <http://www.imdb.com/title/tt0376479/>`_
* `Revelações <http://www.imdb.com/title/tt0308383/>`_
* `O Último Ato <http://www.imdb.com/title/tt1568343/>`_
* `Fatal <http://www.imdb.com/title/tt0974554/>`_

Ainda não ouviu? escute agora!
------------------------------

.. podcast:: castalio-podcast-99

Comunicados e eventos
---------------------

Fique ligado pois o episódio de número 100 será gravado ao vivo pelo YouTube no
dia 10 de maio de 2017 e será um Cage Match de Sistemas Operacionais. Já temos
a confirmação da participação de membros do `DEV na Estrada
<http://devnaestrada.com.br/>`_, `Hack’n’Cast <https://hackncast.org/>`_,
`Opencast <http://tecnologiaaberta.com.br/category/opencast/>`_, `Priscila
Mayumi <https://twitter.com/MayogaX>`_ e você, isso mesmo, você poderá
participar ao vivo. Então não perca essa chance, participe!

Confira os eventos nos quais você poderá encontra nos do Castálio Podcast:

* `Caipyra <http://caipyra.python.org.br/>`_ 2017 em Ribeirão Preto

  * O Bruno Rocha fará um keynote no dia 24 de Junho de 2017.

* `Python Brasil 13 <http://2017.pythonbrasil.org.br/>`_ que acontecerá em Belo
  Horizonte - MG de 06 a 11 de Outubro. Segue algumas palestras e tutoriais que
  recomendamos para você votar:

  * Vote no `Tutorial What The Flask
    <http://speakerfight.com/events/python-brasil-13-tutoriais/#what-the-flask-aprenda-flask-criando-um-cms-e-suas-extensoes>`_
    que o Bruno Rocha vai ministrar.
  * Vote na palestra `Autonomy way: o caminho da autonomia
    <http://speakerfight.com/events/python-brasil-13-palestras/#autonomy-way-o-caminho-da-autonomia>`_
    do Renzo Nuccitelli.
  * Vote na palestra `Just What Is A Quality Engineer?
    <http://speakerfight.com/events/python-brasil-13-palestras/#just-what-is-a-quality-engineer>`_
    do Og Maciel.
  * Vote na palestra `Mantendo Test Case e Código de Automação juntos no código
    fonte
    <http://speakerfight.com/events/python-brasil-13-palestras/#mantendo-test-case-e-codigo-de-automacao-juntos-no-codigo-fonte-2>`_
    do Og Maciel.
  * O Elyézer Rezende ainda não enviou nenhuma proposta de palestra mas tem
    planos de enviar. De qualquer forma, ele estará presente no evento.

Antes de finalizar o post, não podemos deixar de agradecer a todos que nos
deixaram comentários. Se você tem algo a nos dizer, você pode deixar seus
comentários aqui no site, ou no `Twitter <https://twitter.com/castaliopod>`_ ou
no `Facebook <https://www.facebook.com/castaliopod>`_. Também não esqueça de
seguir a `Playlist do Castálio Podcast
<https://open.spotify.com/user/elyezermr/playlist/0PDXXZRXbJNTPVSnopiMXg>`_.

Até o próximo episódio!


.. class:: panel-body bg-info

    **Music (Música)**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Mentioned
.. _Canal do YouTube do Castálio Podcast: http://bit.ly/CanalCastalio

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
