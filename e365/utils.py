from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def base64_encode_slugify(
    value, allow_unicode=False
):  # pylint: disable=unused-argument
    return urlsafe_base64_encode(force_bytes(value))
