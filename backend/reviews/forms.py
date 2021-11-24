from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'review_id',
            'review_title',
            'review_description',
            'review_rating',
            'review_date',
            'user_id',
            'review_update_date',
            'client_id'
        )

