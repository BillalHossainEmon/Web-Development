class Person {
    constructor(fname, lname) {
        this.firstname = fname;
        this.lastname = lname;
    }

    greeting() {
        return `Hello ${this.firstname} ${this.lastname}!`;
    }
}

class Customer extends Person {
    constructor(fname, lname, phone, membership) {
        super(fname, lname);
        this.phone = phone;
        this.membership = membership;
    }

    fullname() {
        return `${this.firstname} ${this.lastname}`;
    }
}

let Person1 = new Person("Emon", "Chowdhury");

//document.write(Person1);
document.write(Person1.greeting() + '<br>');

let Customer1 = new Customer("Rukaiya", "Shupti", 123, 789);
document.write(Customer1.greeting() + '<br>');
document.write(Customer1.fullname() + '<br>');