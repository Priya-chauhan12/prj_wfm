console.log("hi")

function validate() {
    let f = false;
    //username validation
    let uname = $('.username').val();
    if (uname == '' || uname == undefined) {
        f = false;
        $('.username-field-msg').html('This field is required..!')
    } else {

        f = true;
    }
    //name validation
    let name = $('.name-field').val();
    if (name == '' || name == undefined) {
        f = false;
        $('.name-field-msg').html('This field is required..!')
    } else {

        f = true;
    }
    // email validation
    let email = $('.email-field').val();
    let exp = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email == '' || email == undefined) {
        f = false;
        $('.email-field-msg').html('This field is required..!')
    } else if (exp.test(email) == false) {
        f = false;
        $('.email-field-msg').html('Please enter valid email address..!')
    } else {
        f = true;
    }
    // password validation
    let password = $('.password-field').val();
    let exp1 = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    if (password == '' || password == undefined) {
        f = false;

        $('.password-field-msg').html('This field is required..!')
    } else if (exp1.test(password) == false) {
        f = false;
        $('.password-field-msg').html('Your password needs to be between 6 and 20 characters long and contain one uppercase letter, one symbol, and a number..!')
    } else {
        f = true;
    }
    //confirm password
    let p1 = $('.password-field').val();
    let p2 = $('.password1-field').val();
    console.log(p1)
    console.log(p2)
    if (p2 == '' || p2 == undefined) {
        f = false;

        $('.password1-field-msg').html('This field is required..!')
    } else if (p1 != p2) {
        f = false;
        $('.password1-field-msg').html('Passwords did not match..!')
    } else {
        f = true;
    }

    // phone no
    let phone = $('.phone').val();
    console.log(phone)
    if (phone == '' || phone == undefined) {
        f = false;
        $('.phone-field-msg').html('This field is required..!')
    } else if (phone.length != 10) {
        $('.phone-field-msg').html('Only 10 digits are allowed..!')
        f = false;
    } else {
        f = true;
    }

    //aadhar card
    let aadhar = $('.aadhar').val();
    var regexp = /^[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}$/;
    if (aadhar == '' || aadhar == undefined) {
        f = false;
        $('.aadhar-field-msg').html('This field is required..!')
    } else if (regexp.test(aadhar) == false) {
        f = false;
        $('.aadhar-field-msg').html('Aadhaar number must have 12 digits as per UIDAI and must have white space after every 4 digits..!')
    } else {

        f = true;
    }
    //address
    let address = $('.address').val();
    if (address == '' || address == undefined) {
        f = false;
        $('.address-field-msg').html('This field is required..!')
    } else {

        f = true;
    }
    //city
    let city = $('.city').val();
    if (city == '' || city == undefined) {
        f = false;
        $('.city-field-msg').html('This field is required..!')
    } else {

        f = true;
    }
    //city
    let state = $('.city').val();
    if (state == '' || state == undefined) {
        f = false;
        $('.state-field-msg').html('This field is required..!')
    } else {

        f = true;
    }
    //city
    let zip = $('.zip').val();
    let zipCodePattern = /^\d{5}$|^\d{5}-\d{4}$/;
    if (zip == '' || zip == undefined) {
        f = false;
        $('.zip-field-msg').html('This field is required..!')
    }
    // else if (zipCodePattern.test(zip) == false) {
    //     f = false;
    //     $('.zip-field-msg').html('Not in right format..!')
    // } 
    else {

        f = true;
    }

    return f;

}