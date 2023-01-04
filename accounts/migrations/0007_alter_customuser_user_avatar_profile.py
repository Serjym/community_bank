# Generated by Django 4.1.3 on 2022-12-24 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customuser_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_avatar',
            field=models.ImageField(default='default.jpg', upload_to='user_profile/avatars/'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_avatar', models.ImageField(default='default.jpg', upload_to='user_profile/avatars/')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
