function loginUser() {

    let email = document.querySelector(
        'input[type="email"]'
    ).value;

    let password = document.querySelector(
        'input[type="password"]'
    ).value;

    if(email === "" || password === "") {

        alert("Please enter Email and Password");

    } else {

        alert("Logged in Successfully!");

    }
    function confirmDelete() {
    return confirm(
        "Are you sure you want to delete?"
    );
}
}