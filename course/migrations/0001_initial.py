# Generated by Django 4.1.4 on 2022-12-14 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("course_id", models.AutoField(primary_key=True, serialize=False)),
                ("course_title", models.CharField(max_length=100)),
                ("instractor_name", models.CharField(max_length=100)),
                ("capacity", models.IntegerField(default=30)),
                ("open_seats", models.IntegerField(default=30)),
            ],
            options={
                "verbose_name_plural": "Course",
                "db_table": "course",
            },
        ),
        migrations.CreateModel(
            name="Students",
            fields=[
                ("reg_no", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("instractor_name", models.CharField(max_length=100)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Students",
                "db_table": "students",
            },
        ),
        migrations.CreateModel(
            name="Instractor",
            fields=[
                ("instractor_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("course_title", models.CharField(max_length=100)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Instractor",
                "db_table": "instractor",
            },
        ),
    ]