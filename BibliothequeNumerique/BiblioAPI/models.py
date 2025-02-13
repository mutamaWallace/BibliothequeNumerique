from django.db import models

# Create your models here.
class Emprunt(models.Model):
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Emprunt {self.id} - {self.date_emprunt}"

class Personne(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('A', 'Autre'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Vous devriez envisager d'utiliser un hachage pour les mots de passe.
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    profil = models.ImageField(upload_to='photos_passport/', null=True, blank=True) # Champ pour la photo
    tel = models.CharField(max_length=15, blank=True)  # Numéro de téléphone
    matricule = models.CharField(max_length=50, unique=True)  # Matricule unique
    datenaissance = models.DateField()  # Date de naissance
    CNI = models.CharField(max_length=20, unique=True)  # Numéro de CNI
    id_emprunt = models.ForeignKey(Emprunt, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"
class Etudiant(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('A', 'Autre'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Hachage recommandé pour les mots de passe
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    photo_passport = models.ImageField(upload_to='photos_passport/', null=True, blank=True)  # Champ pour la photo
    datenaissance = models.DateField()  # Date de naissance
    id_emprunt = models.ForeignKey(Emprunt, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"
class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Emplacement(models.Model):
    numero = models.CharField(max_length=20, unique=True)  #numero unique de cette emplacement

    def __str__(self):
        return self.numero


class Livre(models.Model):
    LANGUE_CHOICES = [
        ('FR', 'Français'),
        ('EN', 'Anglais'),
        ('ES', 'Espagnol'),
        ('DE', 'Allemand'),
        # Ajoutez d'autres langues si nécessaire
    ]

    titre = models.CharField(max_length=200)
    langueLivre = models.CharField(max_length=2, choices=LANGUE_CHOICES)
    annee_publication = models.PositiveIntegerField()
    nombrepages = models.PositiveIntegerField()
    imageLivre = models.ImageField(upload_to='images_livres/', null=True, blank=True)  # Champ pour l'image
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    id_emplacement = models.ForeignKey(Emplacement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} {self.langueLivre} {self.annee_publication} {self.nombrepages} {self.imageLivre}"
class Etranger(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('A', 'Autre'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Hachage recommandé pour les mots de passe
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    photo_passport = models.ImageField(upload_to='photos_passport/', null=True, blank=True)  # Champ pour la photo
    datenaissance = models.DateField()  # Date de naissance
    CNI = models.CharField(max_length=20, unique=True)  # Numéro de CNI
    id_emprunt = models.ForeignKey(Emprunt, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"
class Abonnement(models.Model):
    type_abonnement = models.CharField(max_length=100)#type d'un abonnement
    date_debut = models.DateField()  #date debut de l'abonnement
    date_fin = models.DateField()   #date fin de l'abonnement

    def __str__(self):
        return f"{self.type_abonnement} {self.date_debut} {self.date_fin}"

class Etagere(models.Model):
    nom = models.CharField(max_length=100)
    etat_etagere = models.CharField(max_length=50)
    mobilite = models.BooleanField(default=False)
    charge_maximal = models.DecimalField(max_digits=100, decimal_places=3)
    id_emplacement = models.ForeignKey(Emplacement, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
class Compartiment(models.Model):
    nom = models.CharField(max_length=100)
    nombreLivre = models.IntegerField()
    etagere = models.ForeignKey(Etagere, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom



class Campus(models.Model):
    campus = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.campus

class Universite(models.Model):
    nom = models.CharField(max_length=255)
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    email = models.EmailField()
    site_web = models.URLField()
    id_campus = models.ForeignKey(Campus, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom


class Faculte(models.Model):
    faculte = models.CharField(max_length=100)
    id_universite = models.ForeignKey(Universite, on_delete=models.CASCADE)

class Departement(models.Model):
    departement = models.CharField(max_length=100)
    id_faculte = models.ForeignKey(Faculte, on_delete=models.CASCADE)


class Classe(models.Model):
    niveau = models.CharField(max_length=100)
    id_departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    

    
    


    



