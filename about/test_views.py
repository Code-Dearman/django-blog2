from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import About
from .forms import CollaborateForm

class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me",
            content="This is about me"
        )
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containg a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm
        )

    def test_successful_collaboration_request_submission(self):
        """Test successful collaboration form submission"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }

        response = self.client.post(reverse('about'), post_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', 
            response.content
        )



    # name = models.CharField(max_length=200)
    # email = models.EmailField()
    # message = models.TextField()