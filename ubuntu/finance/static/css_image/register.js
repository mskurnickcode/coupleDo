var password1 = document.getElementByID("#password1")
var password2 = document.getElementByID("#password2")
var button = document.querySelector('#submit')

function password_match(password1,password2) {
        //Reference the Button.

        //Verify the password values
        if (password1.value == password2.value) {
            //Enable the TextBox when TextBox has value.
            return false
        } else {
            //Disable the TextBox when TextBox is empty.
            return true
        }
    };

password2.keyup = function() {
    if (password_match(password1,password2) == true) {
        button.disabled = false;
    } else {
        button.disabled = true;
    }
}
