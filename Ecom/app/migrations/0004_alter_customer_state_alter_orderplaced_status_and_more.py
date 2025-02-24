# Generated by Django 5.1.3 on 2025-01-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Tripura', 'Tripura'), ('Meghalaya', 'Meghalaya'), ('Punjab', 'Punjab'), ('Tamil Nadu', 'Tamil Nadu'), ('Sikkim', 'Sikkim'), ('Mizoram', 'Mizoram'), ('Odisha', 'Odisha'), ('West Bengal', 'West Bengal'), ('Telangana', 'Telangana'), ('Nagaland', 'Nagaland'), ('Delhi', 'Delhi'), ('Uttarakhand', 'Uttarakhand'), ('Maharashtra', 'Maharashtra'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Rajasthan', 'Rajasthan'), ('Goa', 'Goa'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Gujrat', 'Gujrat'), ('Puducherry', 'Puducherry'), ('Chandigarh', 'Chandigarh'), ('Adaman & Nicobar Island', 'Adaman & Nicobar Island'), ('Bihar', 'Bihar'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('chattisgarh', 'chattisgarh')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('On the way', 'On the way'), ('Packed', 'Packed'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('top wear', 'Top Wear'), ('electronics', 'Electronics'), ('mobile', 'Mobile'), ('bottom wear', 'Bottom Wear'), ('glasses', 'Glasses')], max_length=20),
        ),
    ]
