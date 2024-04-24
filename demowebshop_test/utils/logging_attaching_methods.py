import json
import logging
import allure
from allure_commons.types import AttachmentType

from requests import Response


def response_logging(response: Response):
    logging.info('Request url: ' + response.request.url)
    if response.request.body:
        logging.info('Request body: ' + response.request.body)
    logging.info('Response: ' + response.text)
    logging.info('Response headers: ' + str(response.headers))
    logging.info('Response code: ' + str(response.status_code))


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name='request url',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )
    allure.attach(
        body=response.text,
        name='response text',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )
    allure.attach(
        body=str(response.status_code),
        name='response status code',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )
    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body),
            name='request body',
            attachment_type=AttachmentType.JSON,
            extension='.json'
        )
