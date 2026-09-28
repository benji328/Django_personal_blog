from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("posts", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="country_total_deaths",
            name="deaths",
            field=models.IntegerField(),
        ),
    ]
