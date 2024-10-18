from django.core.exceptions import ValidationError


class QAType:
    title = 'anonymous'

    @classmethod
    def question_details_validation(cls, value):
        pass

    @classmethod
    def answer_details_validation(cls, value):
        pass


class TextQAType(QAType):
    title = 'text'

    @classmethod
    def question_details_validation(cls, value):
        super().question_details_validation(value)

    @classmethod
    def answer_details_validation(cls, value):
        if 'text' not in value:
            raise ValidationError('text is required.')

        if not isinstance(value['text'], str):
            raise ValidationError('text must be string.')

        return super().answer_details_validation(value)


class SingleChoiceQAType(QAType):
    title = 'single-choice'

    @classmethod
    def question_details_validation(cls, value):
        if 'choices' not in value:
            raise ValidationError('choices is required.')

        if isinstance(value['choices'], list):
            for choice in value['choices']:
                if not isinstance(choice, str):
                    raise ValidationError('choices must be a list of strings.')
        else:
            raise ValidationError('choices must be a list of strings.')

        super().question_details_validation(value)

    @classmethod
    def answer_details_validation(cls, value):
        if 'choice' not in value:
            raise ValidationError('choice is required.')

        if not isinstance(value['choice'], str):
            raise ValidationError('choice must be string.')

        return super().answer_details_validation(value)


class MultipleChoiceQAType(QAType):
    title = 'multiple-choice'

    @classmethod
    def question_details_validation(cls, value):
        if 'choices' not in value:
            raise ValidationError('choices is required.')

        if isinstance(value['choices'], list):
            for choice in value['choices']:
                if not isinstance(choice, str):
                    raise ValidationError('choices must be a list of strings.')
        else:
            raise ValidationError('choices must be a list of strings.')

        super().question_details_validation(value)

    @classmethod
    def answer_details_validation(cls, value):
        if 'choices' not in value:
            raise ValidationError('choices is required.')

        if isinstance(value['choices'], list):
            for choice in value['choices']:
                if not isinstance(choice, str):
                    raise ValidationError('choices must be a list of strings.')
        else:
            raise ValidationError('choices must be a list of strings.')

        return super().answer_details_validation(value)


class MatrixQAType(QAType):
    title = 'matrix'

    @classmethod
    def question_details_validation(cls, value):
        if 'rows' not in value:
            raise ValidationError('rows is required.')

        if isinstance(value['rows'], list):
            for row in value['rows']:
                if not isinstance(row, str):
                    raise ValidationError('rows must be a list of strings.')
        else:
            raise ValidationError('rows must be a list of strings.')

        if 'columns' not in value:
            raise ValidationError('columns is required.')

        if isinstance(value['columns'], list):
            for column in value['columns']:
                if not isinstance(column, str):
                    raise ValidationError('columns must be a list of strings.')
        else:
            raise ValidationError('columns must be a list of strings.')

        super().question_details_validation(value)

    @classmethod
    def answer_details_validation(cls, value):
        if 'choices' not in value:
            raise ValidationError('choices is required.')

        if isinstance(value['choices'], list):
            for choice in value['choices']:
                if not isinstance(choice, str):
                    raise ValidationError('choices must be a list of strings.')
        else:
            raise ValidationError('choices must be a list of strings.')

        super().answer_details_validation(value)


APPLIED_QA_TYPES: dict[str, QAType] = {
        TextQAType.title: TextQAType,
        SingleChoiceQAType.title: SingleChoiceQAType,
        MultipleChoiceQAType.title: MultipleChoiceQAType,
        MatrixQAType.title: MatrixQAType,
}
