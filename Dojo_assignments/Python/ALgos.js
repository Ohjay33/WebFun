// Sorting functions//

function selectionSort(arr) {

  for(var i=0; i < arr.length; i++){
    var temp = arr[0]
    var tempIndex = 0;
    for(var j=0; j < arr.length - i; j++){
      if(arr[j] > temp){
        temp = arr[j]
        tempIndex = j

      }
    }
    var tempVar = arr[arr.length - i - 1];
    arr[arr.length - i - 1] = temp
    arr[tempIndex] = tempVar
  }
  return arr;
}


function selectionSort(arr){
  for(var i = arr.length-1; i >= 0; i--){
      let max = i
      for(var j = 0; j< i;j++){
          if(arr[j] > arr[max]) max = j
      }
      [arr[i], arr[max]]=[arr[max], arr[i]];
  }
  return arr




  Binary String Expansion
  You are given a STRING containing chars "0", "1", and "?"
  For every "?" character, either "0" or "1" can be substituted.
  Write a recursive function to return array of all valid strings with "?" chars expanded to "0" or "1". 
*/

const str1 = "1?0?";
const expected1 = ["1000", "1001", "1100", "1101"];
// output list order does not matter
for( i=0; i<str1.length;i++)
/**
 * Add params if needed for recursion
 * Expands a string such that each "?" in the given string will be replaced
 * with a "0" and a "1".
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string containing to expand.
 * @returns {Array<string>} The expanded versions of the given string.
 */
function binaryStringExpansion(str) {}


function   Binary_String_Expansion(str1,expected1)
{
    let str1 = [];
    // Check if str.length() is 1
        if (str1.length == 1)
        {
            str1.push(str);
            return strs;
        }
  
        let str1Temp
            = spaceString(str.substring(1,
                             str.length));
  
        // Iterate over strsTemp
        for (let i = 0; i < strsTemp.length; i++)
        {
  
            strs.push(str[0] +
                            strsTemp[i]);
            strs.push(str[0] + " " +
                             strsTemp[i]);
        }
  
        // Return strs
        return strs;
}
 
// Driver Code
let patterns = spaceString("ABCD");
  
// Print patterns
for (let s of patterns.values())
{
    document.write(s+"<br>");
}