let person = {
    firstname: "Emon",
    lastname: "Chowdhury",
    dob: "23-12-1997",

    fullname() {
        return (`${this.firstname} ${this.lastname}`);
    }

}

document.write(person.fullname());