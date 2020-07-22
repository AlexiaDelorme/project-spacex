(function () {
  emailjs.init(emailjsUser);
})();

function sendMail(contactForm) {
  emailjs
    .send("gmail", "spacex", {
      from_name: contactForm.first.value + " " + contactForm.last.value,
      from_email: contactForm.email.value,
      contact_request: contactForm.message.value,
      subject: contactForm.subject.value,
    })
    .then(function(response) {
        contact_request_success();
        console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
        contact_request_fail();
        console.log('FAILED...', error);
    });
}

function contact_request_success() {
  console.log("The contact_request_success is being called");
  swal({
    title: "Request sent!",
    text: "Your message was successfully sent to SpaceX.",
    icon: "success",
    button: "ok",
  });
}

function contact_request_fail() {
  console.log("The contact_request_fail is being called");
  swal({
    title: "Request not sent!",
    text:
      "Sorry, there was an issue with the server when sending your request.",
    icon: "warning",
    button: "ok",
  });
}
