import logging
from pathlib import Path

import cloudpickle
import kserve

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Model(kserve.Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.ready: bool = False
        self.model = None

    def load(self) -> bool:
        ## homework:start
        ## homework:end
        return self.ready
