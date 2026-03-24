const listMovies = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    const movies = data.results;
    movies.forEach((movie) => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.appendChild(li);
    });
  })
  .catch((error) => {
    console.error('Erreur lors de la récupération des films :', error);
  });