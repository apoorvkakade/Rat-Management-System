from django.shortcuts import render
from django.shortcuts import redirect
import datetime
from nameapp.models import mouse_species
from .models import Entry
from django.contrib import messages
from .Display import Display
# Create your views here.
def home_function(request):
    if request.user.is_authenticated:
        if request.method=='GET':
            display_object=Display()
            species=mouse_species.objects.all()

            username=request.user.username
            print(username)

            display_objects=[]
            if Entry.objects.all().exists():
                for specie in species:
                    if Entry.objects.filter(species=specie):
                        d_obj=Entry.objects.filter(species=specie).latest('entry_date')
                        display_objects.append(d_obj)
                    else:
                        display_objects.append(None)


            else:
                for i in range(len(species)):
                    display_objects.append(None)


            zip_list=zip(species,display_objects)
            # return render(request,'home.html',{'species':species,'username':username,'d_objects':display_objects})
            return render(request,'home.html',{'zip_list':zip_list,'username':username})
        elif request.method=='POST':
            date1=request.POST['entrydate']
            print("printing date")
            print(date1=="")
            if date1=="":  #date not provided so take current date to pass forward
                return redirect('update',specie_name='yoyo')
            return redirect('home')
    else:
        return redirect('login')


def checkNegative(*argv):
    for arg in argv:
        if arg<0:
            return True

    return False


