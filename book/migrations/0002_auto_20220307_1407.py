# Generated by Django 3.2 on 2022-03-07 14:07

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, unique=True)),
                ('dog', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('info', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='availability',
            options={'ordering': ['date']},
        ),
    ]