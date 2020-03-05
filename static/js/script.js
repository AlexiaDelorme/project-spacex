(function () {
    emailjs.init("");
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
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}
