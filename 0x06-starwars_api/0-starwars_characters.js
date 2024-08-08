const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error('Error:', err);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
