var fadeOutInterval = null;

function displayFlashMessage(id, m) {
    let message = "";

    if (m["status"] === 200) message = '<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12"><div class="form-group"><div class="flashes"><div class="alert alert-success" style="width: 105%; margin-right: -30px; margin-left: -15px"><i class="fa fa-check fa-fw"></i>' + m["responseJSON"]["message"] + '</div></div></div></div>';
    else message = '<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12"><div class="form-group"><div class="flashes"><div class="alert alert-danger" style="width: 105%; margin-right: -30px; margin-left: -15px"><i class="fa fa-check fa-fw"></i>' + m["responseJSON"]["message"] + '</div></div></div></div>';     
        
    id["0"]["innerHTML"] = message;

    clearInterval(fadeOutInterval);

    id.fadeIn("fast", "linear");
    
    fadeOutInterval = setInterval(function() {
        id.fadeOut("slow", "linear", "slow");
    }, 4000);
}

$('#submitMessage').submit(function(b) {
    b.preventDefault();
    
    var formData = {
        'name': $('#name')["0"]["value"],
        'email': $('#email')["0"]["value"],
        'message': $('#directMessage')["0"]["value"]
    };

    return $.ajax({
        url: "/sendMessage",
        type: "POST",
        data: JSON.stringify(formData),
        contentType: "application/json;charset=UTF-8",
        complete: function(message) {
            displayFlashMessage($("#messageStatus"), message);
            
            $("#divName").load(document.URL + ' #divName');
            $("#divEmail").load(document.URL + ' #divEmail');
            $("#divMessage").load(document.URL + ' #divMessage');
        }
    });
});