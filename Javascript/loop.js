var i = 1;

while (i <= 5) {
    document.write("<br>The value of i is: " + i);
    i++;
}

document.write("<br>Out of the loop")

i = 1
do {
    document.write("<br>The value of i is: " + i)
    i++
} while (i <= 5);

document.write("<br> the loop ends here<br> ")

i = 1;
var sum = 0;
var product = 1;

while (i <= 10) {
    sum += i;
    product *= i;
    i++
}

document.write(sum + "<br>");
document.write(product + "<br>");

for (i = 1; i < 6; i++) {
    document.write(i + "<br>");
}

let name = "Hello World!";
let len = name.length;

for (i = 0; i < len; i++) {
    document.write('<br>Index: ' + i + '<br>');
    document.write(name[i]);
}

let food = ["cake", "chocolate", "ice cream"];

for (i = 0; i < food.length; i++) {
    document.write('<br>Index: ' + i + '<br>')
    document.write(food[i]);
}

let person = {
    nam: "Tamim Iqbal",
    profession: "Cricketer",
    team: "Bangladesh",
    age: 33,
}

for (var y in name) {
    document.write('<br>' + y)
}

for (var y of name) {
    document.write('<br>' + y)
}

for (var y in person) {
    document.write('<br>' + y);
    document.write('<br>' + person[y])
}