 // Email JS send function adapted from CI lessons
 function sendMail(contactForm) {
    emailjs.send("service_ldj89hd", "little-explorers", {
        "name": contactForm.name.value,
        "email_address": contactForm.email_address.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            alert("Your email was sent!");
        },
        function(error) {
            console.log("FAILED", error);
            alert("Your email failed to send. Please try again later");
        }
    );
    return false;  // To block from loading a new page
}