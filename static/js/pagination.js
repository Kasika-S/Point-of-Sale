var table = document.getElementById('myTable');
var itemsPerPage = 5; // Number of rows to display per page
var currentPage = 1;

function displayPage(page) {
    var rows = table.rows;
    var start = (page - 1) * itemsPerPage;
    var end = start + itemsPerPage;

    for (var i = 1; i < rows.length; i++) {
        if (i > start && i <= end) {
            rows[i].style.display = '';
        } else {
            rows[i].style.display = 'none';
        }
    }
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        displayPage(currentPage);
    }
}

function nextPage() {
    if (currentPage < Math.ceil((table.rows.length - 1) / itemsPerPage)) {
        currentPage++;
        displayPage(currentPage);
    }
}

// Initial page display
displayPage(currentPage);
