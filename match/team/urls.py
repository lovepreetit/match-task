from django.urls import path

from team.views import TeamsView, TeamPlayersView, FixturesView, PointsTableView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(title="Match API", default_version="v1"), public=True
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="documentation"),
    path("teams", TeamsView.as_view()),
    path("teams/<int:id>", TeamPlayersView.as_view()),
    path("fixtures", FixturesView.as_view()),
    path("points-table", PointsTableView.as_view()),
]
