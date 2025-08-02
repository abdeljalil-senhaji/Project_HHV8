from nbconvert import HTMLExporter

from nbconvert.preprocessors import TagRemovePreprocessor

class CustomHTMLExporter(HTMLExporter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_preprocessor(TagRemovePreprocessor(remove_cell_tags={"hide_code"}), run_before="preprocess_outputs")

exporter = CustomHTMLExporter()
#exit
#close
