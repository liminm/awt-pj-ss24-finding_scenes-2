from typing import Tuple
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from utils.constants import HF_TOKEN


def init_model(model_id: str, cache_dir: str = "./model_cache", **kwargs) -> Tuple[AutoModelForCausalLM, AutoTokenizer]:
    """
    Initializes the model and tokenizer.

    Args:
        model_id (str): The ID of the model.
        cache_dir (str, optional): The directory to cache the model. Defaults to "./model_cache".
        kwargs (dict, optional): Keyword arguments to pass to the AutoModelForCausalLM. Usually, this will be the
                                 revision or whether to load the model quantized.

    Returns:
        model (AutoModelForCausalLM): The pretrained model for caption generation.
        tokenizer (AutoTokenizer): The tokenizer for the model.
    """
    revision = kwargs.get('revision', '')

    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_type = torch.float16 if device == "cuda" else torch.float32

    model_dir = os.path.join(cache_dir, model_id.replace('/', '_'), revision)

    # Create the directory if it does not exist
    os.makedirs(model_dir, exist_ok=True)

    if not os.path.exists(os.path.join(model_dir, 'pytorch_model.bin')):
        # Model is not saved locally, download and save it
        model = AutoModelForCausalLM.from_pretrained(
            model_id, kwargs, trust_remote_code=True, token=HF_TOKEN, torch_dtype=torch_type
        )
        tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    else:
        # Load the model and tokenizer from the local disk
        model = AutoModelForCausalLM.from_pretrained(
            model_dir, kwargs, torch_dtype=torch_type,  # TODO: Check whether this still works with moondream
        )
        tokenizer = AutoTokenizer.from_pretrained(model_dir)

    model = model.to(device)
    return model, tokenizer


class Model:
    def __init__(self, model_id: str, revision: str):
        """
        Initializes a Model object.

        Args:
            model_id (str): The ID of the model.
            revision (str): The revision of the model.
        """
        self.model_id = model_id
        self.revision = revision
        self.model, self.tokenizer = init_model(model_id, revision)
        self.prompt = ""