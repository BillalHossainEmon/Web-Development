var num1 = prompt("Enter the first number: ");

num1 = parseInt(num1);

var num2 = prompt("Enter the second number:");

num2 = parseInt(num2);

option = prompt(`Select an option:
1. Add 
2.Subtract 
3.Multiply
4.Divide`)

option = parseInt(option);

var result = null;

switch (option) {
    case 1:
        result = num1 + num2;
        break;

    case 2:
        result = num1 - num2;
        break;

    case 3:
        result = num1 * num2;
        break;

    case 4:
        result = num1 / num2;
        break;
    default:
        break;
}

document.write("The result is " + result);