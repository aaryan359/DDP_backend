# Generated by Django 4.1.7 on 2023-04-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0006_rename_dbtversion_orgdbt_dbt_version_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orgdbt",
            name="gitrepo_access_token_secret",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
