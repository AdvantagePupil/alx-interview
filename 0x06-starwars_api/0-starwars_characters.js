#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters(filmId) {
  try {
    const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
    const response = await request(endpoint);
    const filmData = JSON.parse(response.body);
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      const characterResponse = await request(characterUrl);
      const characterData = JSON.parse(characterResponse.body);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

starwarsCharacters(filmID);

