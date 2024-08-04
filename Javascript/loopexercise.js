document.write("This program will write the square of all the numbers till the input number and sum of those square values.<br>")
var x = parseInt(prompt("Enter a number: "));
var square = 0;
var sum = 0;
var series = "";

for (i = 1; i <= x; i++) {
    square = i ** 2;
    sum += square;
    series += square.toString();
    if (i == x) continue;
    series += " + ";
    //document.write(square + '<br>');
    //document.write(series + '<br>');
}

document.write(series + '<br>');

document.write(sum + '<br>');