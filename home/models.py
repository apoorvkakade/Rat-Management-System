from django.db import models
from nameapp.models import mouse_species
import datetime
# # Create your models here.
#

class Entry(models.Model):
    species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
    entry_date=models.DateField(auto_now_add=True,blank=True)

    q_opening_m=models.IntegerField(default=0)
    q_opening_f=models.IntegerField(default=0)
    q_na_m=models.IntegerField(default=0)
    q_na_f=models.IntegerField(default=0)
    q_dead_m=models.IntegerField(default=0)
    q_dead_f=models.IntegerField(default=0)
    q_exp_m=models.IntegerField(default=0)
    q_exp_f=models.IntegerField(default=0)
    q_bre_m=models.IntegerField(default=0)
    q_bre_f=models.IntegerField(default=0)
    q_total_m=models.IntegerField(default=0)
    q_total_f=models.IntegerField(default=0)

    p_opening=models.IntegerField(default=0)
    p_na=models.IntegerField(default=0)
    p_dead=models.IntegerField(default=0)
    p_total=models.IntegerField(default=0)

    y_opening_m=models.IntegerField(default=0)
    y_opening_f=models.IntegerField(default=0)
    y_na_m=models.IntegerField(default=0)
    y_na_f=models.IntegerField(default=0)
    y_dead_m=models.IntegerField(default=0)
    y_dead_f=models.IntegerField(default=0)
    y_exp_m=models.IntegerField(default=0)
    y_exp_f=models.IntegerField(default=0)
    y_bre_m=models.IntegerField(default=0)
    y_bre_f=models.IntegerField(default=0)
    y_total_m=models.IntegerField(default=0)
    y_total_f=models.IntegerField(default=0)

    e_opening_m=models.IntegerField(default=0)
    e_opening_f=models.IntegerField(default=0)
    e_na_m=models.IntegerField(default=0)
    e_na_f=models.IntegerField(default=0)
    e_dead_m=models.IntegerField(default=0)
    e_dead_f=models.IntegerField(default=0)
    e_total_m=models.IntegerField(default=0)
    e_total_f=models.IntegerField(default=0)

    b_opening_m=models.IntegerField(default=0)
    b_opening_f=models.IntegerField(default=0)
    b_na_m=models.IntegerField(default=0)
    b_na_f=models.IntegerField(default=0)
    b_dead_m=models.IntegerField(default=0)
    b_dead_f=models.IntegerField(default=0)
    b_total_m=models.IntegerField(default=0)
    b_total_f=models.IntegerField(default=0)

    preg_opening=models.IntegerField(default=0)
    preg_dead=models.IntegerField(default=0)
    preg_na=models.IntegerField(default=0)
    preg_total=models.IntegerField(default=0)

    w_opening=models.IntegerField(default=0)
    w_mother=models.IntegerField(default=0)
    w_dead=models.IntegerField(default=0)
    w_total=models.IntegerField(default=0)

    g_total_m=models.IntegerField(default=0)
    g_total_f=models.IntegerField(default=0)

    class Meta:
        unique_together=(("species","entry_date"),)


# class Quarantine(models.Model):
#     species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
#     entry_date=models.DateField(auto_now_add=True,blank=True)
#     opening_m=models.IntegerField(default=0)
#     opening_f=models.IntegerField(default=0)
#     newly_added_m=models.IntegerField(default=0)
#     newly_added_f=models.IntegerField(default=0)
#     dead_m=models.IntegerField(default=0)
#     dead_f=models.IntegerField(default=0)
#     experimental_issue_m=models.IntegerField(default=0)
#     experimental_issue_f=models.IntegerField(default=0)
#     breeding_issue_m=models.IntegerField(default=0)
#     breeding_issue_f=models.IntegerField(default=0)
#     total_m=models.IntegerField(default=0)
#     total_f=models.IntegerField(default=0)
#
#     class Meta:
#         unique_together=(("species","entry_date"),)
#
# class Pups(models.Model):
#     species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
#
#     entry_date = models.DateField(auto_now_add=True,blank=True)
#     opening=models.IntegerField(default=0)
#     newly_added=models.IntegerField(default=0)
#     dead=models.IntegerField(default=0)
#     total=models.IntegerField(default=0)
#
#     class Meta:
#         unique_together=(("species","entry_date"),)
#
#
# class Young(models.Model):
#     species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
#
#     entry_date = models.DateField(auto_now_add=True,blank=True)
#     opening_m=models.IntegerField(default=0)
#     opening_f=models.IntegerField(default=0)
#     newly_added_m=models.IntegerField(default=0)
#     newly_added_f=models.IntegerField(default=0)
#     dead_m=models.IntegerField(default=0)
#     dead_f=models.IntegerField(default=0)
#     experiment_issue_m=models.IntegerField(default=0)
#     experiment_issue_f=models.IntegerField(default=0)
#     breeding_issue_m=models.IntegerField(default=0)
#     breeding_issue_f=models.IntegerField(default=0)
#     total_m=models.IntegerField(default=0)
#     total_f=models.IntegerField(default=0)
#
#     class Meta:
#         unique_together=(("species","entry_date"),)
#
# class Experimental(models.Model):
#     species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
#
#     entry_date = models.DateField(auto_now_add=True,blank=True)
#     opening_m=models.IntegerField(default=0)
#     opening_f=models.IntegerField(default=0)
#     newly_added_m=models.IntegerField(default=0)
#     newly_added_f=models.IntegerField(default=0)
#     dead_m=models.IntegerField(default=0)
#     dead_f=models.IntegerField(default=0)
#     total_m=models.IntegerField(default=0)
#     total_f=models.IntegerField(default=0)
#     class Meta:
#         unique_together=(("species","entry_date"),)
#
# class Breeding(models.Model):
#     species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
#
#     entry_date = models.DateField(auto_now_add=True,blank=True)
#     opening_m=models.IntegerField(default=0)
#     opening_f=models.IntegerField(default=0)
#     newly_added_m=models.IntegerField(default=0)
#     newly_added_f=models.IntegerField(default=0)
#     dead_m=models.IntegerField(default=0)
#     dead_f=models.IntegerField(default=0)
#     total_m=models.IntegerField(default=0)
#     total_f=models.IntegerField(default=0)
#
#     class Meta:
#         unique_together=(("species","entry_date"),)
#
# class Pregnant(models.Model):
#     species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
#
#     entry_date = models.DateField(auto_now_add=True,blank=True)
#     opening=models.IntegerField(default=0)
#     newly_added=models.IntegerField(default=0)
#     dead=models.IntegerField(default=0)
#     total=models.IntegerField(default=0)
#     class Meta:
#         unique_together=(("species","entry_date"),)
#
# class Weaning(models.Model):
#     species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
#
#     entry_date = models.DateField(auto_now_add=True,blank=True)
#     opening=models.IntegerField(default=0)
#     mother=models.IntegerField(default=0)
#     dead=models.IntegerField(default=0)
#     total=models.IntegerField(default=0)
#     class Meta:
#         unique_together=(("species","entry_date"),)
#
# class Grand_total(models.Model):
#     species=models.ForeignKey(mouse_species,on_delete=models.CASCADE,default=1)
#
#     entry_date = models.DateField(auto_now_add=True,blank=True)
#     total_m=models.IntegerField(default=0)
#     total_f=models.IntegerField(default=0)
#
#     class Meta:
#
#         unique_together=(("species","entry_date"),)
#
#
#
#
#
