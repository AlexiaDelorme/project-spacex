$(document).ready(function () {

    /*
        Set up image thumbnail for trip details page
    */
    $('.trip-img-thumbnail').click(function (e) {
        e.preventDefault();
        $('.img-box').attr("src", $(this).attr("src"));
    });

    /*
        Add item to the cart and confirm it to the user using alert
        Request user if they want to keep shopping or go to cart
    */
    $(".add-to-cart").submit(function(e) {

        e.preventDefault();

        var inputPassenger = $(this).find("input#passenger").val();
        var itemId = $(this).attr("id").split("add_")[1];

        var url = `/cart/add/${itemId}/`;
        var data = { 'csrfmiddlewaretoken': csrfToken, 'passenger': inputPassenger };
        $.post(url, data);

        swal({
            title: "Thanks!",
            text: "This trip was successfully added to your cart!",
            icon: "success",
            buttons: {
                cancel: "Keep shopping",
                catch: {
                    text: "Go to cart",
                    value: "cart"
                },
            },
        })
            .then((value) => {
                switch (value) {
                    case "cart":
                        window.location.replace("/cart/");
                        break;
                    default:
                        location.reload();
                }
            });
    });

    /*
        Functions to increment or decrement passenger number
    */

    // ------ Code credit: http://jsfiddle.net/polaszk/1oyfxoor/

    function incrementValue(e) {
        e.preventDefault();
        var fieldName = $(e.target).data('field');
        var parent = $(e.target).closest('div');
        var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

        if (!isNaN(currentVal)) {
            parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
        } else {
            parent.find('input[name=' + fieldName + ']').val(0);
        }
    }

    function decrementValue(e) {
        e.preventDefault();
        var fieldName = $(e.target).data('field');
        var parent = $(e.target).closest('div');
        var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

        if (!isNaN(currentVal) && currentVal > 0) {
            parent.find('input[name=' + fieldName + ']').val(currentVal - 1);
        } else {
            parent.find('input[name=' + fieldName + ']').val(0);
        }
    }

    // ------ End of code credit

    /*
        Buttons to increment or decrement passenger number
    */

    $('.input-group').on('click', '.button-plus', function(e) {
        var inputPassenger = parseInt($(this).prev("input#passenger").val());
        var maxSlot = parseInt($(this).prev("input#passenger").attr("max"));
        if ( inputPassenger >= maxSlot ) {
            swal({
                title: "Sorry!",
                text: "The number of seats for this trip is limited to "+ maxSlot +" passenger(s).",
                icon: "warning",
                button: "ok",
            });
        } else {
            incrementValue(e);
        } 
    });

    $('.input-group').on('click', '.button-minus', function(e) {
        var inputPassenger = parseInt($(this).next("input#passenger").val());
        if ( inputPassenger-1 <= 0 ) {
            swal({
                title: "Sorry!",
                text: "You must select at least 1 passenger to book a trip.",
                icon: "warning",
                button: "ok",
            });
        } else {
            decrementValue(e);
        }
    });

    /*
        Customize title radio input for passengers forms
    */
    var parentWrapper = $(".radio-title").children("#div_id_title").children("div");
    $(parentWrapper).addClass("row text-left ml-2");
    $(parentWrapper).children(".form-check").addClass("col-2");

    /*
        Set up datepicker for trip search form
    */
    $("#datepicker").datepicker({
        autoclose: true,
        todayHighlight: true,
        format: 'yyyy-mm-dd'
    });

    /*
        Set up bootstrap modal script
    */
    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus');
    });

});
