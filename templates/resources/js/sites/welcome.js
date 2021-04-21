let xhttp = new XMLHttpRequest();

//Loads all Cookies and returns Dictionary {Key:Val}

function createUserID32() {
    let v = ""
    for (let i = 0; i < 32; i++) {
        v = v + Math.floor(Math.random() * 9) + 1
    }
    console.log("Called")
    return v;
}
function checkIfUserIsVerified() {
    if (Cookies.get("ID_32") == null) {
        Cookies.set("ID_32", createUserID32())
    }
    xhttp.open("GET", "http://localhost:6969/loginNeeded?ID_32=" + Cookies.get("ID_32"), true)
    xhttp.send()
}
//TODO: Fix other Links
//Change HTML Content
xhttp.onreadystatechange = function () {
    console.log(xhttp.readyState)
    console.log(xhttp.status)
    console.log(xhttp.response)
    if (xhttp.readyState === 4) {
        if (xhttp.status === 200) {
            window.open(window.location.origin + "/Website-Katalog/Main/html/list.html","_self")
        }
        else if (xhttp.status === 201){
            window.open("authenticate.html", "_self")
        }
    }
}


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
    for (let i = 0; i < 6; i++) {
        document.getElementById("num" + i).setAttribute("readonly", "readonly")
    }
    console.log("Not implemented yet.")
}