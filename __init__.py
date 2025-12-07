import yaml
import toml
import xmltodict

class MltoXml:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
                "format": (["text", "yaml", "toml"], {"default": "text"}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def run(self, text, format, unique_id=None, extra_pnginfo=None):
        if isinstance(text, list):
            text = text[0]

        if not isinstance(text, str):
            raise ValueError("errrrrr")

        if isinstance(format, list):
            format = format[0]

        res_string = ""

        match format:
            case "text":
                res_string = text
            case "yaml":
                data = yaml.load(text, Loader=yaml.SafeLoader)
                res_string = xmltodict.unparse(data, full_document=False, pretty=True)
            case "toml":
                data = toml.loads(text)
                res_string = xmltodict.unparse(data, full_document=False, pretty=True)

        return (res_string,)

NODE_CLASS_MAPPINGS = {
    "MltoXml": MltoXml
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MltoXml": "MltoXml"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
