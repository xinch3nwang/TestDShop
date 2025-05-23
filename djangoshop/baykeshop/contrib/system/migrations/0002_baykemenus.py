# Generated by Django 4.2.17 on 2024-12-13 05:47

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sites', '0002_alter_domain_unique'),
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaykeMenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=50, verbose_name='菜单名称')),
                ('icon', models.CharField(blank=True, default='', max_length=50, verbose_name='菜单图标')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('order', models.IntegerField(default=0, verbose_name='排序')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.baykemenus', verbose_name='父级菜单')),
                ('permission', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.permission', verbose_name='权限')),
                ('site', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='站点')),
            ],
            options={
                'verbose_name': '自定义菜单',
                'verbose_name_plural': '自定义菜单',
                'ordering': ['order'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('current_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
