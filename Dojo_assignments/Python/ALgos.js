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