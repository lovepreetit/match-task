import random
from django.core.management.base import BaseCommand
from team.models import Team, Player


class Command(BaseCommand):

    no_of_teams = 5

    def handle(self, *args, **options):

        team_objs = [
            Team(name="Team %s" % (i + 1), logo_file="team.jpg", club="Club Name")
            for i in range(self.no_of_teams)
        ]

        Team.objects.bulk_create(team_objs)

        teams = Team.objects.all()

        for team in teams:
            player_objs = [
                Player(
                    team=team,
                    first_name="Player",
                    last_name="%s" % (i + 1),
                    image_file="player.jpg",
                    jersey_number=random.randint(i * 5, (i * 5) + 5),
                    country="County Name",
                )
                for i in range(11)
            ]

            Player.objects.bulk_create(player_objs)

