# Generated by Django 5.0.4 on 2024-04-17 11:32

import _socket
import django.core.validators
import django.db.models.deletion
import django.db.models.manager
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_revision.revision_field
import edc_model.models.fields.other_charfield
import edc_model.validators.date
import edc_model.validators.phone
import edc_model_fields.fields.other_charfield
import edc_sites.managers
import edc_utils.date
import intecomm_group.models.patient_group
import intecomm_screening.model_mixins.patient_call_model_mixin
import simple_history.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intecomm_lists', '0012_visitreasons_custom_name'),
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPatientGroup',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60, verbose_name='Hostname created')),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50, verbose_name='Hostname modified')),
                ('device_created', models.CharField(blank=True, max_length=10, verbose_name='Device created')),
                ('device_modified', models.CharField(blank=True, max_length=10, verbose_name='Device modified')),
                ('locale_created', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale created')),
                ('locale_modified', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale modified')),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('group_identifier', models.CharField(max_length=36, null=True)),
                ('group_identifier_as_pk', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, validators=[edc_model.validators.date.datetime_not_future])),
                ('name', models.CharField(db_index=True, help_text='The name may be changed at anytime as long as it is unique.', max_length=25, verbose_name='Group name')),
                ('status', models.CharField(choices=[('New', 'New'), ('recruiting', 'Recruiting'), ('COMPLETE', 'Complete/Ready'), ('in_followup', 'In followup'), ('dissolved', 'Dissolved')], default='recruiting', help_text="Will revert to 'Recruiting' if changes are made to the list of selected patients", max_length=25)),
                ('ratio', models.DecimalField(decimal_places=4, max_digits=10, null=True)),
                ('bypass_group_size_min', models.BooleanField(default=False, help_text='If ticked, you must have consulted with your study coordinator first', verbose_name='Bypass group size minimum of 14')),
                ('bypass_group_ratio', models.BooleanField(default=False, help_text='If ticked, you must have consulted with your study coordinator first', verbose_name='Bypass 2:1 NCD:HIV ratio')),
                ('randomize_now', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=15, verbose_name='Randomize now?')),
                ('confirm_randomize_now', models.CharField(blank=True, max_length=15, null=True, verbose_name='If YES, please confirm by typing the word RANDOMIZE here')),
                ('randomized', models.BooleanField(blank=True, default=False)),
                ('randomized_datetime', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Patient Group',
                'verbose_name_plural': 'historical Patient Groups',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='PatientFollowupCall',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60, verbose_name='Hostname created')),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50, verbose_name='Hostname modified')),
                ('device_created', models.CharField(blank=True, max_length=10, verbose_name='Device created')),
                ('device_modified', models.CharField(blank=True, max_length=10, verbose_name='Device modified')),
                ('locale_created', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale created')),
                ('locale_modified', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale modified')),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(db_index=True, default=edc_utils.date.get_utcnow)),
                ('contact_number', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, validators=[edc_model.validators.phone.phone_number])),
                ('alt_contact_number', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_model.validators.phone.phone_number])),
                ('answered', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, null=True)),
                ('respondent', models.CharField(choices=[('patient', 'Patient'), ('family', 'Family'), ('friend', 'friend'), ('OTHER', 'other'), ('N/A', 'Not applicable')], default='N/A', max_length=15)),
                ('survival_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('not_sure', 'Not sure'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Is the participant known to be alive')),
                ('catchment_area', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('not_sure', 'Not sure'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Does the participant still reside within the catchment area')),
                ('last_appt_date', models.DateField(blank=True, help_text='This may be helpful when updating health records', null=True, verbose_name='When did the patient last seek care')),
                ('last_attend_clinic', models.CharField(blank=True, help_text='This may be helpful when updating health records', max_length=25, null=True, verbose_name='Where did the patient last seek care')),
                ('last_attend_clinic_other', edc_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...')),
                ('next_appt_date', models.DateField(blank=True, null=True, verbose_name='When will the patient next attend')),
                ('call_again', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, verbose_name='May we call again?')),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=71, null=True, verbose_name='Note')),
            ],
            options={
                'verbose_name': 'Patient Followup Call',
                'verbose_name_plural': 'Patient Followup Calls',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
                'default_manager_name': 'objects',
            },
            managers=[
                ('objects', intecomm_screening.model_mixins.patient_call_model_mixin.Manager()),
                ('on_site', edc_sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='PatientGroup',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60, verbose_name='Hostname created')),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50, verbose_name='Hostname modified')),
                ('device_created', models.CharField(blank=True, max_length=10, verbose_name='Device created')),
                ('device_modified', models.CharField(blank=True, max_length=10, verbose_name='Device modified')),
                ('locale_created', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale created')),
                ('locale_modified', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale modified')),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('group_identifier', models.CharField(max_length=36, null=True)),
                ('group_identifier_as_pk', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, validators=[edc_model.validators.date.datetime_not_future])),
                ('name', models.CharField(db_index=True, help_text='The name may be changed at anytime as long as it is unique.', max_length=25, unique=True, verbose_name='Group name')),
                ('status', models.CharField(choices=[('New', 'New'), ('recruiting', 'Recruiting'), ('COMPLETE', 'Complete/Ready'), ('in_followup', 'In followup'), ('dissolved', 'Dissolved')], default='recruiting', help_text="Will revert to 'Recruiting' if changes are made to the list of selected patients", max_length=25)),
                ('ratio', models.DecimalField(decimal_places=4, max_digits=10, null=True)),
                ('bypass_group_size_min', models.BooleanField(default=False, help_text='If ticked, you must have consulted with your study coordinator first', verbose_name='Bypass group size minimum of 14')),
                ('bypass_group_ratio', models.BooleanField(default=False, help_text='If ticked, you must have consulted with your study coordinator first', verbose_name='Bypass 2:1 NCD:HIV ratio')),
                ('randomize_now', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=15, verbose_name='Randomize now?')),
                ('confirm_randomize_now', models.CharField(blank=True, max_length=15, null=True, verbose_name='If YES, please confirm by typing the word RANDOMIZE here')),
                ('randomized', models.BooleanField(blank=True, default=False)),
                ('randomized_datetime', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Patient Group',
                'verbose_name_plural': 'Patient Groups',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
                'default_manager_name': 'objects',
            },
            managers=[
                ('objects', intecomm_group.models.patient_group.PatientGroupManager()),
                ('on_site', edc_sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='PatientGroupAppointment',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60, verbose_name='Hostname created')),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50, verbose_name='Hostname modified')),
                ('device_created', models.CharField(blank=True, max_length=10, verbose_name='Device created')),
                ('device_modified', models.CharField(blank=True, max_length=10, verbose_name='Device modified')),
                ('locale_created', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale created')),
                ('locale_modified', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale modified')),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow)),
                ('appt_datetime', models.DateTimeField()),
                ('appt_status', models.CharField(choices=[('new', 'Scheduled'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='new', max_length=25)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Patient Group Appointment',
                'verbose_name_plural': 'Patient Group Appointments',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
                'default_manager_name': 'objects',
            },
            managers=[
                ('on_site', edc_sites.managers.CurrentSiteManager()),
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PatientGroupMeeting',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60, verbose_name='Hostname created')),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50, verbose_name='Hostname modified')),
                ('device_created', models.CharField(blank=True, max_length=10, verbose_name='Device created')),
                ('device_modified', models.CharField(blank=True, max_length=10, verbose_name='Device modified')),
                ('locale_created', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale created')),
                ('locale_modified', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale modified')),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('Attended', 'Attended')], default='scheduled', max_length=25)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow)),
                ('meeting_datetime', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Patient Group Meeting',
                'verbose_name_plural': 'Patient Groups Meeting',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
                'default_manager_name': 'objects',
            },
            managers=[
                ('on_site', edc_sites.managers.CurrentSiteManager()),
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CommunityCareLocation',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60, verbose_name='Hostname created')),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50, verbose_name='Hostname modified')),
                ('device_created', models.CharField(blank=True, max_length=10, verbose_name='Device created')),
                ('device_modified', models.CharField(blank=True, max_length=10, verbose_name='Device modified')),
                ('locale_created', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale created')),
                ('locale_modified', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale modified')),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField()),
                ('name', models.CharField(max_length=25, null=True, unique=True)),
                ('opening_date', models.DateField()),
                ('closing_date', models.DateField(blank=True, help_text="Complete the 'closing' date if the location is no longer being used by any group", null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=25)),
                ('location_type_other', edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...')),
                ('gps', models.CharField(blank=True, help_text='copy and paste directly from google maps', max_length=50, null=True)),
                ('latitude', models.FloatField(blank=True, help_text='in degrees. copy and paste directly from google maps', null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(blank=True, help_text='in degrees. copy and paste directly from google maps', null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('location_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='intecomm_lists.locationtypes')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'Community Care Location',
                'verbose_name_plural': 'Community Care Locations',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
                'default_manager_name': 'objects',
            },
            managers=[
                ('on_site', edc_sites.managers.CurrentSiteManager()),
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPatientFollowupCall',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60, verbose_name='Hostname created')),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50, verbose_name='Hostname modified')),
                ('device_created', models.CharField(blank=True, max_length=10, verbose_name='Device created')),
                ('device_modified', models.CharField(blank=True, max_length=10, verbose_name='Device modified')),
                ('locale_created', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale created')),
                ('locale_modified', models.CharField(blank=True, help_text='Auto-updated by Modeladmin', max_length=10, null=True, verbose_name='Locale modified')),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('report_datetime', models.DateTimeField(db_index=True, default=edc_utils.date.get_utcnow)),
                ('contact_number', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, validators=[edc_model.validators.phone.phone_number])),
                ('alt_contact_number', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_model.validators.phone.phone_number])),
                ('answered', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, null=True)),
                ('respondent', models.CharField(choices=[('patient', 'Patient'), ('family', 'Family'), ('friend', 'friend'), ('OTHER', 'other'), ('N/A', 'Not applicable')], default='N/A', max_length=15)),
                ('survival_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('not_sure', 'Not sure'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Is the participant known to be alive')),
                ('catchment_area', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('not_sure', 'Not sure'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Does the participant still reside within the catchment area')),
                ('last_appt_date', models.DateField(blank=True, help_text='This may be helpful when updating health records', null=True, verbose_name='When did the patient last seek care')),
                ('last_attend_clinic', models.CharField(blank=True, help_text='This may be helpful when updating health records', max_length=25, null=True, verbose_name='Where did the patient last seek care')),
                ('last_attend_clinic_other', edc_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...')),
                ('next_appt_date', models.DateField(blank=True, null=True, verbose_name='When will the patient next attend')),
                ('call_again', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, verbose_name='May we call again?')),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=71, null=True, verbose_name='Note')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Patient Followup Call',
                'verbose_name_plural': 'historical Patient Followup Calls',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]