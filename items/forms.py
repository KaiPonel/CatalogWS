from django import forms

from .models import Item


class ItemAddForm(forms.ModelForm):
    """
        This Website was designed for a very special use case.
        If you want to implement own/other Categories Change the content below respectively.
    """



    name = forms.CharField(label="Titel", max_length=100, required=True, widget=forms.TextInput(attrs={"placeholder": "Name des Objektes"}))
    artist = forms.CharField(label="Künstler", max_length=100, required=False,  widget=forms.TextInput(attrs={"placeholder": "Künstler des Objekts"}))
    quantity = forms.IntegerField(label="Anzahl", required=False, widget=forms.NumberInput(attrs={"value": 1}))
    year = forms.IntegerField(label="Jahr", required=False, widget=forms.NumberInput(attrs={"placeholder": "Jahr der Erstellung"}))
    kindOf = forms.CharField(label="Art", max_length=100, required=False, widget=forms.TextInput(attrs={"placeholder": "Art des Objektes"}))
    description = forms.CharField(label="Beschreibung", required=False, max_length=8000, widget=forms.Textarea(attrs={"placeholder": "Hier ist viel Platz..."}))
    glashuette = forms.CharField(label="Glashütte", max_length=100, required=False, widget=forms.TextInput(attrs={"placeholder": "Zugehörige Glashuette"}))
    color = forms.CharField(label="Farbe", max_length=120, required=False, widget=forms.TextInput(attrs={"placeholder": "Farbe des Objekts"}))
    # item_Image = forms.FileField(upload_to="images/", verbose_name="Bild des Objekts", blank=True)
    class Meta:
        model = Item
        fields = [
            "name",
            "artist",
            "quantity",
            "year",
            "kindOf",
            "glashuette",
            "color",
            "description",
            "item_Image"
                  ]


class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "artist",
            "quantity",
            "year",
            "kindOf",
            "glashuette",
            "color",
            "description",
            "item_Image"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name des Objektes"}),
            "artist": forms.TextInput(attrs={"placeholder": "Künstlername"}),
            "quantity": forms.NumberInput(attrs={}),
            "year": forms.NumberInput(attrs={"placeholder": "Jahr der Erstellung"}),
            "kindOf": forms.TextInput(attrs={"placeholder": "Art des Objektes"}),
            "description": forms.Textarea(attrs={"placeholder": "zusätzliche Beschreibung "}),
            "glashuette": forms.TextInput(attrs={"placeholder": "Zugehörige Glashütte"}),
            "color": forms.TextInput(attrs={"placeholder": "Farbe des Objektes"}),
            # "item_Image": forms.TextInput(attrs={"placeholder": "Bild zum Objekt"})
        }