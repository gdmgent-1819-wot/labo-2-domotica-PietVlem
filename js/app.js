window.onload = function () {
    /*
    Check is user is authenticated
    */
    if (localStorage.getItem("loggedInUser") === null) {
        window.location.replace("../index.html");
    }

    /*
    
    */
}