# Generated by Django 5.0.3 on 2024-07-02 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_group_groupmember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmember',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupmember',
            name='user',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='GroupMember',
        ),
    ]
