from rest_framework import serializers
from team.models import Team, Player, Match, PointsTable


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            "first_name",
            "last_name",
            "image_file",
            "jersey_number",
            "country",
            "matches_played",
            "run_scored",
            "highest_score",
            "fifties",
            "hundreds",
        ]


class TeamSerializer(serializers.ModelSerializer):

    team_players = serializers.SerializerMethodField()

    def get_team_players(self, team):
        return PlayerSerializer(team.team_players.filter(team=team), many=True).data

    class Meta:
        model = Team
        fields = ["id", "name", "logo_file", "club", "team_players"]


class MatchSerializer(serializers.ModelSerializer):

    team_1 = serializers.StringRelatedField()
    team_2 = serializers.StringRelatedField()
    winning_team = serializers.StringRelatedField()

    class Meta:
        model = Match
        fields = [
            "team_1",
            "team_2",
            "match_date",
            "winning_team",
        ]


class PointsTableSerializer(serializers.ModelSerializer):

    team = serializers.StringRelatedField()

    class Meta:
        model = PointsTable
        fields = [
            "team",
            "matches_won",
            "matches_lost",
            "matches_tie",
            "total_points",
        ]
