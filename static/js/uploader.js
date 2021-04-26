// JAVASCRIPT HANDLING OF THE UPLOAD BOX ON THE INDEX PAGE


// Function to enable bootstrap tooltips
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

// Function to update the file uploader with the file name and then to reveal the submit button.
$(".custom-file-input").on("change", function () {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);

    // Reveal the submit button
    var x = document.getElementById("submit");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
});



