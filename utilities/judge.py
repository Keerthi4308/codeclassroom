"""All Judge/Code Running Utilities"""
from app.models import Question, Assignment
import coderunner


def run_code(code, lang, question):
    """Judge Code for correctness"""
    execution = {}

    expected_output = Question.objects.only(
        'sample_output').get(pk=question).sample_output
    standard_input = Question.objects.only(
        'sample_input').get(pk=question).sample_input

    if standard_input != "":
        r = coderunner.code(code, lang, standard_input, expected_output, False)
    else:
        r = coderunner.code(code, lang, expected_output, False)

    r.run()

    execution["status"] = r.getStatus()
    execution["output"] = r.getOutput()
    execution["error"] = r.getError()
    execution["memory"] = r.getMemory()
    execution["execution_time"] = r.getTime()

    return execution


def submit_code(question, assignment, code):

    lang = Assignment.objects.only('language').get(pk=assignment).language

    program_status = run_code(code, lang, question)

    if program_status["status"] == "Accepted":
        execution_status = "accepted"
    elif program_status["status"] == "Wrong Answer":
        execution_status = "wrong"
    else:
        execution_status = "not-attempted"

    return program_status, execution_status
