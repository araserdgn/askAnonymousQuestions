# Generated by Django 4.2 on 2023-08-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_remove_profile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="konum",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="nickname",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="isim",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
