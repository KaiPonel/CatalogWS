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
/*
    --- PAGE: Authenticate ---
 */
let codeRequest = new XMLHttpRequest();
function handleButtons(){
    sendCodeRequestToServer()
}
//Send Request to send the Code via E-Mail
//200 = OK
//500 = Server Cant send Code
//404 = Server does not respond.
function sendCodeRequestToServer(){
    //ToDO Implement in Python
    console.log(Cookies.get("ID_32"))
    codeRequest.open("GET", "http://localhost:6969/CodeRequest?ID_32=" + getID_32(), true)
    codeRequest.send()
}

codeRequest.onreadystatechange = function(){
    if(codeRequest.status === 200 || codeRequest.status === 201){
        window.open("enterCode.html", "_self")
    }
    else if(codeRequest.status === 500){
        //ToDo Server cant Generate Code, What to do?
        window.open("Error/ServiceFailed.html", "_self")
    }
    else if(codeRequest.status === 404){
        window.open("Error/ServiceUnreachable.html", "_self")
    }
}



/*
    --- PAGE: enterCode ---
 */
let validateCodeRequest = new XMLHttpRequest();


function userHasInputValue(position) {
    let currentFieldName = "num" + position
    let currentField = document.getElementById(currentFieldName)
    let valueOfField = currentField.value
    if (valueOfField.length > 1 || isNaN(valueOfField)) {
        currentField.value = null;
        return;
    }
    let nextField = getNextFieldThatIsEmpty();
    if (getNextFieldThatIsEmpty() !== null) {
        document.getElementById(nextField).select();
    } else {
        submitCode()
        //Implement Greying out Button
    }
}

function getNextFieldThatIsEmpty() {
    for (let i = 0; i < 6; i++) {
        if (document.getElementById("num" + i).value === "") {
            return "num" + i;
        }
    }
    return null;
}
function submitCode() {
    //Grey Out NumFields
    let code = ""
    for (let i = 0; i < 6; i++) {
        document.getElementById("num" + i).setAttribute("readonly", "readonly")
        code = code + document.getElementById("num" + i).value
    }
    validateCodeRequest.open("GET", "http://localhost:6969/validateCode?ID_32=" + getID_32()+ "?code=" + code, true)
    validateCodeRequest.send()
}

validateCodeRequest.onreadystatechange = function (){
    if (validateCodeRequest.status === 200){
        //Grant User Access
        window.open("C:\\Users\\kaipo\\IdeaProjects\\Website-Katalog\\Main\\html\\list.html", "_self")
    }
    else if(validateCodeRequest.status === 401){
        //Code wrong
        window.open("enterCode.html", "_self")
    }
    else if(codeRequest.status === 500){
        //ToDo Server cant Generate Code, What to do?
        window.open("Error/ServiceFailed.html", "_self")
    }
    else if(codeRequest.status === 404){
        window.open("Error/ServiceUnreachable.html", "_self")
    }

}



