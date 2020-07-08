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
        Remove item from cart after user confirmed his choice
    */

    $(".remove-cart-form").submit(function (e) {

        e.preventDefault();

        swal({
            title: "Are you sure?",
            text: "This trip will be removed from your cart.",
            icon: "warning",
            buttons: {
                cancel: "Cancel",
                catch: {
                    text: "Delete",
                    value: "delete"
                },
            },
        })
            .then((value) => {
                switch (value) {
                    case "delete":
                        swal("This trip was removed from your cart!", {
                            icon: "success"
                        })
                            // Sent form to delete item from cart
                            .then((value) => {
                                var itemId = $(this).attr("tripid").split("trip_")[1];
                                $.ajax({
                                    type: "POST",
                                    url: `/cart/remove/${itemId}/`,
                                    data: $(this).serialize(),
                                    success: function () {
                                        location.reload();
                                    }
                                });
                            });
                        break;
                    default:
                        swal("The trip is still in your cart!");
                }
            });
    });

    /*
        Update cart information according to changes in passenger number
    */
    $(".passengerAdjust").change(function () {

        var inputPassenger = $(this).val();
        var tripPrice = $(this).siblings(".tripPrice").val();

        // Update total price for each cart item
        var totalTripPrice = (inputPassenger * tripPrice).toLocaleString();
        $(this).parents("form").siblings(".d-inline-flex").children(".totalPrice").text(totalTripPrice);

        // Update amount for the total cart
        var sum = 0;
        $(".totalPrice").each(function () {
            sum += parseFloat($(this).text().replace(/,/g, ''));
        });
        $("#totalCartPrice").text(sum.toLocaleString());

        // Update number of cart item in the navbar
        var cartItem = 0;
        $(".passengerAdjust").each(function () {
            cartItem += parseFloat($(this).val());
        });
        if (cartItem > 0) {
            $("#cart-label").text(cartItem);
        }

        // Update cart content without reloading the page
        var itemId = $(this).siblings(".tripPrice").attr("id").split("remove_")[1];
        var url = `/cart/adjust/${itemId}/`;
        var data = { 'csrfmiddlewaretoken': csrfToken, 'passenger': inputPassenger };
        $.post(url, data);

        swal({
            title: "Cart updated!",
            text: "We have adjusted the number of passengers for this trip.",
            icon: "success",
            button: "ok",
        });

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
