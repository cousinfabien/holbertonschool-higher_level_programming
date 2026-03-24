const listMoviesElement = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    const movies = data.results;
    movies.forEach((movie) => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error('Erreur lors de la récupération des films :', error);
  });
  