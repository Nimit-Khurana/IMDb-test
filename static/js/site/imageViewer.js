const viewer = new Viewer(document.getElementById('images'), {
    inline: true,
    viewed() {
        viewer.zoomTo(1);
    },
});