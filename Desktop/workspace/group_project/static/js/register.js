// select input, use query selector to select by id.
const usernameField=document.querySelector("#usernameField");
// select email
const emailField=document.querySelector("#emailField");
//if username is not a valid input
const wrongFeedback = document.querySelector(".false-feedback");
//if email is not a valid input
const wrongFeedbackEmail = document.querySelector(".invalidEmailType");
//validate username and email
const successfullUsername = document.querySelector(".successfullUsername");
const successfullEmail = document.querySelector(".successfullEmail");
//access password field to toggle 
const passwordField = document.querySelector("#passwordField");
const submitButton = document.querySelector(".submitButton")

// add event listener to check if user is typing
emailField.addEventListener("keyup",(event)=>{
    const valueOfEmail = event.target.value;
    successfullEmail.style.display = "block";
    successfullEmail.textContent= `Validating ${valueOfEmail} `;
    emailField.classList.remove("notValid")
    wrongFeedbackEmail.style.display = "none";
    if(valueOfEmail.length > 0){
    fetch("/register/validate-email/", {
        body: JSON.stringify({ email: valueOfEmail}),
        method: "POST",
    })
    .then((res)=>res.json())
    .then((data)=> {
        console.log("data", data);
        successfullEmail.style.display="none";
        if(data.email_error){
            submitButton.disabled = true
            emailField.classList.add("notValid");
            //display error message
            wrongFeedbackEmail.style.display = "block";

            wrongFeedbackEmail.innerHTML = `<p>${data.email_error} </p>`
        }else{
            submitButton.removeAttribute("disabled");
        }
    });
}
})
// add event listener to check if user is typing
usernameField.addEventListener("keyup", (event) =>{
    const valueOfUsername = event.target.value;
    successfullUsername.style.display = "block";
    successfullUsername.textContent= `Validating ${valueOfUsername} `;
    usernameField.classList.remove("notValid")
    wrongFeedback.style.display = "none";
    if(valueOfUsername.length > 0){
    fetch("/register/validate-username/", {
        body: JSON.stringify({ username: valueOfUsername}),
        method: "POST",
    })
    .then((res)=>res.json())
    .then((data)=> {
        console.log("data", data);
        successfullUsername.style.display="none";
        if(data.username_error){
            submitButton.disabled = true
            usernameField.classList.add("notValid")
            //display error message
            wrongFeedback.style.display = "block";

            wrongFeedback.innerHTML = `<p>${data.username_error} </p>`
        }else{
            submitButton.removeAttribute("disabled");
        }
    });
}
});
