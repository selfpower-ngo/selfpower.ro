'''
Tokens used for  password reset
'''
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    '''
    Tokens generator for password resetting
    '''
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
ACCOUNT_ACTIVATION_TOKEN = TokenGenerator()
