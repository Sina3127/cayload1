from django.db import models

class Track(models.Model):
    container_number = models.CharField(max_length=100)
    hbl_number = models.CharField(max_length=100)
    mbl_number = models.CharField(max_length=100)

    shipper = models.CharField(max_length=100)
    consignee = models.CharField(max_length=100)
    vessel_name = models.CharField(max_length=100)
    voyage_number = models.CharField(max_length=100)

    port_of_loading = models.CharField(max_length=100)
    port_of_discharge = models.CharField(max_length=100)
    dispatched_date = models.DateField()
    transit_port = models.CharField(max_length=100)
    arrival_date_to_transit_port = models.DateField()
    dispatch_date_to_final_port = models.DateField()
    load_on_rail = models.DateField()
    arrival_to_final_destination = models.DateField()
    date_of_arriving_to_warehouse = models.DateField()
    pick_up_date_of_warehouse = models.DateField()
    release_status = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=100)