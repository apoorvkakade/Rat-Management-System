# Generated by Django 3.1.5 on 2021-02-05 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nameapp', '0002_auto_20210121_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('q_opening_m', models.IntegerField(default=0)),
                ('q_opening_f', models.IntegerField(default=0)),
                ('q_na_m', models.IntegerField(default=0)),
                ('q_na_f', models.IntegerField(default=0)),
                ('q_dead_m', models.IntegerField(default=0)),
                ('q_dead_f', models.IntegerField(default=0)),
                ('q_exp_m', models.IntegerField(default=0)),
                ('q_exp_f', models.IntegerField(default=0)),
                ('q_bre_m', models.IntegerField(default=0)),
                ('q_bre_f', models.IntegerField(default=0)),
                ('q_total_m', models.IntegerField(default=0)),
                ('q_total_f', models.IntegerField(default=0)),
                ('p_opening', models.IntegerField(default=0)),
                ('p_na', models.IntegerField(default=0)),
                ('p_dead', models.IntegerField(default=0)),
                ('p_total', models.IntegerField(default=0)),
                ('y_opening_m', models.IntegerField(default=0)),
                ('y_opening_f', models.IntegerField(default=0)),
                ('y_na_m', models.IntegerField(default=0)),
                ('y_na_f', models.IntegerField(default=0)),
                ('y_dead_m', models.IntegerField(default=0)),
                ('y_dead_f', models.IntegerField(default=0)),
                ('y_exp_m', models.IntegerField(default=0)),
                ('y_exp_f', models.IntegerField(default=0)),
                ('y_bre_m', models.IntegerField(default=0)),
                ('y_bre_f', models.IntegerField(default=0)),
                ('y_total_m', models.IntegerField(default=0)),
                ('y_total_f', models.IntegerField(default=0)),
                ('e_opening_m', models.IntegerField(default=0)),
                ('e_opening_f', models.IntegerField(default=0)),
                ('e_na_m', models.IntegerField(default=0)),
                ('e_na_f', models.IntegerField(default=0)),
                ('e_dead_m', models.IntegerField(default=0)),
                ('e_dead_f', models.IntegerField(default=0)),
                ('e_total_m', models.IntegerField(default=0)),
                ('e_total_f', models.IntegerField(default=0)),
                ('b_opening_m', models.IntegerField(default=0)),
                ('b_opening_f', models.IntegerField(default=0)),
                ('b_na_m', models.IntegerField(default=0)),
                ('b_na_f', models.IntegerField(default=0)),
                ('b_dead_m', models.IntegerField(default=0)),
                ('b_dead_f', models.IntegerField(default=0)),
                ('b_total_m', models.IntegerField(default=0)),
                ('b_total_f', models.IntegerField(default=0)),
                ('preg_opening', models.IntegerField(default=0)),
                ('preg_dead', models.IntegerField(default=0)),
                ('preg_na', models.IntegerField(default=0)),
                ('preg_total', models.IntegerField(default=0)),
                ('w_opening', models.IntegerField(default=0)),
                ('w_mother', models.IntegerField(default=0)),
                ('w_dead', models.IntegerField(default=0)),
                ('w_total', models.IntegerField(default=0)),
                ('g_total_m', models.IntegerField(default=0)),
                ('g_total_f', models.IntegerField(default=0)),
                ('species', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nameapp.mouse_species')),
            ],
            options={
                'unique_together': {('species', 'entry_date')},
            },
        ),
    ]