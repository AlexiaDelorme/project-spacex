$(document).ready(function () {

    /*
        Set up image thumbnail for trip details page
    */
    $('.trip-img-thumbnail').click(function (e) {
        e.preventDefault();
        $('.img-box').attr("src", $(this).attr("src"))
    })

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
        $('#myInput').trigger('focus')
    })

});
