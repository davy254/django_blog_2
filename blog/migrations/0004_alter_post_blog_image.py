# Generated by Django 4.2.7 on 2023-11-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(default='new_post.jpg', upload_to='blog_pics'),
        ),
    ]
