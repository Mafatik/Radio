$(document).ready(function() {
    const play = $("#play");
    const volume = $("#volume");
    const sync = $("#sync");
    const sync_check = $("sync_check");
    const audio = $("#audio")[0];

    play.click(function() {
        if (audio.paused) {
            if (sync_check.checked) {
                audio.load();
            }
            audio.play();
            play.text("pause");
        } else {
            audio.pause();
            play.text("play");
        }
    });

    volume.on('input', function() {
        audio.volume = volume.val() / 100;
        if (volume.val() == 1) {
            audio.muted = true;
        } else {
            audio.muted = false;
        }
    });

    sync.click(function() {
        sync_check.checked = !sync_check.checked;
    });
});

function buffering() {
    $("#play").text("buffering...");
}

function canPlay() {
    if ($("#audio").prop("paused")) {
        $("#play").text("play");
    } else {
        $("#play").text("pause");
    }
}