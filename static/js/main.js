// Custom project-wide JavaScript can be added here.

// Example: Sidebar toggle functionality
document.addEventListener("DOMContentLoaded", function() {
    const sidebarToggle = document.body.querySelector("#sidebarToggle");
    if (sidebarToggle) {
        sidebarToggle.addEventListener("click", function(event) {
            event.preventDefault();
            // A simple toggle might need more work (e.g., toggling a class on the body)
            console.log("Sidebar toggle clicked");
        });
    }
});