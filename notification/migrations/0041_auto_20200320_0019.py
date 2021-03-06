# Generated by Django 2.1.8 on 2020-03-20 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0040_auto_20200320_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('joinTeam', 'joinTeam'), ('recruitingComment', 'recruitingComment'), ('leagueComment', 'leagueComment'), ('leaguePersonalApply', 'leaguePersonalApply'), ('resultConfirm', 'resultConfirm'), ('resultInput', 'resultInput'), ('recruitingDenied', 'recruitingDenied'), ('denySuggestion', 'denySuggestion'), ('personalApply', 'personalApply'), ('recruitingApply', 'recruitingApply'), ('personalReply', 'personalReply'), ('teamMatchingApply', 'teamMatchingApply'), ('teamComment', 'teamComment'), ('resultEdit', 'resultEdit'), ('suggestTeamMatching', 'suggestTeamMatching'), ('teamAccepted', 'teamAccepted'), ('leagueTeamApply', 'leagueTeamApply'), ('teamApplicationDenied', 'teamApplicationDenied'), ('recruitingAccepted', 'recruitingAccepted'), ('prComment', 'prComment'), ('recruitingReply', 'recruitingReply'), ('leagueReply', 'leagueReply'), ('acceptSuggestion', 'acceptSuggestion'), ('teamReply', 'teamReply')], max_length=30),
        ),
    ]
