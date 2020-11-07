# Generated by Django 3.0.8 on 2020-11-07 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='logo_pics')),
                ('organisation', models.TextField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('website', models.URLField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_organisation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]