def update(request,specie_name,entry_date):
    if request.user.is_authenticated:
        if request.method=='GET':
            blank_columns=[8,11,20,23,26,29]
            username=request.user.username
            return render(request,'update.html',{'data':specie_name,'entry_date':entry_date,'n':range(32),'blank_columns':blank_columns,'username':username})
        elif request.method=='POST':

            quarantine_na_M=int(request.POST['quarantine_na_M'])
            quarantine_na_F=int(request.POST['quarantine_na_F'])
            quarantine_d_M=int(request.POST['quarantine_d_M'])
            quarantine_d_F=int(request.POST['quarantine_d_F'])
            quarantine_ei_M=int(request.POST['quarantine_ei_M'])
            quarantine_ei_F=int(request.POST['quarantine_ei_F'])
            quarantine_bi_M=int(request.POST['quarantine_bi_M'])
            quarantine_bi_F=int(request.POST['quarantine_bi_F'])
            pups_pups=int(request.POST['pups_pups'])
            pups_dead=int(request.POST['pups_dead'])
            young_na_M=int(request.POST['young_na_M'])
            young_na_F=int(request.POST['young_na_F'])
            young_d_M=int(request.POST['young_d_M'])
            young_d_F=int(request.POST['young_d_F'])
            young_ei_M=int(request.POST['young_ei_M'])
            young_ei_F=int(request.POST['young_ei_F'])
            young_bi_M=int(request.POST['young_bi_M'])
            young_bi_F=int(request.POST['young_bi_F'])
            experimental_d_M=int(request.POST['exp_d_M'])
            experimental_d_F=int(request.POST['exp_d_F'])
            breeding_d_M=int(request.POST['bre_d_M'])
            breeding_d_F=int(request.POST['bre_d_F'])
            pregnant_added=int(request.POST['preg_added'])
            pregnant_dead=int(request.POST['preg_dead'])
            weaning_mother=int(request.POST['weaning_mother'])
            weaning_dead=int(request.POST['weaning_dead'])

            today=datetime.datetime.today().strftime('%Y-%m-%d')
            entry_date_obj=datetime.datetime.strptime(str(entry_date),'%Y-%m-%d').date()
            previous_day=str(entry_date_obj-datetime.timedelta(days=1))

            species_obj=mouse_species.objects.get(specie_name=specie_name)

            #if entry is already done overwrite that
            if Entry.objects.filter(species=species_obj).filter(entry_date=entry_date).exists():
                pass
            else:  ## entry not done
                if Entry.objects.filter(entry_date=str(previous_day)).exists(): ##previous record exists
                    # previous_quarantine=Quarantine.objects.get(entry_date=previous_day)
                    # previous_pups=Pups.objects.get(entry_date=previous_day)
                    # previous_young=Young.objects.get(entry_date=entry_date)
                    # previous_exp=Experimental.objects.get(entry_date=entry_date)
                    # previous_breeding=Breeding.objects.get(entry_date=entry_date)
                    # previous_preg=Pregnant.objects.get(entry_date=entry_date)
                    # previous_weaning=Weaning.objects.get(entry_date=entry_date)
                    previous_entry=Entry.objects.get(entry_date=previous_day)
                    quarantine_opening_M=previous_entry.q_total_m
                    quarantine_opening_F=previous_entry.q_total_f
                    pups_opening=previous_entry.p_opening
                    young_opening_M=previous_entry.y_opening_m
                    young_opening_F=previous_entry.y_opening_f
                    experimental_opening_M=previous_entry.e_opening_m
                    experimental_opening_F=previous_entry.e_opening_f
                    breeding_opening_M=previous_entry.b_opening_m
                    breeding_opening_F=previous_entry.b_opening_f
                    pregnant_opening = previous_entry.preg_opening
                    weaning_opening=previous_entry.w_opening

                else: ##previous record does not exist so opening stock would be 0
                    print("previous record doesnt exist")

                    quarantine_opening_M=0
                    quarantine_opening_F=0
                    pups_opening=0
                    young_opening_M=0
                    young_opening_F=0
                    experimental_opening_M=0
                    experimental_opening_F=0
                    breeding_opening_M=0
                    breeding_opening_F=0
                    pregnant_opening = 0
                    weaning_opening=0


                quarantine_total_M=quarantine_na_M+quarantine_opening_M-quarantine_d_M-quarantine_ei_M-quarantine_bi_M
                quarantine_total_F = quarantine_na_F + quarantine_opening_F - quarantine_d_F - quarantine_ei_F - quarantine_bi_F

                pups_total=pups_opening+pups_pups-pups_dead

                young_total_M=young_na_M+young_opening_M-young_d_M-young_ei_M-young_bi_M
                young_total_F = young_na_F + young_opening_F - young_d_F - young_ei_F - young_bi_F

                experimental_na_M=quarantine_ei_M+young_ei_M
                experimental_na_F = quarantine_ei_F + young_ei_F

                experimental_total_M=experimental_opening_M+experimental_na_M-experimental_d_M
                experimental_total_F=experimental_opening_F+experimental_na_F-experimental_d_F

                breeding_na_M=quarantine_bi_M+young_bi_M
                breeding_na_F=quarantine_bi_F+young_bi_F

                breeding_total_M=breeding_opening_M+breeding_na_M-breeding_d_M
                breeding_total_F=breeding_opening_F+breeding_na_F-breeding_d_F


                pregnant_total=pregnant_opening+pregnant_added-pregnant_dead

                weaning_total=weaning_mother+weaning_opening-weaning_dead

                grand_total_M=quarantine_total_M+young_total_M+experimental_total_M+breeding_total_M
                grand_total_F = quarantine_total_F + young_total_F + experimental_total_F + breeding_total_F

                    ##not allowed
                n_flag=checkNegative(quarantine_total_M,quarantine_total_F,pups_total,young_total_M,young_total_F,experimental_na_M,experimental_na_F,experimental_total_M,experimental_total_F,
                                     breeding_na_M,breeding_na_F,breeding_total_M,breeding_total_F,pregnant_total,weaning_total,grand_total_M,grand_total_F)
                if n_flag==True:
                    messages.error(request,"Update Unsuccessful, incorrect values")

                    return redirect('update',specie_name,entry_date)

                Entry_db_object=Entry()
                Entry_db_object.entry_date=entry_date
                Entry_db_object.species=species_obj

                Entry_db_object.q_opening_m=quarantine_opening_M
                Entry_db_object.q_opening_f=quarantine_opening_F
                Entry_db_object.q_na_m=quarantine_na_M
                Entry_db_object.q_na_f=quarantine_na_F
                Entry_db_object.q_dead_m=quarantine_d_M
                Entry_db_object.q_dead_f=quarantine_d_F
                Entry_db_object.q_exp_m=quarantine_ei_M
                Entry_db_object.q_exp_f=quarantine_ei_F
                Entry_db_object.q_bre_m=quarantine_bi_M
                Entry_db_object.q_bre_f = quarantine_bi_F
                Entry_db_object.q_total_m=quarantine_total_M
                Entry_db_object.q_total_f=quarantine_total_F

                Entry_db_object.p_opening=pups_opening
                Entry_db_object.p_na=pups_pups
                Entry_db_object.p_dead=pups_dead
                Entry_db_object.p_total=pups_total

                Entry_db_object.y_opening_m=young_opening_M
                Entry_db_object.y_opening_f=young_opening_F
                Entry_db_object.y_na_m=young_na_M
                Entry_db_object.y_na_f=young_na_F
                Entry_db_object.y_dead_m=young_d_M
                Entry_db_object.y_dead_f=young_d_F
                Entry_db_object.y_exp_m=young_ei_M
                Entry_db_object.y_exp_f=young_ei_F
                Entry_db_object.y_bre_m=young_bi_M
                Entry_db_object.y_bre_f=young_bi_F
                Entry_db_object.y_total_m=young_total_M
                Entry_db_object.y_total_f=young_total_F

                Entry_db_object.e_opening_m=experimental_opening_M
                Entry_db_object.e_opening_f=experimental_opening_F
                Entry_db_object.e_na_m=experimental_na_M
                Entry_db_object.e_na_f=experimental_na_F
                Entry_db_object.e_dead_m=experimental_d_M
                Entry_db_object.e_dead_f=experimental_d_F
                Entry_db_object.e_total_m=experimental_total_M
                Entry_db_object.e_total_f=experimental_total_F

                Entry_db_object.b_opening_m=breeding_opening_M
                Entry_db_object.b_opening_f=breeding_opening_F
                Entry_db_object.b_na_m=breeding_na_M
                Entry_db_object.b_na_f=breeding_na_F
                Entry_db_object.b_dead_m=breeding_d_M
                Entry_db_object.b_dead_f=breeding_d_F
                Entry_db_object.b_total_m=breeding_total_M
                Entry_db_object.b_total_f=breeding_total_F

                Entry_db_object.preg_opening=pregnant_opening
                Entry_db_object.preg_na=pregnant_added
                Entry_db_object.preg_dead=pregnant_dead
                Entry_db_object.preg_total=pregnant_total

                Entry_db_object.w_opening=weaning_opening
                Entry_db_object.w_mother=weaning_mother
                Entry_db_object.w_dead=weaning_dead
                Entry_db_object.w_total=weaning_total

                Entry_db_object.g_total_m=grand_total_M
                Entry_db_object.g_total_f=grand_total_F

                # quarantine_db_object=Quarantine(entry_date=entry_date,opening_m=quarantine_opening_M,opening_f=quarantine_opening_F,newly_added_m=quarantine_na_M,newly_added_f=quarantine_na_F,
                #                                 dead_m=quarantine_d_M,dead_f=quarantine_d_F,experimental_issue_m=quarantine_ei_M,experimental_issue_f=quarantine_ei_F,
                #                                 breeding_issue_m=quarantine_bi_M,breeding_issue_f=quarantine_bi_F,total_m=quarantine_total_M,total_f=quarantine_total_F,species=species_obj)
                # pups_db_object=Pups()
                # pups_db_object.entry_date=entry_date
                # pups_db_object.species=species_obj
                # pups_db_object.newly_added=pups_pups
                # pups_db_object.dead=pups_dead
                # pups_db_object.opening=pups_opening
                # pups_db_object.total=pups_total
                #
                #
                # young_db_object=Young()
                # young_db_object.entry_date=entry_date
                # young_db_object.species = species_obj
                # young_db_object.opening_m=young_opening_M
                # young_db_object.opening_f = young_opening_F
                # young_db_object.newly_added_m=young_na_M
                # young_db_object.newly_added_f=young_na_F
                # young_db_object.dead_m=young_d_M
                # young_db_object.dead_f=young_d_F
                # young_db_object.experiment_issue_m=young_ei_M
                # young_db_object.experiment_issue_f=young_ei_F
                # young_db_object.breeding_issue_m=young_bi_M
                # young_db_object.breeding_issue_f=young_bi_F
                # young_db_object.total_m=young_total_M
                # young_db_object.total_f=young_total_F
                #
                # experimental_db_object=Experimental()
                # experimental_db_object.entry_date=entry_date
                # experimental_db_object.species=species_obj
                # experimental_db_object.opening_m=experimental_opening_M
                # experimental_db_object.opening_f=experimental_opening_F
                # experimental_db_object.newly_added_m=experimental_na_M
                # experimental_db_object.newly_added_f=experimental_na_F
                # experimental_db_object.dead_m=experimental_d_M
                # experimental_db_object.dead_f=experimental_d_F
                # experimental_db_object.total_m=experimental_total_M
                # experimental_db_object.total_f=experimental_total_F
                #
                # breeding_db_object=Breeding()
                # breeding_db_object.entry_date=entry_date
                # breeding_db_object.species=species_obj
                # breeding_db_object.opening_m=breeding_opening_M
                # breeding_db_object.opening_f=breeding_opening_F
                # breeding_db_object.newly_added_m=breeding_na_M
                # breeding_db_object.newly_added_f = breeding_na_F
                # breeding_db_object.dead_m=breeding_d_M
                # breeding_db_object.dead_f=breeding_d_F
                # breeding_db_object.total_m=breeding_total_M
                # breeding_db_object.total_f = breeding_total_F
                #
                # pregnant_db_object=Pregnant()
                # pregnant_db_object.species=species_obj
                # pregnant_db_object.entry_date=entry_date
                # pregnant_db_object.opening=pregnant_opening
                # pregnant_db_object.newly_added=pregnant_added
                # pregnant_db_object.dead=pregnant_dead
                # pregnant_db_object.total=pregnant_total
                #
                # weaning_db_object=Weaning()
                # weaning_db_object.species=species_obj
                # weaning_db_object.opening=weaning_opening
                # weaning_db_object.entry_date=entry_date
                # weaning_db_object.mother=weaning_mother
                # weaning_db_object.dead=weaning_dead
                # weaning_db_object.total=weaning_total
                #
                # grand_total_db_object=Grand_total()
                # grand_total_db_object.species=species_obj
                # grand_total_db_object.entry_date=entry_date
                # grand_total_db_object.total_m=grand_total_M
                # grand_total_db_object.total_f=grand_total_F
                #
                #
                # quarantine_db_object.save()
                # pups_db_object.save()
                # young_db_object.save()
                # experimental_db_object.save()
                # breeding_db_object.save()
                # pregnant_db_object.save()
                # weaning_db_object.save()
                # grand_total_db_object.save()
                Entry_db_object.save()
                messages.success(request,"Update Successful")
                return redirect('update', specie_name, entry_date)


    else:
        return redirect('login')





