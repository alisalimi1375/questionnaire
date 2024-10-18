from django.core.exceptions import ValidationError
from .qa_types import APPLIED_QA_TYPES


def question_details_validator(value):
    if 'type' not in value:
        raise ValidationError('type is required.')

    if value['type'] not in APPLIED_QA_TYPES:
        raise ValidationError('type is not valid.')

    APPLIED_QA_TYPES[value['type']].question_details_validation(value)


def answer_details_validator(value):
    if 'type' not in value:
        raise ValidationError('type is required.')

    if value['type'] not in APPLIED_QA_TYPES:
        raise ValidationError('type is not valid.')

    APPLIED_QA_TYPES[value['type']].answer_details_validation(value)
