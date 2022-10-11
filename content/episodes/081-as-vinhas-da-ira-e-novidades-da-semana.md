---
title: "Episódio 81: Book Review: As Vinhas da Ira e Novidades da Semana"
slug: episodio-81-book-review-as-vinhas-da-ira-e-novidades-da-semana
aliases:
- /episodio-81-book-review-as-vinhas-da-ira-e-novidades-da-semana.html
date: 2017-01-01
authors:
- Og Maciel
- Elyézer Rezende
- Bruno Rocha
podcast: "https://archive.org/download/castalio-podcast-81/castalio-podcast-81.mp3"
tags:
- book review
- novidades da semana
- john steinbeck
- maya
- surprise
- pytone
- q
description: Hoje, trazemos mais um book review com o livro As Vinhas da Ira
              por John Steinbeck. Também trazemos algumas novidades da semana
              com notícias, pacotes e projetos interessantes.
image: /images/as-vinhas-da-ira.jpg
image-alt: As Vinhas da Ira por John Steinbeck
---

Olá pessoal e sejam bem-vindos à mais um episódio do Castálio Podcast!

No episódio de hoje o Og nos traz um book review do livro As Vinhas da Ira por
John Steinbeck. Também trazemos algumas notícias, pacotes e projetos que valem
a pena comentar e compartilhar.

Antes de começar, gostaríamos de desejar um feliz e próspero ano novo para
todos os nossos amigos e ouvintes. Obrigado por todos os comentários e
indicações, o Castálio é feito por todos nós e por isso a sua participação é
muito importante para o podcast. Que em 2017 agente consiga ter ainda mais
entrevistas, book reviews e novidades da semana inspiradoras.

Começamos hoje com uma pequena dica de Python, ou melhor, pip. Você pode criar
um cache local de pacotes utilizando a opção `--download` do pip, com isso você
pode ter seu backup de pacotes. Para salvar os pacotes em um diretório
especifico você pode executar:

```bash
pip install --download=/caminho/do/diretorio -r requirements.txt
```

Depois quando quiser usar o seu cache local, basta rodar:

```bash
pip install --no-index --find-links=/caminho/do/diretorio -r requirements.txt
```

Com isso o pip não irá fazer nenhum download e usará os pacotes salvos no
diretório.

Depois dessa pequena dica, falamos sobre as novidades da semana:

**Maya**

[Maya](https://github.com/kennethreitz/maya) é um projeto escrito em Python
pelo Kenneth Reitz (nosso entrevistado da semana passada). Ele facilita
trabalhar com datetimes pois o Maya faz todo o trabalho pesado de lidar com
timezones e permite que você foque no que realmente importa: importar ou
exportar dados de datetime nos formatos para humanos e máquinas. O Kenneth fez
um post com uma [introdução ao
Maya](https://www.kennethreitz.org/essays/introducing-maya-datetimes-for-humans).

**Surprise**

[Surprise](http://surpriselib.com/) é uma biblioteca em Python para análise
preditiva para sistemas de recomendação.

**PyTone**

[PyTone](https://www.luga.de/pytone/) é um jokebox com interface baseada em
ncurses (terminal). Ele oferece vários recursos entre eles crossfading, seleção
de música simples, playlist editável, mostra informações sobre a música atual
(lê os metadados), seleção de músicas aleatórias e inteligente (que leva em
consideração a avaliação e a última vez que a música foi tocada) entre outros.

O projeto é um pouco antigo (Python 2.5) mas é bem interessante a proposta.

**q : Quick-and-dirty debugging output for tired programmers**

[q](http://pyvideo.org/video/1858/sunday-evening-lightning-talks#t=25m15s) é
uma biblioteca que auxilia na geração de mensagens de debug rápidas. As
mensagens são escritas em arquivos (`$TEMPDIR/q`) e basta apenas incluir a
seguinte linha para adicionar uma mensagem: `import q; q("mensagem")`.

A biblioteca também permite fazer o trace de funções (informações de argumentos
e valor de retorno) utilizando o decorator [\@q]{.title-ref} antes da definição
da função. Também permite iniciar uma seção interativa no ponto em que a linha
`import q; q.d()` for adicionada no código.

Para uma demonstração em vídeo, assista ao [lightning talk sobreo
q](https://github.com/zestyping/q)

**Novidades**

Vamos deixar algumas novidades e links interessantes:

- [Full Stack Web Workshop GruPy-SP](https://github.com/rg3915/fs2w): Tutoriais gratuitos do Grupy-SP em 2017
- [Stack on a budget](https://github.com/255kb/stack-on-a-budget): Lista colaborativa de serviços cloud que oferecem períodos grátis para developers
- [Firebug lives on in Firefox DevTools](https://hacks.mozilla.org/2016/12/firebug-lives-on-in-firefox-devtools/): Firebug foi descontinuado como um add-on do Firefox pois agora ele será incorporado ao Mozilla DevTools

**Book Review: As Vinhas da Ira**

Fechamos o episódio com o book review feito pelo Og. O Og tem uma identidade
com a história apresentada no livro pois ele passou por momentos similares aos
apresentados no livro quando se mudou para os Estados Unidos.

A história do livro se passou durante a grande depressão e conta a história de
uma família pobre que foi expulsa de sua propriedade devido a mudanças na
atividade agrícola, a seca, dificuldades econômicas e execução de dívidas pelos
bancos. Por isso a família partiu de Oklahoma para a Califórnia em busca de
emprego, terra, dignidade e um futuro.

# Escute Agora

{{< podcast castalio-podcast-81 >}}

# Links

- [Maya](https://github.com/kennethreitz/maya)
- [introdução ao Maya](https://www.kennethreitz.org/essays/introducing-maya-datetimes-for-humans)
- [Surprise](http://surpriselib.com/)
- [PyTone](https://www.luga.de/pytone/)
- [lightning talk sobreo q](https://github.com/zestyping/q)
- [q](http://pyvideo.org/video/1858/sunday-evening-lightning-talks#t=25m15s)
- [Full Stack Web Workshop GruPy-SP](https://github.com/rg3915/fs2w)
- [Stack on a budget](https://github.com/255kb/stack-on-a-budget)
- [Firebug lives on in Firefox DevTools](https://hacks.mozilla.org/2016/12/firebug-lives-on-in-firefox-devtools/)
- [Vinhas da Ira - Filme - 1940](https://www.youtube.com/watch?v=BjPUQ4Apfhk)

{{< alert >}}
**Music (Música)**: [Ain\'t Gonna Give Jelly
Roll](http://freemusicarchive.org/music/Red_Hook_Ramblers/Live__WFMU_on_Antique_Phonograph_Music_Program_with_MAC_Feb_8_2011/Red_Hook_Ramblers_-_12_-_Aint_Gonna_Give_Jelly_Roll)
by [Red Hook Ramblers](http://www.redhookramblers.com/) is licensed under a
Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing)
License.
{{< /alert >}}
