# JavaScript - DOM Manipulation

## Description

This project is part of the Holberton School Higher Level Programming curriculum.

The goal of this project is to learn how to use JavaScript to interact with and modify HTML elements through the Document Object Model (DOM).

The project covers selecting HTML elements, handling user events, modifying styles and content, creating new elements, and fetching data from external APIs.

## Learning Objectives

By the end of this project, I will be able to:

- Understand the Document Object Model (DOM).
- Select HTML elements using `document.querySelector()`.
- Modify element styles and CSS classes.
- Handle user interactions using event listeners.
- Create and append new HTML elements.
- Update HTML content dynamically.
- Fetch data from external APIs using the Fetch API.
- Work with JSON responses and Promises.
- Use `DOMContentLoaded` to ensure HTML elements are available before accessing them.

## Project Tasks

| Task | File | Description |
|---|---|---|
| 0. Color Me | `0-script.js` | Change the header text color to red. |
| 1. Click and Turn Red | `1-script.js` | Change the header text color when an element is clicked. |
| 2. Add `.red` Class | `2-script.js` | Add a CSS class to the header when clicked. |
| 3. Toggle Classes | `3-script.js` | Toggle the header between red and green classes. |
| 4. List of Elements | `4-script.js` | Add new list items dynamically when clicked. |
| 5. Change the Text | `5-script.js` | Update the header text when clicked. |
| 6. Star Wars Character | `6-script.js` | Fetch and display a Star Wars character's name. |
| 7. Star Wars Movies | `7-script.js` | Fetch and display a list of Star Wars movie titles. |
| 8. Say Hello! | `8-script.js` | Fetch and display the French translation of "hello". |

## Technologies Used

- JavaScript
- HTML5
- CSS3
- DOM API
- Fetch API
- JSON

## Project Structure

```text
javascript-dom_manipulation/
├── README.md
├── 0-script.js
├── 1-script.js
├── 2-script.js
├── 3-script.js
├── 4-script.js
├── 5-script.js
├── 6-script.js
├── 7-script.js
└── 8-script.js
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/alsalmandana-boop/holbertonschool-higher_level_programming.git
```

2. Navigate to the project directory:

```bash
cd holbertonschool-higher_level_programming/javascript-dom_manipulation
```

3. Create or open the corresponding HTML test file and include the JavaScript file:

```html
<script src="0-script.js"></script>
```

4. Open the HTML file in a web browser.

For tasks that fetch data from external APIs, you can start a local server:

```bash
python3 -m http.server 8000
```

Then open the corresponding HTML page at `http://localhost:8000/`.

## Key Concepts

**DOM Manipulation:** Accessing and modifying HTML elements using JavaScript.

**Event Listeners:** Responding to user actions such as mouse clicks.

**CSS Class Manipulation:** Adding, removing, or replacing CSS classes dynamically.

**Fetch API:** Retrieving data from external web services.

**Promises:** Handling asynchronous operations and API responses.

**DOMContentLoaded:** Waiting until the HTML document has been parsed before accessing its elements.

## Author

**Dana Ibrahim Alsalman**

Holberton School Student

## Repository

[holbertonschool-higher_level_programming](https://github.com/alsalmandana-boop/holbertonschool-higher_level_programming)
