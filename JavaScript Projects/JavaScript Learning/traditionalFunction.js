//creating a function 

function square(num) {
    var result = num * num;
    document.write("Result = " + result + "<br>");
}

function multiply(num1, num2) {
    var result = num1 * num2;
    document.write("Result = " + result + "<br>");
}

function squareReturn(num) {
    var result = num * num;
    return result;
}

function multiplyReturn(num1, num2) {
    var result = num1 * num2;
    return result;
}


square(5);
square(6);
square(7);
multiply(5, 6);
document.write(squareReturn(2) + "<br>");
var x = multiplyReturn(10, 2);
document.write(x);