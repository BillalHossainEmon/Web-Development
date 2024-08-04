var marks = prompt("Enter your marks: ");
marks = parseInt(marks);

var grade;

if (marks <= 100 && marks >= 80) {
    grade = "A+";
} else if (marks < 80 && marks >= 70) {
    grade = "A";
} else if (marks < 70 && marks >= 60) {
    grade = "A-";
} else if (marks < 60 && marks >= 50) {
    grade = "B";
} else if (marks < 50 && marks > 40) {
    grade = "C";
} else if (marks < 40 && marks >= 30) {
    grade = "D";
} else if (marks < 30 && marks >= 0) {
    grade = "F";
} else {
    document.write('Invalid Input! ');
}

document.write("Your Grade is " + grade);