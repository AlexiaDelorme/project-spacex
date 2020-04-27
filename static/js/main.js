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
        // itemID is an empty <span> of the cart.html file to get the url-for item.id
        // var itemID =  $(this).parents("form").children("span[id^=item-id-]").attr("id").replace("item-id-", "");
        // $.post(`/cart/adjust/${itemID}/`, {passenger: inputPassenger}); // ajax call without refreshing page
        var form = $(this).parents("form");
        form.submit();
    });
    

    // Set up datepicker
	$("#datepicker").datepicker({
        autoclose: true,
        todayHighlight: true,
        format: 'yyyy-mm-dd'
	});

});
