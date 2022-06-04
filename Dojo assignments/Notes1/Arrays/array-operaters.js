var usersFirstName = "Dwight";    
var usersLastName = "Schrute";    
var usersEmail = "beetsbears@battlestar.com";copy
Arrays
// Instead, we may want to use a data structure called an array:

var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];copy



var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];    
user.push("jello");    
console.log(user);    // ["Dwight", "Schrute", "beetsbears@battlestar.com", "jello"]copy


// To remove a value from the end, we use the pop method.  As a note, pop can only remove the end item from an array, we can't use it to remove a specified item nested within our array. While there are built-ins that can do it for us, we're going to start with just pop for now.

var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];    
user.pop();    
console.log(user);    // ["Dwight", "Schrute"]copy


// Arrays are indexed.  Meaning that every item in the array is in a indeed position, starting with 0. To access or update values in an array we access the name of the array (I.E. use in the example below) and the item we want from within it. (I.E. user[0] would be the first item in our array) 

var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];    
console.log(user[0]);    // reading the value -- OUTPUT: Dwight    
user[1] = "Martin";    // updating the value    
console.log(user);    // ["Dwight", "Martin", "beetsbears@battlestar.com"]copy


// Arrays also have a length property, which tells us how many values are contained in the array:

var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];    
console.log(user.length);    // 3    
user.pop();    
console.log(user.length);    // 2