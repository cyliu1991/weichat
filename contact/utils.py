import logging
import pystache


class Utils:
    @classmethod
    def parse(cls, template_path, dict):
        logging.basicConfig(level=logging.DEBUG)
        template = "".join(open(template_path, encoding='utf-8').readlines())
        logging.debug(template)
        return pystache.render(template, dict)