from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=255)
    logo_file = models.CharField(max_length=255)
    club = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.name)


class Player(models.Model):

    team = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="team_players"
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_file = models.CharField(max_length=255)
    jersey_number = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=255)
    matches_played = models.PositiveSmallIntegerField(blank=True, null=True)
    run_scored = models.PositiveIntegerField(blank=True, null=True)
    highest_score = models.PositiveSmallIntegerField(blank=True, null=True)
    fifties = models.PositiveSmallIntegerField(blank=True, null=True)
    hundreds = models.PositiveSmallIntegerField(blank=True, null=True)


class Match(models.Model):

    team_1 = models.ForeignKey("Team", related_name="team_1", on_delete=models.CASCADE)
    team_2 = models.ForeignKey("Team", related_name="team_2", on_delete=models.CASCADE)
    match_date = models.DateField()
    winning_team = models.ForeignKey(
        "Team", related_name="winning_team", on_delete=models.CASCADE, null=True
    )


class PointsTable(models.Model):

    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    matches_won = models.PositiveSmallIntegerField()
    matches_lost = models.PositiveSmallIntegerField()
    matches_tie = models.PositiveSmallIntegerField()
    total_points = models.PositiveSmallIntegerField()

