document.addEventListener("DOMContentLoaded", function() {
    var options = {
        strings: ["Bonjour, bienvenue sur notre site web.,Nous espérons que vous apprécierez votre visite."],
        typeSpeed: 50,
        backSpeed: 25,
        loop: true
    };

    var typed = new Typed("#typed-output", options);
});
