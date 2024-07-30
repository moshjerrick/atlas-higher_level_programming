$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $.each(data.results, function (index, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
}
);