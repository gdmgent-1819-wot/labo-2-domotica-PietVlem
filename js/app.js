window.onload = function () {
    /*
    Check is user is authenticated
    */
    if (localStorage.getItem("loggedInUser") === null) {
        window.location.replace("../index.html");
    }

    /*
    Firebase get
    */
    var starCountRef = firebase.database().ref('test');
    starCountRef.on('value', function (snapshot) {
        console.log(snapshot.val());
    });

    /*
    Get all switches from a room
    update value to firebase
    */
    const btn = document.querySelector("#r1l");
    btn.addEventListener('click', function () {
        btn.checked ? firebase.database().ref('room1/light').set('true') : firebase.database().ref('room1/light').set('false');
    })

}