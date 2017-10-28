//********************************* Cookies *******************************************


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


//************************************************************************


/* ******************************* display new PCL values ***************************** */

function GetNewAmmount() {

    $.ajax({
            type: 'GET',
            url: '/api/pcl/1/',
            dataType: "json",
            success: function (data) {
                console.log("GetNewAmmount is working");
                console.log(data['PCL_amount'])
                $( "#amount" ).text(data['PCL_amount'])
                $( "#number_of_PCL" ).text(data['number_of_PCL'])
            },

            error: function () {
                console.log("GetNewAmmount is not working");
            }
        }
    );


}
setInterval(GetNewAmmount, 1000);

/* ***************************************************** */


