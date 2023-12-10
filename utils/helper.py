import logging
import torch
import numpy as np
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from densepose import add_densepose_config
from densepose.vis.extractor import (
    DensePoseResultExtractor,
)
from densepose.vis.densepose_results import (
    DensePoseResultsFineSegmentationVisualizer as Visualizer,
)


class GetLogger:
    @staticmethod
    def logger(name):
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger(name)


class Predictor:
    def __init__(self):
        cfg = get_cfg()
        add_densepose_config(cfg)
        cfg.merge_from_file(
            "model_configs/densepose_rcnn_R_50_FPN_s1x.yaml"
        )  # Use the path to the config file from DensePose
        cfg.MODEL.WEIGHTS = "models/model_final_162be9.pkl"  # Use the path to the pre-trained model weights
        cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # Adjust as needed
        self.predictor = DefaultPredictor(cfg)
        self.extractor = DensePoseResultExtractor()
        self.visualizer = Visualizer()

    def predict(self, frame):
        with torch.no_grad():
            outputs = self.predictor(frame)["instances"]
        outputs = self.extractor(outputs)

        out_frame = frame.copy()
        out_frame_seg = np.zeros(out_frame.shape, dtype=out_frame.dtype)

        self.visualizer.visualize(out_frame, outputs)
        self.visualizer.visualize(out_frame_seg, outputs)

        return (out_frame, out_frame_seg)
