# Generated by Django 4.1.9 on 2025-03-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_contact_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='experience_logos/')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-order', '-start_date'],
            },
        ),
    ]
