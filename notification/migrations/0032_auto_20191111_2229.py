# Generated by Django 2.1.8 on 2019-11-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0031_auto_20191111_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('prComment', 'prComment'), ('teamAccepted', 'teamAccepted'), ('joinTeam', 'joinTeam'), ('recruitingComment', 'recruitingComment'), ('recruitingApply', 'recruitingApply'), ('recruitingAccepted', 'recruitingAccepted'), ('leaguePersonalApply', 'leaguePersonalApply'), ('recruitingDenied', 'recruitingDenied'), ('resultEdit', 'resultEdit'), ('personalApply', 'personalApply'), ('teamApplicationDenied', 'teamApplicationDenied'), ('acceptSuggestion', 'acceptSuggestion'), ('resultInput', 'resultInput'), ('teamComment', 'teamComment'), ('recruitingReply', 'recruitingReply'), ('leagueComment', 'leagueComment'), ('teamMatchingApply', 'teamMatchingApply'), ('denySuggestion', 'denySuggestion'), ('teamReply', 'teamReply'), ('suggestTeamMatching', 'suggestTeamMatching'), ('personalReply', 'personalReply'), ('leagueReply', 'leagueReply'), ('resultConfirm', 'resultConfirm'), ('leagueTeamApply', 'leagueTeamApply')], max_length=30),
        ),
    ]
