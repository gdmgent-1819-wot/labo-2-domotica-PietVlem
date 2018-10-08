window.onload = function () {
    /*
    Check is user is authenticated
    */
    if (localStorage.getItem("loggedInUser") === null) {
        window.location.replace("../index.html");
    }

    /*
    Firebase get
    
    let firebaseJson = firebase.database().ref();
    firebaseJson.on('value', function (snapshot) {
        console.log(snapshot.val());
    });
    */

    /*
    Get all switches from a room
    update value to firebase
    */
    var chkboxes = document.querySelectorAll("input[type='checkbox']");
    for(let i = 0; i < chkboxes.length ; i++){
        console.log(chkboxes[i]);
        onOffSwitch(document.querySelector("#"+chkboxes[i].id));
    }

    function onOffSwitch(btn) {
        btn.addEventListener('click', function () {
            btn.checked ? console.log(btn.id+' : '+true) : console.log(btn.id+' : '+false);
            btn.checked ? firebase.database().ref(btn.id).set(true) : firebase.database().ref(btn.id).set(false);
        })
    }
}