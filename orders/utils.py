import string
import secrets
from .models import Coupon  # assuming you have a Coupon model storing codes

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    Default length is 10 characters.
    """
    alphabet = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(alphabet) for _ in range(length))

        # Ensure uniqueness by checking database
        if not Coupon.objects.filter(code=code).exists():
            return code
