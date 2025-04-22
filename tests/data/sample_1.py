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
        ## homework:replace:on
        model_path = Path("./models/model.pkl")
        if model_path.exists():
            with open(model_path, "rb") as f:
                self.model = cloudpickle.load(f)
                logger.info("Model loaded successfully from %s", model_path)
                self.ready = True

        ## homework:replace:off
        return self.ready
