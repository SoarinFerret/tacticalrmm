# Generated by Django 3.0.5 on 2020-04-14 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_auto_20200411_0212'),
        ('checks', '0008_auto_20200414_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memcheck',
            name='task_on_failure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memtaskfailure', to='automation.AutomatedTask'),
        ),
    ]
