let userAllowedRequest = new XMLHttpRequest()

function createUserID32() {
    let v = ""
    for (let i = 0; i < 32; i++) {
        v = v + Math.floor(Math.random() * 9) + 1
    }
    console.log("Called")
    return v;
}
function getID_32(){
    if(Cookies.get("ID_32") == null){
        Cookies.set("ID_32", createUserID32())
    }
    return Cookies.get("ID_32")
}




//Sends Request if User Session is Allowed
//If ok                 ->          Nothing
//If illegalSession     ->          IllegalSession Page -> Option to Relogin
//If ServiceUnreachable ->          ServiceUnreachable Page -> ???
function sendUserAllowedRequest(){
    userAllowedRequest.open("GET", "http://localhost:6969/loginNeeded?ID_32=" + Cookies.get("ID_32"), true)
    userAllowedRequest.send()
}
userAllowedRequest.onreadystatechange = function (){
    console.log(userAllowedRequest.status)
    if(userAllowedRequest.status === 201){
        window.open("html/Error/illegalSession.html", "_self")
    }
    else if (userAllowedRequest.status === 404){
        window.open("html/Error/ServiceUnreachable.html")
    }
}