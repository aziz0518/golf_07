from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: AbstractBaseUser, timestamp: int) -> text_type:
        return (
            text_type(user.id) + text_type(timestamp)+
            text_type(user.is_superuser)

        )
    
account_activation_token = TokenGenerator()