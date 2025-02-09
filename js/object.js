---
//Object
const product = {
    name: "Tablet",
    price: 300,
    available: false
}

console.log(product)
console.table(product)
console.log(typeof product)
console.log(product.name)
console.log(product.price)
console.log(product.available)
--- 
//Destructuring
const {name, price} = producto
console.log(name, price)
--- 
//Asignation
const name = "Justin"
const age = 12

const pets = {
  name,
  age,
  fullInformation(){
    return  `${this.name} ${this.age}`
  }
}

console.log(pets.fullInformation())
---
//Modification
pets.image = 'image.jpg'
console.log(pets)
---
//Remove
delete pets.image
console.log(pets)
// set
pets.name = "Violeta"
console.log(pets)




// utils
Object.freeze(pets) //No permite modificar el objeto
Object.seal(pets) //Permite modificar las propiedades existentes, pero no eliminar o agregar nuevas propiedades
console.log(pets)


//merge two objects
// Destructuring of two or more objects

const product = {
    name: 'PC',
    price: 300,
    availability: false
}

const customers = {
    name: 'Juan',
    premium: true,
    address: {
        street: "Calle 4"
    }
}

const {name} = product
const {name: nameCustomers, address: {street}} = customers //Rename variable

console.log(name)
console.log(nameCustomers)
console.log(street)


// Merge of two or more objects

const product = {
    name: 'PC',
    price: 300,
    availability: false
}

const customers = {
    name: 'Juan',
    premium: true,
    address: {
        street: "Calle 4"
    }
}

const carrito = {
    count: 1,
    ...product
}

//console.log(carrito)

const newObject = {
    producto: {...product},
    cliente: {...carrito}
}

//console.log(newObject)


const newObject2 = {
    ...product,
    ...customers

}

//console.log(newObject2)

const newObject3 = Object.assign(product, customers)
console.log(newObject3)
