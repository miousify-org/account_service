# Generated by Django 3.0.1 on 2020-01-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MStore',
            fields=[
                ('phone', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('lga', models.CharField(max_length=20, null=True)),
                ('zip_code', models.CharField(max_length=10, null=True)),
                ('user_account', models.CharField(max_length=30, null=True)),
                ('miousify_domain_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False, null=True)),
                ('trial_expired', models.BooleanField(default=False, null=True)),
                ('plan', models.CharField(choices=[('basic', 'basic'), ('premium', 'premium'), ('enterprise', 'enterprise')], max_length=15)),
                ('miousify_store_resource_id', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
