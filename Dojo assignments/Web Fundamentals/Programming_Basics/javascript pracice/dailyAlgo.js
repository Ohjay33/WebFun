// WARM UP: Write some code that loops through an array and prints the values out.
// EX: given var arr = [1,5,8,2,6], your console should print out:
// 1
// 5
// 8
// 2
// 6



// //var arr = [1,5,8,2,6];
// //for(var i = 0; i < arr.length; i++ ){
//     console.log(arr[i])
// }




// Values greater than second
// Given an array, write a function that returns the number of values in the array that are larger than the second value in the array.

//var a = [1, 5, 8, 2, 6];
//var sum = 0
//for (var i = 0; i < a.length; i++) {
    //if (a[i] > a[1]){
      //  sum = sum + 1
  //  } 
//}
//console.log(sum)

var a = [1,5,8,2,6];
let x = 0
function ax(){
    for(var i = 0; i < a.length; i++  ){
        if(a[i] > a[1]){
            x= x + 1
        }
        }
        console.log(x)
}
ax()



// EX: given an array [2,5,19,3,10,9], your second value is 5 and the number of values greater than 5 in the array is 3

var arr = [2,5,19,3,10,9];
for(var i=0; i< arr.length; i++){

function answer (){
    for ( var i=0; i< Array.length; i++)
}


// EX: given an array [4,3,10,1,6,9,2], your second value is 3 and the number of values greater than 3 in the array is 4

// Bonus: add a feature that makes sure the array is large enough before running
// EX: if your array only has [2]...we don't have enough values -- in this situation return "Not enough values"


function countInRange(arr, 4,3,10,1,6,9,2)
    {
           
    
        let count = 0;
        for (let i = 0; i < n; i++) {
       
            if (arr[i] >= x && arr[i] <= y)
                count++;
        }
        return count;
    }
