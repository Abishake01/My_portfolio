# Generated by Django 4.1.9 on 2025-03-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_auto_20250109_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('icon', models.ImageField(blank=True, upload_to='contact_images/')),
            ],
        ),
    ]
