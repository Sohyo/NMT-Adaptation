import torch
import argparse
import os

from typing import List
import fairseq
from fairseq.models.transformer import TransformerModel
from fairseq.data import Dictionary


def load_dict(langs: List[str], path: str) -> Dictionary:
    dict = Dictionary.load(path)
    for lan in langs:
        dict.add_symbol(f"[{lan}]")
    dict.add_symbol("<PT>")
    return dict


def my_load_dict(path: str) -> Dictionary:
    dict = Dictionary.load(path)
    # for lan in langs:
    dict.add_symbol("<PT>")
    return dict


def main() -> None:
    parser = argparse.ArgumentParser(description="Trims pre-trained wmt19.en-de model for fine-tuning.")
    parser.add_argument("--pre-train-dir", type=str, default="../models/wmt19.en-de.joined-dict.ensemble", help="The pre-trained wmt19.en-de model directory.")
    parser.add_argument("--ft-dict", type=str, default="", help="The fine-tuning model dictionary.")
    # parser.add_argument("--langs", type=str, default="de, en", help="The pre-trained model languages.")
    # parser.add_argument("--output", type=str, required=True, help="The trimmed wmt19.en-de model.")
    args = parser.parse_args()

    #getting the dictionaries
    #langs = args.langs.split(",")
    # example = my_load_dict(os.path.join(args.pre_train_dir, "dict.de.txt"))
    # print(len(example))
    # new = my_load_dict(os.path.join(args.pre_train_dir, "newdict.de.txt"))
    ft_dict = my_load_dict(os.path.join(args.pre_train_dir, "dict.de.txt"))
    print(f"length of finetune dictionary : {len(ft_dict)}")
    #ft_dict = load_dict(langs, args.ft_dict)
    #print(pre_dict)
    # print(model)
    # mapping: List[int] = []
    # for i in range(len(ft_dict)):
    #     word = ft_dict[i]
    #     mapping.append(pre_dict.index(word))

    # load the pre-trained model
    data = torch.load(os.path.join(args.pre_train_dir, "model1.pt"))
    model = data["model"]
    # print(len(model["encoder.layers.0.self_attn.in_proj_weight"]))
    # print(len(model['encoder.embed_tokens.weight'])) #42024
    for name in ["encoder.embed_tokens.weight", "decoder.embed_tokens.weight"]:
        pre_tensor: torch.Tensor = model[name] #pre_tensor = model[name]
        # print(pre_tensor)
        # print(f"shape : {pre_tensor.device}")
        ft_tensor = torch.zeros(
            [len(ft_dict), 1024], dtype=pre_tensor.dtype, layout=pre_tensor.layout, device=pre_tensor.device,
        )
        print(ft_dict)
        # for ft_i, pre_i in enumerate(mapping):
        #     ft_tensor[ft_i] = pre_tensor[pre_i]
        # model[name] = ft_tensor

    # torch.save(data, args.output)


if __name__ == "__main__":
    main()
