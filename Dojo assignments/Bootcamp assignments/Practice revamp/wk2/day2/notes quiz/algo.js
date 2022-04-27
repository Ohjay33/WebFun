Math.ceil(9.51)
Math.ceil(9.1)

Math.floor(8.45)
Math.floor(8.99)

//Generating a random number
for(var i =0;i<10;i++){

    var random = Math.floor(Math.random() * 10 + 1) ;
    console.log(random)

}

// Dice Roller
// Using what we've learned about the Math library in JavaScript, complete the following function that should return a value between 1 through 6 at random.

function d6() {
    
    var roll =Math.floor( Math.random() * 6 + 1):

    return roll
}
    
var playerRoll = d6();
console.log("The player rolled: " + playerRoll);


// Consult the Oracle
// Using the following array, write a function that will answer all of our questions by randomly choosing a response

var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    
];


function life (arr) {Life}
var roll =Math.floor( Math.random() * 6 + 1):


//PRactice2



var monster = {
    id: 1,
    name: "Bulbasaur",
    types: ["poison", "grass"]
};

console.log(monster.name)
console.log(monster.types[1])
var pokémon = [
    { "id": 1,   "name": "Bulbasaur",  "types": ["poison", "grass"] },
    { "id": 5,   "name": "Charmeleon", "types": ["fire"] },
    { "id": 9,   "name": "Blastoise",  "types": ["water"] },
    { "id": 12,  "name": "Butterfree", "types": ["bug", "flying"] },
    { "id": 16,  "name": "Pidgey",     "types": ["normal", "flying"] },
    { "id": 23,  "name": "Ekans",      "types": ["poison"] },
    { "id": 24,  "name": "Arbok",      "types": ["poison"] },
    { "id": 25,  "name": "Pikachu",    "types": ["electric"] },
    { "id": 37,  "name": "Vulpix",     "types": ["fire"] },
    { "id": 52,  "name": "Meowth",     "types": ["normal"] },
    { "id": 63,  "name": "Abra",       "types": ["psychic"] },
    { "id": 67,  "name": "Machamp",    "types": ["fighting"] },
    { "id": 72,  "name": "Tentacool",  "types": ["water", "poison"] },
    { "id": 74,  "name": "Geodude",    "types": ["rock", "ground"] },
    { "id": 87,  "name": "Dewgong",    "types": ["water", "ice"] },
    { "id": 98,  "name": "Krabby",     "types": ["water"] },
    { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
    { "id": 122, "name": "Mr. Mime",   "types": ["psychic"] },
    { "id": 133, "name": "Eevee",      "types": ["normal"] },
    { "id": 144, "name": "Articuno",   "types": ["ice", "flying"] },
    { "id": 145, "name": "Zapdos",     "types": ["electric", "flying"] },
    { "id": 146, "name": "Moltres",    "types": ["fire", "flying"] },
    { "id": 148, "name": "Dragonair",  "types": ["dragon"] }
];
function pokenames(pokémon){
    for(var i =0; i<pokémon.length; i++){
        if(pokémon[i].id > 99){
            console.log(pokémon[i].name)
        }
    }
}

// Challenges - using the array of pokémon above and loops:

// console.log the pokémon objects whose id is evenly divisible by 3
function div3(Pokemon){
    for(var i=0; i< Pokemon.length; i++)
    if(Pokemon)[i].id 3==0){
        console.log(pokemon[i])
    }
}

// console.log the pokémon objects that have more than one type
function moreThenOneType(Pokemon){
    for(var i=0; i<pokemon.lenght; i++){
        if(Pokemon[i].types.length >1){
            console.log(pokemon[i]);
        }
    }
}

// console.log the names of the pokémon whose only type is "poison"
function onlyPoison(pokemon){
    for(var i=0; i< pokemon.length; i++){
        if(pokemon[1].types.length < 2 pokemon[1].types =="poison"){
            // console.log(pokemon[1]);
            for (var) z=0;z<5; z++){
                
            }
        }
    }
}

// console.log the first type of all the pokémon whose second type is "flying"

// Bonus Challenge: console.log the reverse of the names of the pokémon whose only type is "poison"











var isSunny = false;
var isRaining = true;
    
if(isSunny) {
    console.log("Wear sunscreen");
}
    
if(isRaining) {
    console.log("Bring an umbrella");
}


