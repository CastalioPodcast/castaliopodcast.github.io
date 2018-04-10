Agenda
######
:slug: agenda
:date: 2017-05-25 08:00
:author: Og Maciel, Elyézer Rezende, Bruno Rocha
:comments: enabled

Às quartas, gravamos os episódios ao vivo pelo
YouTube e você está convidado a participar!  Basta se inscrever
no `Canal do Castálio <http://youtube.com/c/CastalioPodcast>`_ e
acompanhar nosso `Twitter <http://twitter.com/castaliopod>`_ ou `Facebook
<http://facebook.com/castaliopod>`_ para ficar sabendo quando estaremos  ao vivo!

Abaixo está a nossa agenda de episódios confirmados, a confirmar e temas sugeridos
pelos nossos ouvintes.

Caso você tenha alguma sugestão para o nosso próximo tema ou convidado, deixe
aqui nos comentários e inscreva-se em `nosso canal
<http://youtube.com/c/CastalioPodcast>`_ para receber as notificações e
participar das gravações ao vivo!

.. raw:: html

    <div class="alert alert-warning">
       <strong>Atenção:</strong> A agenda está sujeita a alterações e sempre
       anunciaremos no Twitter e Facebook no dia da gravação.
    </div>

    <table id="schedule" class="table table-bordered table-hover table-stripped">
        <thead>
            <tr><th>Data</th><th>Hora</th><th>Convidados</th><th>YouTube</th></tr>
        </thead>
        <tr id="loadingSchedule"><td colspan="4">Carregando a agenda...</td></tr>
    </table>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.0/moment.min.js"></script>
    <script src="https://www.gstatic.com/firebasejs/4.12.1/firebase.js"></script>
    <script src="https://www.gstatic.com/firebasejs/4.12.1/firebase-firestore.js"></script>
    <script>
    // Initialize Firebase
    var config = {
        apiKey: "AIzaSyANvstN_naRUktCRa0gLAYS4hruiHmsHhE",
        authDomain: "castalio-podcast.firebaseapp.com",
        databaseURL: "https://castalio-podcast.firebaseio.com",
        projectId: "castalio-podcast",
        storageBucket: "castalio-podcast.appspot.com",
        messagingSenderId: "119890203318"
    };
    firebase.initializeApp(config);

    var db = firebase.firestore();
    db.collection("schedule").where("datetime", ">=", new Date()).get().then((querySnapshot) => {
        var schedule = $('#schedule');
        schedule.find('#loadingSchedule').remove();
        if (querySnapshot.size > 0) {
            querySnapshot.forEach((doc) => {
                var data = doc.data();
                var date = moment(data.datetime);
                var guests = data.guests.map(g => g.name).join(', ');
                var youtubeEvent = data.youtubeEvent ? data.youtubeEvent : '-';
                var tr = $("<tr/>");
                tr.html(`<td>${date.format("DD/MM/YYYY")}</td><td>${date.format("HH:mm")}</td><td>${guests}</td><td>${youtubeEvent}`);
                schedule.append(tr);
            });
        } else {
            schedule.append("<tr><td  colspan=\"4\">Nenhum episódio agendado neste momento.</td></tr>");
        }
    });
    </script>

Sugestão de tema ou convidado?
------------------------------
Por favor comente abaixo sugerindo um tema ou convidado para nossos próximos
episódios.
