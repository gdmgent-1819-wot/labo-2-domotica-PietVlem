window.onload = function () {
    /*
    Check is user is already authenticated
    */
    if (localStorage.getItem("loggedInUser") !== null) {
        window.location.replace("pages/app.html");
    }

    /*
    Login
    */
    document.getElementById("login").addEventListener('click', function (event) {
        event.preventDefault();
        //Get user creds
        let email = document.getElementById("email").value;
        let pw = document.getElementById("pw").value;
        //Send api logn rquest
        firebase.auth().signInWithEmailAndPassword(email, pw).then(function (firebaseUser) {
            localStorage.setItem('loggedInUser', JSON.stringify(firebaseUser));
            window.location.replace("pages/app.html");
        })
            .catch(function (error) {
                window.alert(error.message);
            });
    })
};