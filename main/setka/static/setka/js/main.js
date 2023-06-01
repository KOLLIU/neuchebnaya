pos = 0;

function set_event_draggable() {
    $('.draggable_game,.draggable_club').draggable({
        start: function(){
            pos = $(this).offset();
        },
        drag: function() {
        },
        stop: function() {
            new_pos = $(this).offset();

            x = new_pos.left + $(this).width() / 2
            y = new_pos.top + $(this).height() / 2
            event_id = $(this).attr("id")
            flag = true;

            $(".day_card").each(function(index, element){
                left = $(this).offset().left
                right = $(this).offset().left +  $(this).width()
                top = $(this).offset().top
                bottom = $(this).offset().top + $(this).height()
                day_id = ""
                if (left <= x & x <= right & $(this).offset().top <= y & y <= bottom){
                    day_id = $(this).attr("id")
                    data = {csrfmiddlewaretoken: csrftoken, "event_id": event_id, "day_id": day_id}
                    flag = false;
                    $.ajax({type: "POST", url: 'set_event_day_by_id', data: data, dataType: "json"});
                }
            });
            if (flag) {
                data = {csrfmiddlewaretoken: csrftoken, "event_id": event_id, "day_id": day_id}
                $.ajax({type: "POST", url: 'set_event_day_by_id', data: data, dataType: "json"});
            }
            window.location.replace("");
        }
    });
}