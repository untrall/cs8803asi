# coding=utf-8
# Copyright 2018-2022 EVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
from typing import List

import pandas as pd

from eva.udfs.abstract.pytorch_abstract_udf import PytorchAbstractClassifierUDF

try:
    import torch
    from torch import Tensor

except ImportError as e:
    raise ImportError(
        f"Failed to import with error {e}, \
        please try `pip install torch`"
    )


class YoloV5(PytorchAbstractClassifierUDF):
    """
    Arguments:
        threshold (float): Threshold for classifier confidence score

    """

    @property
    def name(self) -> str:
        return "yolo"

    def setup(self, threshold=0.85, filter = []):
        logging.getLogger("yolov5").setLevel(logging.CRITICAL)  # yolov5
        self.threshold = threshold
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='model.pt', force_reload=True)
        self.filter = ["car"]
    @property
    def labels(self) -> List[str]:
        return [
            "__background__",
            "person",
            "bicycle",
            "car",
            "motorcycle",
            "airplane",
            "bus",
            "train",
            "truck",
            "boat",
            "traffic light",
            "fire hydrant",
            "N/A",
            "stop sign",
            "parking meter",
            "bench",
            "bird",
            "cat",
            "dog",
            "horse",
            "sheep",
            "cow",
            "elephant",
            "bear",
            "zebra",
            "giraffe",
            "N/A",
            "backpack",
            "umbrella",
            "N/A",
            "N/A",
            "handbag",
            "tie",
            "suitcase",
            "frisbee",
            "skis",
            "snowboard",
            "sports ball",
            "kite",
            "baseball bat",
            "baseball glove",
            "skateboard",
            "surfboard",
            "tennis racket",
            "bottle",
            "N/A",
            "wine glass",
            "cup",
            "fork",
            "knife",
            "spoon",
            "bowl",
            "banana",
            "apple",
            "sandwich",
            "orange",
            "broccoli",
            "carrot",
            "hot dog",
            "pizza",
            "donut",
            "cake",
            "chair",
            "couch",
            "potted plant",
            "bed",
            "N/A",
            "dining table",
            "N/A",
            "N/A",
            "toilet",
            "N/A",
            "tv",
            "laptop",
            "mouse",
            "remote",
            "keyboard",
            "cell phone",
            "microwave",
            "oven",
            "toaster",
            "sink",
            "refrigerator",
            "N/A",
            "book",
            "clock",
            "vase",
            "scissors",
            "teddy bear",
            "hair drier",
            "toothbrush",
        ]

    def forward(self, frames: Tensor) -> pd.DataFrame:
        """
        Performs predictions on input frames
        Arguments:
            frames (np.ndarray): Frames on which predictions need
            to be performed

        Returns:
            tuple containing predicted_classes (List[List[str]]),
            predicted_boxes (List[List[BoundingBox]]),
            predicted_scores (List[List[float]])

        """
        # Stacking all frames, and changing to numpy
        # because of yolov5 error with Tensors

        outcome = []
        # Convert to HWC
        # https://github.com/ultralytics/yolov5/blob/3e55763d45f9c5f8217e4dad5ba1e6c1f42e3bf8/models/common.py#L658
        frames = torch.permute(frames, (0, 2, 3, 1))
        predictions = self.model([its.cpu().detach().numpy() * 255 for its in frames])

        for i in range(frames.shape[0]):
            single_result = predictions.pandas().xyxy[i]
            pred_class = single_result["name"].tolist()
            pred_score = single_result["confidence"].tolist()
            pred_boxes = single_result[["xmin", "ymin", "xmax", "ymax"]].apply(
                lambda x: list(x), axis=1
            )
            new_pred_class = []
            new_pred_score = []
            new_pred_boxes = []
            for i in range(len(pred_class)):
              if pred_class[i] not in self.filter:
                new_pred_class.append(pred_class[i])
                new_pred_score.append(pred_score[i])
                new_pred_boxes.append(pred_boxes[i])
            outcome.append(
                {
                    "labels": new_pred_class,
                    "bboxes": new_pred_boxes,
                    "scores": new_pred_score,
                },
            )
        return pd.DataFrame(
            outcome,
            columns=[
                "labels",
                "bboxes",
                "scores",
            ],
        )
