function validate() {
    const username = document.getElementById("username-field").value;
    const password = document.getElementById("password-field").value;
    if (username == null || username == "") {
        document.getElementById("username-field").style.border = "3px solid red";
        // return false;
    } else if (password == null || password == "") {
        document.getElementById("password-field").style.border = "3px solid red";
    } else if (username != "" && password != "") {
        alert('login sucessfull..!');
    }

}