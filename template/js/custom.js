/*
Template Name: OsahanBus - Bus Booking HTML Mobile Template
Author: Askbootstrap
Author URI: https://themeforest.net/user/askbootstrap
Version: 0.1
*/

(function($) {
    "use strict"; // Start of use strict

    // Tooltip
    $('[data-toggle="tooltip"]').tooltip();

    // Osahan Slider
    $('.osahan-slider').slick({
        infinite: true,
        autoplay: true,
        autoplaySpeed: 5000,
        centerMode: false,
        slidesToShow: 1,
        arrows: false,
        dots: true
    });

    // Sidebar Nav
    var $main_nav = $('#main-nav');
    var $toggle = $('.toggle');

    var defaultOptions = {
        disableAt: false,
        customToggle: $toggle,
        levelSpacing: 40,
        navTitle: '',
        levelTitles: true,
        levelTitleAsBack: true,
        pushContent: '#container',
        insertClose: 2
    };

    // call our plugin
    var Nav = $main_nav.hcOffcanvasNav(defaultOptions);

    // Select2
    $('.js-example-basic-single').select2();


})(jQuery); // End of use strict
    

// ==========index========

function redirectAfterDelay() 
{
    setTimeout(function() 
    {
      window.location.href = "landing.html";
    }, 
    5000); // 2 seconds in milliseconds
};

// =======signup.js=======
const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}


function validate() {
    var mail = document.getElementById("mail");
    var pass = document.getElementById("pass");
    var pass2 = document.getElementById("pass2");
  
    if (mail.value.trim() == "") {
      alert("Email required!");
      return false;
    } else if (pass.value.trim() == "") {
      alert("Password required!");
      return false;
    } else if (!isValidEmail(mail.value.trim())) {
      alert("Provide a valid email address");
      return false;
    } else if (pass.value.trim().length < 8) {
      alert("Password too short!");
      return false;
    } else if (pass2.value.trim() == "") {
      alert("Please confirm your password!");
      return false;
    } else if (pass2.value.trim() !== pass.value.trim()) {
      alert("Passwords do not match!");
      return false;
    } else {
      return true;
    }
  }
  
