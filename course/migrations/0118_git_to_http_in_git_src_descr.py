# Generated by Django 3.2.8 on 2022-01-11 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0117_django32_bigauto_nullboolean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='git_source',
            field=models.CharField(help_text="A Git URL from which to pull course updates. If you're just starting out, enter <tt>https://github.com/inducer/relate-sample.git</tt> to get some sample content.", max_length=200, verbose_name='git source'),
        ),
    ]