# Generated by Django 2.2.9 on 2020-01-16 07:45

import app.models
import app.storage
from django.conf import settings
import django.core.validators
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
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.CharField(choices=[('Python3', 'Python3'), ('Java', 'Java'), ('C++', 'C++'), ('C', 'C'), ('PHP', 'PHP'), ('Bash', 'Bash')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
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
                ('marks', models.IntegerField(blank=True, null=True)),
                ('draft', models.BooleanField(default=False)),
                ('check_plagiarism', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='StudentProfilePic')),
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
                ('status', models.CharField(choices=[('accepted', 'Accepted'), ('partially-submit', 'Partially Submitted'), ('wrong', 'Wrong Answer'), ('not-attempted', 'Not Attempted')], default='not-attempted', max_length=100)),
                ('submission', models.FileField(storage=app.storage.OverwriteStorage(), upload_to=app.models.submission_directory_path)),
                ('remark', models.CharField(blank=True, max_length=500)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Assignment')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='ProfessorProfilePic')),
                ('moss_id', models.CharField(blank=True, max_length=50, null=True)),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlagResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perc_1', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('perc_2', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('lines_matched', models.CharField(max_length=100)),
                ('lines_match_count', models.IntegerField()),
                ('moss_page_url', models.URLField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
                ('solution_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution_1', to='app.Solution')),
                ('solution_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution_2', to='app.Solution')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('join_code', models.CharField(default=app.models.random_code, editable=False, max_length=5, unique=True)),
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
