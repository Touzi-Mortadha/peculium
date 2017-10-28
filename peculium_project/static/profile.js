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
                $("#amount").text(data['PCL_amount'])
                $("#number_of_PCL").text(data['number_of_PCL'])
            },

            error: function () {
                console.log("GetNewAmmount is not working");
            }
        }
    );


}
setInterval(GetNewAmmount, 1000);

/* ***************************************************** */



/* ******************************* GetHistory ***************************** */

function GetHistory() {


    $.ajax({
            type: 'GET',
            url: '/api/user/'.concat(current_user.toString(), '/'),
            dataType: "json",
            success: function (data) {

                console.log("GetHistory is working");
                console.log(data['transactions'])
                var sorted_transactions =data['transactions']
                sorted_transactions.forEach(function (element) {

                    var date_of_trasaction=element.date_of_transaction;
                    var time_of_transaction=element.time_of_transaction;
                    var transaction_id=element.id;
                    var amount_sent=element.amount_sent;
                    var pcl_assignd=element.TCL_assigned;
                    $("#history").prepend("<tr><td>".concat(date_of_trasaction,"</td><td>",time_of_transaction,"</td><td>",transaction_id,"</td><td>",amount_sent,"</td><td>",pcl_assignd,"</td></tr>"))
                });

            },

            error: function () {
                console.log("GetHistory is not working");
            }
        }
    );


}
jQuery(document).ready(GetHistory);

/* ***************************************************** */


