# Generated by Django 2.2.4 on 2019-09-14 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(default=100)),
                ('category', models.CharField(choices=[('gaming', 'gaming'), ('servers', 'servers'), ('casual', 'casual use'), ('general', 'general')], max_length=10)),
                ('labels', models.CharField(choices=[('p', 'primary'), ('e', 'secondary'), ('d', 'danger')], max_length=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.png', upload_to='products')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='orderitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.item')),
                ('user', models.ForeignKey(default="User.objects.get(username='sujit')", on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateTimeField(auto_now_add=True)),
                ('orderdate', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='ecom.orderitem')),
                ('user', models.ForeignKey(default="User.objects.get(username='sujit')", on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
