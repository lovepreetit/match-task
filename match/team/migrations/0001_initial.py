# Generated by Django 3.1 on 2020-08-22 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo_file', models.CharField(max_length=255)),
                ('club', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PointsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches_won', models.PositiveSmallIntegerField()),
                ('matches_lost', models.PositiveSmallIntegerField()),
                ('matches_tie', models.PositiveSmallIntegerField()),
                ('total_points', models.PositiveSmallIntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('image_file', models.CharField(max_length=255)),
                ('jersey_number', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=255)),
                ('matches_played', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('run_scored', models.PositiveIntegerField(blank=True, null=True)),
                ('highest_score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('fifties', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hundreds', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_players', to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateField()),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='team.team')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to='team.team')),
                ('winning_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning_team', to='team.team')),
            ],
        ),
    ]
