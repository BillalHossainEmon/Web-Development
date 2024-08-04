var foods = ["Cake", "Ice Cream", "Chocolates", "Bread"];
var numbers = [1, 32, 31, 2];

foods.forEach(function(item, i, array) {
    document.write(`Index: ${i} and Item ${item}<br>`)
    document.write(array);
})

let printEverything = function(item, i, array) {
    document.write(`Index: ${i} and Item ${item}<br>`)
    document.write(array);
}

foods.forEach(printEverything);

//mapping

function addArray(item) {
    return (item ** 2);
}

let arrSquare = numbers.map(addArray);

document.write(arrSquare);