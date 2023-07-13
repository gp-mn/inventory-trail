$("#inventorytable").append('<tr><th>Item Name</th><th>Availability</th><th>Location</th></tr>');

var lst = [[], ["Volleyball", "1/1", "Dartmouth Kao"], ["A2F Table Tennis", "2/4", "Dartmouth Lu"]];

function generateTable(){
    var table = document.getElementById("inventorytable");
    var numRows = lst.length;
    var numCols = 3;

    for (var i = 1; i < numRows; i++){
        let row = table.insertRow(i);
        for (var j = 0; j < numCols; j++){
            let obj = lst[i][j];
            let cell = row.insertCell(j);
            cell.innerHTML = obj;
        }
    }
}
window.onload = generateTable;