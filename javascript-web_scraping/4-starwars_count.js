#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const characterID = '18';
const URL = 'https://swapi-api.hbtn.io/api/films/';

request.get(URL, (err, response, body) => {
    if (err) {
        console.log(err);
    }
    else {
        const movies = JSON.parse(body).results;
        let count = 0;
        for (const movie of movies) {
            for (const character of movie.characters) {
                if (character.includes(characterID)) {
                    count++;
                    break;
                }
            }
        }
        console.log(count);
    }
});
