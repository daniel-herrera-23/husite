// JavaScript code for navigation pane functionality

// Attach click event listener to the parent container (.left-nav)
const leftNavContainer = document.querySelector('.left-nav');
leftNavContainer.addEventListener('click', toggleSubMenu);

// Toggle display of sub-menu when a menu item is clicked
function toggleSubMenu(event) {
    const target = event.target;

    // Check if the clicked element is an <a> tag
    if (target.tagName === 'A') {
        event.preventDefault();
        
        // Check if the clicked element has a sub-menu
        const subMenu = target.nextElementSibling;
        if (subMenu && subMenu.tagName === 'UL') {
            subMenu.classList.toggle('show');
        }
    }
}
