# Generated by Django 4.1.7 on 2023-03-31 02:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_lists", "0003_dmmanagement_dmmanagement_intecomm_li_id_b4d41f_idx"),
    ]

    operations = [
        migrations.CreateModel(
            name="RxModificationReasons",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "plural_name",
                    models.CharField(max_length=250, null=True, verbose_name="Plural name"),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name": "Treatment Modification Reasons",
                "verbose_name_plural": "Treatment Modification Reasons",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
        ),
        migrations.CreateModel(
            name="RxModifications",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "plural_name",
                    models.CharField(max_length=250, null=True, verbose_name="Plural name"),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name": "Treatment Modifications",
                "verbose_name_plural": "Treatment Modifications",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
        ),
        migrations.AddIndex(
            model_name="rxmodifications",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="intecomm_li_id_4fd810_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="rxmodificationreasons",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="intecomm_li_id_c4f7bb_idx",
            ),
        ),
    ]
