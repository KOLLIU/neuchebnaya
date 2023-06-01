function set_draggable() {
    $('.character').draggable({
        drag: function() {
            update_line($(this).attr("id"));
        },
        stop: function() {
            return set_coord_by_id($(this).attr("id"));
        }
    });
}

function get_all_characters_coord(){
    $.ajax({ url: 'get_all_characters_div', type: 'GET', dataType: 'json', success: function(res) {
            $.each(res, function(key ,value){
                $('#' + key).offset({top: value['y'], left: value['x']});
            });
            update_lines();
        }
    });
}

function set_coord_by_id(character_id){
    var x = $('#' + character_id).offset().left;
    var y = $('#' + character_id).offset().top;
    data = {csrfmiddlewaretoken: csrftoken, "character_id": character_id, "x": x, "y": y}
    $.ajax({type: "POST", url: 'set_coord_by_id', data: data, dataType: "json"});
}

function update_line(char_id){
    var dy = $('#main_svg').offset().top;
    $("."+char_id).each(function(index, element){
        var classes = element.getAttribute("class").split(" ");
        var x1 = $('#' + classes[0]).offset().left;
        var y1 = $('#' + classes[0]).offset().top - dy;
        var x2 = $('#' + classes[1]).offset().left;
        var y2 = $('#' + classes[1]).offset().top - dy;
        element.setAttribute("x1", x1);
        element.setAttribute("y1", y1);
        element.setAttribute("x2", x2);
        element.setAttribute("y2", y2);
    });
}

function update_lines(){
    $(".character").each(function(index, element){
        update_line(element.getAttribute("id"));
    });
}