# Generated by Django 4.2.5 on 2023-09-28 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spend', '0001_initial'),
        ('revenue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenuestatistic',
            name='spend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revenue_statistic', to='spend.spendstatistic'),
        ),
    ]
