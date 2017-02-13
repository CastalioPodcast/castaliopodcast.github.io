Episódio 83: Tarek Ziadé - Mozilla
##################################
:date: 2017-01-15
:authors: Og Maciel, Elyézer Rezende, Bruno Rocha
:category: Podcast
:podcast: https://archive.org/download/castalio-podcast-83/castalio-podcast-83.mp3
:tags: tarek ziade, python, mozilla, english
:description: Hoje, conversamos com o Tarek Ziadé que é um desenvolvedor Python
              na Mozilla. Em nosso bate-papo conhecemos um pouco mais sobre o
              que ele faz trabalhando na Mozilla, sua paixão quando não está
              desenvolvendo e sobre os livros que escreveu e o que está
              escrevendo atualmente.
:image: images/tarekziade.jpg
:image-alt: Tarek Ziadé - Mozilla

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

Nosso convidado de hoje é um desenvolvedor Python que trabalha na Mozilla no
time de Serviços, escreveu vários livros sobre Python em inglês e francês, pai
de 3, é um corredor ávido, usuário Vim e trabalha de Dijon, na França.  É com
grande prazer que trazemos mais uma entrevista em inglês e conversamos com o
Tarek Ziadé.

Já vai aquecendo o seu inglês porque de agora em diante o post será escrito
nesta lingua. Como sempre, qualquer feedback que você tenha sobre esse formato
de post é muito bem vindo.

.. more

Hello everyone and welcome to Castálio Podcast!

Our guest for today is a Python developer currently working at Mozilla in the
Services team, has written several books about Python, both in French and
English, father of 3, is an avid runner, is a Vim user and works from Dijon,
France. It is with a great pleasure that we welcome Tarek Ziadé to our podcast!

First we started talking about Tarek's current role in the Mozilla's Services
team. We could not start better since recently he has changed his activities
and started doing something different spending these last few months in a new
role as a manager. He told us that he is working on tools for the quality
assurance of the products Services team creates and maintain.

Next we took a step back, and asked him how he ended up working at Mozilla and
what he had done before working there. He told us that he was looking for a
company which does open source and the opportunity came when Mozilla was
looking for a Python developer to work on porting some PHP projects to Python.
Continuing on, he commented that Python is very big in Mozilla. To finish this
topic he told us about Rust at Mozilla (the Mozilla language).

After that, we talked about what exactly he is doing to ensure the quality of
the products. Tarek mentions that he worked on a project which helped
orchestrate machines on Amazon Web Services and make hundreds of them to run a
Python script in order to do a request to a web services and gather metrics.
The other thing he's working on is to make sure all Mozilla's web services
follows the `OpenAPI 2.0 specification`_ (aka Swagger). He highlight that the
QA tools can get information and do some automatic work if the API follows that
specification. To complement, Bruno mentioned about his project `Flasgger`_
which creates Swagger 2.0 documentation for all the views by extracting specs
from the docstrings or referenced YAML files.

Then we talked about `Circus`_, a Python program which can be used to monitor
and control processes and sockets. The project was created in order avoid
struggling with `Supervisor`_. Now the project is not being used since they
moved to deploy the project on the cloud and each application runs on its own
virtual machine, so there's no need to control many process on the same
machine. It does not mean that the project is dead, it still active and
maintained but not so actively as it used to be.

As we mentioned in the beginning, Tarek has written a good book about Python
`Expert Python Programming`_ (he mentions that he was not involved on the
second edition because one of his children was born). And we can expect the
same or better quality for his next book, `Python Microservices Development`_
which is available to pre-order and is expected to be published in September
2017.  Tarek gave us an overview of what he is going to cover on the new book.

Moving away from the technical conversation for a while, Tarek tell us about
his passion for running and participating of a marathon. Also he gives some
tips about how he prepares and some extra activities that helps on getting not
only the body but also the brain ready for running long distances.

Our last question was about Tarek's opinion about Python 3. He comments that
sometimes we need to pick a version of Python based on the Operating System
because not all them have Python 3, for example, CentOS. He mentions that two
or three years ago we didn't have many libraries supporting Python 3 and now we
do. Also, he thinks Python 3 does not offer a killer feature other than perhaps
asyncio to convince people to upgrade, which could be slowing down the
adoption.

Finally it is Top 5 time! But before we get into it, we wanted to thank Tarek
for his `contributions as a Python core committer`_ on tools such as distutils,
pkgutil, sysconfig and other modules around packaging.

Before we end this post, we want to thank all the listeners who left
comments. Feel free to leave any comment below, on our `Twitter
<https://twitter.com/castaliopod>`_ or `Facebook
<https://www.facebook.com/castaliopod>`_ page.

See you all on our next episode!

Contact (Contato)
-----------------
* **Site**: https://ziade.org/
* **Twitter**: https://twitter.com/tarek_ziade
* **LinkedIn**: https://www.linkedin.com/in/tarekziade
* **Github**: https://github.com/tarekziade

Listen Now (Escute Agora)
-------------------------

.. podcast:: castalio-podcast-83

Top 5
-----
* **Music (Música)**: `Tyler Yarema <http://www.last.fm/music/Tyler+Yarema>`_
* **Music (Música)**: `Chali 2na <http://www.last.fm/pt/music/Chali+2na>`_
* **Music (Música)**: `Ghislain Poirier <http://www.last.fm/music/Ghislain+Poirier>`_
* **Music (Música)**: `Chinese Man <http://www.last.fm/music/Chinese+Man>`_
* **Book (Livro)**: `Dan Simmons <https://www.goodreads.com/author/show/2687.Dan_Simmons>`_
* **Book (Livro)**: `Terry Pratchett <https://www.goodreads.com/author/show/1654.Terry_Pratchett>`_
* **Book (Livro)**: `Warren Ellis <https://www.goodreads.com/author/show/12772.Warren_Ellis>`_
* **Book (Livro)**: `Ed Brubaker <https://www.goodreads.com/author/show/37450.Ed_Brubaker>`_
* **Book (Livro)**: `Philip K. Dick <https://www.goodreads.com/author/show/4764.Philip_K_Dick>`_
* **Movie (Filme)**: `Free to Run <http://www.imdb.com/title/tt3530882/>`_
* **Movie (Filme)**: `Summits of My Life: A Fine Line <http://www.imdb.com/title/tt2625054/>`_

Links
-----
* `OpenAPI 2.0 specification`_
* `Flasgger`_
* `Circus`_
* `Supervisor`_
* `Expert Python Programming`_
* `Python Microservices Development`_
* `contributions as a Python core committer`_

.. class:: panel-body bg-info

    **Music (Música)**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Mentioned
.. _OpenAPI 2.0 specification: http://swagger.io/specification/
.. _Flasgger: https://pypi.python.org/pypi/flasgger
.. _Circus: https://pypi.python.org/pypi/circus
.. _Supervisor: http://supervisord.org/
.. _Expert Python Programming: https://www.goodreads.com/book/show/5069668-expert-python-programming
.. _Python Microservices Development: https://www.packtpub.com/web-development/python-microservices-development
.. _contributions as a Python core committer: https://github.com/python/cpython/commits?author=tarekziade

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
