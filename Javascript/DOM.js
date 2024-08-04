// document.getElementById()
let val;

//Getting an element
val = document.getElementById('document-title');
val = document.getElementById('document-title').className;

//Changing Style

document.getElementById('document-title').style.background = '#333';
document.getElementById('document-title').style.color = '#fff';
document.getElementById('document-title').style.padding = '10px';
document.getElementById('document-title').style.display = 'block';

//Changing Content
document.getElementById('document-title').textContent = 'New Title';
document.getElementById('document-title').innerText = 'Again New Title';
document.getElementById('document-title').innerHTML = "<i>Again again new title</i>"

//If we want to do it in a simpler way
val = document.getElementById('document-title');
val.innerText = "Ha Ha Ha";

//Query Selector

val = document.querySelector('#document-title'); //using id 
val = document.querySelector('.title-class'); //using class
val = document.querySelector('h3'); //using tag

val = document.querySelector('ol');

val = document.querySelector('li');

val = document.querySelector('ol li'); //Inheritence/Parent to child selecting

val.style.background = 'red';
val.style.color = 'white';

val = document.querySelector('li:last-child'); //Calling the last child

val = document.querySelector('li:nth-child(2)');

//Multiselector

let list = document.getElementsByClassName('sample-class');
list[0].style.background = 'red';
list[0].style.color = 'white';
list[0].style.padding = '10px';
list[0].textContent = 'Hello World!';

//document.getElementByTagNAme()

list = document.getElementsByTagName('li'); //will select all the elements of li tag

list = document.querySelector('ol').getElementsByTagName('li'); // will select just the elements of li tag of the ol list

let lis = Array.from(list);
lis.forEach(function(item) {
    //console.log(item);
});

// document.querySelectorAll()
// id -> #
// classname -> .
// tagname -> nothing

list = document.querySelectorAll('ol li');

//console.log(list);

list = document.querySelectorAll('ol li');
list.forEach(function(item) {
    //    console.log(item);
});

let liOdd = document.querySelectorAll('li:nth-child(odd)');
let liEve = document.querySelectorAll('li:nth-child(even)');

liOdd.forEach(function(item) {
    item.style.background = 'grey';
    item.style.color = 'white';
});

liEve.forEach(function(item) {
    item.style.background = 'red';
    item.style.color = 'white';
});


//console.log(list);

// Traversing the DOM

list = document.querySelector('ul');
let listItem = document.querySelector('ul li:first-child');


val = list;
val = listItem;

// Get Child Nodes
val = list;
val = list.childNodes;
val = list.childNodes[0];
val = list.childNodes[1];
val = list.childNodes[2];
val = list.childNodes[1].nodeName;
val = list.childNodes[0].nodeType;

// 1 Element
// 2 Attribute
// 3 Text Node
// 8 Comment
// 9 Document Itself
// 10 Doctype
val = list.childNodes;

val = list.children;
val = list.children[1];
list.children[0].textContent = "Hello";
val = list.children[1].children[0];
val = list.children[1].children[0].href;

val = list.firstChild;
val = list.firstElementChild;
val = list.lastChild;
val = list.lastElementChild;

val = list.childElementCount;

val = listItem;
val = listItem.parentElement;
val = listItem.parentNode;
val = listItem.parentElement.parentElement;

val = listItem.nextSibling.nextSibling;
val = listItem.nextElementSibling;
val = listItem.nextElementSibling.nextElementSibling;

val = document.querySelector('ul li:last-child');
val = val.previousSibling;
val = val.previousElementSibling;

//console.log(val);

//Adding element to DOM
//Create element

let olItem = document.createElement('li');

//Add id and class
olItem.className = 'A new another-class';
olItem.id = 'new-element';
//Add Attribute

olItem.setAttribute('title', 'A title to new Element');

olItem.appendChild(document.createTextNode('Javascript'));
document.querySelector('ol').appendChild(olItem);

//Addin elemnt in ul

let ulItem = document.createElement('li');
let link = document.createElement('a');

link.appendChild(document.createTextNode('Instagram'));
link.setAttribute('href', 'https://www.instagram.com');

ulItem.appendChild(link);

document.querySelector('ul').appendChild(ulItem);

console.log(ulItem);