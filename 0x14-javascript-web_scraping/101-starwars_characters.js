#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    const fetchCharacter = (characterUrl) => {
      return new Promise((resolve) => {
        request(characterUrl, (error, response, body) => {
          if (!error) {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    };

    const fetchAllCharacters = async () => {
      const characters = await Promise.all(charactersUrls.map(fetchCharacter));
      characters.forEach((characterName) => {
        console.log(characterName);
      });
    };

    fetchAllCharacters();
  }
});
