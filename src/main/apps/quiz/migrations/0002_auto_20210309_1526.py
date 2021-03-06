# Generated by Django 3.1.7 on 2021-03-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q10_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q10_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q10_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q10_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q10_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q10_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q1_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q1_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q1_opt2',
            field=models.TextField(default=2, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q1_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q1_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q1_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q2_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q2_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q2_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q2_opt3',
            field=models.TextField(default=2, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q2_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q2_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q3_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q3_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q3_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q3_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q3_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q3_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q4_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q4_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q4_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q4_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q4_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q4_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q5_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q5_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q5_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q5_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q5_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q5_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q6_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q6_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q6_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q6_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q6_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q6_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q7_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q7_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q7_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q7_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q7_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q7_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q8_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q8_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q8_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q8_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q8_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q8_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q9_answer',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q9_opt1',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q9_opt2',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q9_opt3',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q9_opt4',
            field=models.TextField(default=0, max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_q9_qstn',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
    ]
