$('#submitMessage').submit(function(b) {
    b.preventDefault();
    
    var formData = {
        'name': $('#name')["0"]["value"],
        'email': $('#email')["0"]["value"],
        'message': $('#directMessage')["0"]["value"]
    };

    return $.ajax({
        url: "/getMessage",
        type: "POST",
        data: JSON.stringify(formData),
        contentType: "application/json;charset=UTF-8",
        success: function(list) {
            $("#divName").load(document.URL + ' #divName');
            $("#divEmail").load(document.URL + ' #divEmail');
            $("#divMessage").load(document.URL + ' #divMessage');
        }
    });
});