function loadFeaturedSongs() {
    Promise.all([
        fetch('http://127.0.0.1:5000/featured-songs').then(response => response.json()),
        fetch('http://127.0.0.1:5000/albums').then(response => response.json())
    ]).then(([featuredSongs, albums]) => {
        const featuredSongsList = document.getElementById("featuredSongs");

        const albumMap = new Map(albums.map(album => [album.id, album]));

        featuredSongs.forEach(song => {
            const listItem = document.createElement("li");
            const songContainer = document.createElement("div");

            songContainer.className = "songContainer";

            const album = albumMap.get(song.album_id);

            if (album && album.image) {
                const image = document.createElement("img");
                image.src = album.image;
                songContainer.appendChild(image);
            }
            else{
                const songTitle = document.createElement("p");
                songTitle.textContent = song.title;
                songContainer.appendChild(songTitle);
            }

            const songTitle = document.createElement("p");
            songTitle.textContent = song.title;
            songContainer.appendChild(songTitle);

            songContainer.addEventListener("click", () => {
                playAudio(song.audio);
            });
            

            listItem.appendChild(songContainer);
            featuredSongsList.appendChild(listItem);
        });
    }).catch(error => console.error('Erro ao carregar músicas e álbuns:', error));
}

loadFeaturedSongs();

function playAudio(audioUrl) {
    const audioElement = document.getElementById('audioPlayer');
    audioElement.src = audioUrl;
    audioElement.style.display = "block";
    audioElement.play();
}

function loadAlbums() {
    fetch('http://127.0.0.1:5000/albums')
        .then(response => response.json())
        .then(data => {
            const albumsList = document.getElementById("albumsList");

            data.forEach(album => {
                const listItem = document.createElement("li");
                const albumContainer = document.createElement("div");

                albumContainer.className = "albumContainer";

                if (album.image) {
                    const image = document.createElement("img");
                    image.src = album.image;
                    albumContainer.appendChild(image);
                }

                const title = document.createElement("p");
                title.textContent = album.title;
                albumContainer.appendChild(title);

                listItem.appendChild(albumContainer);
                albumsList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Erro ao carregar álbuns:', error));
}

loadAlbums();
