''' Tornado Web Server Starting Script - Application Entry Point '''

from threading import Thread

from aiocron import crontab
from biothings.web.launcher import main

from discovery.handlers import HANDLERS, TemplateHandler
from discovery.notify import update_n3c_routine


def run_routine():
    thread = Thread(target=update_n3c_routine, daemon=True)
    thread.start()


if __name__ == '__main__':

    crontab('0 0 * * *', func=run_routine, start=True)
    main(HANDLERS, {
        "default_handler_class": TemplateHandler,
        "default_handler_args": {
            "filename": "404.html",
            "status_code": 404
        }
    }, use_curl=True)
