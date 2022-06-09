// Const = Substitute for variable "cannot be changed"
// Let = Subtitute for Variable. "can be changed"




// Countdown by Fours
// Print positive numbers starting with 2020, counting down by fours (excluding 0)
//     Challenge:Do this with a FOR loop first and then do it using a WHILE loop afterwards

//for(var i=2020; i>=1; i-=4){
//console.log(i)}


// var i = 2020;
//while(i >=1){
// console.log(i);
// i-=4;}


// function Greeting(Wave){
//     console.log(Wave)
// }

//<--
// function example(element){
//     console.log("element clicked", element);
// }

// <---Switch element back and forth ["on/off", "renaming"] -->



// function turnoff(element) {
//     element.innerText = "dislike"
// }



// <--hide or remove elements-->
// function hide(element){
//     element.remove();
// }



//// <--Functions for hovering over and out.["changing colores when hovered",]-->//
// <-- HTML EXample-- [<div class="block" onmouseover="over(this)" onmouseout="out(this)"></div>] -->//

// function over(element) {
//     alert("mouseover");    
// }

// function out(element) {
//     alert("mouseout");    
// }




// // --Hover to change color function--//
// function over(element) {
//     element.style.backgroundColor = "lime";    
// }

// function out(element) {
//     element.style.backgroundColor = "silver";   
// }



// increment counter function increase or decrease every click!//
// --HTML EXAMPLE!--//

// { <form>
//      <input type="text" id="number" value="0"/>
//      <input type="button" onclick="incrementValue()" value="Increase" />
//  </form> }


// --increment numbers--/every click adds 1--//
// var counter = 0;
// function increment(){
//     counter++;
//     console.log(counter);
// }

// function incrementValue()
//     {
//         var value = parseInt(document.getElementById('number').value, 10);
//         value = isNaN(value) ? 0 : value;
//         value++;
//         document.getElementById('number').value = value;
//     }


// --counting numbers 1-10 function "print numbers 1-10"--//

// function counter(){
//    for(var num = 0; num <=10; num++){
//       console.log(num);
//    }
// }

// --calling the function--//
// counter()


// ---> counting numbers from 50 to 1 function <--//

// function counter(startNum){
//    for(var num = startNum; num >= 0 ; num--){
//       console.log(num)
//    }
// }
// counter(50)


// --->Creating a array <---//

// function createArray(num) {
//    var newArray = [];
//    for (var i = 0; i <= num; i++) {
//       newArray.push(i);
//    }
//    return newArray;        // added the return statement//
// }
// var y = createArray(5);        // now y is the variable that is calling on createArray



// ------alerting input value in search bar-----//
// function getInputValue(){
//     var inputVal = document.getElementById("myInput").value;
//     alert(inputVal);
// }
// ---------HTML input--------
{/* <input type="text" placeholder="Type something..." id="myInput">
    <button type="button" onclick="getInputValue();">Get Value</button> */}


//     function changeImg() {
//         var image = document.getElementById('myImg');
//         if (image.src.match("img/more.jpg")) {
//             image.src = "img/less.jpg";
//         }
//         else {
//             image.src = "img/more.jpg";
//         }
//     }

// //-------HTML example----------//
    
//     <img src="img/more.jpg" id="myImg" width="40" height="40">
// <input type="button" onclick="changeImg()" value="Change" />


// -------Generate random Numbers---------//
// function alertRandom() {
//     var randomNumber = Math.floor(Math.random()* 6) + 1;
//     alert(randomNumber);
//     }

// for(let i=0; i < 120; i++)
// console.log(i)

