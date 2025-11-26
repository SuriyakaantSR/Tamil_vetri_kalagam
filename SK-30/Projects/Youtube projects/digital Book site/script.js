// Selecting the popup elements
var popupoverlay = document.querySelector(".popup-overlay");
var popupbox = document.querySelector(".popup-box");
var addpopuptoogle = document.getElementById("add-popup-button");

// Event Listener to open the popup when '+' button is clicked
addpopuptoogle.addEventListener("click", function() {
    popupoverlay.style.display = "block";
    popupbox.style.display = "block";
});

// Selecting the Cancel Button
var cancelpopup = document.getElementById("cancel-popup");

// Event Listener to close the popup when CANCEL is clicked
cancelpopup.addEventListener("click", function(event) {
    event.preventDefault(); 
    popupoverlay.style.display = "none";
    popupbox.style.display = "none";
});

// Selecting container and input fields
var container = document.querySelector(".container");
var addbook = document.getElementById("add-book");
var booktitleinput = document.getElementById("book-title-input");
var bookauthorinput = document.getElementById("book-author-input");
var bookdescriptioninput = document.getElementById("book-description-input");

// Add new book when ADD is clicked
addbook.addEventListener("click", function(event) {
    event.preventDefault();

    // Basic validation
    if (booktitleinput.value.trim() === "" || bookauthorinput.value.trim() === "") {
        alert("Please fill out both the title and author fields.");
        return;
    }

    var div = document.createElement("div");
    div.setAttribute("class", "book-container");

    div.innerHTML = `
        <h2>${booktitleinput.value}</h2>
        <h5>${bookauthorinput.value}</h5>
        <p>${bookdescriptioninput.value}</p>
        <button onclick="deletebook(event)">Delete</button>
    `;

    container.append(div);

    // Close popup and clear input fields
    popupoverlay.style.display = "none";
    popupbox.style.display = "none";
    booktitleinput.value = "";
    bookauthorinput.value = "";
    bookdescriptioninput.value = "";
});

// Function to delete a book
function deletebook(event) {
    event.target.parentElement.remove();
}
