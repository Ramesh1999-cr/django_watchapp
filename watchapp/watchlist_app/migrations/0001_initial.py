# Generated by Django 4.2.4 on 2023-08-23 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=150)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('storyline', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('avg_rating', models.FloatField(default=0)),
                ('number_rating', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform')),
            ],
        ),
    ]