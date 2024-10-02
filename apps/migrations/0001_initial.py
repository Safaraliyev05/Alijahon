# Generated by Django 5.1.1 on 2024-10-01 06:55

import apps.models.managers
import apps.models.proxy_manager
import django.db.models.deletion
import django.utils.timezone
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='categories/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yaratilgan Vaqti')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yangilangan Vaqti')),
                ('started_at', models.DateField(verbose_name='Konkurs Boshlanish Vaqti')),
                ('ended_at', models.DateField(verbose_name='Konkurs Yakunlanish Vaqti')),
                ('image', models.ImageField(upload_to='competition/', verbose_name='Konkurs Uchun Rasm')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Konkurs Uchun Tavsif')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Tuman Nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Viloyat Nomi')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_price_regions', models.PositiveIntegerField(db_default=0, verbose_name='Viloyatlar Uchun Yetkazib Berish Narxi')),
                ('delivery_price_tashkent_region', models.PositiveIntegerField(db_default=0, verbose_name='Toshkent Viloyati Uchun Yetkazib Berish Narxi')),
                ('delivery_price_tashkent', models.PositiveIntegerField(db_default=0, verbose_name='Toshkent shahri Uchun Yetkazib Berish Narxi')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='Telefon Raqam')),
                ('about', models.TextField(blank=True, null=True, verbose_name='User Haqida')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Manzil')),
                ('telegram_id', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Telegram Id')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Rasmi')),
                ('type', models.CharField(choices=[('operator', 'Operator'), ('manager', 'Manager'), ('admin_side', 'Admin_side'), ('currier', 'Currier'), ('user', 'User')], default='user', max_length=25, verbose_name='Foydalanuvchi Turi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.district', verbose_name='Tuman')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', apps.models.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminUserProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Adminlar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.user',),
            managers=[
                ('objects', apps.models.proxy_manager.AdminUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DriverUserProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Kuryer',
                'verbose_name_plural': 'Kuryerlar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.user',),
            managers=[
                ('objects', apps.models.proxy_manager.DriverUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ManagerUserProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managerlar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.user',),
            managers=[
                ('objects', apps.models.proxy_manager.ManagerUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='OperatorUserProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Operator',
                'verbose_name_plural': 'Operatorlar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.user',),
            managers=[
                ('objects', apps.models.proxy_manager.OperatorUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Foydalanuvchilar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.user',),
            managers=[
                ('objects', apps.models.proxy_manager.UserUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Categoriya',
                'verbose_name_plural': 'Categoriyalar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.category',),
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
        ),
        migrations.CreateModel(
            name='FavouritesProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Layk',
                'verbose_name_plural': 'Layklar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.favourite',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yaratilgan Vaqti')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yangilangan Vaqti')),
                ('quantity', models.PositiveSmallIntegerField(db_default=1, verbose_name='Buyurtma Soni')),
                ('phone', models.CharField(max_length=12, verbose_name='Buyurtma Beruvchining Telefon Raqami')),
                ('full_name', models.CharField(max_length=255, verbose_name='Buyurtma Qabul Qiluvchi')),
                ('status', models.CharField(choices=[('new', 'New'), ('ready', 'Ready'), ('deliver', 'Deliver'), ('delivered', 'Delivered'), ('cant_phone', 'Cant_phone'), ('canceled', 'Canceled'), ('returned', 'Returned'), ('archived', 'Archived'), ('hold', 'Hold')], default='new', max_length=255, verbose_name='Buyurtma Holati')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.district', verbose_name='Buyurtma Yetkaziladigan Tuman')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Buyurtma Beruvchi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArchivedOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Arhivlangan Buyurtma',
                'verbose_name_plural': 'Arhivlandi',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='CanceledOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Bekor qilingan Buyurtma',
                'verbose_name_plural': 'Bekor qilindi',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='CantPhoneOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Telefon Kutarmmadi',
                'verbose_name_plural': 'Telefon kutarmadi',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='DeliveredOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Yetkazilgan Buyurtma',
                'verbose_name_plural': 'Yetkazildi',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='DeliverOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Yetkazilayotgan Buyurtma',
                'verbose_name_plural': 'Yetkazilmoqda',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='HoldOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Hold',
                'verbose_name_plural': 'Hold',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='NewOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Yangi Buyurtma',
                'verbose_name_plural': 'Yangi',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='OrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='ReadyOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Dastavkaga tayyor Buyurtma',
                'verbose_name_plural': 'Dastavkaga tayyor',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='ReturnedOrderProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Qaytib keldi',
                'verbose_name_plural': 'Qaytib keldi',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yaratilgan Vaqti')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yangilangan Vaqti')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Mahsulot Haqida')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Mahsulot Rasmi')),
                ('price', models.PositiveIntegerField(verbose_name='Mahsulot Narxi')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Mahsulot Soni')),
                ('payment_referral', models.PositiveIntegerField(blank=True, default=0, help_text="so'mda", null=True, verbose_name='Oqim Egasiga Beriladigan Pul')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='apps.category', verbose_name='Mahsulot Categoriasi')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.product', verbose_name='Buyurtmaga Tegishli Mahsulot'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='apps.product', verbose_name='Mahsulot'),
        ),
        migrations.CreateModel(
            name='ProductProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.product',),
        ),
        migrations.AddField(
            model_name='order',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.region', verbose_name='Buyurtma Yetkaziladigan Viloyat'),
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.region', verbose_name='Viloyat'),
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yaratilgan Vaqti')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yangilangan Vaqti')),
                ('name', models.CharField(max_length=255, verbose_name='Oqim Nomi')),
                ('discount', models.IntegerField(db_default=0, verbose_name='Oqimning Chegirma Narhi')),
                ('visit_count', models.PositiveIntegerField(default=0, verbose_name='Tashriflar Soni')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Oqim Egasi')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.product', verbose_name='Oqimning Mahsuloti')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='apps.stream', verbose_name='Buyurtma Oqimi'),
        ),
    ]
