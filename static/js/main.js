$(document).ready(function () {

    // Image thumbnail for trips page
    $('.trip-img-thumbnail').click(function (e) {
        e.preventDefault();
        $('.img-box').attr("src", $(this).attr("src"))
    })

    // Update total price per trip according to passenger number  
    $(".passengerAdjust").change(function () {
        var inputPassenger = $(this).val();
        var tripPrice = $(this).siblings(".tripPrice").val();
        var totalTripPrice = (inputPassenger * tripPrice).toLocaleString();
        $(this).parents("form").siblings(".d-inline-flex").children(".totalPrice").text(totalTripPrice);
        var sum = 0;
        $(".totalPrice").each(function () {
            sum += parseFloat($(this).text().replace(/,/g, ''));
        });
        $("#totalCartPrice").text(sum.toLocaleString());

        // Update cart without reloading the page
        var itemId = $(this).siblings(".tripPrice").attr("id").split("remove_")[1];
        var url = `/cart/adjust/${itemId}/`;
        var data = { 'csrfmiddlewaretoken': csrfToken, 'passenger': inputPassenger };
        $.post(url, data);

        // Submit form on input change
        // var form = $(this).parents("form");
        // form.submit();

    });

    // Set up datepicker
    $("#datepicker").datepicker({
        autoclose: true,
        todayHighlight: true,
        format: 'yyyy-mm-dd'
    });

});
