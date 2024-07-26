#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const characterID = '18';
const URL = 'https://swapi-api.hbtn.io/api/films/';

request.get(URL, (err, response, body) => {
    