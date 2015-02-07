Episódio 56: Splinter
#####################
:date: 2014-12-07
:author: Og Maciel e Elyézer Rezende
:category: Podcast
:podcast: https://archive.org/download/castalio-podcast-56/castalio-podcast-56.mp3
:tags: splinter, selenium, automatização, splinter, selenium, python

No episódio de hoje, eu e o Elyézer conversamos um pouco sobre o
**Splinter**, uma ferramente muito interessante para quem trabalha com a
**automatização** de aplicativos web com **python**.

Na Red Hat, eu e Elyézer trabalhamos na automatização de testes
funcionais do produto **Satellite 6**, certificando que todos recursos
expostos pelas camadas de API, CLI (linha de comando) e UI (interface
web gráfica) funcionam conforme as expectativas do design. Uma opção
para efetuar estes testes seria fazer um mutirão no trabalho e testar
tudo manualmente... mas isso é coisa de iniciante, e todo engenheiro de
automatização que se preze eventualmente tenta automatizar tudo.

Apesar de usarmos o **Selenium** para efetuar testes de interface
gráfica, o **Splinter** é uma excelente alternativa para quem deseja
experimentar uma forma bem simples e fácil de interagir com um navegador
web (o tal do 'browser'), e é justamente por causa desta facilidade que
o episódio de hoje é dedicado ao **Splinter**.

.. more

Durante nosso bate-papo, outras ferramentas são mencionadas, como o
**Selenium IDE**, um add-on para o **Firefox** que permite gravar e
reproduzir interações com um navegador, e o **Selenium WebDriver**, uma
interface que permite interagir com um navegador usando uma linguagem de
programação.

Para reforçar o material, também criamos um pequeno "projeto exemplo"
onde discutimos sobre o uso do **Splinter** para detectar, catalogar e
enviar notícias pendentes do **Facebook** para o seu celular. Para um
exemplo mais concreto, vamos abrir um navegador **Firefox** e visitar o
site do **Castálio**, e checar na página de arquivos o nome do último
episódio:

.. code-block:: python

    from splinter import Browser

    browser = Browser('firefox')
    browser.driver.maximize_window()
    browser.visit('http://castalio.info/')

    browser.find_link_by_href('http://castalio.info/archives.html').click()

    element = browser.find_by_css('#archives p a').first
    print(element.text)

    browser.screenshot(name='castalio')
    browser.quit()

Como vocês podem ver, o código acima ate mesmo tira um screenshot da
pagina que foi aberta no navegador e salva no arquivo de sistemas:

.. figure:: {filename}/images/castalio5FkGWm.png
   :alt: Editor Vim

   Editor Vim

O bacana é que o método que tira screenshots foi
`contribuição <https://github.com/cobrateam/splinter/commit/9913fbb236455fdd94aaa06317536a74c4cd780a>`__
minha. :)

Agora, vamos fazer a mesma coisa, mas desta vez usando o **Selenium
WebDriver**:

.. code-block:: python

    from selenium import webdriver

    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get('http://castalio.info/')

    browser.find_element_by_css_selector(
    'a[href="http://castalio.info/archives.html"]'
    ).click()

    element = browser.find_element_by_css_selector('#archives p:first-child a')
    print(element.text)

    browser.save_screenshot('webdriver-castalio.png')
    browser.close()

Na nossa opinião, dentre as vantagens em usar o **Splinter**, gostamos
do fato que existem vários métodos para interagir com elementos de uma
página web que são bem completos e exigem menos linhas de código
comparado com o **Selenium**. Outra coisa que é bem atraente são os
nomes dos métodos, que são bem explícitos sobre qual o resultado que
será retornado. Por exemplo, para buscar elementos, temos os métodos:

.. code-block:: python

    browser.find_by_css('h1')
    browser.find_by_xpath('//h1')
    browser.find_by_tag('h1')
    browser.find_by_name('name')
    browser.find_by_id('firstheader')
    browser.find_by_value('query')

Os metodos acima retornam uma lista de elementos, se encontrados, o que
facilita encontrar elementos por índice. O **Splinter** também adiciona
dois métodos (**syntatic sugar**) que permitem acessar o primeiro e
ultimo elemento de uma lista:

.. code-block:: python

    browser.find_by_name('name').first
    browser.find_by_name('name').last

Buscando por links é super fácil:

.. code-block:: python

    links_found = browser.find_link_by_text('Link for Example.com')
    links_found = browser.find_link_by_partial_text('for Example')
    links_found = browser.find_link_by_href('http://example.com')
    links_found = browser.find_link_by_partial_href('example')

E para fechar com chave de ouro, você pode "encadear" suas buscas para
efetuar várias ações em uma só linha de código:

.. code-block:: python

    divs = browser.find_by_tag("div")
    within_elements = divs.first.find_by_name("name")

Ainda pretendemos trazer um dos desenvolvedores do projeto **Splinter**
para aprendermos um pouco mais sobre a história do projeto, seu design e
seu futuro... mas isso vai ficar para um próximo episódio!

Escute Agora
------------

.. podcast:: castalio-podcast-56

Links
-----

-  `Splinter <http://splinter.cobrateam.info/en/latest/>`__
-  `Selenium <http://docs.seleniumhq.org/>`__
-  `Selenium IDE <http://docs.seleniumhq.org/projects/ide/>`__
-  `Selenium WebDriver <http://docs.seleniumhq.org/projects/webdriver/>`__
-  `Satellite 6 <https://www.youtube.com/watch?v=BlNl7BJTUBs&list=PLcvmpY7C1j8l2rizvq7HLxLxX2fZioEuw>`__

.. class:: panel-body bg-info

        **Música**: `Ain't Gonna Give Jelly Roll`_ by `Red Hook Ramblers`_ is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.

.. Footer
.. _Ain't Gonna Give Jelly Roll: http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll
.. _Red Hook Ramblers: http://www.redhookramblers.com/
