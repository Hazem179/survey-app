# Generated by Django 4.1.7 on 2023-03-29 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments', verbose_name='الملفات المرفقة'),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=100, verbose_name='السؤال'),
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100, verbose_name='السؤال')),
                ('is_correct', models.BooleanField(default=False, verbose_name='الإجابة الصحيحة')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
            ],
        ),
    ]
