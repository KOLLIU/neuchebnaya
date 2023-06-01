var character_onclick_block;
var character_first = -1;
var character_second = -1;


function character_first_set(character_id){
    character_onclick_block = false;

    elements = document.getElementsByClassName("character_active_block")
    for (var i = 0; i < elements.length; i ++){
        element = elements[i]
        element.classList.remove("character_active_block");
    }

    if (character_id == character_first){
        element = document.getElementById(character_id)
        element.classList.remove("character_active_block");
        character_first = -1;
    } else {
        element = document.getElementById(character_id)
        element.classList.add("character_active_block");
        character_first = character_id;
    }

    character_second = -1;
    console.log("Первый персонаж", character_first, "Второй персонаж", character_second)
}

function character_second_set(character_id){
    if (!character_onclick_block | character_first == -1 | character_first == character_id){
        return
    }
    character_onclick_block = false;

    elements = document.getElementsByClassName("character_active_block")
    for (var i = 0; i < elements.length; i ++){
        element = elements[i]
        element.classList.remove("character_active_block");
    }

    var character_second = character_id;

    result = prompt("Связь персонажей", "");
    console.log(result)

    if (result == null){
        character_first = -1;
        character_second = -1;
    }

    console.log("Первый персонаж", character_first, "Второй персонаж", character_second)

    data = {csrfmiddlewaretoken: csrftoken, "first_character_id": character_first,
    "second_character_id": character_second, "text": result}
    $.ajax({type: "POST", url: 'create_character_link', data: data, dataType: "json",
    success: function(res) {window.location.replace("");},
    error: function(res) {window.location.replace("");}
    });

}

function character_ondblclick(character_id){
    character_onclick_block = false;
    character_first_set(character_id)
}

function character_onclick(character_id){
    character_onclick_block = true;
    setTimeout(function(){character_second_set(character_id)}, 500)
}

function set_draggable() {
    $('.character').draggable({
        drag: function() {
            update_line($(this).attr("id"));
            character_drag_block = true;
            setTimeout(function(){character_onclick_block=false;}, 100)
        },
        stop: function() {
            setTimeout(function(){character_onclick_block=false;}, 100)
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