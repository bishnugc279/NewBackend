from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'booking_id',
            'booking_name',
            'reserve_seat',
            'booking_menu',
            'number_of_people',
            'booking_date',
            'user_id',
            'status',
            'start_date',
            'end_date',
            'clientuser_email',
            'client_id'
        )