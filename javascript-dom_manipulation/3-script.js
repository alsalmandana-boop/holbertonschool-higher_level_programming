
const header = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');

toggleHeader.addEventListener('click', function () {
  if (header.classList.contains('green')) {
    header.classList.replace('green', 'red');
  } else {
    header.classList.replace('red', 'green');
  }
});

