var SERVER_URL = 'http://127.0.0.1:8000/',
    API_ENDPOINT = SERVER_URL + 'api/',
    STATIC_ENDPOINT = SERVER_URL + 'static/',
    TEAMS_URI = 'teams',
    PLAYERS_URI = 'teams/{team_id}',
    FIXTURES_URI = 'fixtures',
    POINT_TABLE_URI = 'points-table';

$(document).ready(function() {
    fetchTeams();

    $(document).on('click', 'a.team-link', function(e) {
        e.preventDefault();

        fetchPlayers($(this).data('id'));
    });

    $('#create-fixtures').click(function(e) {
        e.preventDefault();

        createFixtures();
    });
});


function call(uri, method, data, callback) {
    $.ajax({
        url: API_ENDPOINT + uri,
        method: method || 'GET',
        dataType: "json",
        data: data || {},
        success: function(response) {
            if (callback && typeof callback === 'function') {
                callback(response);
            }
        },
        error: function(xhr, settings) {
            if (xhr.status === 0) {
                alert('Not connected to internet. Please verify network and try again.');
            } else if (xhr.status === 404) {
                alert('Requested resource not found.');
            } else {
                alert('Something went wrong.');
            }
        }
    });
}

function fetchTeams() {

    call(TEAMS_URI, 'GET', {}, function(response) {

        var target = $('#teams-table tbody');
        $.each(response, function(key, team) {
            target.append(
                $('<tr />')
                .append($('<td />', { text: key + 1 }))
                .append($('<td />', { html: $('<img class="img-fluid img-thumb" src="' + STATIC_ENDPOINT + team.logo_file + '" alt="' + team.name + '" />') }))
                .append($('<td />', { html: $('<a />', { text: team.name, href: 'javascript:void(0);', 'data-id': team.id, class: 'team-link' }) }))
            );
        });
    });
}

function fetchPlayers(teamId) {

    var playerTable = $('#players-table'),
        target = playerTable.find('tbody');

    target.html('')
    playerTable.addClass('d-none');

    call(PLAYERS_URI.replace('{team_id}', teamId), 'GET', {}, function(response) {


        $('#team-name').text(response.name);

        var players = response.team_players;
        $.each(players, function(key, player) {
            target.append(
                $('<tr />')
                .append($('<td />', { text: key + 1 }))
                .append($('<td />', { html: $('<img class="img-fluid img-thumb" src="' + STATIC_ENDPOINT + player.image_file + '" alt="' + player.first_name + ' ' + player.last_name + '" />') }))
                .append($('<td />', { text: player.last_name }))
                .append($('<td />', { text: player.first_name }))
            );
            playerTable.removeClass('d-none');
        });
    });
}

function createFixtures() {
    call(FIXTURES_URI, 'POST', {}, function(response) {
        alert(response.message);

        fetchFixtures();
    });
}

function fetchFixtures() {
    var target = $('#fixtures-table tbody');
    target.html('');

    call(FIXTURES_URI, 'GET', {}, function(response) {

        $.each(response, function(key, fixture) {
            target.append(
                $('<tr />')
                .append($('<td />', { text: fixture.team_1 }))
                .append($('<td />', { text: fixture.team_2 }))
                .append($('<td />', { text: fixture.match_date }))
                .append($('<td />', { text: fixture.winning_team || "Tie" }))
            );
        });

        fetchPointsTable();
    });
}

function fetchPointsTable() {
    var target = $('#points-table tbody');
    target.html('');

    call(POINT_TABLE_URI, 'GET', {}, function(response) {

        $.each(response, function(key, record) {
            target.append(
                $('<tr />')
                .append($('<td />', { text: record.team }))
                .append($('<td />', { text: record.matches_won + record.matches_lost + record.matches_tie }))
                .append($('<td />', { text: record.matches_won }))
                .append($('<td />', { text: record.matches_lost }))
                .append($('<td />', { text: record.matches_tie }))
                .append($('<td />', { text: record.total_points }))
            );
        });
    });
}