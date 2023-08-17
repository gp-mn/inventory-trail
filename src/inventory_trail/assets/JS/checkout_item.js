$("#checkouttable").append('<tr><th>Item Name</th><th>Availability</th><th>Location</th></tr>');

function generateTable(){
    var table = document.getElementById("checkouttable");
    var numCols = 3;
    console.log(jsonData.length);
    for (let j = 0; j < jsonData.length; j++){
        let row = table.insertRow(j + 1);
        for (let i = 0; i < numCols; i++){
            let cell = row.insertCell(i);
            let obj = jsonData[j];
            if (i == 0){
                cell.innerHTML = obj.name;
            }
            if (i == 1){
                if (obj.item_count == 0){
                    obj = "Check Out";
                }
                else if (obj.item_count > 0 && obj.item_count < obj.num_items){
                    obj = "Check out or check in";
                }
                else{
                    obj = "Check In";
                }
            }
            if (i == 2){
                cell.innerHTML = obj.location;
            }
        }
    }
}
window.onload = generateTable;