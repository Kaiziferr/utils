const producto = {
    name: "Fruit",
    price: 500,
    disponibilidad: false
}

console.log(typeof producto)
console.table(producto)
console.log(producto.name)
console.log(producto.price)
console.log(producto.disponibilidad)

//Destructuring

const {name, price} = producto
console.log(name, price)

const pets = {
    name: "Justin",
    lastname: "Tovar",
    age: 7
}

//Object.freeze(pets) //No permite modificar el objeto
Object.seal(pets) //Permite modificarlo, pero no eliminar o agregar new properties
console.log(pets)

// set
pets.name = "Violeta"
console.log(pets)
pets.image = "violeta.jpg"
console.log(pets)

//Delete



delete pets.lastname

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
