# Generated by Django 5.1.2 on 2024-10-16 18:00

import board.services
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('tanks', 'Танки'), ('healers', 'Хилы'), ('damage_dealers', 'ДД'), ('dealers', 'Торговцы'), ('guild_masters', 'Гилдмастеры'), ('quest_givers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potion_makers', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], max_length=15, verbose_name='Категория')),
                ('datetime_in', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=60, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to=board.services.get_path_upload_image, verbose_name='Изображение')),
                ('video', models.FileField(blank=True, null=True, upload_to=board.services.get_path_upload_video, verbose_name='Видео')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_response', models.DateTimeField(auto_now_add=True)),
                ('condition', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
