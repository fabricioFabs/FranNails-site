# Generated by Django 3.2.19 on 2023-06-05 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20230604_0224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id'], 'verbose_name': 'Post', 'verbose_name_plural': 'Post'},
        ),
        migrations.RenameField(
            model_name='config',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
