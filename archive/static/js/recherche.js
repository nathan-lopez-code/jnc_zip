function filterTable(inputId, tableId) {
    const input = document.getElementById(inputId);
    const filter = input.value.toLowerCase();
    const table = document.getElementById(tableId);
    const trs = table.getElementsByTagName("tr");

    for (let i = 0; i < trs.length; i++) {
        let tds = trs[i].getElementsByTagName("td");
        let showRow = false;
        for (let j = 0; j < tds.length; j++) {
            if (tds[j]) {
                if (tds[j].textContent.toLowerCase().indexOf(filter) > -1) {
                    showRow = true;
                    break;
                }
            }
        }
        trs[i].style.display = showRow ? "" : "none";
    }
}

// Event listeners for search inputs
document.getElementById("searchOldBuildings").addEventListener("keyup", function() {
    filterTable("searchOldBuildings", "oldBuildingsTable");
});

document.getElementById("searchNewBuildings").addEventListener("keyup", function() {
    filterTable("searchNewBuildings", "newBuildingsTable");
});