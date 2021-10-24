from django.test import TestCase
from authy.models import Profile 

# Create your tests here.
class ProfileTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.Ratchez= Profile(name='Roy')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Ratchez,Profile))
        
    # Testing save method
    def test_save_method(self):
        self.Ratchez.save()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    # Test delete method
    def test_delete_method(self,id):
        self.Ratchez.delete(id='')
        profile = Profile.objects.all(id)
        self.assertTrue(len(profile) == 0)
