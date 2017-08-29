var tracklist = [];
var t = document.getElementsByClassName("song");
for ( var j = 0; j < t.length; j++){
    t[j].setAttribute("amplitude-song-index", j);
}

var temp = document.getElementsByClassName("song-meta-data");

for ( var i = 0; i < temp.length; i++){
    var temp_url = temp[i].getElementsByClassName("song-url")[0].innerHTML;
    var temp_title = temp[i].getElementsByClassName("song-title")[0].innerHTML;
    var temp_thumbnail = temp[i].getElementsByClassName("song-thumbnail")[0].innerHTML;
    var temp_artist = temp[i].getElementsByClassName("song-artist")[0].innerHTML;

    tracklist.push({name: temp_title, artist: temp_artist, album:"Unknown Album", url: temp_url, cover_art_url: temp_thumbnail});
    }

Amplitude.init({"songs": tracklist });