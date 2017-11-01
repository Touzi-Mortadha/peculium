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
                console.log(data['PCL_amount']);
                $("#amount").text(data['PCL_amount'] * data['number_of_PCL']);
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
                console.log(data['transactions']);

                var sorted_transactions = data['transactions'];
                sorted_transactions.forEach(function (element) {

                    var date_of_trasaction = element.date_of_transaction;
                    var time_of_transaction = element.time_of_transaction;
                    var transaction_id = element.id;
                    var amount_sent = element.amount_sent;
                    var pcl_assignd = element.TCL_assigned;
                    var verified = element.verified;
                    $("#history").prepend("<tr style='text-align: center;'><td style='padding: 20px;'>".concat(date_of_trasaction, "</td><td style='padding: 20px;'>", time_of_transaction, "</td><td style='padding: 20px;' >", transaction_id, "</td><td style='padding: 20px;'>", amount_sent, "</td><td style='padding: 20px;'>", pcl_assignd, "</td><td>", verified, "</td></tr>"));
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
/* ****************** Cryptocompare *********************************** */


function Cryptocompare() {

    $.ajax({
            type: 'GET',
            url: '/payment/api/currency/',
            url: 'https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=BTC,ETH',
            dataType: "json",
            success: function (data) {
                console.log("Cryptocompare is working");
                console.log(data);
                console.log(data['BTC'])
                $("#btc").text(data['BTC']);
                $("#eth").text(data['ETH']);
                $("#euro").text(1.0);
                // console.log(data[0]['Bitcoin'])
                // $("#btc").text(data[0]['Bitcoin']);
                // $("#eth").text(data[0]['Ethereum']);
                // $("#euro").text(data[0]['Euro']);
            },

            error: function (error) {
                console.log("Cryptocompare is not working");
                console.log(error)
            }
        }
    );


}
setInterval(Cryptocompare, 1000);

/* ********************************************** */
/* ******************* SUBMIT FORM *************************** */

$(document).on('click', '#button_submit', function () {

    var available_amount= document.getElementById("amount").innerHTML;
    var invested_amount= $("#buy").val() * amount

    if (invested_amount <= available_amount) {
    $("#invest_form").submit();
} else {
   alert("Sorry You have exceeded th allowed amount")
}



});

/* ********************************************** */






