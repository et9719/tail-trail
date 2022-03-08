# Generated by Django 3.2 on 2022-03-08 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'ordering': ['date']},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, unique=True)),
                ('dog', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('info', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]