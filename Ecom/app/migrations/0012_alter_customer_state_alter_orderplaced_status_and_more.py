# Generated by Django 5.1.3 on 2025-01-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Mizoram', 'Mizoram'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Gujrat', 'Gujrat'), ('Goa', 'Goa'), ('Odisha', 'Odisha'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Chandigarh', 'Chandigarh'), ('Delhi', 'Delhi'), ('Adaman & Nicobar Island', 'Adaman & Nicobar Island'), ('West Bengal', 'West Bengal'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Meghalaya', 'Meghalaya'), ('chattisgarh', 'chattisgarh'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Nagaland', 'Nagaland'), ('Rajasthan', 'Rajasthan'), ('Maharashtra', 'Maharashtra'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Assam', 'Assam'), ('Punjab', 'Punjab'), ('Uttarakhand', 'Uttarakhand'), ('Puducherry', 'Puducherry'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Bihar', 'Bihar')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('On the way', 'On the way'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Accepted', 'Accepted')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('bottom wear', 'Bottom Wear'), ('laptops', 'laptops'), ('mobile', 'Mobile'), ('glasses', 'Glasses'), ('top wear', 'Top Wear')], max_length=20),
        ),
    ]
