#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error("Usage: ./0-starwars_characters.js <Movie_ID>");
  process.exit(1);
}

// Fetch the movie data to get character URLs
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Function to fetch and display each character name
  for (const url of characterUrls) {
    await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        resolve();
      });
    });
  }
});

