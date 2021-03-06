# Generated by Django 3.2.10 on 2022-01-01 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0004_auto_20211225_1456'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.medicine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
