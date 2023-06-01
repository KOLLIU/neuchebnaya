function delete_quest(url){
    let conf = confirm("Вы уверены, что хотите удалить этот квест?");
    if (conf) {
        location.replace(url);
    }
}

function edit_link(link_id, link_text, edit_link_url, redirect_url){
    let result = prompt('Связь: ', link_text);
    data = {csrfmiddlewaretoken: csrftoken, "link_id": link_id, "text": result}
    $.ajax({type: "POST", url: edit_link_url, data: data, dataType: "json"});
    location.replace(redirect_url);
}