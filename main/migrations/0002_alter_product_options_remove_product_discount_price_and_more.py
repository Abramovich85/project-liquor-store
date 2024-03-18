# Generated by Django 5.0.3 on 2024-03-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_price',
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна производства'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена без скидки(зачеркнутое)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]