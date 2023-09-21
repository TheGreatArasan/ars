from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name','address','company','pan_number','current_salary','previous_salary','own_house','house_rent','grocery_expense','current_emis','last_hike_date','other_expenses']
