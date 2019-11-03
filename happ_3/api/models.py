from django.db import models

# caracteristiques table 

class caracteristiques(models.Model):
    Num_Acc  = models.BigIntegerField(blank=True, null=False,unique= True, primary_key=True)
    annee  = models.IntegerField(blank=True, null=True)
    mois =  models.IntegerField(blank=True, null=True)
    jour= models.IntegerField(blank=True, null=True)
    heure_min_acc = models.IntegerField(blank=True, null=True) 
    lumiere =models.IntegerField(blank=True, null=True)
    agg_localisation = models.IntegerField(blank=True, null=True)
    intersection= models.IntegerField(blank=True, null=True)
    atmosphere = models.IntegerField(blank=True, null=True)
    collison = models.IntegerField(blank=True, null=True)
    commune = models.IntegerField(blank=True,null=True)
    adresse = models.CharField(max_length=30, blank=True, null=True)
    gps = models.CharField(max_length=30,blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    departement = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'Caracteristiques'
    def __str__(self):
        return "{}".format(self.Num_Acc)
    

# lieux table 
class lieux(models.Model):
    Num_Acc = models.BigIntegerField(blank=True, null=False,unique= True, primary_key=True)
    cat_route = models.IntegerField( blank=True, null=True)
    voie = models.IntegerField( blank=True, null=True)
    v1 = models.CharField(max_length=30,blank=True, null=True)
    v2 =models.CharField(max_length=30,blank=True, null=True)
    circulation = models.IntegerField( blank=True, null=True)
    nbv_total = models.IntegerField( blank=True, null=True)
    pr =  models.IntegerField(blank=True, null=True)
    pr1 =  models.IntegerField( blank=True, null=True)
    vosp =  models.IntegerField( blank=True, null=True)
    prof =  models.IntegerField( blank=True, null=True)
    plan =  models.IntegerField( blank=True, null=True)
    lartpc =  models.IntegerField( blank=True, null=True)
    larrout =  models.IntegerField( blank=True, null=True)
    surf =  models.IntegerField( blank=True, null=True)
    infra =  models.IntegerField( blank=True, null=True)
    situ =  models.IntegerField( blank=True, null=True)
    env1 =  models.IntegerField( blank=True, null=True)
    
    class Meta:
        db_table = 'lieux'
    def __str__(self):
        return "{}".format(self.Num_Acc)
    
# usagers table         
class usagers(models.Model):
    Num_Acc = models.BigIntegerField(unique = True, null = False, primary_key=True, blank = True )
    place = models.IntegerField(blank = True, null = True)
    catu_usager =  models.IntegerField(blank = True, null = True)
    gravite = models.IntegerField(blank = True, null = True)
    sexe = models.IntegerField(blank = True, null = True)
    trajet = models.IntegerField(blank = True, null = True)
    secu = models.IntegerField(blank = True, null = True) 
    localisation_pie = models.IntegerField(blank = True, null = True)
    acttion_piet = models.IntegerField(blank = True, null = True)
    etatp = models.IntegerField(blank = True, null = True)
    annee_nais = models.IntegerField(blank = True, null = True)
    num_veh  = models.CharField(max_length=30,blank=True, null=True)
    
    class Meta :
        db_table = 'usagers'
    def __str__(self):
        return "{}".format(self.Num_Acc)

# vehicules table 
class vehicules(models.Model):
    Num_Acc = models.BigIntegerField(unique = True, null = False, primary_key=True, blank = True )
    senc = models.IntegerField(blank = True, null  = True)
    catv = models.IntegerField(blank = True, null  = True)
    occutc = models.IntegerField(blank = True, null  = True)
    obs = models.IntegerField(blank = True, null  = True)
    obsm = models.IntegerField(blank = True, null  = True)
    choc = models.IntegerField(blank = True, null  = True)
    manv = models.IntegerField(blank = True, null  = True)
    num_veh = models.CharField(max_length=30,blank=True, null=True)
    
    class Meta:
        db_table = 'vehicules'
    def __str__(self):
        return "{}".format(self.Num_Acc)
        
# table contains all the data

class acc_data(models.Model):
    Num_Acc = models.BigIntegerField(unique = True, null = False, primary_key=True, blank = True )
    annee  = models.IntegerField(blank=True, null=True)
    mois =  models.IntegerField(blank=True, null=True)
    jour= models.IntegerField(blank=True, null=True)
    heure_min_acc = models.IntegerField(blank=True, null=True) 
    lumiere =models.IntegerField(blank=True, null=True)
    agg_localisation = models.IntegerField(blank=True, null=True)
    intersection= models.IntegerField(blank=True, null=True)
    atmosphere = models.IntegerField(blank=True, null=True)
    collison = models.IntegerField(blank=True, null=True)
    commune = models.IntegerField(blank=True,null=True)
    adresse = models.CharField(max_length=30, blank=True, null=True)
    gps = models.CharField(max_length=30,blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    departement = models.IntegerField(blank=True, null=True)
    cat_route = models.IntegerField( blank=True, null=True)
    voie = models.IntegerField( blank=True, null=True)
    v1 = models.CharField(max_length=30,blank=True, null=True)
    v2 =models.CharField(max_length=30,blank=True, null=True)
    circulation = models.IntegerField( blank=True, null=True)
    nbv_total = models.IntegerField( blank=True, null=True)
    pr =  models.IntegerField(blank=True, null=True)
    pr1 =  models.IntegerField( blank=True, null=True)
    vosp =  models.IntegerField( blank=True, null=True)
    prof =  models.IntegerField( blank=True, null=True)
    plan =  models.IntegerField( blank=True, null=True)
    lartpc =  models.IntegerField( blank=True, null=True)
    larrout =  models.IntegerField( blank=True, null=True)
    surf =  models.IntegerField( blank=True, null=True)
    infra =  models.IntegerField( blank=True, null=True)
    situ =  models.IntegerField( blank=True, null=True)
    env1 =  models.IntegerField( blank=True, null=True)
    place = models.IntegerField(blank = True, null = True)
    catu_usager =  models.IntegerField(blank = True, null = True)
    gravite = models.IntegerField(blank = True, null = True)
    sexe = models.IntegerField(blank = True, null = True)
    trajet = models.IntegerField(blank = True, null = True)
    secu = models.IntegerField(blank = True, null = True) 
    localisation_pie = models.IntegerField(blank = True, null = True)
    acttion_piet = models.IntegerField(blank = True, null = True)
    etatp = models.IntegerField(blank = True, null = True)
    annee_nais = models.IntegerField(blank = True, null = True)
    num_veh_usager  = models.CharField(max_length=30,blank=True, null=True)
    senc = models.IntegerField(blank = True, null  = True)
    catv = models.IntegerField(blank = True, null  = True)
    occutc = models.IntegerField(blank = True, null  = True)
    obs = models.IntegerField(blank = True, null  = True)
    obsm = models.IntegerField(blank = True, null  = True)
    choc = models.IntegerField(blank = True, null  = True)
    manv = models.IntegerField(blank = True, null  = True)
    num_veh_vehicule = models.CharField(max_length=30,blank=True, null=True)
    class Meta:
        db_table = 'acc_data'
    def __str__(self):
        return "{}".format(self.Num_Acc)