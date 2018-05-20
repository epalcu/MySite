function setActive(element) {
    element["0"]["style"]["color"] = '#f0ad4e';
    element["0"]["style"]["border"] = '2px solid #f0ad4e';
    element["0"]["value"] = "Active"
}

function setInactive(element) {
    element["0"]["style"]["color"] = 'white';
    element["0"]["style"]["border"] = '2px solid white';
    element["0"]["value"] = "Inactive"
}

function hide(element) {
    element.hide();
}

function show(element) {
    element.show();
}

// Just a function to make things a little more screen resolution responsive
function resizeObjects() {
    var windowWidth = (+window.getComputedStyle(document.body).width.replace(/px/,''));
    var windowHeight = (+window.getComputedStyle(document.body).height.replace(/px/,''));

    var setTitleSize = function(size) {
        $('#pageTitle')["0"]["style"]["fontSize"] = size;
    }

    var setBtnSizes = function(size) {
        $('#resumeBtn')["0"]["style"]["fontSize"] = size;
        $('#timelineBtn')["0"]["style"]["fontSize"] = size;
        $('#projectBtn')["0"]["style"]["fontSize"] = size;
        $('#goalBtn')["0"]["style"]["fontSize"] = size;
    }

    if (windowHeight >= 976) {
        if (windowWidth <= 1024 && windowWidth >= 553) setTitleSize("5vh");
        else if (windowWidth < 553) setTitleSize("3vh");
    }
    else {
        if (windowWidth >= 820) {
            setTitleSize("8vh");
            setBtnSizes("15px");
        }
        else if (windowWidth < 820 && windowWidth >= 600) setTitleSize("5vh");
        else if (windowWidth < 600 && windowWidth >= 400) {
            setTitleSize("3vh");
            setBtnSizes("10px");
        }
        else {
            setTitleSize("3vh");
            setBtnSizes("7px");
        }
    }
}

$('#timelineBtn').on('click', function(e) {
    if ($('#timelineBtn').val() != "Active") {
        setActive($('#timelineBtn'));
        setInactive($('#projectBtn'));
        setInactive($('#goalBtn'));

        hide($('#projects'));
        hide($('#goals'));
        show($('#timeline'));
    }
    else {
        setInactive($('#timelineBtn'));

        hide($('#timeline'));
    }
});

$('#projectBtn').on('click', function(e) {
    if ($('#projectBtn').val() != "Active") {
        setActive($('#projectBtn'));
        setInactive($('#timelineBtn'));
        setInactive($('#goalBtn'));

        hide($('#timeline'));
        hide($('#goals'));
        show($('#projects'));
    }
    else {
        setInactive($('#projectBtn'));

        hide($('#projects'));
    }
});

$('#goalBtn').on('click', function(e) {
    if ($('#goalBtn').val() != "Active") {
        setActive($('#goalBtn'));
        setInactive($('#timelineBtn'));
        setInactive($('#projectBtn'));

        hide($('#timeline'));
        hide($('#projects'));
        show($('#goals'));
    }
    else {
        setInactive($('#goalBtn'));

        hide($('#goals'));
    }
});

window.onload = function() {
    resizeObjects();
    hide($('#timeline'));
    hide($('#projects'));
    hide($('#goals'));
};

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});

window.onresize = function() {
    resizeObjects();
}