$(document).ready(function () {

    /*
        Set up image thumbnail for trip details page
    */
    $('.trip-img-thumbnail').click(function (e) {
        e.preventDefault();
        $('.img-box').attr("src", $(this).attr("src"))
    })

    /*
        Add item to the cart without reload the page
    */
    $(".btn-cart").click(function () {

        var inputPassenger = $(this).prev('input').val();
        console.log(inputPassenger);
        var itemId = $(this).attr("id").split("add_")[1];
        console.log(itemId);

        var url = `/cart/add/${itemId}/`;
        var data = { 'csrfmiddlewaretoken': csrfToken, 'passenger': inputPassenger };
        $.post(url, data);

    });

    /*
        Reload trip results page if user wants to keep shopping
    */
    $("#btn-keep-shopping").click(function() {
        location.reload();
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
