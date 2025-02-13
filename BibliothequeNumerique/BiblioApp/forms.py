from django import forms
from BiblioAPI.models import *

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ('titre','langueLivre','annee_publication','nombrepages','imageLivre','auteur','id_emplacement')
        widgets ={
            'titre': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'langueLivre': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'annee_publication': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'nombrepages': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'imageLivre': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'auteur': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'id_emplacement': forms.CharField(
               
            )
        }


class EmplacementForm(forms.ModelForm):
    class Meta:
        model = Emplacement
        fields = ('numero',)
        widgets ={
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            }
        
class EtagereForm(forms.ModelForm):
    class Meta:
        model = Etagere
        fields = ('nom','etat_etagere','mobilite','charge_maximal','id_emplacement')
        widgets ={
            'nom': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
              'etat_etagere': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
                'mobilite': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'charge_maximal': forms.NumberInput(attrs={'class': 'form-control'}),
                'id_emplacement': forms.CharField()
            }
               
class CompartimentForm(forms.ModelForm):
    class Meta:
        model = Compartiment
        fields = ('nom','nombreLivre','etagere')
        widgets ={
            'nom': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
              'nombreLivre': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
                'etagere': forms.CharField(
                
            )
            }
        