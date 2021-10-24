class languageToTool:
    """Средства разработки для языков
    программирования (реализция много-ко-многим)"""
    def __init__(self, language_id, tool_id):
        self.language_id = language_id
        self.tool_id = tool_id