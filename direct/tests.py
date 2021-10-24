from django.test import TestCase
from direct.models import Message
# Create your tests here.
class ProfileTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.message= Message(name='say hello!')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.message,Message))
        
    # Testing send message method
    def test_send_message_method(self):
        self.message.send_message()
        new = Message.objects.all()
        self.assertTrue(len(new) > 0)

    # Test get message method
    def test_get_message_method(self,id):
        self.message.get_messages(id='')
        new = Message.objects.all(id)
        self.assertTrue(len(new) == 0)