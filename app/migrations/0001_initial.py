# Generated by Django 2.2.6 on 2019-11-22 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True)),
                ('sample_input', models.TextField(blank=True)),
                ('sample_output', models.TextField(blank=True)),
                ('marks', models.IntegerField()),
                ('draft', models.BooleanField(default=False)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='StudentProfilePic')),
                ('course', models.CharField(blank=True, max_length=50)),
                ('roll_no', models.IntegerField()),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('accepted', 'Accepted'), ('partially-submit', 'Partially Submitted'), ('wrong', 'Wrong Answer'), ('not-attempted', 'Not Attempted')], max_length=100)),
                ('submission', models.FileField(upload_to='assignments/<django.db.models.fields.related.ForeignKey>/questions/<django.db.models.fields.related.ForeignKey>/submissions/<django.db.models.fields.related.ForeignKey>')),
                ('remark', models.CharField(blank=True, max_length=500)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Assignment')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='ProfessorProfilePic')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Professor')),
                ('students', models.ManyToManyField(blank=True, to='app.Student')),
            ],
            options={
                'verbose_name': 'Classroom',
                'verbose_name_plural': 'Classrooms',
            },
        ),
        migrations.AddField(
            model_name='assignment',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Classroom'),
        ),
    ]
