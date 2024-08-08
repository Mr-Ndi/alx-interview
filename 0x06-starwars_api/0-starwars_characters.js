#!/usr/bin/node
/*
Star Wars Characters
*/

const arg1 = process.argv[2];
const request = require('request');

async function makeRequest (url) {
  const options = {
    url,
    method: 'GET',
    json: true
  };

  return new Promise((resolve, reject) => {
    request(options, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function getData (url) {
  try {
    const body = await makeRequest(url);
    const characters = body.characters;
    for (const peopleUrl of characters) {
      const character = await makeRequest(peopleUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
}
const url = `https://swapi-api.alx-tools.com/api/films/${arg1}`;
getData(url);
