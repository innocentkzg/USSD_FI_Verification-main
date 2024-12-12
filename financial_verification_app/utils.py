from django.http import HttpResponse
from .languages import LANGUAGES, STATUS_TRANSLATIONS
import logging

logger = logging.getLogger(__name__)

logger.info("User authenticated successfully.")


def create_ussd_response(text, freeflow='FC'):
    headers = {
        'Freeflow': freeflow,
        'Cache-Control': 'max-age=0',
        'Pragma': 'no-cache',
        'Expires': '-1',
        'Content-Type': 'text/plain;charset=UTF-8'
    }
    return HttpResponse(text, headers=headers)

def translate_status(status, language):
    return STATUS_TRANSLATIONS.get(status, {}).get(language, status)

def has_permission(user, action):
    permissions = {
        "Admin": {
            "manage_bankusers": ["create", "update", "view", "delete"],
            "manage_categories": ["create", "update", "view", "delete"],
            "assign_privileges": ["assign"],
        },
        "BankUser": {
            "manage_institutions": ["view", "add", "edit"],
        },
    }
    user_role = user.role.name
    for key, actions in permissions.get(user_role, {}).items():
        if action in actions:
            return True
    return False
