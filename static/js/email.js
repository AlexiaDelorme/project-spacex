(function () {
    emailjs.init(emailjsUser);
})();

function sendMail(contactForm) {
    emailjs.send("gmail", "spacex", {
        "from_name": contactForm.first.value + " " + contactForm.last.value,
        "from_email": contactForm.email.value,
        "contact_request": contactForm.message.value,
        "subject": contactForm.subject.value
    })
    .then(
        function(response) {
            alert(response);
        },
        function(error) {
            alert(error);
        }
    );
}
