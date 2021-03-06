# Generated by Django 2.1.7 on 2019-03-21 10:14

from django.db import migrations
import ei.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ei', '0002_question_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='image',
            new_name='image_a',
        ),
        migrations.AddField(
            model_name='question',
            name='image_b',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=ei.models.ei_image_path),
        ),
    ]
