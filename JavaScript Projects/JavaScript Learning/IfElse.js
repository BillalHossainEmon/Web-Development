var num1 = parseFloat(prompt("Enter a number : "));
var num2 = parseFloat(prompt("Enter another number : "));

if (num1 > num2)
    document.write("First number is greater than the second number");

else if (num2 > num1)
    document.write("Second number is greater than the first number");

else
    document.write("Both numbers are equal");