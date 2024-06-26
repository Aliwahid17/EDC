# Generated by Django 5.0.4 on 2024-04-17 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intecomm_group', '0001_initial'),
        ('intecomm_screening', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpatientfollowupcall',
            name='patient_log',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='intecomm_screening.patientlog'),
        ),
        migrations.AddField(
            model_name='historicalpatientfollowupcall',
            name='site',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site'),
        ),
        migrations.AddField(
            model_name='historicalpatientgroup',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalpatientgroup',
            name='site',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site'),
        ),
        migrations.AddField(
            model_name='patientfollowupcall',
            name='patient_log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='intecomm_screening.patientlog'),
        ),
        migrations.AddField(
            model_name='patientfollowupcall',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site'),
        ),
        migrations.AddField(
            model_name='patientgroup',
            name='dm_patients',
            field=models.ManyToManyField(blank=True, related_name='dm_patients', to='intecomm_screening.patientlog', verbose_name='DM-only'),
        ),
        migrations.AddField(
            model_name='patientgroup',
            name='hiv_patients',
            field=models.ManyToManyField(blank=True, related_name='hiv_patients', to='intecomm_screening.patientlog', verbose_name='HIV-only'),
        ),
        migrations.AddField(
            model_name='patientgroup',
            name='htn_patients',
            field=models.ManyToManyField(blank=True, related_name='htn_patients', to='intecomm_screening.patientlog', verbose_name='HTN-only'),
        ),
        migrations.AddField(
            model_name='patientgroup',
            name='multi_patients',
            field=models.ManyToManyField(blank=True, related_name='multi_patients', to='intecomm_screening.patientlog', verbose_name='Multi-morbidity'),
        ),
        migrations.AddField(
            model_name='patientgroup',
            name='patients',
            field=models.ManyToManyField(blank=True, to='intecomm_screening.patientlog', verbose_name='Patients'),
        ),
        migrations.AddField(
            model_name='patientgroup',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site'),
        ),
        migrations.AddField(
            model_name='patientgroupappointment',
            name='community_care_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='intecomm_group.communitycarelocation'),
        ),
        migrations.AddField(
            model_name='patientgroupappointment',
            name='patient_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='intecomm_group.patientgroup'),
        ),
        migrations.AddField(
            model_name='patientgroupappointment',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site'),
        ),
        migrations.AddField(
            model_name='patientgroupmeeting',
            name='patient_group_appointment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='intecomm_group.patientgroupappointment'),
        ),
        migrations.AddField(
            model_name='patientgroupmeeting',
            name='patients',
            field=models.ManyToManyField(to='intecomm_screening.patientlog', verbose_name='Patients'),
        ),
        migrations.AddField(
            model_name='patientgroupmeeting',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site'),
        ),
        migrations.AddIndex(
            model_name='communitycarelocation',
            index=models.Index(fields=['modified', 'created'], name='intecomm_gr_modifie_9695bc_idx'),
        ),
        migrations.AddIndex(
            model_name='communitycarelocation',
            index=models.Index(fields=['user_modified', 'user_created'], name='intecomm_gr_user_mo_b4b5cb_idx'),
        ),
        migrations.AddIndex(
            model_name='patientfollowupcall',
            index=models.Index(fields=['modified', 'created'], name='intecomm_gr_modifie_55b38c_idx'),
        ),
        migrations.AddIndex(
            model_name='patientfollowupcall',
            index=models.Index(fields=['user_modified', 'user_created'], name='intecomm_gr_user_mo_b1771e_idx'),
        ),
        migrations.AddIndex(
            model_name='patientgroup',
            index=models.Index(fields=['modified', 'created'], name='intecomm_gr_modifie_709aa8_idx'),
        ),
        migrations.AddIndex(
            model_name='patientgroup',
            index=models.Index(fields=['user_modified', 'user_created'], name='intecomm_gr_user_mo_88354b_idx'),
        ),
        migrations.AddIndex(
            model_name='patientgroup',
            index=models.Index(fields=['group_identifier', 'status'], name='intecomm_gr_group_i_d392d3_idx'),
        ),
        migrations.AddIndex(
            model_name='patientgroupappointment',
            index=models.Index(fields=['modified', 'created'], name='intecomm_gr_modifie_bc2cdb_idx'),
        ),
        migrations.AddIndex(
            model_name='patientgroupappointment',
            index=models.Index(fields=['user_modified', 'user_created'], name='intecomm_gr_user_mo_aaafcb_idx'),
        ),
        migrations.AddIndex(
            model_name='patientgroupmeeting',
            index=models.Index(fields=['modified', 'created'], name='intecomm_gr_modifie_12dbed_idx'),
        ),
        migrations.AddIndex(
            model_name='patientgroupmeeting',
            index=models.Index(fields=['user_modified', 'user_created'], name='intecomm_gr_user_mo_746ccc_idx'),
        ),
    ]
