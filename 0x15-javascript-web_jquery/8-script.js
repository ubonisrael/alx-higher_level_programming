$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  // console.log(data);
  const movieTitles = data.results.map(movie => `<li>${movie.title}</li>`);
  // console.log(movie_titles);
  $('#list_movies').append(movieTitles.join(''));
});
