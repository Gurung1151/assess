# Generated by Django 4.0.3 on 2022-03-19 13:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='classData',
            fields=[
                ('dept', models.CharField(blank=True, choices=[('BCT', 'BCT'), ('BEL', 'BEL'), ('BEX', 'BEX'), ('BEI', 'BEI')], max_length=200)),
                ('year', models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], max_length=200)),
                ('part', models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II')], max_length=200)),
                ('batch', models.CharField(blank=True, max_length=200)),
                ('group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=200, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('subjectName', models.CharField(blank=True, max_length=200, null=True)),
                ('subjectCode', models.CharField(blank=True, max_length=20, null=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch', models.CharField(max_length=4, null=True)),
                ('Dept', models.CharField(max_length=3, null=True)),
                ('Roll', models.CharField(max_length=3, null=True)),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Section', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentMarks',
            fields=[
                ('getClass', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='classes.classdata')),
                ('dept', models.CharField(blank=True, choices=[('BCT', 'BCT'), ('BEL', 'BEL'), ('BEX', 'BEX'), ('BEI', 'BEI')], max_length=200)),
                ('year', models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], max_length=200)),
                ('part', models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II')], max_length=200)),
                ('batch', models.CharField(blank=True, max_length=200)),
                ('group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=200, null=True)),
                ('subjectName', models.CharField(blank=True, max_length=200, null=True)),
                ('subjectCode', models.CharField(blank=True, max_length=20, null=True)),
                ('fullMarks', models.IntegerField(null=True)),
                ('type', models.CharField(choices=[('theory', 'th'), ('practical', 'Prac')], max_length=200)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_submitted', models.BooleanField(default=False)),
                ('SubmittedMarks1', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks2', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks3', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks4', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks5', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks6', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks7', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks8', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks9', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks10', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks11', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks12', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks13', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks14', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks15', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks16', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks17', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks18', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks19', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks20', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks21', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks22', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks23', models.CharField(blank=True, max_length=20, null=True)),
                ('SubmittedMarks24', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
