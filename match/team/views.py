import random
from datetime import datetime, timedelta

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from team.models import Team, Player, Match, PointsTable
from team.serializers import (
    TeamSerializer,
    PlayerSerializer,
    MatchSerializer,
    PointsTableSerializer,
)


class TeamsView(APIView):
    def get(self, request):
        teams = Team.objects.all().order_by("name")

        team_serializer = TeamSerializer(teams, many=True)
        return Response(team_serializer.data)


class TeamPlayersView(APIView):
    def get(self, request, id):

        try:
            team = Team.objects.get(pk=id)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        team_serializer = TeamSerializer(team)
        return Response(team_serializer.data)


class FixturesView(APIView):
    def get(self, request):

        matches = Match.objects.all().order_by("match_date")

        match_serializer = MatchSerializer(matches, many=True)
        return Response(match_serializer.data)

    def post(self, request):

        Match.objects.all().delete()
        PointsTable.objects.all().delete()

        teams = Team.objects.all()

        match_date = datetime.today()

        points_table_data = {}
        for team in teams:
            points_table_data[team.id] = {
                "matches_won": 0,
                "matches_lost": 0,
                "matches_tie": 0,
                "total_points": 0,
            }

        for i in range(len(teams) - 1):
            for j in range(i + 1, len(teams)):

                team_1 = teams[i]
                team_2 = teams[j]

                winning_team = losing_team = None
                result_number = random.randint(0, 2)
                match_date = match_date + timedelta(days=1)

                if result_number == 0:
                    winning_team = team_1
                    losing_team = team_2
                elif result_number == 1:
                    losing_team = team_1
                    winning_team = team_2

                match = Match(
                    **{
                        "team_1": team_1,
                        "team_2": team_2,
                        "match_date": match_date.date(),
                        "winning_team": winning_team
                        if winning_team is not None
                        else None,
                    }
                )
                match.save()

                # if match came to a result
                if winning_team and losing_team:

                    # increment matches won by winning team
                    points_table_data[winning_team.id]["matches_won"] += 1

                    # increment 2 points for winning team in points table
                    points_table_data[winning_team.id]["total_points"] += 2

                    # increment matches lost for losing team
                    points_table_data[losing_team.id]["matches_lost"] += 1
                # if match tie
                else:
                    # increment matches tie for both team
                    points_table_data[team_1.id]["matches_tie"] += 1
                    points_table_data[team_2.id]["matches_tie"] += 1

                    # increment 1 point for tie match for both team
                    points_table_data[team_1.id]["total_points"] += 1
                    points_table_data[team_2.id]["total_points"] += 1

        for team_id, record in points_table_data.items():

            team = teams.get(pk=team_id)

            points_table = PointsTable(
                **{
                    "team": team,
                    "matches_won": record["matches_won"],
                    "matches_lost": record["matches_lost"],
                    "matches_tie": record["matches_tie"],
                    "total_points": record["total_points"],
                }
            )

            points_table.save()

        return Response({"message": "Fixtures created"}, status=status.HTTP_201_CREATED)


class PointsTableView(APIView):
    def get(self, request):
        points_table = PointsTable.objects.all().order_by("-total_points")

        point_table_serializer = PointsTableSerializer(points_table, many=True)
        return Response(point_table_serializer.data)
