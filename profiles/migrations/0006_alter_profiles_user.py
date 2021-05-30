# Generated by Django 3.2.3 on 2021-05-29 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0005_alter_profiles_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]