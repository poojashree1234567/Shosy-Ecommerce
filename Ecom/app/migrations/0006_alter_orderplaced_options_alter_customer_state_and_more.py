# Generated by Django 5.1.3 on 2025-01-22 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderplaced',
            options={'ordering': ['-ordered_date'], 'verbose_name': 'Order Placed', 'verbose_name_plural': 'Orders Placed'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Sikkim', 'Sikkim'), ('Bihar', 'Bihar'), ('Meghalaya', 'Meghalaya'), ('Adaman & Nicobar Island', 'Adaman & Nicobar Island'), ('Chandigarh', 'Chandigarh'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Nagaland', 'Nagaland'), ('Mizoram', 'Mizoram'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Tripura', 'Tripura'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Gujrat', 'Gujrat'), ('Tamil Nadu', 'Tamil Nadu'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Delhi', 'Delhi'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Assam', 'Assam'), ('Rajasthan', 'Rajasthan'), ('Telangana', 'Telangana'), ('Puducherry', 'Puducherry'), ('chattisgarh', 'chattisgarh'), ('West Bengal', 'West Bengal'), ('Maharashtra', 'Maharashtra'), ('Goa', 'Goa')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('Cancel', 'Cancel'), ('On the way', 'On the way'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('electronics', 'Electronics'), ('bottom wear', 'Bottom Wear'), ('top wear', 'Top Wear'), ('mobile', 'Mobile'), ('glasses', 'Glasses')], max_length=20),
        ),
    ]
