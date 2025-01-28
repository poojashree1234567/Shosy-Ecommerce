# Generated by Django 5.1.3 on 2025-01-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Rajasthan', 'Rajasthan'), ('chattisgarh', 'chattisgarh'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Punjab', 'Punjab'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Meghalaya', 'Meghalaya'), ('West Bengal', 'West Bengal'), ('Delhi', 'Delhi'), ('Maharashtra', 'Maharashtra'), ('Odisha', 'Odisha'), ('Gujrat', 'Gujrat'), ('Adaman & Nicobar Island', 'Adaman & Nicobar Island'), ('Uttarakhand', 'Uttarakhand'), ('Sikkim', 'Sikkim'), ('Bihar', 'Bihar'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Puducherry', 'Puducherry'), ('Goa', 'Goa'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Assam', 'Assam'), ('Nagaland', 'Nagaland'), ('Chandigarh', 'Chandigarh'), ('Tamil Nadu', 'Tamil Nadu'), ('Mizoram', 'Mizoram'), ('Tripura', 'Tripura'), ('Telangana', 'Telangana')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('On the way', 'On the way'), ('Packed', 'Packed'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('mobile', 'Mobile'), ('top wear', 'Top Wear'), ('laptops', 'laptops'), ('bottom wear', 'Bottom Wear'), ('glasses', 'Glasses')], max_length=20),
        ),
    ]
