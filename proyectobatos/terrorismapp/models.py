# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gname(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    gname = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'gname'
        unique_together = (('eventid', 'gname'),)


class Incidentes(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    crit1 = models.IntegerField(blank=True, null=True)
    crit2 = models.IntegerField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    suicide = models.IntegerField(blank=True, null=True)
    nkill = models.FloatField(blank=True, null=True)
    nkillter = models.FloatField(blank=True, null=True)
    nwound = models.FloatField(blank=True, null=True)
    nwoundte = models.FloatField(blank=True, null=True)
    perpcapture = models.FloatField(blank=True, null=True)
    propdamage = models.FloatField(blank=True, null=True)
    int_log = models.FloatField(blank=True, null=True)
    int_ideo = models.FloatField(blank=True, null=True)
    motive = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidentes'


class Lugar(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=400, blank=True, null=True)
    provstate = models.CharField(max_length=400, blank=True, null=True)
    city = models.CharField(max_length=400, blank=True, null=True)
    vicinity = models.FloatField(blank=True, null=True)
    specificity = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lugar'


class Secuestros(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    nhostkid = models.FloatField(blank=True, null=True)
    nhours = models.FloatField(blank=True, null=True)
    ndays = models.FloatField(blank=True, null=True)
    hostkidoutcome = models.CharField(max_length=500, blank=True, null=True)
    nreleased = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secuestros'


# class TerrorismappGname(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     eventid = models.BigIntegerField()
#     gname = models.CharField(max_length=450)

#     class Meta:
#         managed = False
#         db_table = 'terrorismapp_gname'
#         unique_together = (('eventid', 'gname'),)


class Tiempo(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    iyear = models.IntegerField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiempo'


class Tipoarma(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    weapontype = models.CharField(max_length=500)
    weaponsubtype = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'tipoarma'
        unique_together = (('eventid', 'weapontype', 'weaponsubtype'),)


class Tipoataque(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    attacktype = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'tipoataque'
        unique_together = (('eventid', 'attacktype'),)


class Tipotarget(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    targtype = models.CharField(max_length=500)
    targsubtype = models.CharField(max_length=500)
    corp = models.CharField(max_length=500)
    natlty = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'tipotarget'
        unique_together = (('eventid', 'targtype', 'targsubtype', 'corp', 'natlty'),)