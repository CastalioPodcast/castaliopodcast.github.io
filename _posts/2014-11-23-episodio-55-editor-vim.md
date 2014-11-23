---
title: "Episodio 55: Editor Vim"
tags: [vim, github, gist, editor]
---

![Editor Vim]({{ site.baseurl }}/images/episodio-55-vim.png)
Depois de um longo e tenebroso inverno, estamos de volta no ar, desta vez para ficar e com algumas novidades.Mas primeiramente, uma explicação sobre o sumiço súbito.

O processo de planejamento, gravação e edição de um podcast requere muitas horas e perseverança para poder correr atrás de assuntos (ou no caso deste podcast, entrevistados), pesquisar para ter um bom "background", e horas e horas editando arquivos de áudio para poder fornecer algo de (espero) boa qualidade para vocês que nos honra com sua presença e apoio. Devido a algumas mudanças no trabalho (algumas promoções com mais responsabilidades e longas horas) e na vida pessoal (o nascimento de minha terceira filha, Iza), eu senti que eu não teria mais o tempo livre requerido para continuar o podcast sem que o mesmo não perdesse a qualidade das entrevistas ou áudio. Foi muito difícil simplemente abandonar o projeto às moscas, sem sequer dar alguma explicação a` vocês que sempre acompanhou o podcast... por isso, quero então pedir 1,000 desculpas e que perdoem esta minha falta de professionalismo.

Durante os muitos meses que o podcast ficou parado, foram muitos os e-mails e comentários de amigos e ouvintes perguntando se o projeto estava realmente morto ou se existia alguma chance de trazê-lo de volta no ar, e eu sempre respondi que sem tempo livre, nem mesmo para editar o áudio, que a resposta era não.

Eis que nas últimas semanas, tendo participado como convidado do Opencast podcast, aquela vontade enorme que eu tive para começar o Castálio podcast voltou com uma força total, e depois de bater um papo com meu amigo Evandro Pastor, muso inspirador e responsável principal pela criação deste, decidi voltar a fazer o podcast, porêm com algumas mudanças:

Invés de somente fazer episódios de entrevistas (que realmente é mais complicado devido ao agendamento com convidados, etc), desta vez também farei episódios temáticos, onde descutiremos sobre algum aplicativo, tecnologia ou assunto que seja interessante ao ouvinte.
Notou que falei "descutiremos", no plural? Pois é, um dos grandes motivos para trazer o podcast de volta é a presença do Elyézer que aceitou formar uma parceria comigo e me ajudar a manter o projeto no ar. Com a presença dele, vocês terão a oportunidade de escutar uma pessoa super técnica e tarimbada em tudo quanto é assunto de tecnologia e programação. E tem mais, além de saber sobre um monte de assunto, ele ainda acha tempo para cozinhar uns rangos prá lá de interessantes e até mesmo fazer suchi!
Quer mais novidade? Beleza! Estamos também considerando deixar o WordPress de lado e usar algo mais "programático" que utilize Github, Jekyll e outras tecnologias do gênero, já que somos para lá de inspirados sobre programação e automatização (que é onde ganhamos o nosso "pão de cada dia" aqui na Red Hat). Um dia destes vou mostrar como que as coisas estão...
Para finalizar, eu não estaria aqui, depois de ter passado um tempinho editando um bate-papo que tive com o Elyézer esta última semana se não fosse por vocês que deixaram comentários aqui, no Twitter, pedindo pela volta do podcast... e especialmente quero deixar aqui o meu agradecimento ao Ivan Fuzzer e Evandro Pastor, pelo apoio e incentivo para voltar! Muito obrigado mesmo!

Então, para nosso primeiro episódio temático decidimos falar sobre o editor Vim, aquele editor que vem instalado por padrão na maioria de distribuições GNU/Linux e no Mac OS, mas que muitos não devem usar por ser um pouco estranho e assustador para quem somente conhece editores com interface gráfica.

Neste episódio falamos um pouco sobre o que atrai as pessoas a usarem o Vim como editor de texto e código, como sair dele (já que este deve ser o primeiro problema que novos usuários encontram pela primeira vez) e sobre formas de deixá-lo super configurado da forma mais fácil do mundo!

Mesmo que você não use o Vim (eu mesmo uso o Emacs!!!) ou já tenha usado mas nao achou nada interessante para convencê-lo(a) a a converter como usuário, algumas das ferramentas mencionadas aqui são super interessantes e podem ser úteis para que você mesmo(a) possa desenvolver algo para o seu editor ou aplicativo favorito!!!

Escute agora:
--------------
[MP3](http://downloads.ogmaciel.com/castalio-podcast-55.mp3)
[Ogg](http://downloads.ogmaciel.com/castalio-podcast-55.ogg)
[M4A](http://downloads.ogmaciel.com/castalio-podcast-55.m4a)

Links:
-------
* Editor Vim
* Github
* Gist
* Cygwin
* Gerenciadores de plugins:
  * Vundle
  * NeoBundle (versão melhorada do Vundle)
* Vim Bootstrap (vim-bootstrap no Github, consulte para uma lista de atalhos)
* oh-my-vim
* oh-my-zsh (framework para o zsh)
* vim-solarized (tema de cores)
* Syntastic (plugin para verificação da sintaxe)
* vim-fugitive (git wrapper para o vim)
* ctrlp plugin
* gist-vim plugin
* jedi-vim plugin
* Snippets plugin
* Pacote com vários plugins
* .vim Elyézer

Notas Adicionais: Entrando e saindo do modo de edição no Vim
---------------------------------------------------------------------
Durante o episódio foi comentado do modo de inserção (edição) porém ficou faltando as teclas. Ao entrar no Vim ao digitar "i" você entrará no modo de inserção e poderá digitar textos livremente como em qualquer outro editor.

Para retornar ao modo normal basta pressionar "Esc". Lembre-se que neste modo é onde você irá executar os comandos como ":q" para sair, ":w" para salvar o arquivo (ou ":w teste.txt" para salvar como teste.txt), ":x" para salvar e sair, entre outros.

Seleções visuais são feitas no modo visual que pode ser acessado a partir do modo normal utilizando a tecla "v" onde você poderá realizar a seleção caracter por caracter. "Shift+v" ("V") para entrar no modo visual mas selecionando linhas. Ao realizar uma seleção utilize "y" para copiar e "p" no modo normal para colar.

Creditos
---------
``Música``: **Ain't Gonna Give Jelly Roll**  by
[Red Hook Ramblers](http://music.redhookramblers.com/) is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives (aka Music Sharing) License.
