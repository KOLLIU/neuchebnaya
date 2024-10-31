var primaryMouseButtonDown = false;

function setPrimaryButtonState(e) {
  var flags = e.buttons !== undefined ? e.buttons : e.which;
  primaryMouseButtonDown = (flags & 1) === 1;
}


const history = new Array();
const redo_history_list = new Array();

document.addEventListener("mousedown", setPrimaryButtonState);
document.addEventListener("mousemove", setPrimaryButtonState);
document.addEventListener("mouseup", setPrimaryButtonState);

function change_td(str){
    date_time = str.split("_")

    day_id = date_time[1];

    time = date_time[0];
    time = time.split("-");
    start = Number(time[0].split(":")[0]) * 60 + Number(time[0].split(":")[1])
    stop = Number(time[1].split(":")[0]) * 60 + Number(time[1].split(":")[1])

    history_data = [];

    for (i = start; i < stop; ++i){
        history_data.push(data[day_id][i]);
        data[day_id][i] = active_free_time_type;
    }

    history.push({"str": str, "day_id": day_id, "time":time, "start": start, "stop":stop, "history_data": history_data, "act": active_free_time_type});
    document.getElementById(str).style["background-color"] = free_time_types_dict[active_free_time_type]["color"];

    redo_history_list.length = 0;
    send_data();
    update_history_buttons();
}

function mouse_over_td(str){
    if (primaryMouseButtonDown){
        change_td(str);
    }
}

function set_colors(){
    cells = document.getElementsByClassName("cell")
    for (i = 0; i < cells.length; ++i) {
        cell = cells[i].id;
        date_time = cell.split("_")
        time = date_time[0];
        day_id = date_time[1];

        for (const [key, value] of Object.entries(cell_free_time_types_dict)) {
            cell_free_time_types_dict[key] = 0;
        }

        time = time.split("-");
        start = Number(time[0].split(":")[0]) * 60 + Number(time[0].split(":")[1])
        stop = Number(time[1].split(":")[0]) * 60 + Number(time[1].split(":")[1])

        for (j = start; j < stop; ++j){
            cell_free_time_types_dict[data[day_id][j]] += 1;
        }

        max_key = "1";
        max_value = 0;
        for (const [key, value] of Object.entries(cell_free_time_types_dict)) {
            if (cell_free_time_types_dict[key] >= max_value){
                max_value = cell_free_time_types_dict[key];
                max_key = key;
            }
        }

        cells[i].style["background-color"] = free_time_types_dict[max_key]["color"];
    }
    update_history_buttons();
}

function choose_table(step_str){
    for (i = 0; i < tables.length; ++i) {
        tables[i].style["display"] = "none";
    }
    for (i = 0; i < table_buttons.length; ++i) {
        table_buttons[i].classList.remove('btn-danger');
        table_buttons[i].classList.remove('btn-primary');
        table_buttons[i].classList.add('btn-danger')
    }
    document.getElementById("table_" + step_str).style["display"] = "block";
    document.getElementById("table_button_" + step_str).classList.remove('btn-danger');
    document.getElementById("table_button_" + step_str).classList.add('btn-primary')
    set_colors();
}

function choose_free_time_type(type_id){
    active_free_time_type = type_id;
    document.getElementById("filling_free_time_type").innerHTML = "Выбрать: " + free_time_types_dict[type_id]["title"]
    document.getElementById("filling_free_time_type").style["background-color"] = free_time_types_dict[type_id]["color"]
}

function choose_filling_pattern(pattern_str){
    if (window.confirm("Вы действительно хотите применить шаблон к таблице? Это приведёт к перезаписи всех ранее заполенных данных")) {
        if (pattern_str != "-"){
            for (const [key, value] of Object.entries(data)) {
                for (i = 0; i < data[key].length; ++i){
                    data[key][i] = pattern_str;
                }
            }
            set_colors();
            send_data();
        } else {
            location.replace(fill_data_with_weekdays_data_url);
        }
    }
}

function update_history_buttons(){
    undo = document.getElementById("btn_arrow_undo");
    redo = document.getElementById("btn_arrow_redo");
    if (history.length > 0){
        undo.style["color"] = "#FFFFFF";
        undo.style["background-color"] = "rgba(255, 255, 255, 0.3)";
        undo.style["font-size"] = "min(3.2vw, 15px)";
        undo.style["cursor"] = "pointer";
    } else {
        undo.style["color"] = "#888888";
        undo.style["background-color"] = "rgba(255, 255, 255, 0.1)";
        undo.style["font-size"] = "min(3.2vw, 15px)";
        undo.style["cursor"] = "not-allowed";
    }
    
    if (redo_history_list.length > 0){
        redo.style["color"] = "#FFFFFF";
        redo.style["background-color"] = "rgba(255, 255, 255, 0.3)";
        redo.style["font-size"] = "min(3.2vw, 15px)";
        redo.style["cursor"] = "pointer";
    } else {
        redo.style["color"] = "#888888";
        redo.style["background-color"] = "rgba(255, 255, 255, 0.1)";
        redo.style["font-size"] = "min(3.2vw, 15px)";
        redo.style["cursor"] = "not-allowed";
    }
}

function undo_history(){
    if (history.length > 0){
        last = history[history.length - 1];
        start = last["start"];
        stop = last["stop"];
        for (i = start; i < stop; ++i){
            pr = data[last["day_id"]][i];
            data[last["day_id"]][i] = last["history_data"][i-start];
        }
        history.pop();
        redo_history_list.push(last);
        set_colors();
        send_data();
    }
}

function redo_history(){
    if (redo_history_list.length > 0){
        last = redo_history_list[redo_history_list.length - 1];
        start = last["start"];
        stop = last["stop"];
        for (i = start; i < stop; ++i){
            pr = data[last["day_id"]][i];
            data[last["day_id"]][i] = last["act"];
        }
        redo_history_list.pop();
        history.push(last);
        set_colors();
        send_data();
    }
}

function send_data(){
    $.post(data_send_url, {csrfmiddlewaretoken: csrftoken, "data": JSON.stringify(data)}, function (answer, status) {
        console.log(answer);
    });
}

function dont_show_modal_free_time(){

}