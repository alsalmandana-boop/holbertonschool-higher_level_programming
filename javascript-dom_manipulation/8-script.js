
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to fetch translation');
      }
      return response.json();
    })
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});

