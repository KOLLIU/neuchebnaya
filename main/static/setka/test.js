function set_draggable() {
    $('.draggable_game').draggable({
        drag: function() {
            console.log("123")
        },
        stop: function() {
            console.log("finish")
        }
    });
}