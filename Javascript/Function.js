// Basic Function

function basicFunction() {
    document.write("Hello World!<br>");
}

basicFunction();

//Parameter Function

function parameterCall(para1) {
    document.write(`Hello ${para1}!<br>`);
}

parameterCall("Emon");

function doubleParameter(param1, param2) {
    document.write(`Hello ${param1} ${param2}!<br>`);
}

let firstName = 'Emon';
let lastName = 'Chowdhury';
doubleParameter(firstName, lastName);

function sum(num1, num2) {
    document.write(`${num1} + ${num2} = ${num1 + num2}<br>`);
}

sum(2, 5);

function product(n1, n2) {
    return n1 * n2;
}

document.write("The product of 2 and 5 is: " + product(2, 5));

//Function Expression

let saySomething = function() {
    document.write("<br>Hello Again!<br>");
}

saySomething();

let saySomething1 = function(name) {
    document.write(`Hello ${name}!`);
}

saySomething1('Emon')

//Arrow Function

let saySomething2 = () => {
    document.write("<br>I am an Arrow Function<br>");
}

saySomething2();

let saySomething3 = (name) => {
    document.write(`Hello ${name}<br>`);
}

saySomething3('Emon');