document.addEventListener('DOMContentLoaded', () => {
  const helloElement = document.querySelector('#hello');
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      helloElement.textContent = data.hello;
    })
    .catch((error) => {
      console.error('Erreur lors de la récupération :', error);
    });
});
