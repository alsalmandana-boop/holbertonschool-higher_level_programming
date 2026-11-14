
const character = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Failed to fetch character');
    }
    return response.json();
  })
  .then(data => {
    character.textContent = data.name;
  })
  .catch(error => {
    console.error('Error:', error);
  });

