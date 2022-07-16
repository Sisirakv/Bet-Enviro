# Generated by Django 4.0.6 on 2022-07-15 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_service_alter_blog_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_locator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=200)),
                ('local_area', models.CharField(max_length=200)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.service')),
            ],
        ),
    ]