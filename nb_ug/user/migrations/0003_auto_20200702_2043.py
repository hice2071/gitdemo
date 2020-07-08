# Generated by Django 3.0.5 on 2020-07-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200702_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='entry_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='finally_log_ip',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='finally_log_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='jurisdiction',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='visits',
            field=models.CharField(max_length=10, null=True),
        ),
    ]