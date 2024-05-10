// console.log("Hello from file");


// const title = document.getElementById("myHeader")

// title.innerText = "another content"
// title.style = "background-color: red"

// title.innerHTML = "<button>Add new contact</button>"

// Write function to get two arguments your name 
// and age and should print to console “My name” + name + “, and my age:” + age.
// Call that function with your name and age
// Rewrite function to be arrow function.
// Call the second function.


// const myName = "Arja"



// function sayHello(name) {
//     console.log("How are you, " + name)
// }

// sayHello(myName)


// const arrowSayHello = (name) => {
//     console.log("How are you, " + name)
// }

// const myName = "Arja"
// const myAge = 15

// function printNameAndAge(param1, param2) {
//     // console.log("My name is" + param1 + "and my age is "+ param2);
//     console.log(`My name is ${param1} and my age is ${param2}`);
// }

// printNameAndAge(myName, myAge)


// const arrowPrintNameAndAge = (param1, param2) => {
//     console.log(`My name is ${param1} and my age is ${param2}`);
// }

// arrowPrintNameAndAge("Deynerrys", 19)


// Create page with “Hello world” in <h1> header.
// You can use id or class attribute.

// Add javascript and change text to your name and family name.
// Add background color of your choice using style.
// Mynode.style….


// let myNode = document.getElementById("myHeader")
// myNode.style.backgroundColor = "grey";
// myNode.innerText = "Jon Snow"


// let myNode3= document.getElementsByClassName("myClass")[0]
// // myNode3.style.backgroundColor = "blue";


// myNode3.style = "background-color: green; color: yellow;"


// for (let i=0 ; i<5; i++) {
//     document.body.appendChild(myNode3.cloneNode(true))
// }

// let newNode = document.createElement("p")
// newNode.style.color = "orange"
// newNode.innerText = "My new paragraph"

// document.body.appendChild(newNode)

const myP = document.getElementById("myParagraph");
myP.addEventListener("click", ()=> {
    myP.innerText = "oops"
    myP.style.fontWeight = "bold"
    myP.style.color
}
)