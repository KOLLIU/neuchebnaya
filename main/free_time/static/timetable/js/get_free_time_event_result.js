function set_colors(){
    cells = document.getElementsByClassName("cell")
    for (i = 0; i < cells.length; ++i) {
        cell = cells[i].id;
        prep_date_time = cell.split("_");
        prep = prep_date_time[0];;
        day_id = prep_date_time[1];
        time = prep_date_time[2];


        for (const [key, value] of Object.entries(cell_free_time_types_dict)) {
            cell_free_time_types_dict[key] = 0;
        }

        time = time.split("-");
        start = Number(time[0].split(":")[0]) * 60 + Number(time[0].split(":")[1])
        stop = Number(time[1].split(":")[0]) * 60 + Number(time[1].split(":")[1])

        for (j = start; j < stop; ++j){
            cell_free_time_types_dict[prep_data_dict[prep][day_id][j]] += 1;
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
}