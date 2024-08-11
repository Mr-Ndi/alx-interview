#!/usr/bin/node
const request = require('request');

async function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      resolve(body);
    });
  });
}

async function getStarWarsCharacters(movieId) {
  try {
    const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    const filmData = await makeRequest(filmUrl);
    const characterUrls = filmData.characters;

    for (const url of characterUrls) {
      const characterData = await makeRequest(url);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

const movieId = process.argv[2];
if (movieId) {
  getStarWarsCharacters(movieId);
} else {
  console.error('Please provide a Movie ID as an argument.');
}
