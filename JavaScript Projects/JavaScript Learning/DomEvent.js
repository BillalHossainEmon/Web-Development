const input = document.querySelector("input[name=name]");
input.addEventListener("change", changeHandler);

function changeHandler(e) {
    console.log("changed");
    console.log(e.type);
    console.log(e.target.class);
    console.log(e.target.id);
    console.log(e.target.value);

}

const varName = document.querySelectorAll("input[name=program]");