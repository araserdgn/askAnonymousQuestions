# Generated by Django 4.2 on 2023-08-30 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sorular", "0004_cevaplar"),
    ]

    operations = [
        migrations.AddField(
            model_name="sorular",
            name="kullanici",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
