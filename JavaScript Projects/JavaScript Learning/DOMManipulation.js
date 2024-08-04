//creating html element
var heading3 = document.createElement("h1");
var text = document.createTextNode("This is heading 3");
heading3.appendChild(text);

var myDiv = document.getElementById("my-div");
myDiv.appendChild(heading3);

var heading2 = document.getElementsByTagName("h1")[1];
myDiv.removeChild(heading2);

var heading4 = document.createElement("h1");
var text1 = document.createTextNode("This heading is created above");
heading4.appendChild(text1);
var heading1 = document.getElementsByTagName("h1")[0];
myDiv.insertBefore(heading4, heading1);