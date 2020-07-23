(function () {
  emailjs.init(emailjsUser);
})();

const contactForm = document.getElementById("contact-form");

$("#contact-form").submit(function (e) {
  e.preventDefault();
  var data = {
    service_id: "gmail",
    template_id: "spacex",
    user_id: emailjsUser,
    template_params: {
      from_name: contactForm.first.value + " " + contactForm.last.value,
      from_email: contactForm.email.value,
      contact_request: contactForm.message.value,
      subject: contactForm.subject.value,
    },
  };

  $.ajax("https://api.emailjs.com/api/v1.0/email/send", {
    type: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
  })
    .done(function () {
      contact_request_success();
      console.log("Your mail is sent!");
    })
    .fail(function (error) {
      contact_request_fail();
      console.log("Oops... " + JSON.stringify(error));
    });
});

function contact_request_success() {
  swal({
    title: "Message sent!",
    text: "Thank you, your message request was successfully sent to SpaceX.",
    icon: "success",
    confirmButtonText: 'ok',
    confirmButtonColor: '#64a19d',
  }).then(() => {
    location.reload();
  });
}

function contact_request_fail() {
  swal({
    title: "Message not sent!",
    text:
      "Sorry, there was an issue with the server when sending your request.",
    icon: "warning",
    buttons: false,
    timer: 5000,
  });
}
