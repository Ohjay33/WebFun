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
var counter = 0;
    function increment(){
        counter++;
        console.log(counter);
    }

// function incrementValue()
//     {
//         var value = parseInt(document.getElementById('number').value, 10);
//         value = isNaN(value) ? 0 : value;
//         value++;
//         document.getElementById('number').value = value;
//     }





