# Generated by Django 2.0.6 on 2018-06-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('login', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('node_id', models.CharField(max_length=100)),
                ('avatar_url', models.URLField()),
                ('gravatar_id', models.CharField(max_length=20, null=True)),
                ('url', models.URLField()),
                ('html_url', models.URLField()),
                ('followers_url', models.URLField()),
                ('following_url', models.URLField()),
                ('gists_url', models.URLField()),
                ('starred_url', models.URLField()),
                ('subscriptions_url', models.URLField()),
                ('organizations_url', models.URLField()),
                ('repos_url', models.URLField()),
                ('events_url', models.URLField()),
                ('received_events_url', models.URLField()),
                ('type', models.CharField(max_length=50)),
                ('site_admin', models.BooleanField()),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('blog', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('hireable', models.CharField(max_length=256, null=True)),
                ('bio', models.CharField(max_length=256, null=True)),
                ('public_repos', models.IntegerField()),
                ('public_gists', models.IntegerField()),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
