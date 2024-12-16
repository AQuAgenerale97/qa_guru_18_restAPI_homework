import logging

import allure
import requests
from allure_commons.types import AttachmentType
from requests import Response


def post_with_logging2(url, **kwargs):
    with allure.step("Logging API"):
        response = requests.post(url, **kwargs)
        allure.attach(body=response.text,
                      name="Response",
                      attachment_type=AttachmentType.TEXT,
                      extension=".txt")
        allure.attach(body=str(response.cookies),
                      name="Cookies",
                      attachment_type=AttachmentType.TEXT,
                      extension=".txt")
        logging.info(f'POST: {response.request.url}')
        logging.info(f'With payload {response.request.body}')
        logging.info(f'Finished with status code {response.status_code}')
        return response


def post_with_logging(url, **kwargs):
    with allure.step("API Requset"):
        response = requests.post(url, **kwargs)
        allure.attach(
            body=response.text,
            name="Response",
            attachment_type=AttachmentType.TEXT,
            extension="txt")
        allure.attach(
            body=str(response.cookies),
            name="Cookies",
            attachment_type=AttachmentType.TEXT,
            extension="txt")
        allure.attach(
            body=str(response.request.headers),
            name="Request headers",
            attachment_type=AttachmentType.TEXT,
            extension="txt")
        logging.info(f'POST: {response.request.url}')
        logging.info(f'With payload {response.request.body}')
        logging.info(f'Finished with status code {response.status_code}')
        logging.info(f'Response URL {response.url}')
        return response


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)
