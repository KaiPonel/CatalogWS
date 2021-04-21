TYPE_VARCHAR = "varchar"
TYPE_NUM = "int"
TYPE_DATE = "date"
TYPE_BOOL = "bool"

//Items = Dictionary
items = [];
itemFromDBRequest = new XMLHttpRequest();

function loadItems() {
    //TODO Load Items from Server (Currently Test Items)
    /*let testProperty = []
    testProperty.push(new property("unbekannt", TYPE_VARCHAR, "null", true))
    for (let i = 0; i < 1; i++) {
        items.push({"id": 1234, "item": new item("1234", "default.png", testProperty)})
        items.push({"id": 12345, "item": new item("1234", "default.png", testProperty)})
    }*/
    itemFromDBRequest.open("POST", "http://localhost:6969/getItemsFromDB?ID_32=" + Cookies.get("ID_32") + "?limit=-1")
    itemFromDBRequest.send();
}
itemFromDBRequest.onreadystatechange = function(){
    if(codeRequest.status === 200){

    }
}






class item {
    itemID
    changeableProperties = [property]
    imgLink = ""

    constructor(itemID, imgLink, properties) {
        this.itemID = itemID;
        this.imgLink = imgLink;
        this.changeableProperties = properties;
    }
}

class property {
    name = "unbenannt";
    type = TYPE_VARCHAR;
    value = "";
    isSearchable = false;

    constructor(name, type, value, isSearchable) {
        this.name = name;
        this.type = type;
        this.value = value;
        this.isSearchable = isSearchable;
    }
}

function printItems() {
    let section = document.getElementById("ItemSection");
    let tmp = "<div class=\"row h-25 align-items-center\">"
    console.log(section)

    //Loop for all items
    for (let i = 0; i < items.length; i++) {
        //Every 6 Items -> New Row
        if (i % 6 === 0 && i !== 0) {
            tmp = tmp + "</div><div class=\"row h-25 align-items-center\">"
        }
        let itemURL = items[i].imgLink;
        tmp = tmp + "<div class=\"col-sm-2 text-center h-100\" style=\"background-image: url(" + itemURL + ") \"></div>"
    }
    section.innerHTML = tmp;

}
//Unneeded?
window.onload = function () {
    //printItems()
}
//Unneeded?
function printItemInformation(itemID) {
    let htmlSection = document.getElementById(itemID);
    let item = null;
    /*let item = items.filter(obj => {
        return obj.itemID === itemID;
        }
    )*/
    for (let i = 0; i < items.length; i++) {
        if (items[i].itemID === itemID) {
            item = items[i];
            break;
        }
    }
    if (item !== null) {
        let name = ""
        for (let i = 0; i < item.changeableProperties.length; i++) {
            if (item.changeableProperties[i].name === "name") {
                name = item.changeableProperties[i].value;
            }
        }
        console.log(name)
        htmlSection.innerHTML = htmlSection.innerHTML + " <h3>" + name + "</h3>"
    }
}


function setItemTarget(itemID) {
    sessionStorage.setItem("ViewItem", itemID)
}

function addRow(tableSection, propName, propValue) {
    let str = "<tr> <th scope='row'>" + propName + "</th><td>" + propValue + "</td></tr>"
    tableSection.innerHTML = tableSection.innerHTML + str;
}
//viewItem.html
function printContentToViewPage(){
    let itemID = sessionStorage.getItem("ViewItem");
    let tableSection = document.getElementById("tableContent")
    let item = undefined;
    for(let i = 0; i<items.length; i++){
        if(items[i].id.toString() === itemID.toString()){
            item = items[i]
        }
    }


    if (item !== undefined){ //TODO: Error Case?
        console.log(items)
        for(let i = 0; i<item.item.changeableProperties.length; i++){
            console.log(item.item.changeableProperties[i].name)
            console.log(item.item.changeableProperties[i].value)
            addRow(tableSection, item.item.changeableProperties[i].name, item.item.changeableProperties[i].value)
        }
    }
}