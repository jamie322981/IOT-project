document.addEventListener('DOMContentLoaded', function() {
    function updateVideo(videoSrc) {
        var videoSource = document.getElementById('videoSource');
        var videoPlayer = document.getElementById('videoPlayer');
        videoSource.src = videoSrc;
        videoPlayer.load();
        videoPlayer.play();
    }

    function checkForNfcUpdate() {
        fetch('/update_video')
            .then(response => response.json())
            .then(data => {
                if (data.success && data.video) {
                    updateVideo(data.video);
                }
            });
    }

    setInterval(checkForNfcUpdate, 1000);
});
